from behave import given, when, then
from features.pages.sem_dados_page import *

@given("que o usuário esteja na página de ofertas")
def step_acessar_pagina(context):
    acessar_pagina_ofertas()

@when("fizer pesquisa de um produto que não consta na oferta")
def step_pesquisar_produto_inexistente(context):
    digitar_pesquisa_invalida()

@then('aparecerá uma mensagem "No data"')
def step_verificar_mensagem(context):
    assert verificar_mensagem_no_data(), 'A mensagem "No data" não foi exibida.'
