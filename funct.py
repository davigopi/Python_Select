# flake8: noqa
# pyright: # type: ignore

import sys
import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotInteractableException,
    ElementClickInterceptedException,
    UnexpectedAlertPresentException
)
from bs4 import BeautifulSoup
from log import Log


class Funct:
    def __init__(self, *args, **kwargs):
        self.driver = kwargs.get('driver')
        self.path = kwargs.get('path')
        self.pathX = kwargs.get('pathX')
        self.digitar = kwargs.get('digitar')
        self.faz = kwargs.get('faz')
        self.esperar = kwargs.get('esperar')
        self.vertical = kwargs.get('vertical')
        self.retorno = kwargs.get('retornar')
        self.tag = kwargs.get('tag')
        self.tag1 = kwargs.get('tag1')
        self.tag2 = kwargs.get('tag2')
        self.tag3 = kwargs.get('tag3')
        self.g_newcon = kwargs.get('g_newcon')
        self.xpath_present_secreen = kwargs.get('xpath_present_secreen')
        self.path_loading = kwargs.get('path_loading')
        self.time = int(kwargs.get('time', 10))
        self.num_tentativas = 0
        self.quantidades_tentativas = 4
        self.text = ''
        self.dados = ''
        self.segundos = 0
        self.repetir = int(kwargs.get('repetir', 0))
        self.local = kwargs.get('local', '*')
        self.pAL = kwargs.get('pAL')
        self.error = None
        self.log = Log()
        self.e = ''
        self.value = ''
        self.key_single = ''

        self.excecao = (
            NoSuchElementException,
            ElementNotInteractableException,
            ElementClickInterceptedException,
            UnexpectedAlertPresentException,
            AttributeError,
        )

        # Dicionário mapeando ações para funções
        self.acoes = {
            None: self.funct_click,
            'click_texto': self.funct_click_texto,
            'keys': self.funct_keys,
            'locate': self.funct_locate,
            'scroll': self.funct_scroll,
            # 'inform': self.funct_inform,
            'get_select': self.funct_get_select,
            'select_value': self.funct_select_value,
            'checkbox': self.funct_checkbox,
            'wait_df_or_empty': self.funct_wait_df_or_empty,
            'key_single': self.funct_key_single,
        }

    # =============================== FUNÇÕES BASE ===============================

    def reset_var(self):
        self.faz = None
        self.time = 10
        self.repetir = 1
        self.local = '*'
        self.xpath_present_secreen = None

    def msn_padrao(self):
        if self.faz:
            faz = self.faz
        else:
            faz ='click'
        self.segundos = round(self.segundos, 1)
        self.text = (
            f"FUNCOES OBS: Grupo: {self.g_newcon} | "
            f"Tempo: {self.segundos}/{self.time}s | "
            f"Tentativas: {self.num_tentativas} | "
            f"Ação: {faz} | "
            f"Path: {self.path} | "
            f"Digitar: {self.digitar} | "
            f"Erro: {self.e.__class__.__name__}\n"
        )



    def msn_sys_exit(self):
        self.msn_padrao()
        self.text += "Programa interrompido: não há tratamento para este erro.\n\n"
        print(self.text)
        sys.exit()

    def wait_loading_invisiblility(self):
        # print("1 — esperar loading sumir (se existir)")
        try:
            WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH, self.path_loading)))
        except:
            pass

    def wait_path_visibility(self):
        self.wait_loading_invisiblility()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.path)))

    def wait_path_clickable(self):
        self.wait_loading_invisiblility()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.path)))
        # time.sleep(0.3)

    def funct_click(self):
        try:
            self.wait_path_clickable()
            self.driver.find_element(By.XPATH, self.path).click()
            return True
        
        except self.excecao as e:
            self.e = e
            return False
        
        except Exception as e:
            self.msn_sys_exit()

    def funct_click_texto(self):
        path_local = f"//{self.local}[contains(text(),'{self.path}')]"
        try:
            self.wait_path_clickable()
            self.driver.find_element(By.XPATH, path_local).click()
            return True
        
        except self.excecao as e:
            self.e = e
            return False
        
        except Exception as e:
            self.msn_sys_exit()

    def funct_keys(self):
        try:
            self.wait_path_visibility()
            self.driver.find_element(By.XPATH, self.path).send_keys(self.digitar)
            return True
        
        except self.excecao as e:
            self.e = e 
            return False

        except Exception as e:
            self.e = e
            self.msn_sys_exit()

    def funct_key_single(self):
        try:
            self.wait_path_visibility()
            self.driver.find_element(By.XPATH, self.path).send_keys(Keys.PAGE_UP)
            return True

        except self.excecao as e:
            self.e = e 
            return False

        except Exception as e:
            self.e = e
            self.msn_sys_exit()
        

    def funct_locate(self):
        try:
            self.wait_path_visibility()
            self.driver.find_element(By.XPATH, self.path).location_once_scrolled_into_view
            return True

        except self.excecao as e:
            self.e = e
            return False

        except Exception as e:
            self.e = e
            self.msn_sys_exit()

    def funct_scroll(self):
        try:
            self.wait_path_visibility()
            iframe = self.driver.find_element(By.XPATH, self.path)
            scroll_origin = ScrollOrigin.from_element(iframe)
            ActionChains(self.driver).scroll_from_origin(scroll_origin, 0, int(self.vertical)).perform()
            return True

        except self.excecao as e:
            self.e = e
            return False

        except Exception as e:
            self.e = e
            self.msn_sys_exit()

    # def funct_get_select(self):
    #     try:
    #         self.wait_path_visibility()
    #         html = self.driver.find_element(By.XPATH, self.path).get_attribute('outerHTML')
    #         if self.tag2:
    #             self.dados = BeautifulSoup(html, "lxml").find(self.tag1).findAll(self.tag2)
    #         elif self.tag1:
    #             self.dados = BeautifulSoup(html, "lxml").find(self.tag1)
    #         else:
    #             self.dados = BeautifulSoup(html, "lxml")
    #         return True

    #     except self.excecao as e:
    #         self.e = e
    #         return False

    #     except Exception as e:
    #         self.e = e
    #         self.msn_sys_exit()

    def funct_get_select(self):
        try:
            self.wait_path_visibility()
            elemento = self.driver.find_element(By.XPATH, self.path)
            html = elemento.get_attribute("outerHTML")
            self.dados = BeautifulSoup(html, "html.parser")
            return True

        except self.excecao as e:
            self.e = e
            return False

        except Exception as e:
            self.e = e
            self.msn_sys_exit()

    def funct_select_value(self):
        try:
            self.wait_path_visibility()
            xpath_option = f"{self.path}/option[@value='{self.value}']"
            elemento = self.driver.find_element(By.XPATH, xpath_option)
            elemento.click()
            return True

        except self.excecao as e:
            self.e = e
            return False

        except Exception as e:
            self.e = e
            self.msn_sys_exit()

    def funct_checkbox(self):
        try:
            self.wait_path_visibility()
            elemento = self.driver.find_element(By.XPATH, self.path)
            if not elemento.is_selected():
                self.dados = 'OK'
            return True

        except self.excecao as e:
            self.e = e
            return False

        except Exception as e:
            self.msn_sys_exit()


    def funct_wait_df_or_empty(self):
        try:
            self.wait_loading_invisiblility()
            # print("2 — esperar tabela OU mensagem de vazio")
            WebDriverWait(self.driver, 10).until(
                EC.any_of(
                    EC.presence_of_element_located((By.XPATH, self.path + "table")),
                    EC.presence_of_element_located((By.XPATH, self.path + "*[contains(text(),'Nenhum')]")),
                )
            )
            return True
        
        except self.excecao as e:
            self.e = e
            return False

        except Exception as e:
            self.msn_sys_exit()


    def funct_present_screen(self):
        self.path = self.xpath_present_secreen
        try:
            self.wait_path_visibility()
            elemento = self.driver.find_element(By.XPATH, self.path)
            if elemento.is_displayed():
                self.retorno = 'ERROR'
                return True
            return False
        
        except self.excecao as e:
            self.e = e
            return False

        except Exception as e:
            self.msn_sys_exit()

# =============================== PROCESSOS ===============================

    def processo_present_screen(self):
        respost = self.funct_present_screen()
        present_screen = False
        if respost:
            self.text = '\nFUNCOES OBS: Existe processando? Sim!'
            print(self.text)
            self.text = 'FUNCOES OBS: '
            tentativas = 0
            time_espera = 0.5

            while True:
                time.sleep(time_espera)
                respost = self.funct_present_screen()
                if respost:
                    tentativas += 1
                    if tentativas >= self.quantidades_tentativas:
                        tempo_pecorrido = tentativas * time_espera
                        self.text += f'Em {tempo_pecorrido} seg NÃO teve resposta.'
                        print(self.text)
                        present_screen = True
                        self.retorno = 'ERROR'
                        break
                else:
                    tempo_pecorrido = tentativas * time_espera
                    path_texto = f'Depois de {tempo_pecorrido} OK foi encontrado. \n'
                    self.msn_sys_exit(path_texto)
        return present_screen



    def processo_tempo_pecorrido(self):
        time.sleep(0.3)
        self.segundos += 0.35
        if self.segundos >= self.time:
            self.msn_padrao()
            self.log.escreva = self.text
            self.log.escrever()
            print(self.text)
            return True
        return False

    def processo_repetir_tarefa(self):
        self.repetir -= 1
        if self.repetir <= 0:
            return False
        self.segundo = 0
        return True

    # =============================== FUNÇÃO PRINCIPAL ===============================

    def funct(self):
        self.dados = None
        self.num_tentativas = 0
        self.segundos = 0
        self.error = None
        self.e = ''
        while True:
            self.num_tentativas += 1
            if self.path:
                func = self.acoes.get(self.faz)
                if func:
                    sair = func()
                else:
                    self.msn_sys_exit()
                    self.error = True
                    break
                if sair:
                    if not self.processo_repetir_tarefa():
                        break

            if self.processo_tempo_pecorrido():
                self.error = True
                break

            if self.processo_present_screen():
                self.error = True
                break

        self.reset_var()

        if self.error:
            return False
        
        if self.dados:
            return self.dados
        
        return True
