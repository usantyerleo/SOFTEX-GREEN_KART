Funcionalidade: Finalizar uma compra com sucesso

  @checkout
  Cenário: Finalizar compra com sucesso após adicionar produtos
    Dado que o usuário adicionou produtos ao carrinho
    Quando ele clica no botão "Place Order" e seleciona o país
    E aceita os termos e condições
    E clica em "Proceed"
    Então a compra deve ser concluída com uma mensagem de sucesso