# ============================================================
# CONTROLE DE EXECUÇÃO / JUMPS
# ============================================================

jump_clickvenda = False
jump_newcon = False

jump_clickvenda = True
# jump_newcon = True


# ============================================================
# CHROMEDRIVER / AUTOMAÇÃO
# ============================================================

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


# ============================================================
# PARÂMETROS DE NEGÓCIO
# ============================================================

mesQuantidade = 5
menor_g_newcon = 2953
# menor_g_newcon = 3319
maior_g_newcon = 10000
# maior_g_newcon = 3320


# ============================================================
# LIMITES / CONTROLE 360
# ============================================================

nTab360Infinuto = True   # se pegar a cota no 360 não precisa limitar o newcon
nMaximoTab360 = 1       # número máximo de tabelas no 360


# ============================================================
# VARIÁVEIS DE PADRÃO / NOMENCLATURA
# ============================================================

underscore = '_'
pasta = ''

datas = 'datas/'
# tabelas = 'Tabelas/'
logs = 'logs/'
src = 'src/'

arq_log = 'log'
ext_Log = '.txt'

ext_Xlsx = '.xlsx'
ext_CSV = '.csv'
ext_JSON = '.json'

arq_df = 'df' + underscore
arq_json = 'json' + underscore

arq_df_clickvenda = arq_df + 'clickvenda'
arq_df_newcon = arq_df + 'newcon'

arq_json_clickvenda = arq_json + 'clickvenda'
arq_json_newcon = arq_json + 'newcon'
tratado = underscore + 'tratado'
sorteio = underscore + "sorteio"

p_df = pasta + datas
p_log = pasta + logs



prazo = 'Prazo'
realizadas = 'Realizadas'
a_realizar = 'A_Realizar'

# ============================================================
# VARIÁVEIS DE CONTROLE – SITES / LOGIN
# ============================================================

site360 = "https://www.disal360.com.br/Acesso/Entrar"
usuario360 = '08171710379'
senha360 = '36vad28'


loading = 'loading'
user = 'user'
password = 'password'
btn_open = 'btn_open'
modal = 'modal'
btn_modal = 'btn_modal'



info_clickvenda = {
    'site': 'https://clickvenda.app/Acesso/Entrar',
    user: '05787535375',
    password: '123456',
    'log': 'log_site',
    'navegate_start': 'navegate_start_clickvend',
    'navegate': 'navegate_clickvend',
    'read': 'read_arq',
    'arq': p_df + arq_df + 'clickvenda' + ext_JSON
}


info_newcon = {
    'site': 'https://web.disalconsorcio.com.br/',
    user: '0000995789',
    password: 'Select@1425',
    'log': 'log_site',
    'navegate_start': 'navegate_start_newcon',
    'navegate': 'navegate_newcon',
    'read': 'read_newcon',
    'arq': p_df + arq_df + 'newcon' + ext_JSON
}


# ============================================================
# PATHS DE SAÍDA
# ============================================================

path_clickvenda_json = p_df + arq_json_clickvenda + ext_JSON

path_newcon_json = p_df + arq_json_newcon + ext_JSON
path_newcon_tratado_json = p_df + arq_json_newcon + tratado + ext_JSON

path_newcon_sorteio_json =  p_df + arq_json_newcon + sorteio + ext_JSON


# ============================================================
# CONSTANTES DE DOMÍNIO / STATUS
# ============================================================



# grupo = 'grupo'

info = 'info'
conf = 'conf'
desc = 'desc'
canc = 'canc'
apur = 'apur'

grupo = 'Grupo'
confirmada = 'confirmada'
cancelada = 'cancelada'
desclassificada = 'desclassificada'
apurada = 'apurada'
lance = 'Lance'
num_prox_assembleia = 'Num_Prox_Assembleia'
dt_prox_assembleia = 'Dt_Prox_Assembleia'
dt_prox_vencimento = 'Dt_Prox_Vencimento'
dt_prox_sorteio = 'Dt_Prox_Sorteio'
dt_ex_assembleia = 'Dt_Ex_Assembleia'
ocorrencia = 'Ocorrencia'
total_lance_livre = 'Total_Lance_Livre'
total_lance_fixo = 'Total_Lance_Fixo'
total_sorteio = 'Total_Sorteio'

contemplacao = 'id_CP'
contemplacao_2 = 'id_subs'
resultado_de_assembleia = 'id_ctl00_Conteudo_ctl00_tvwMenut1'
input_grupo = 'id_ctl00_Conteudo_edtCD_Grupo'
btn_confirmar = 'id_ctl00_Conteudo_btnOK'

btn_retorna_uma_assembleia = 'id_ctl00_Conteudo_btnRetornaAssembleia'
# df_confirmadas_2 = 'id_ctl00_Conteudo_div_Confirmadas'
df_confirmadas = 'id_ctl00_Conteudo_grdContemplacoes_Confirmadas'

btn_confirmadas_canceladas = 'id_ui_id_8'
df_confirmadas_canceladas = 'id_ctl00_Conteudo_grdContemplacoes_Confirmadas_Canceladas'

btn_desclassificadas = 'id_ui_id_9'
df_desclassificadas  = 'id_ctl00_Conteudo_div_Desclassificadas'

btn_sequencia_de_apuracao = 'id_ctl00_Conteudo_btnCotasSorteadas'


# ============================================================
# CHAVES DE CONTROLE
# ============================================================

key_controle = 'key_controle'
# key_controle_1 = 'key controle 1'
# key_controle_2 = 'key controle 2'
# key_controle_3 = 'key controle 3'
# key_controle_4 = 'key controle 4'


# ============================================================
# LISTAS DE COLUNAS / DATAFRAME
# ============================================================

list_column_join = ['Vr. Lance', '% Lance']

list_column_specifies_assemble = [
    'Dt. Contemplação',
    'Dts. Confirmações',
    'Desclassifica',
    lance
]

list_column_del = [
    'Cota',
    'Bem',
    'Filial',
    'Pto.',
    'controle',
    'Confirmação',
    'Sequência'
]


# ============================================================
# PATHS – CLICKVENDA
# ============================================================

path_clickvenda = {
    loading: '//*[@id="loading"]',
    user: '//*[@id="CPF"]',
    password: '//*[@id="Senha"]',
    btn_open: '//*[@id="btn-entrar"]',
    modal: '//*[@id="md-avisos-vendedor"]/div',
    btn_modal: '//*[@id="btn-confirmar-aviso"]',
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

# ============================================================
# PATHS – NEWCON
# ============================================================

path_newcon = {
    loading: '//*[@id="divLoading"]',
    user: '//*[@id="edtUsuario"]',
    password: '//*[@id="edtSenha"]',
    btn_open: '//*[@id="btnLogin"]',

    contemplacao: '//*[@id="CP"]',
    contemplacao_2: '//*[@id="subs"]/ul/li[2]/a',
    resultado_de_assembleia: '//*[@id="ctl00_Conteudo_ctl00_tvwMenut1"]',
    input_grupo: '//*[@id="ctl00_Conteudo_edtCD_Grupo"]',
    btn_confirmar: '//*[@id="ctl00_Conteudo_btnOK"]',

    prazo: '//*[@id="ctl00_Conteudo_lblPZ_Comercializacao"]',
    realizadas: '//*[@id="ctl00_Conteudo_lblQT_Assembleia_Realizada"]',
    a_realizar: '//*[@id="ctl00_Conteudo_lblQT_Assembleia_ARealizar"]',
    num_prox_assembleia: '//*[@id="ctl00_Conteudo_lblNO_Prox_Assembleia"]',
    dt_prox_assembleia: '//*[@id="ctl00_Conteudo_lblDT_Prox_Assembleia"]',
    dt_prox_vencimento: '//*[@id="ctl00_Conteudo_lblDT_Prox_Vencimento"]',
    dt_prox_sorteio: '//*[@id="ctl00_Conteudo_lblDT_Prox_Sorteio"]',

    total_lance_livre: '//*[@id="ctl00_Conteudo_lblTotalLL"]',
    total_lance_fixo: '//*[@id="ctl00_Conteudo_lblTotalLF"]',
    total_sorteio: '//*[@id="ctl00_Conteudo_lblTotalSO"]',
    
    dt_ex_assembleia: '//*[@id="ctl00_Conteudo_lblDT_Assembleia_Ex"]',
    ocorrencia: '//*[@id="ctl00_Conteudo_lblOcorrencia"]',

    # 'id_tabs': '//*[@id="tabs"]/ul/li[1]',
    btn_retorna_uma_assembleia: '//*[@id="ctl00_Conteudo_btnRetornaAssembleia"]',

    # df_confirmadas_2: '//*[@id="ctl00_Conteudo_div_Confirmadas"]/div',
    df_confirmadas: '//*[@id="ctl00_Conteudo_grdContemplacoes_Confirmadas"]',

    btn_confirmadas_canceladas: '//*[@id="ui-id-8"]',
    df_confirmadas_canceladas: '//*[@id="ctl00_Conteudo_grdContemplacoes_Confirmadas_Canceladas"]',

    btn_desclassificadas: '//*[@id="ui-id-9"]',
    df_desclassificadas: '//*[@id="ctl00_Conteudo_div_Desclassificadas"]',

    btn_sequencia_de_apuracao: '//*[@id="ctl00_Conteudo_btnCotasSorteadas"]',
}


# ============================================================
# MAPEAMENTOS / DISCIONÁRIOS AUXILIARES
# ============================================================

list_path_info = [ prazo, realizadas, a_realizar, num_prox_assembleia, dt_prox_assembleia, dt_prox_vencimento, dt_prox_sorteio, total_lance_livre, total_lance_fixo, total_sorteio ]
# list_path_sort = [ ocorrencia, dt_ex_assembleia ]

btns_df_newcon = {
    conf: '',
    canc: btn_confirmadas_canceladas,
    desc: btn_desclassificadas,
    apur: btn_sequencia_de_apuracao,
}

df_newcon = {
    conf: df_confirmadas,
    canc: df_confirmadas_canceladas,
    desc: df_desclassificadas,
    apur: df_confirmadas_canceladas,
}

disc_tabela_newcon = {
    info: '',
    conf: {'tabela': confirmada},
    canc: {'tabela': cancelada},
    desc: {'tabela': desclassificada},
    apur: {'tabela': apurada}
}

disc_msn_newcon = {
    info: '❌  MAIN: O discionario de informações esta retornando vazio, já mais é para não ter as informações. Do grupo:',
    conf: '⁉️  MAIN: O discionario de confirmadas esta retornando vazio, pode acontecer em poucos casos, continuar no grupo:',
    canc: '⁉️  MAIN: O discionario de canceladas esta retornando vazio, pode acontecer continuar no grupo:',
    desc: '⁉️  MAIN: O discionario de desclassificados esta retornando vazio, pode acontecer continuar no grupo:',
    apur: '⁉️  MAIN: O discionario de apurações esta retornando vazio, pode acontecer continuar no grupo:'
}


# ============================================================
# TAGS HTML
# ============================================================

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


# ============================================================
# MAIN
# ============================================================

if __name__ == '__main__':
    import main
    # main()


# # VARIAVEIS DE CONTROL
# site360 = "https://www.disal360.com.br/Acesso/Entrar"
# usuario360 = '08171710379'
# senha360 = '36vad28'



# info_clickvenda = {
#     'site': 'https://clickvenda.app/Acesso/Entrar',
#     user: '62437942378',
#     password: '123456',
#     'log': 'log_site',
#     'navegate_start': 'navegate_start_clickvend',
#     'navegate': 'navegate_clickvend',
#     'read': 'read_arq',
#     'arq': p_df + arq_df + 'clickvenda' + ext_JSON
# }



# jump_clickvenda = False
# jump_newcon = False

# # jump_clickvenda = True
# # jump_newcon = True


# # variaveis 

# underscore = '_'
# pasta = ''
# tabelas = 'Tabelas/'
# logs = 'Logs/'
# arq_log = 'log'
# ext_Log = '.txt'
# arq_df = 'df' + underscore
# arq_json = 'json' + underscore
# arq_df_clickvenda = arq_df + 'clickvenda'
# arq_df_newcon = arq_df + 'newcon'
# arq_json_clickvenda = arq_json + 'clickvenda'
# arq_json_newcon = arq_json + 'newcon'
# tratado = underscore + 'tratado'
# ext_Xlsx = '.xlsx'
# ext_CSV = '.csv'
# ext_JSON = '.json'
# p_df = pasta + tabelas
# p_log = pasta + logs


# grupo = 'grupo'

# info = 'info'
# conf = 'conf'
# desc = 'desc'
# canc = 'canc'
# apur = 'apur'
# confirmada = 'confirmada'
# cancelada = 'cancelada'
# desclassificada = 'desclassificada'
# apurada = 'apurada'

# key_controle_1 = 'key controle 1'
# key_controle_2 = 'key controle 2'
# key_controle_3 = 'key controle 3'
# key_controle_4 = 'key controle 4'


# list_column_join = ['Vr. Lance', '% Lance']
# list_column_specifies_assemble = ['Dt. Contemplação', 'Dts. Confirmações', 'Desclassifica', 'Lance']
# list_column_del = ['Cota', 'Bem', 'Filial', 'Pto.', 'controle', 'Confirmação', 'Sequência']




# # variavels do chrmeDriveauto
# list_kill_proc = ["chromedriver.exe", "chrome.exe"]
# dict_url_download_google = {
#     'base': "https://storage.googleapis.com/chrome-for-testing-public/",
#     'driver_zip': "/win64/chromedriver-win64.zip", 
#     'chrome_zip': "/win64/chrome-win64.zip"
# }
# path_driver_zip = "driver.zip"
# path_chrome_zip = "chrome.zip"
# extract_path = "driver"
# if_not_exist_version_chrome = "142.0.7444.122"




#     # user: '0000926979',
#     # password: 'Dp@9685',

#     # usuario da debora:
#     # user: '0000926979',
#     # password: 'Dp@1425',


# info_newcon = {
#     'site': 'https://web.disalconsorcio.com.br/',
#     user: '0000995789',
#     password: 'Select@1425',
#     'log': 'log_site',
#     'navegate_start': 'navegate_start_newcon',
#     'navegate': 'navegate_newcon',
#     'read': 'read_newcon',
#     'arq': p_df + arq_df + 'newcon' + ext_JSON
# }

# path_clickvenda = {
#     loading: '//*[@id="loading"]',
#     modal: '//*[@id="md-avisos-vendedor"]/div',
#     btn_modal: '//*[@id="btn-confirmar-aviso"]',
#     user: '//*[@id="CPF"]',
#     password: '//*[@id="Senha"]',
#     btn_open: '//*[@id="btn-entrar"]',
#     'btn_nova_venda': '/html/body/div[4]/main/header/div/div[1]/nav/ul/li[2]/a',
#     'btn_automovel': '/html/body/div[4]/main/header/div/div[1]/nav/ul/li[2]/ul/li/a',
#     'btn_selecionar': '/html/body/div[4]/main/div/div/table/tbody/tr[2]/td[3]/a',
#     'btn_parcela': '//*[@id="divPasso1"]/div/div[1]/div/label[2]',
#     'id_divPasso1': '//*[@id="divPasso1"]/div/div[2]/div/div[1]/div/input',
#     'busca_andamento_plano': '//*[@id="busca_andamento_plano"]',
#     'credito_referenciado': '//*[@id="divPasso1"]/div/div[2]/div/div[4]/div/input',
#     'busca_andamento_modelo': '//*[@id="busca_andamento_modelo"]',
#     'btn_buscar': '//*[@id="divPasso1"]/div/div[2]/div/div[5]/div[3]/div/input',
#     'id_divPasso21': '//*[@id="divPasso21"]',
#     'id_divPasso21_divs': '//*[@id="divPasso21"]/div/div/div/div/div/table/tbody',
#     'id_divPasso21_table': '//*[@id="divPasso21"]/div/div/div/div/div/table',
# }



# path_newcon = {
#     loading: '//*[@id="divLoading"]',
#     user: '//*[@id="edtUsuario"]',
#     password: '//*[@id="edtSenha"]',
#     btn_open: '//*[@id="btnLogin"]',
#     contemplacao: '//*[@id="CP"]',
#     contemplacao_2: '//*[@id="subs"]/ul/li[2]/a',
#     resultado_de_assembleia: '//*[@id="ctl00_Conteudo_ctl00_tvwMenut1"]',
#     input_grupo: '//*[@id="ctl00_Conteudo_edtCD_Grupo"]',
#     btn_confirmar: '//*[@id="ctl00_Conteudo_btnOK"]',

#     'PZ_Comercializacao': '//*[@id="ctl00_Conteudo_lblPZ_Comercializacao"]',
#     'QT_Assembleia_Realizada': '//*[@id="ctl00_Conteudo_lblQT_Assembleia_Realizada"]',
#     'QT_Assembleia_ARealizar': '//*[@id="ctl00_Conteudo_lblQT_Assembleia_ARealizar"]',
#     'DT_Prox_Assembleia': '//*[@id="ctl00_Conteudo_lblDT_Prox_Assembleia"]',
#     'DT_Prox_Vencimento': '//*[@id="ctl00_Conteudo_lblDT_Prox_Vencimento"]',

#     # df_confirmadas: '//*[@id="ctl00_Conteudo_grdContemplacoes_Confirmadas"]',

#     'id_tabs': '//*[@id="tabs"]/ul/li[1]',

#     btn_retorna_uma_assembleia: '//*[@id="ctl00_Conteudo_btnRetornaAssembleia"]',
    
#     df_confirmadas_2: '//*[@id="ctl00_Conteudo_div_Confirmadas"]/div',
#     df_confirmadas: '//*[@id="ctl00_Conteudo_grdContemplacoes_Confirmadas"]',
   

#     btn_confirmadas_canceladas: '//*[@id="ui-id-8"]',
#     df_confirmadas_canceladas: '//*[@id="ctl00_Conteudo_grdContemplacoes_Confirmadas_Canceladas"]',

#     # 'id_ctl00_Conteudo_tabDesclassificadas': '//*[@id="ctl00_Conteudo_tabDesclassificadas"]',
#     btn_desclassificadas: '//*[@id="ui-id-9"]',
#     df_desclassificadas: '//*[@id="ctl00_Conteudo_div_Desclassificadas"]',

#     btn_sequencia_de_apuracao: '//*[@id="ctl00_Conteudo_btnCotasSorteadas"]',


#     # df_desclassificadas: '//*[@id="ctl00_Conteudo_div_Desclassificadas"]/div[1]' ,
#     # '//*[@id="tabs-2"]'
#     # '//*[@id="tabs-1"]'
    
# }




# btns_df_newcon = {
#     conf: '',
#     canc: btn_confirmadas_canceladas,
#     desc: btn_desclassificadas,
#     apur: btn_sequencia_de_apuracao,
# }

# df_newcon = {
#     conf: df_confirmadas,
#     canc: df_confirmadas_canceladas,
#     desc: df_desclassificadas,
#     apur: df_confirmadas_canceladas,
# }



# disc_tabela_newcon = {
#     info: '',
#     conf: {'tabela': confirmada}, 
#     canc: {'tabela': cancelada},
#     desc: {'tabela': desclassificada}, 
#     apur: {'tabela': apurada} 
# }

# disc_msn_newcon ={
#     info: f'❌  MAIN: O discionario de informações esta retornando vazio, já mais é para não ter as informações. Do grupo:',
#     conf: f'⁉️  MAIN: O discionario de confirmadas esta retornando vazio, pode acontecer em poucos casos, continuar no grupo:', 
#     canc: f'⁉️  MAIN: O discionario de canceladas esta retornando vazio, pode acontecer continuar no grupo:',
#     desc: f'⁉️  MAIN: O discionario de desclassificados esta retornando vazio, pode acontecer continuar no grupo:', 
#     apur: f'⁉️  MAIN: O discionario de apurações esta retornando vazio, pode acontecer continuar no grupo:'              
# }


# tag_table = 'table'
# tag_tbody = 'tbody'
# tag_tr = 'tr'
# tag_td = 'td'
# tag_th = 'th'
# tag_option = 'option'
# tag_value = 'value'
# tag_text = 'text'

# tag_span = 'span'
# tag_img = 'img'
# tag_attr = 'attr'



# mesQuantidade = 3
# # menor_g_newcon = 2626
# menor_g_newcon = 2953
# maior_g_newcon = 10000




# # Limitar os 360?
# # nTab360Infinuto = False
# nTab360Infinuto = True  # o 360 que se pegar a cota entâo nao precisa limitar o newcon
# nMaximoTab360 = 1   # ira pegar numero n de tabelas no 360

# # VARIAVEIS



# path_clickvenda_json = p_df + arq_json_clickvenda + ext_JSON

# path_newcon_json = p_df + arq_json_newcon + ext_JSON
# path_newcon_tratado_json = p_df + arq_json_newcon + tratado + ext_JSON



# # ap = 'newcon' + underscore

# # apur = 'apur' + underscore
# # conf = 'conf' + underscore
# # desc = 'desc' + underscore
# # apur = 'apur' + underscore
# # info = 'info' + underscore

# # arq_conf = p_df + arq_df + ap + conf + 'bruto' + ext_CSV
# # arq_desc = p_df + arq_df + ap + desc + 'bruto' + ext_CSV
# # arq_apur = p_df + arq_df + ap + apur + 'bruto' + ext_CSV
# # arq_info = p_df + arq_df + ap + info + 'bruto' + ext_CSV

# # arq_conf_tratadas = p_df + arq_df + ap + conf + 'tratar' + ext_CSV
# # arq_desc_tratadas = p_df + arq_df + ap + desc + 'tratar' + ext_CSV
# # arq_apur_tratadas = p_df + arq_df + ap + apur + 'tratar' + ext_CSV
# # arq_info_tratadas = p_df + arq_df + ap + info + 'tratar' + ext_CSV

# # arq_df_xlsx = p_df + arq_df + ext_Xlsx
# # arq_df_csv = p_df + arq_df + ext_CSV

# # arq_df_2_xlsx = p_df + arq_df + '_2' + ext_Xlsx
# # arq_df_2_csv = p_df + arq_df + '_2' + ext_CSV


# if __name__ == '__main__':
#     import main
#     # main()
