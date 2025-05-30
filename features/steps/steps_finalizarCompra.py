from behave import given, when, then
from pages.catalogo_page import CatalogoPage
from pages.checkout_page import CheckoutPage
from time import sleep

@given("que o usuário adicionou produtos ao carrinho")
def step_usuario_adicionou_produtos(context):
    context.catalogo = CatalogoPage(context.driver)
    context.catalogo.carregar_pagina()
    context.catalogo.adicionar_produto_por_indice(0)
    sleep(1)
    context.catalogo.abrir_carrinho()
    sleep(1)

@when('ele clica no botão "Place Order" e seleciona o país')
def step_place_order(context):
    context.checkout = CheckoutPage(context.driver)
    context.checkout.place_order()
    context.checkout.selecionar_pais("Brazil")
    sleep(2)

@when("aceita os termos e condições")
def step_aceita_termos(context):
    context.checkout.aceitar_termos()
    sleep(2)

@when('clica em "Proceed"')
def step_proceed(context):
    context.checkout.clicar_em_proceed()
    sleep(2)

@then("a compra deve ser concluída com uma mensagem de sucesso")
def step_mensagem_sucesso(context):
    mensagem = context.checkout.mensagem_de_sucesso()
    assert "Thank you" in mensagem or "successfully" in mensagem, "Mensagem de sucesso não encontrada"
    sleep(2)
