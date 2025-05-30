import time
from behave import given, when, then
from features.helpers.driver import get_driver
from features.pages.loja_page import *

#Cenário: Verificar se ao clicar no ícone do carrinho sem itens, ele mostra vazio

@given(u'que o usuário não adicionou nenhum produto ao carrinho')
def step_usuario_nao_adicionou_produto(context):
    acessar_site()
    assert pagina_carregada(), "A página de produtos não carregou."

@when(u'o usuário clica no ícone do carrinho')
def step_clicar_no_carrinho(context):
    context.checkout_realizado = acessar_carrinho_e_verificar_se_estiver_vazio()

@then(u'o carrinho deve indicar que está vazio')
def step_verificar_carrinho_vazio(context):
    assert context.checkout_realizado is False, "O carrinho não está vazio como esperado."