from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--start-maximized', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,
    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver


driver = iniciar_driver()
driver.get('https://lista.mercadolivre.com.br/celas#D[A:celas]'); sleep(5)

arquivo_csv = open('celas.csv', 'w', encoding='utf-8', newline='')
arquivo_csv.close()
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)'); sleep(60)
    titulos = driver.find_elements(By.XPATH, "//div[@class='ui-search-item__group ui-search-item__group--title shops__items-group']//a//h2")

    precos = driver.find_elements(By.XPATH, "//div[@class='ui-search-item__group ui-search-item__group--price ui-search-item__group--price-grid-container shops__items-group']//div//div//div//span//span[@class='andes-money-amount__fraction']")

    links = driver.find_elements(By.XPATH, "//div[@class='ui-search-item__group ui-search-item__group--title shops__items-group']//a")

    for titulo, preco, link in zip(titulos, precos, links):
        link_processado = link.get_attribute('href')
        with open('celas.csv', 'a', encoding='utf-8', newline='') as arquivo_csv:
            arquivo_csv.write(f'{titulo.text};R${preco.text};{link_processado}\n')

    try:
        proxima_pagina = driver.find_element(By.XPATH, "//li[@class='andes-pagination__button andes-pagination__button--next shops__pagination-button']//a[@class='andes-pagination__link shops__pagination-link ui-search-link']")
        sleep(2)
        proxima_pagina.click(); sleep(10)
    except:
        break

driver.close()