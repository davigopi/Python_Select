underscore = '_'
pasta = ''
tabelas = 'Tabelas/'
logs = 'Logs/'
arq_log = 'log'
ext_Log = '.txt'
arq_df = 'df' + underscore
arq_json = 'json' + underscore
arq_df_clickvenda = arq_df + 'clickvenda'
arq_df_newcon = arq_df + 'newcon'
arq_json_clickvenda = arq_json + 'clickvenda'
arq_json_newcon = arq_json + 'newcon'
tratado = underscore + 'tratado'
ext_Xlsx = '.xlsx'
ext_CSV = '.csv'
ext_JSON = '.json'
p_df = pasta + tabelas
p_log = pasta + logs

# variavels do chrmeDriveauto
list_kill_proc = ["chromedriver.exe", "chrome.exe"]
dict_url_download_google = {
    'base': "https://storage.googleapis.com/chrome-for-testing-public/",
    'driver_zip': "/win64/chromedriver-win64.zip", 
    'chrome_zip': "/win64/chrome-win64.zip"
}
path_driver_zip = "driver.zip"
path_chrome_zip = "chrome.zip"
extract_path = "driver"
if_not_exist_version_chrome = "142.0.7444.122"


# VARIAVEIS DE CONTROL
site360 = "https://www.disal360.com.br/Acesso/Entrar"
usuario360 = '08171710379'
senha360 = '36vad28'



info_clickvenda = {
    'site': 'https://clickvenda.app/Acesso/Entrar',
    'user': '62437942378',
    'password': '123456',
    'log': 'log_site',
    'navegate_start': 'navegate_start_clickvend',
    'navegate': 'navegate_clickvend',
    'read': 'read_clickvend',
    'arq': p_df + arq_df + 'clickvenda' + ext_JSON
}

    # 'user': '0000926979',
    # 'password': 'Dp@9685',

info_newcon = {
    'site': 'https://web.disalconsorcio.com.br/',
    'user': '0000995789',
    'password': '2520@Select',
    'log': 'log_site',
    'navegate_start': 'navegate_start_newcon',
    'navegate': 'navegate_newcon',
    'read': 'read_newcon',
    'arq': p_df + arq_df + 'newcon' + ext_JSON
}

path_clickvenda = {
    'loading': '//*[@id="loading"]',
    'modal': '//*[@id="md-avisos-vendedor"]/div',
    'modal_btn': '//*[@id="btn-confirmar-aviso"]',
    'user': '//*[@id="CPF"]',
    'password': '//*[@id="Senha"]',
    'btn_open': '//*[@id="btn-entrar"]',
    'btn_nova_venda': '/html/body/div[4]/main/header/div/div[1]/nav/ul/li[2]/a',
    'btn_automovel': '/html/body/div[4]/main/header/div/div[1]/nav/ul/li[2]/ul/li/a',
    'btn_selecionar': '/html/body/div[4]/main/div/div/table/tbody/tr[2]/td[3]/a',
    'btn_parcela': '//*[@id="divPasso1"]/div/div[1]/div/label[2]',
    'id_divPasso1': '//*[@id="divPasso1"]/div/div[2]/div/div[1]/div/input',
    'busca_andamento_plano': '//*[@id="busca_andamento_plano"]',
    'credito_referenciado': '//*[@id="divPasso1"]/div/div[2]/div/div[4]/div/input',
    'busca_andamento_modelo': '//*[@id="busca_andamento_modelo"]',
    'btn_buscar': '//*[@id="divPasso1"]/div/div[2]/div/div[5]/div[3]/div/input',
    'id_divPasso21': '//*[@id="divPasso21"]',
    'id_divPasso21_divs': '//*[@id="divPasso21"]/div/div/div/div/div/table/tbody',
    'id_divPasso21_table': '//*[@id="divPasso21"]/div/div/div/div/div/table',
}



path_newcon = {
    'loading': '//*[@id="divLoading"]',
    'user': '//*[@id="edtUsuario"]',
    'password': '//*[@id="edtSenha"]',
    'btn_open': '//*[@id="btnLogin"]',
    'id_CP': '//*[@id="CP"]',
    'id_subs': '//*[@id="subs"]/ul/li[2]/a',
    'id_ctl00_Conteudo_ctl00_tvwMenut1': '//*[@id="ctl00_Conteudo_ctl00_tvwMenut1"]',
    'id_ctl00_Conteudo_edtCD_Grupo': '//*[@id="ctl00_Conteudo_edtCD_Grupo"]',
    'id_ctl00_Conteudo_btnOK': '//*[@id="ctl00_Conteudo_btnOK"]',

    'id_ctl00_Conteudo_lblPZ_Comercializacao': '//*[@id="ctl00_Conteudo_lblPZ_Comercializacao"]',
    'id_ctl00_Conteudo_lblQT_Assembleia_Realizada': '//*[@id="ctl00_Conteudo_lblQT_Assembleia_Realizada"]',
    'id_ctl00_Conteudo_lblQT_Assembleia_ARealizar': '//*[@id="ctl00_Conteudo_lblQT_Assembleia_ARealizar"]',
    'id_ctl00_Conteudo_lblDT_Prox_Assembleia': '//*[@id="ctl00_Conteudo_lblDT_Prox_Assembleia"]',
    'id_ctl00_Conteudo_lblDT_Prox_Vencimento': '//*[@id="ctl00_Conteudo_lblDT_Prox_Vencimento"]',

    'id_ctl00_Conteudo_grdContemplacoes_Confirmadas': '//*[@id="ctl00_Conteudo_grdContemplacoes_Confirmadas"]',

    'id_tabs': '//*[@id="tabs"]/ul/li[1]',

    'id_ctl00_Conteudo_btnRetornaAssembleia': '//*[@id="ctl00_Conteudo_btnRetornaAssembleia"]',
    
    'id_ctl00_Conteudo_div_Confirmadas': '//*[@id="ctl00_Conteudo_div_Confirmadas"]/div',

    'id_ui_id_8': '//*[@id="ui-id-8"]',
    'id_ctl00_Conteudo_grdContemplacoes_Confirmadas_Canceladas': '//*[@id="ctl00_Conteudo_grdContemplacoes_Confirmadas_Canceladas"]',

    # 'id_ctl00_Conteudo_tabDesclassificadas': '//*[@id="ctl00_Conteudo_tabDesclassificadas"]',
    'id_ui_id_9': '//*[@id="ui-id-9"]',
    'id_ctl00_Conteudo_div_Desclassificadas': '//*[@id="ctl00_Conteudo_div_Desclassificadas"]',

    'id_ctl00_Conteudo_btnCotasSorteadas': '//*[@id="ctl00_Conteudo_btnCotasSorteadas"]',


    # 'id_ctl00_Conteudo_div_Desclassificadas': '//*[@id="ctl00_Conteudo_div_Desclassificadas"]/div[1]' ,
    # '//*[@id="tabs-2"]'
    # '//*[@id="tabs-1"]'
    
}

disc_path_info = {
    'prazo': 'id_ctl00_Conteudo_lblPZ_Comercializacao', 
    'realizadas': 'id_ctl00_Conteudo_lblQT_Assembleia_Realizada',
    'arealizar': 'id_ctl00_Conteudo_lblQT_Assembleia_ARealizar',
    'assembleia': 'id_ctl00_Conteudo_lblDT_Prox_Assembleia',
    'vencimento': 'id_ctl00_Conteudo_lblDT_Prox_Vencimento'
}


tag_table = 'table'
tag_tbody = 'tbody'
tag_tr = 'tr'
tag_td = 'td'
tag_th = 'th'
tag_option = 'option'
tag_value = 'value'
tag_text = 'text'

tag_span = 'span'
tag_img = 'img'
tag_attr = 'attr'



mesQuantidade = 3
# menor_g_newcon = 2626
menor_g_newcon = 2953
maior_g_newcon = 10000

jump_clickvenda = False
jump_newcon = False

jump_clickvenda = True
# jump_newcon = True


# Limitar os 360?
# nTab360Infinuto = False
nTab360Infinuto = True  # o 360 que se pegar a cota entâo nao precisa limitar o newcon
nMaximoTab360 = 1   # ira pegar numero n de tabelas no 360

# VARIAVEIS



arq_clickvenda = p_df + arq_json_clickvenda + ext_JSON

arq_newcon = p_df + arq_json_newcon + ext_JSON
arq_newcon_tratado = p_df + arq_json_newcon + tratado + ext_JSON

ap = 'newcon' + underscore

apur = 'apur' + underscore
conf = 'conf' + underscore
desc = 'desc' + underscore
apur = 'apur' + underscore
info = 'info' + underscore

arq_conf = p_df + arq_df + ap + conf + 'bruto' + ext_CSV
arq_desc = p_df + arq_df + ap + desc + 'bruto' + ext_CSV
arq_apur = p_df + arq_df + ap + apur + 'bruto' + ext_CSV
arq_info = p_df + arq_df + ap + info + 'bruto' + ext_CSV

arq_conf_tratadas = p_df + arq_df + ap + conf + 'tratar' + ext_CSV
arq_desc_tratadas = p_df + arq_df + ap + desc + 'tratar' + ext_CSV
arq_apur_tratadas = p_df + arq_df + ap + apur + 'tratar' + ext_CSV
arq_info_tratadas = p_df + arq_df + ap + info + 'tratar' + ext_CSV

arq_df_xlsx = p_df + arq_df + ext_Xlsx
arq_df_csv = p_df + arq_df + ext_CSV

arq_df_2_xlsx = p_df + arq_df + '_2' + ext_Xlsx
arq_df_2_csv = p_df + arq_df + '_2' + ext_CSV


if __name__ == '__main__':
    import main
    # main()
