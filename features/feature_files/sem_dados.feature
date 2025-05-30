Funcionalidade: Verificar se aparece mensagem "no data" em caso de falta do produto em oferta
 
  @negative
  Cenário: Pesquisar produto em falta
    Dado que o usuário esteja na página de ofertas
    Quando fizer pesquisa de um produto que não consta na oferta
    Então aparecerá uma mensagem "No data"