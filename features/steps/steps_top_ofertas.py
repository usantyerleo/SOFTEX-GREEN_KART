from behave import given, when, then
from features.pages.top_ofertas_page import *

@given("que o usuário acessa a página principal")
def step_abrir_pagina_principal(context):
    acessar_pagina_principal()

@when("o usuário clicar em top ofertas")
def step_clicar_top_ofertas(context):
    clicar_em_top_ofertas()

@then("deverá ser direcionado para a página de promoções")
def step_verificar_redirecionamento(context):
    assert esta_na_pagina_de_promocoes(), "Usuário não foi direcionado para a página de promoções."
