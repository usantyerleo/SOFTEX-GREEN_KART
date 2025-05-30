# language: pt
Funcionalidade: Exibição e manipulação da lista de produtos

  Cenário: Verificar se a lista de produtos é carregada corretamente ao acessar a página
    Dado que o usuário acessa a página principal da loja
    Quando a página terminar de carregar
    Então os produtos devem ser exibidos em uma lista visível

  Cenário: Verificar se o botão "ADD TO CART" muda para "ADDED" após clicar
    Dado que o usuário está na página com a lista de produtos visível
    Quando o usuário clica no botão "ADD TO CART" de um produto
    Então o botão deve mudar para "ADDED"

