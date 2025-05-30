from features.helpers.driver import get_driver
from selenium.webdriver.common.by import By
from time import sleep

URL = "https://rahulshettyacademy.com/seleniumPractise/#/"

def acessar_pagina_principal():
    driver = get_driver()
    driver.get(URL)

def clicar_em_top_ofertas():
    driver = get_driver()
    botao = driver.find_element(By.CSS_SELECTOR, "a[href*='offers']")
    botao.click()
    sleep(1)

def esta_na_pagina_de_promocoes():
    driver = get_driver()
    abas = driver.window_handles

    if len(abas) > 1:
        driver.switch_to.window(abas[-1])

    print(f"URL atual na nova aba: {driver.current_url}")
    return "offers" in driver.current_url
