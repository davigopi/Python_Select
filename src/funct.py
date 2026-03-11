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
    UnexpectedAlertPresentException,
    TimeoutException,
    StaleElementReferenceException
)
from bs4 import BeautifulSoup
from src.log import Log
from src.exceptions import BlockExecution
from src.var import *

class Funct:
    def __init__(self, *args, **kwargs):
        self.driver = kwargs.get('driver')
        self.path_all_log = kwargs.get('path_all_log')

        self.path = kwargs.get('path')
        self.path_loading = kwargs.get('path_loading')
        self.path_modal = kwargs.get('path_modal')
        self.path_modal_btn = kwargs.get('path_modal_btn')
        self.error = kwargs.get("error")
        self.dados = kwargs.get('dados')
        self.tag: kwargs.get('tag')
        
        self.excecao = (
            AttributeError,
            NoSuchElementException,
            ElementNotInteractableException,
            ElementClickInterceptedException,
            UnexpectedAlertPresentException,
            StaleElementReferenceException
        )

        # self.acoes = {
        #     None: self.funct_click,
        #     'click_texto': self.funct_click_texto,
        #     'keys': self.funct_keys,
        #     'locate': self.funct_locate,
        #     'scroll': self.funct_scroll,
        #     'get_select': self.funct_get_select,
        #     'select_value': self.funct_select_value,
        #     'checkbox': self.funct_checkbox,
        #     'wait_df_or_empty': self.funct_wait_df_or_empty,
        #     'key_single': self.funct_key_single,
        # }

        self.acoes = {
            None: self._click,
            'click_texto': self._click_texto,
            'keys': self._keys,
            'locate': self._locate,
            'scroll': self._scroll,
            'get_select': self._get_select,
            'select_value': self._select_value,
            'checkbox': self._checkbox,
            'wait_df_or_empty': self._wait_df_or_empty,
            'key_single': self._key_single,
        }

        self._reset_defaults = {
            'digitar': kwargs.get('digitar'),
            'faz': kwargs.get('faz'),
            'vertical': kwargs.get('vertical'),
            'repetir': int(kwargs.get('repetir', 0)),
            'local': kwargs.get('local', '*'),
            'time_total_set': int(kwargs.get('time_total_set', 10)),
            'time_start': 0,
            'time_end': 0,
            'text': '',
            'value': '',
            'e': '',
        }
        self._apply_reset_defaults()

    def _apply_reset_defaults(self):
        for attr, value in self._reset_defaults.items():
            setattr(self, attr, value)

        # self.driver = kwargs.get('driver')
        # self.path_all_log = kwargs.get('path_all_log')
        # self.path = kwargs.get('path')
        # self.path_loading = kwargs.get('path_loading')
        # self.path_modal = kwargs.get('path_modal')
        # self.path_modal_btn = kwargs.get('path_modal_btn')

        # self.digitar = kwargs.get('digitar')
        # self.faz = kwargs.get('faz')
        # self.vertical = kwargs.get('vertical')
        # self.tag = kwargs.get('tag')
        # self.repetir = int(kwargs.get('repetir', 0))
        # self.local = kwargs.get('local', '*')
        # self.time_total_set = int(kwargs.get('time_total_set', 10))
        # self.time_start = 0
        # self.time_end = 0  
        # self.text = ''
        # self.dados = ''
        # self.value = ''
        # self.error = None
        # self.e = ''
        # self.excecao = (
        #     AttributeError,
        #     NoSuchElementException,
        #     ElementNotInteractableException,
        #     ElementClickInterceptedException,
        #     UnexpectedAlertPresentException,
        #     TimeoutException
        # )
        # # Dicionário mapeando ações para funções
        # self.acoes = {
        #     None: self.funct_click,
        #     'click_texto': self.funct_click_texto,
        #     'keys': self.funct_keys,
        #     'locate': self.funct_locate,
        #     'scroll': self.funct_scroll,
        #     # 'inform': self.funct_inform,
        #     'get_select': self.funct_get_select,
        #     'select_value': self.funct_select_value,
        #     'checkbox': self.funct_checkbox,
        #     'wait_df_or_empty': self.funct_wait_df_or_empty,
        #     'key_single': self.funct_key_single,
        # }

    # =============================== FUNÇÕES BASE ===============================

    # def reset_var(self):
        
        # self.faz = None
        # self.repetir = 1
        # self.local = '*'
        # self.digitar = ''
        # self.e = ''
        # self.time_total_set = 10

    def msn_padrao(self):
        if self.faz:
            faz = self.faz
        else:
            faz ='click'
        self.time_end = round(self.time_end, 1)
        self.text = (
            f"⚠️  FUNCT: "
            f"Tempo: {self.time_end}/{self.time_total_set}s | "
            f"Ação: {faz} | "
            f"Path: {self.path} | "
            f"Digitar: {self.digitar} | "
            f"Erro: {self.e.__class__.__name__}"
        )

    def msn_sys_exit(self):
        for _ in range(5):
            self.msn_padrao()
            self.text += f"\n❌ FUNCT: Programa interrompido, pois não há tratamento do erro: {self.e.__class__.__name__}. Programa sera interrompido em 2 minutos.\n\n"
            print(self.text)
            time.sleep(10)
        sys.exit()

    def wait_loading_invisiblility(self):
        try:
            WebDriverWait(self.driver, 3).until(EC.invisibility_of_element_located((By.XPATH, self.path_loading)))
        except:
            pass

    def wait_modal_invisiblility(self):
        if not self.path_modal:
            return False
        try:
            WebDriverWait(self.driver, 0.3).until(EC.invisibility_of_element_located((By.XPATH, self.path_modal)))
            return False
        except TimeoutException:
            pass
        try:
            WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, self.path_modal_btn)))
            self.driver.find_element(By.XPATH, self.path_modal_btn).click()
            self.path_modal = None
            print("⛏️  FUNCT: Modal detectado e fechado.")
            return True
        except TimeoutException:
            return False

    def wait_path_visibility(self):
         WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.XPATH, self.path)))

    def wait_path_located(self):
        return WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, self.path)))

    def wait_path_clickable(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, self.path)))
        # time.sleep(0.3)

    def scroll_view_path(self):
        # self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", self.driver.find_element(By.XPATH, self.path))
        header_px = 90
        # elem = self.driver.find_element(By.XPATH, self.path)
        elem = self.wait_path_located()
        self.driver.execute_script("const el=arguments[0]; const rect=el.getBoundingClientRect(); window.scrollBy(0, rect.top - %d - 20);" % header_px, elem)

    def funct_all(self, func):
        try:
            func()  # executa o código que você passou
            return True
        except self.excecao as e:
            self.e = e
            return False
        except TimeoutException as e:
            raise BlockExecution("Timeout detectado")
        except Exception as e:
            self.e = e
            self.msn_sys_exit()
        
    def _click(self):
        self.scroll_view_path()
        self.wait_path_clickable().click()

    def _click_texto(self):
        path_local = f"//{self.local}[contains(text(),'{self.path}')]"
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, path_local))).click()

    def _keys(self):
        self.driver.find_element(By.XPATH, self.path).send_keys(self.digitar)

    def _key_single(self):
        self.driver.find_element(By.XPATH, self.path).send_keys(Keys.PAGE_UP)

    def _locate(self):
        self.driver.find_element(By.XPATH, self.path).location_once_scrolled_into_view

    def _scroll(self):
        iframe = self.driver.find_element(By.XPATH, self.path)
        scroll_origin = ScrollOrigin.from_element(iframe)
        ActionChains(self.driver).scroll_from_origin(scroll_origin, 0, int(self.vertical)).perform()

    def _get_select(self):
        elemento = self.driver.find_element(By.XPATH, self.path)
        html = elemento.get_attribute("outerHTML")
        self.dados = BeautifulSoup(html, "html.parser")

    def _select_value(self):
        xpath_option = f"{self.path}/{tag_option}[@{tag_value}='{self.value}']"
        elemento = self.driver.find_element(By.XPATH, xpath_option)
        elemento.click()

    def _checkbox(self):
        elemento = self.driver.find_element(By.XPATH, self.path)
        if not elemento.is_selected():
            self.dados = 'OK'

    def _wait_df_or_empty(self):
        # print("2 — esperar tabela OU mensagem de vazio")
        WebDriverWait(self.driver, 3).until(
            EC.any_of(
                EC.presence_of_element_located((By.XPATH, self.path + "//" + tag_table)),
                EC.presence_of_element_located((By.XPATH, self.path + "//*[contains(text(),'Nenhum')]")),
            )
        )


    # def funct_click(self):
    #     return self.funct_all(lambda: self._click())
    
    # def funct_click_texto(self):
    #     return self.funct_all(lambda: self._click_texto())
    
    # def funct_keys(self):
    #     return self.funct_all(lambda: self._keys())
    
    # def funct_key_single(self):
    #     return self.funct_all(lambda: self._key_single())
    
    # def funct_locate(self):
    #     return self.funct_all(lambda: self._locate())
    
    # def funct_scroll(self):
    #     return self.funct_all(lambda: self._scroll())
    
    # def funct_get_select(self):
    #     return self.funct_all(lambda: self._get_select())
    
    # def funct_select_value(self):
    #     return self.funct_all(lambda: self._select_value())
    
    # def funct_checkbox(self):
    #     return self.funct_all(lambda: self._checkbox())
    
    # def funct_wait_df_or_empty(self):
    #     return self.funct_all(lambda: self._wait_df_or_empty())

    def processo_tempo_pecorrido(self):
        self.time_end = time.perf_counter() - self.time_start
        if self.time_end >= self.time_total_set:
            self.msn_padrao()
            log = Log()
            log.path_all_log = self.path_all_log 
            log.write_log = self.text
            log.escrever()
            print(self.text)
            return True
        return False

    def processo_repetir_tarefa(self):
        self.repetir -= 1
        if self.repetir <= 0:
            return False
        self.segundo = 0
        return True
    
    def process_tag(self):
        if self.tag == tag_text:
            self.dados = self.dados.text.strip()
        elif self.tag == tag_table:
            tabela = []
            for tr in self.dados.find_all(tag_tr):
                linha = [td.get_text(strip=True) for td in tr.find_all([tag_td, tag_th])]
                tabela.append(linha)
            self.dados = tabela
        elif self.tag == tag_span:
            self.dados = self.dados.text.strip()
        elif self.tag == tag_img:
            self.dados = self.dados.get("src")
        elif self.tag == tag_attr:
            self.dados = self.dados.get(self.atributo, None)
        self.tag = None


    # =============================== FUNÇÃO PRINCIPAL ===============================
    def funct(self):
        self.time_start = time.perf_counter()
        self.dados = None
        self.error = None
        while True:
            self.wait_loading_invisiblility()
            self.wait_modal_invisiblility()
            try: 
                self.wait_path_visibility()
            except self.excecao as e:
                self.e = e
                self.msn_sys_exit()
            # print(f'self.path: {self.path}')
            if self.path:
                func_ = self.acoes.get(self.faz)
                if func_:
                    # sair = func_()
                    sair = self.funct_all(func_)
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

            # if self.processo_present_screen():
            #     self.error = True
            #     break

        self._apply_reset_defaults()

        if self.error:
            return False
        
        if self.dados:
            self.process_tag()
            return self.dados
        
        return True



if __name__ == '__main__':
    import main
    # main()