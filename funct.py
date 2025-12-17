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
    TimeoutException
)
from bs4 import BeautifulSoup
from log import Log

from var import *

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
            TimeoutException
        )

        self.acoes = {
            None: self.funct_click,
            'click_texto': self.funct_click_texto,
            'keys': self.funct_keys,
            'locate': self.funct_locate,
            'scroll': self.funct_scroll,
            'get_select': self.funct_get_select,
            'select_value': self.funct_select_value,
            'checkbox': self.funct_checkbox,
            'wait_df_or_empty': self.funct_wait_df_or_empty,
            'key_single': self.funct_key_single,
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
        self.msn_padrao()
        self.text += "\n❌ FUNCT: Programa interrompido, pois não há tratamento para este erro.\n\n"
        print(self.text)
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


    def wait_path_located(self):
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, self.path)))

    def wait_path_visibility(self):
         WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.XPATH, self.path)))

    def wait_path_clickable(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, self.path)))
        # time.sleep(0.3)

    def scroll_view_path(self):
        # self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", self.driver.find_element(By.XPATH, self.path))
        header_px = 90
        elem = self.driver.find_element(By.XPATH, self.path)
        self.driver.execute_script("const el=arguments[0]; const rect=el.getBoundingClientRect(); window.scrollBy(0, rect.top - %d - 20);" % header_px, elem)
        
    def funct_click(self):
        try:
            self.wait_path_located()
            self.scroll_view_path()
            self.wait_path_clickable()
            self.driver.find_element(By.XPATH, self.path).click()
            return True
        except self.excecao as e:
            self.e = e
            return False
        except Exception as e:
            self.e = e
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
            self.e = e
            self.msn_sys_exit()

    def funct_keys(self):
        try:
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

    def funct_get_select(self):
        try:
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
            xpath_option = f"{self.path}/{tag_option}[@{tag_value}='{self.value}']"
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
            elemento = self.driver.find_element(By.XPATH, self.path)
            if not elemento.is_selected():
                self.dados = 'OK'
            return True
        except self.excecao as e:
            self.e = e
            return False
        except Exception as e:
            self.e = e
            self.msn_sys_exit()

    def funct_wait_df_or_empty(self):
        try:
            # print("2 — esperar tabela OU mensagem de vazio")
            WebDriverWait(self.driver, 3).until(
                EC.any_of(
                    EC.presence_of_element_located((By.XPATH, self.path + "//" + tag_table)),
                    EC.presence_of_element_located((By.XPATH, self.path + "//*[contains(text(),'Nenhum')]")),
                )
            )
            return True
        except self.excecao as e:
            self.e = e
            return False
        except Exception as e:
            self.e = e
            self.msn_sys_exit()

    def processo_tempo_pecorrido(self):
        self.time_end = time.perf_counter() - self.time_start
        # print(f' tempo pecoccid o é {self.time_end} >=  {self.time_total_set}')
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
            self.wait_path_visibility()
            # print(f'self.path: {self.path}')
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