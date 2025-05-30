Funcionalidade: Verificar se os produtos em oferta estão listados conforme digitação

  @smoke
  Cenário: Acessar produto conforme digitação
    Dado que o usuário esteja na página de oferta
    Quando digitar no campo de pesquisa a inicial do item desejado
    E o item existir
    Então o item irá aparecer como opção