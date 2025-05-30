import time
from behave import given, when, then
from features.helpers.driver import get_driver
from features.pages.loja_page import *

#Cenário: Verificar se a lista de produtos é carregada corretamente ao acessar a página

@given(u'que o usuário acessa a página principal da loja')
def step_acessar_pagina(context):
    acessar_site()

@when(u'a página terminar de carregar')
def step_pagina_carregada(context):
    assert pagina_carregada(), "A página não carregou corretamente."

@then(u'os produtos devem ser exibidos em uma lista visível')
def step_verificar_produtos_visiveis(context):
    assert pagina_carregada(), "Os produtos não estão visíveis na página."


#Cenário: Verificar se o botão "ADD TO CART" muda para "ADDED" após clicar

@given(u'que o usuário está na página com a lista de produtos visível')
def step_usuario_esta_na_pagina(context):
    acessar_site()
    assert pagina_carregada(), "A página de produtos não carregou."

@when(u'o usuário clica no botão "ADD TO CART" de um produto')
def step_clicar_add_to_cart(context):
    clicar_add_to_cart()

@then(u'o botão deve mudar para "ADDED"')
def step_verificar_texto_adicionado(context):
    assert verificar_texto_do_botao(), "O botão não mudou para '✔ ADDED'."
