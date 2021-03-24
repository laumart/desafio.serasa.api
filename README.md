# Serasa Consumidor - Teste para analista desenvolvedor

Olá, obrigado pelo interesse em fazer parte da nossa equipe.  

O objetivo deste teste é verificar (até certo ponto) suas habilidades de codificação e arquitetura. Para isso você receberá um problema simples onde poderá mostrar suas técnicas de desenvolvimento.

Nós encorajamos você a exagerar um pouco na solução para mostrar do que você é capaz.

Considere um cenário em que você esteja construindo uma aplicação pronta para produção, onde outros desenvolvedores precisarão trabalhar e manter essa aplicação ao longo do tempo.  

Você **PODE** e **DEVE** usar bibliotecas de terceiros, usando ou não um framework, você decide. Lembre-se, um desenvolvedor eficaz sabe o que construir e o que reutilizar.

Na entrevista de "code review", esteja preparado para responder algumas perguntas sobre essas bibliotecas e, caso utilize, sobre o framework. Como e por que você as escolheu e com quais outras alternativas você está familiarizado, serão algumas dessas perguntas.

Como este é um processo de "code review", evite adicionar código gerado ao projeto.

***Obs***: Para realizar esse teste, não crie um repositório público! Esse desafio é compartilhado apenas com pessoas que estamos entrevistando e gostaríamos que permanecesse assim.  


Aqui no Serasa Consumidor, nós utilizamos o [Docker](https://www.docker.com/products/docker) para executar as aplicações, por isso, pedimos que você faça o mesmo neste teste. Isso garante que tenhamos um resultado idêntico ao seu quando testarmos sua aplicação.

Para facilitar o teste, disponibilizamos alguns containters que vão lhe ajudar a construir e executar suas aplicações, mas fique à vontade para alterá-los conforme preferir!

Para executá-los é fácil, acesse o diretório `user-api` e execute o comando: `docker-compose -up -d` e em seguida acesse o diretório `order-api` e execute o mesmo comando: `docker-compose -up -d`

## Requisitos mínimos para o teste:

- Persistência de dados em banco relacional e não relacional. Pode ser MySQL ou PostgreeSQL e queremos ver você utilizar Elastic Search!
- Camada de cache em memória. Pode ser Redis, Memcached, ou APCU.
- Utilização de um ORM para manipulação dos dados.
- Testes unitários.
- Documentação de setup e do funcionamento das APIs (um Makefile cai muito bem!).
- Caso decida utilizar um framework, utilize um  micro-framework, você está construindo microsserviços!

## Instruções

- Clone este repositório.
- Crie uma nova branch chamada `dev`
- Desenvolva as aplicações.
- Crie uma "pull request" da branch `dev` para a "branch" `master`. Essa PR deve conter as instruções para executarmos as suas aplicações, as tecnologias que você decidiu usar, por que decidiu utilizá-las e também as decisões que você teve quanto ao design do seu código.


## Requisitos das aplicações:

Nós desejamos que você crie 2 aplicações básicas (microserviços) que comuniquem-se entre si.

O primeiro deles deverá ser um cadastro de usuários, contendo os seguintes recursos:

- Listar, exibir, criar, alterar e excluir usuários  

Tabela de usuários `user` deverá conter os campos: id, name, cpf, email, phone_number, created_at, updated_at  

E o segundo deverá ser um serviço de pedidos, onde este deverá conter o id do usuário que fez o pedido e se comunicar com o serviço de usuários para retornar as informações do mesmo. Esse serviço deverá ter os seguintes recursos:

- Listar, Listar por usuário, exibir, criar, alterar e excluir.  

Tabela de pedidos `order` deverá conter os campos: id, user_id, item_description, item_quantity, item_price, total_value, created_at, updated_at  


Lembre-se de fazer a comunicação necessária entre os serviços para garantir a consistência de dados.  

Essas aplicações também **DEVEM** estar de acordo com os padrões REST e **DEVE** ser disponibilizada uma documentação contendo os endpoints e payloads utilizados nas requisições.


## Critérios de avaliação

Dê uma atenção especial aos seguintes aspectos:

- Você **DEVE** usar bibliotecas de terceiros, e pode escolher usar um framework, utilizar não vai ser uma penalidade, mas você vai precisar justificar a sua escolha.
- Suas aplicações **DEVEM** executar em containers Docker.
- Suas aplicações **DEVEM** retornar um JSON válido e **DEVEM** conter os recursos citados anteriormente.
- Você **DEVE** escrever um código testável e demonstrar isso escrevendo testes unitários.
- Você **DEVE** prestar atenção nas melhores práticas para segurança de APIs.
- Você **DEVE** seguir as diretizes de estilo de código.
- Você **NÃO** precisa desenvolver um "frontend" (telas) para esse teste.

Pontos que consideramos um bônus:

- Fazer uso de uma criptografia reversível de dados sensíveis do usuário, como: email, cpf e telefone, antes de persisti-los no banco de dados
- Suas respostas durante o code review
- Sua descrição do que foi feito na sua "pull request"
- Setup da aplicação em apenas um comando ou um script que facilite esse setup
- Outros tipos de testes, como: testes funcionais e de integração
- Histórico do seus commits, com mensagens descritivas do que está sendo desenvolvido.

---

Boa sorte!

---
---

## VERSÃO FINAL 
## Desafio Serasa - Laudinei Martins

Atendendo aos requisitos do desafio proposto, foram desenvolvidos dois microserviços denominados user-api e user-order.
As duas APIs foram desenvolvidas dentro do padrão REST e são executadas em containeres Docker, favorecendo execução de deploys mais rápidos, além do escalonamento de aplicações com  maior facilidade.
As APIs foram desenvolvidas com o Framework Fastapi e foram utilizados o Postgresql como banco de dados relacional, Eslasticsearch como não relacional, Memcached para camada de cache em memória, Sqlalchemy para ORM e o Pytest para testes unitários e de persistência.
Somente o campo do cpf foi criptografado para salvar no DB. Na inserção do CPF ele é criptografado pela biblioteca cryptography sendo descriptografado para exibição na opção exibir.

ATENÇÂO: A opção de descriptografar o CPF não foi aplicado para a opção listar todos usuarios, inclusive fica como uma forma de verificação dos dados.

O user-api é responsável por cadastrar usuarios, e dentre suas funcionalidades estão:
- Inserir, listar, exibir, alterar e excluir
- Somente será permitido exclusão do usuario que não estiver em um pedido.

O order-api é responsável por cadastrar pedidos, e dentre suas funcionalidades estão:
- Inserir, listar, listar por usuário, exibir, alterar e excluir
- Somente será permitido a inclusão do pedido se o id do usurio informado estiver cadastrado na api-user.


# Tecnologias, Frameworks e Libraries:

- user-api utiliza:
  FastApi, Postgresql, SQLAlchemy, Memcached, Cryptography e Pytest.

- order-api utiliza:
  FastApi, ElasticSearch e PyTest.

O Framework FastAPI foi escolhido para a implementação das APIs devido ao alto desempenho, fácil de aprender, rápido para codificar, pronto para produção, e a documentação das APIs são geradas pelos Swagger UI e ReDoc de forma automática.
FastAPI é uma estrutura da web moderna e rápida (de alto desempenho) para a construção de APIs com Python.

Memcached é um sistema de armazenamento em cache de objetos de memória distribuída destinado ao uso na aceleração de aplicativos da web dinâmicos, aliviando a carga do banco de dados.

SQLAlchemy é utilizado para a camada ORM que fornece aos desenvolvedores de aplicativos todo o poder e flexibilidade do SQL.
Ele fornece um conjunto completo de padrões de persistência projetados para acesso eficiente e de alto desempenho ao banco de dados, adaptado em uma linguagem de domínio simples e Pythônica.

Elasticsearch é uma ferramenta para buscas desenvolvida em Java e também é uma solução NoSQL de armazenamento de dados que tem capacidade para tratar de grandes quantidades de dados em tempo real.

Pytest é uma ferramenta que facilita a escrita de pequenos testes, mas pode ser escalada para suportar testes funcionais complexos para aplicativos e bibliotecas.

Cryptograph é uma biblioteca que contém um algorítimo de alto nível e interfaces de baixo nível para algoritmos criptográficos comuns, como cifras simétricas, resumos de mensagens e funções de derivação de chaves.

- Optei por utilizar como DB o Postgresql devido a minha familiaridade do dia a dia com esse DB. Os padrões e lógica que utilizei para desenvolvimento da codificação foram alicerçados nos padrões de APIs REST MVC, porém pesquisei e tentei realizar nos padrões utilizados para as API python.  

# Recursos, parâmetros e requisitos:
Cada imagem e suas respectivas portas serão configuradas:

Postgres 5432 - Usuário: postgres - Senha: postgres

Memcached 11211 

Elasticsearch 9200

user-api 8080
  
order-api 8081

Para executar as APIs, o docker deverá estar instalado em execução e deverá entrar no diretório raiz de cada projeto, começando pela user-api e executar o comando:
    docker-compose up -d

Na sequencia, na raiz da order-api, executar o mesmo comando. Esse comando baixará as imagens e criará os containers e subirá as aplicações.


- A base de dados serasa foi configurada para criação no postgres.
  - Para verificação dos dados, caso necessário, após os containeres estarem no ar, utilizar o comando abaixo:
  
  docker exec -it $(docker ps -aqf "name=postgres") bash
  
  - Na linha de comando que se abrir, utilize os comandos na sequencia, para acessar a base serasa e selecionar os dados da tabela user:
  psql -U postgres serasa
  select * from public.user;

- Para documentação e testes/utilização das APIS, acesse o navegador:

user-api: http://localhost:8080/docs e http://localhost:8080/redoc

order-api: http://localhost:8081/docs e http://localhost:8081/redoc


- Variáveis de ambiente estão localizadas no arquivo ".env"


# Referencias:
  Python: https://docs.python.org
  FastApi: https://fastapi.tiangolo.com
  Docker: https://www.docker.com
  Docker-Compose: https://docs.docker.com/compose
  Memcache: https://memcached.org
  Pyteste: https://docs.pytest.org
  Sqlalchemy: https://www.sqlalchemy.org
  Elasticsearch: https://elasticsearch-py.readthedocs.io
