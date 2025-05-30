from features.helpers.driver import get_driver
from selenium.webdriver.common.by import By
from time import sleep

URL = "https://rahulshettyacademy.com/seleniumPractise/#/offers"

def acessar_pagina_ofertas():
    driver = get_driver()
    driver.get(URL)

def digitar_pesquisa_invalida():
    driver = get_driver()
    campo = driver.find_element(By.ID, "search-field")
    campo.clear()
    campo.send_keys("kiwi") 
    sleep(1)

def verificar_mensagem_no_data():
    driver = get_driver()
    elemento = driver.find_element(By.TAG_NAME, "td")

    return "No data" in elemento.text
