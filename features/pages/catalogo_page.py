from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CatalogoPage:
    def __init__(self, driver):
        self.driver = driver
        self.campo_busca = (By.CSS_SELECTOR, "input.search-keyword")
        self.lista_produtos = (By.CSS_SELECTOR, "div.products-wrapper div.product")
        self.botao_carrinho = (By.CSS_SELECTOR, "a.cart-icon")
        self.produtos_carrinho = (By.CSS_SELECTOR, "div.cart-preview.active div.product")
        self.wait = WebDriverWait(driver, 10)

    def carregar_pagina(self):
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

    def buscar_produto(self, nome):
        campo = self.driver.find_element(*self.campo_busca)
        campo.clear()
        campo.send_keys(nome)

    def produtos_exibidos(self):
        self.wait.until(EC.presence_of_all_elements_located(self.lista_produtos))
        return self.driver.find_elements(*self.lista_produtos)

    def adicionar_primeiro_produto_ao_carrinho(self):
        produtos = self.produtos_exibidos()
        if produtos:
            primeiro_produto = produtos[0]
            botao_adicionar = primeiro_produto.find_element(By.CSS_SELECTOR, "div.product-action button")
            botao_adicionar.click()
        else:
            raise Exception("Nenhum produto exibido para adicionar ao carrinho.")

    def adicionar_produto_por_indice(self, indice):
        produtos = self.produtos_exibidos()
        if len(produtos) > indice:
            produto = produtos[indice]
            botao_adicionar = produto.find_element(By.CSS_SELECTOR, "div.product-action button")
            botao_adicionar.click()
        else:
            raise IndexError(f"Índice {indice} fora do intervalo dos produtos exibidos.")

    def texto_botao_primeiro_produto(self):
        produtos = self.produtos_exibidos()
        if produtos:
            primeiro_produto = produtos[0]
            botao = primeiro_produto.find_element(By.CSS_SELECTOR, "div.product-action button")
            return botao.text
        else:
            raise Exception("Nenhum produto exibido para verificar botão.")

    def abrir_carrinho(self):
        self.driver.find_element(*self.botao_carrinho).click()

    def produtos_no_carrinho(self):
        self.abrir_carrinho()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.cart-preview.active")))
        return self.driver.find_elements(*self.produtos_carrinho)

    def quantidade_itens_carrinho(self):
        produtos = self.produtos_no_carrinho()
        return len(produtos)
