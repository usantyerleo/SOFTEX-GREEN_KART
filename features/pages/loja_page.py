from features.helpers.driver import get_driver
from features.pages.base_page import *
from selenium.webdriver.support.ui import Select
import time


URL = "https://rahulshettyacademy.com/seleniumPractise/#/"


def acessar_site():
    driver = get_driver()
    driver.get(URL)


def pagina_carregada():
    driver = get_driver()
    time.sleep(2)
    produtos = driver.find_elements(By.CLASS_NAME, "products")
    return len(produtos) > 0


def clicar_add_to_cart():
    driver = get_driver()
    botao = driver.find_element(By.XPATH, "//button[text()='ADD TO CART']")
    botao.click()
    return botao


def verificar_texto_do_botao():
    driver = get_driver()
    try:
        botao = WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element((By.XPATH, "//button[contains(text(),'✔ ADDED')]"), "✔ ADDED")
        )
        return botao
    except:
        return False
    

def acessar_carrinho_e_verificar_se_estiver_vazio():
    driver = get_driver()


    icone = driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']")
    icone.click()
    time.sleep(1)

    if "Your cart is empty!" in driver.page_source:
        print("Carrinho está vazio. Checkout não será clicado.")
        return False

   
    botao_checkout = driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")
    if "disabled" in botao_checkout.get_attribute("class"):
        print("Botão de checkout está desativado visualmente.")
        return False

    
    botao_checkout.click()
    return True
    