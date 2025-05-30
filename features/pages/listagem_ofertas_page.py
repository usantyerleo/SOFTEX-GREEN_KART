from features.helpers.driver import get_driver
from selenium.webdriver.common.by import By
from time import sleep

URL = "https://rahulshettyacademy.com/seleniumPractise/#/offers"

ITEM = "banana"

def acessar_pagina_de_ofertas():
    driver = get_driver()
    driver.get(URL)

def digitar_pesquisa_valida():
    driver = get_driver()
    campo = driver.find_element(By.ID, "search-field")
    campo.clear()
    campo.send_keys(ITEM)
    sleep(1)

def produtos_listados():
    driver = get_driver()
    produtos = driver.find_elements(By.TAG_NAME, "td")

    return len(produtos) and produtos[0].text == ITEM.capitalize()
