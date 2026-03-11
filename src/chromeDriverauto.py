import os
import sys
import shutil
import subprocess
import requests
import zipfile
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import winreg
from var import *
import time

# ============================================================
# Baixa o ZIP
# ============================================================
def download_driver_zip(version):
    url = dict_url_download_google['base'] + version + dict_url_download_google['driver_zip']
    urllib.request.urlretrieve(url, path_driver_zip)
    

# ============================================================
# Limpa pasta driver
# ============================================================
def clean_path_driver():
    if os.path.exists(extract_path):
        shutil.rmtree(extract_path, ignore_errors=True)
    os.makedirs(extract_path, exist_ok=True)

# ============================================================
# Mata processos travados
# ============================================================
def kill_process():
    '''Mata processo pelo nome (chrome.exe ou chromedriver.exe).'''
    try:
        for proc in list_kill_proc:
            subprocess.run(['taskkill', '/f', '/im', proc], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except:
        pass


class ChromeDriverAuto:
    def __init__(self):
        self.driver = None
        self.path_driver = ''
        self.version = ''

    # ============================================================
    #   UTILIDADES
    # ============================================================
    def kill_chrome(self):
        subprocess.run('taskkill /F /IM chrome.exe /T', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def delete_chrome_folders(self):
        folders = [
            r'C:\Program Files\Google\Chrome',
            r'C:\Program Files (x86)\Google\Chrome',
            os.path.expanduser(r'~\AppData\Local\Google\Chrome'),
            os.path.expanduser(r'~\AppData\Local\Google\Chromium'),
        ]
        for p in folders:
            if os.path.exists(p):
                shutil.rmtree(p, ignore_errors=True)

    # ============================================================
    #   LÊ A VERSÃO DO CHROME INSTALADO
    # ============================================================
    def get_chrome_version(self):
        try:
            key = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                r'Software\Google\Chrome\BLBeacon'
            )
            self.version, _ = winreg.QueryValueEx(key, 'version')
        except:
            return None


    # ============================================================
    #   INSTALAÇÃO DO CHROME FOR TESTING (SILENCIOSA)
    # ============================================================
    def install_chrome_version(self):
        print(f'⛏️ CHROMEDRIVE: Instalando Chrome versão {self.version}...')
        url = dict_url_download_google['base'] + self.version + dict_url_download_google['chrome_zip']

        urllib.request.urlretrieve(url, path_chrome_zip)

        install_path = r'C:\Program Files\Google\Chrome\Application'
        os.makedirs(install_path, exist_ok=True)

        with zipfile.ZipFile(path_chrome_zip, 'r') as zip_ref:
            zip_ref.extractall(install_path)

        # mover arquivos
        src = os.path.join(install_path, 'chrome-win64')
        for file in os.listdir(src):
            shutil.move(os.path.join(src, file), os.path.join(install_path, file))

        shutil.rmtree(src)
        os.remove(path_chrome_zip)

        print('✅ CHROMEDRIVE: Chrome instalado com sucesso!')

    # ============================================================
    #   INSTALA O DRIVER COMPATÍVEL
    # ============================================================
    def install_driver(self):
        print(f'⛏️  CHROMEDRIVE: Instalando ChromeDriver versão {self.version}...')
        download_driver_zip(self.version)
        for i in range(2):     
            clean_path_driver()
            try:
                with zipfile.ZipFile(path_driver_zip, 'r') as zip_ref:
                    zip_ref.extractall(extract_path)
                print('✅ CHROMEDRIVE: Extração concluída após liberar os arquivos.')
                break
            except PermissionError:
                if i == 0:
                    print('❌ CHROMEDRIVE: PermissionError: tentando liberar recursos...')
                else:
                    print('❌ CHROMEDRIVE: O arquivo ainda está bloqueado. Feche tudo e tente novamente.')
                    sys.exit()
                kill_process()
        os.remove(path_driver_zip)
        self.path_driver = os.path.join(extract_path, 'chromedriver-win64', 'chromedriver.exe')
        print('✅ CHROMEDRIVE: Driver instalado!')

    # ============================================================
    #   SISTEMA COMPLETO DE VERIFICAÇÃO + INSTALAÇÃO
    # ============================================================
    def ensure_chrome_and_driver(self):
        self.get_chrome_version()
        if self.version is None:
            print('❌ CHROMEDRIVE: Chrome não está instalado. Instalando versão padrão...')
            self.version = if_not_exist_version_chrome
            self.install_chrome_version()
        print('⛏️  CHROMEDRIVE: Chrome instalado na versão:', self.version)
        self.install_driver()

    # ============================================================
    #   CRIA O DRIVER SEM ERROS
    # ============================================================
    def create_driver(self):
        self.ensure_chrome_and_driver()
        options = webdriver.ChromeOptions()
        # options.add_argument('--ignore-certificate-errors')
        # 🔇 Silenciar logs do Chrome
        options.add_argument('--log-level=3')          # só erros críticos
        options.add_argument('--disable-logging')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-notifications')
        options.add_argument('--disable-infobars')
        print('✅ CHROMEDRIVE: Abrindo o Chrome com o driver correto...')
        service = Service(self.path_driver, log_path=os.devnull)
        return webdriver.Chrome(service=service, options=options)

    # ============================================================
    #   ABRIR O DRIVER E RETONA-LO
    # ============================================================  
    def open_site(self, info):
        print(f'⛏️  CHROMEDRIVE: Iniciando a aberturar do site: {info["site"]}')
        driver = chromeDriverAuto.create_driver()
        driver.get(info["site"])
        driver.maximize_window()
        return driver


    def close_driver(self, driver):
        print(f'✅  CHROMEDRIVE: Fechando do driver')
        driver.quit()

# ============================================================
#   EXEMPLO DE USO
# ============================================================
chromeDriverAuto = ChromeDriverAuto()
if __name__ == '__main__':
    info = {'site': 'https://google.com'}
    
    driver = chromeDriverAuto.open_site(info)
    time.sleep(10)
    chromeDriverAuto.close_driver(driver)
