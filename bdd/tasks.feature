Scenario: Testar os endpoints da API de Tasks
  Given que eu acesso a raiz da API de Tasks
  And nessa requisição eu tenho a URL para acessar Tasks
  When eu acesso essa URL
  Then eu vejo a lista de Tasks
  And eu crio uma nova Task para Estudar
