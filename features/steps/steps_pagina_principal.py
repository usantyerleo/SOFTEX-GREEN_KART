import time 
from behave import given, when, then
from features.helpers.driver import get_driver
from features.pages.loja_page import *
from time import sleep
from pages.catalogo_page import CatalogoPage

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
    sleep(2)


#busca de produtos no catálogo

@given("que o usuário está na página inicial")
def step_usuario_esta_na_pagina_inicial(context):
    context.page = CatalogoPage(context.driver)
    context.page.carregar_pagina()

@when("ele digita o nome de um produto existente na barra de busca")
def step_usuario_busca_produto_existente(context):
    context.page.buscar_produto("ber")
    sleep(4)

@then("apenas produtos relacionados ao termo digitado devem ser exibidos")
def step_resultado_da_busca(context):
    produtos = context.page.produtos_exibidos()
    assert len(produtos) > 0, "Nenhum produto foi exibido na busca"

#adicionar múltiplos produtos ao carrinho 

@given("que o usuário está na página de produtos")
def step_usuario_esta_na_pagina_de_produtos(context):
    context.page = CatalogoPage(context.driver)
    context.page.carregar_pagina()

@when("ele adiciona três produtos diferentes ao carrinho")
def step_adiciona_tres_produtos_ao_carrinho(context):
    context.page.adicionar_produto_por_indice(0)
    sleep(2)
    context.page.adicionar_produto_por_indice(1)
    sleep(2)
    context.page.adicionar_produto_por_indice(2)
    sleep(2)

@then("ambos os produtos devem aparecer no resumo do carrinho")
def step_verifica_produtos_no_carrinho(context):
    produtos_no_carrinho = context.page.produtos_no_carrinho()
    print(f"{len(produtos_no_carrinho)} produto(s) encontrados no carrinho.")
    sleep(4)
