from features.helpers.driver import get_driver
from features.pages.base_page import *
from selenium.webdriver.support.ui import Select
import time

# Definindo a variável para pegar a URL do site
URL = "https://rahulshettyacademy.com/seleniumPractise/#/"

# Acessando site
def acessar_site():
    driver = get_driver()
    driver.get(URL)

# Página carregada
def pagina_carregada():
    driver = get_driver()
    time.sleep(2)
    produtos = driver.find_elements(By.CLASS_NAME, "products")
    return len(produtos) > 0

# Clicar ADD TO CART
def clicar_add_to_cart():
    driver = get_driver()
    botao = driver.find_element(By.XPATH, "//button[text()='ADD TO CART']")
    botao.click()
    return botao

# Verificar texto do botão = ADDED
def verificar_texto_do_botao():
    driver = get_driver()
    try:
        botao = WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element((By.XPATH, "//button[contains(text(),'✔ ADDED')]"), "✔ ADDED")
        )
        return botao
    except:
        return False
    
# Clicar no ícone do carrinho e verificar se está vazio
def acessar_carrinho_e_verificar_se_estiver_vazio():
    driver = get_driver()

    # Clica no ícone do carrinho
    icone = driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']")
    icone.click()
    time.sleep(1)

    # Verifica se o carrinho está vazio
    if "Your cart is empty!" in driver.page_source:
        print("Carrinho está vazio. Checkout não será clicado.")
        return False

    # Verifica se o botão está visualmente desativado pela classe
    botao_checkout = driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")
    if "disabled" in botao_checkout.get_attribute("class"):
        print("Botão de checkout está desativado visualmente.")
        return False

    # Clica no botão se estiver visível e habilitado
    botao_checkout.click()
    return True
    