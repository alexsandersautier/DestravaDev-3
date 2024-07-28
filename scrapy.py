from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import datetime
import pytz
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

sao_paulo = pytz.timezone('America/Sao_Paulo')
data_e_hora_sao_paulo = datetime.datetime.now(sao_paulo)


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1920,1080', '--headless']
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

def execute(product = 'Trabalhe 4 horas por semana'):
    try:
        browser = iniciar_driver()

        browser.get('https://www.amazon.com.br/')
        sleep(2)
        search = browser.find_element(By.ID, 'twotabsearchtextbox')
        search.click()
        sleep(1)
        search.send_keys(product)
        search.click()
        bloom = browser.find_element(By.ID, 'nav-search-submit-button')
        bloom.click()
        sleep(1)
        result = browser.find_element(By.XPATH, '//div[@data-cy="title-recipe"]/h2/a/span')
        if 'Trabalhe 4 horas por semana' in result.text:
            div_text = browser.find_element(By.XPATH, '//div[@data-cy="price-recipe"]//div[2]').text
            price = div_text.replace('\n','').split(' ')[0]
            formatted = price[2:4] + '.' + price[4:6]
            link = browser.find_element(By.XPATH, '//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]').get_attribute("href")
            return 'Trabalhe 4 horas por semana', formatted, data_e_hora_sao_paulo.strftime("%d/%m/%Y %H:%M:%S"), link
        browser.close()
    except Exception as e:
        print(e)