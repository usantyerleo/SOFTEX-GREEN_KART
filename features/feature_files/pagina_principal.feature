Funcionalidade: Exibição e manipulação da lista de produtos

  Cenário: Verificar se a lista de produtos é carregada corretamente ao acessar a página
    Dado que o usuário acessa a página principal da loja
    Quando a página terminar de carregar
    Então os produtos devem ser exibidos em uma lista visível

  Cenário: Verificar se o botão "ADD TO CART" muda para "ADDED" após clicar
    Dado que o usuário está na página com a lista de produtos visível
    Quando o usuário clica no botão "ADD TO CART" de um produto
    Então o botão deve mudar para "ADDED"

@smoke
  Cenário: Buscar um produto existente
    Dado que o usuário está na página inicial
    Quando ele digita o nome de um produto existente na barra de busca
    Então apenas produtos relacionados ao termo digitado devem ser exibidos

  @smoke @carrinho
  Cenário: Adicionar múltiplos produtos diferentes ao carrinho
    Dado que o usuário está na página de produtos
    Quando ele adiciona três produtos diferentes ao carrinho
    Então ambos os produtos devem aparecer no resumo do carrinho