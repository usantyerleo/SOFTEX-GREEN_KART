from behave import given, when, then
from features.pages.listagem_ofertas_page import *

@given("que o usuário esteja na página de oferta")
def step_acessar_pagina_oferta(context):
    acessar_pagina_de_ofertas()

@when("digitar no campo de pesquisa a inicial do item desejado")
def step_digitar_inicial_item(context):
    digitar_pesquisa_valida()

@when("o item existir")
def step_item_existe(context):
    pass

@then("o item irá aparecer como opção")
def step_item_listado(context):
    assert produtos_listados(), "Nenhum produto foi listado."
