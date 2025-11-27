import os
import io
import re
import time
import shutil
import zipfile
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class ChromeDriverAuto:
    def __init__(self, driver_dir="chrome-driver"):
        self.driver_dir = driver_dir

    # -------------------------------
    # Obter versão do Chrome instalado
    # -------------------------------
    def get_chrome_version(self):
        stream = os.popen(r'reg query "HKEY_CURRENT_USER\Software\Google\Chrome\BLBeacon" /v version')
        output = stream.read()
        match = re.search(r"version\s+REG_SZ\s+([0-9.]+)", output)
        if match:
            return match.group(1)
        raise Exception("Chrome não encontrado no registro do Windows.")

    # -------------------------------
    # Baixar ChromeDriver correspondente
    # -------------------------------
    def download_chrome_for_testing(self, chrome_version):
        major = chrome_version.split(".")[0]
        # Baixar lista oficial
        url = "https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json"
        data = requests.get(url).json()
        # Achar versão estável para Windows 64
        stable = data["channels"]["Stable"]["downloads"]["chromedriver"]
        zip_url = None
        for item in stable:
            if item["platform"] == "win64":
                zip_url = item["url"]
                break
        if not zip_url:
            raise Exception("Nenhum ChromeDriver compatível encontrado para Windows 64")
        print("Baixando:", zip_url)
        # Download do ZIP
        content = requests.get(zip_url).content
        z = zipfile.ZipFile(io.BytesIO(content))

        # Remove pasta antiga
        if os.path.exists(self.driver_dir):
            try:
                shutil.rmtree(self.driver_dir)
            except PermissionError:
                print("Pasta travada, tentando matar processos...")
                os.system("taskkill /F /IM chromedriver.exe 2>nul")
                os.system("taskkill /F /IM chrome.exe 2>nul")
                time.sleep(1)
                shutil.rmtree(self.driver_dir)

        # Extrair com fallback
        try:
            z.extractall(self.driver_dir)
        except PermissionError:
            print("Permissão negada ao extrair, tentando novamente...")
            time.sleep(1)
            z.extractall(self.driver_dir)

        # Caminho final
        driver_path = os.path.abspath(os.path.join(self.driver_dir, "chromedriver-win64", "chromedriver.exe"))

        if not os.path.exists(driver_path):
            raise Exception("O ChromeDriver não foi encontrado após a extração.")

        return driver_path

    # -------------------------------
    # Criar driver já funcional
    # -------------------------------
    def create_driver(self):
        version = self.get_chrome_version()
        driver_path = self.download_chrome_for_testing(version)

        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-certificate-errors")

        service = Service(driver_path)
        driver = webdriver.Chrome(service=service, options=options)
        return driver
    
    def site_open(self, dictionary):
        driver = self.create_driver()
        driver.get(dictionary["site"])
        driver.maximize_window()
        return driver