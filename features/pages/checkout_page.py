from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def place_order(self):
        place_order_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")))
        place_order_button.click()

    def selecionar_pais(self, pais):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Place Order']"))).click()
        dropdown = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "select")))
        dropdown.find_element(By.XPATH, f"//option[text()='{pais}']").click()

    def aceitar_termos(self):
        checkbox = self.driver.find_element(By.CLASS_NAME, "chkAgree")
        checkbox.click()

    def clicar_em_proceed(self):
        self.driver.find_element(By.XPATH, "//button[text()='Proceed']").click()

    def mensagem_de_sucesso(self):
        return self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "wrapperTwo"))).text
