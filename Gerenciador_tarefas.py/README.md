## Trabalho da Aula 1 - Intensivão de Desenvolvimento
## Banco de Dados

Para a realização do banco de dados, usei como base o código exemplo gerenciador_banco.py. Estudei o básico da nomenclatura do SQLite3, compreendendo que o connect() cria o arquivo caso não exista e que o cursor é o objeto que executa os comandos SQL. Aprendi a utilizar placeholders (?) para segurança contra SQL Injection e a configuração do row_factory para acessar os dados pelos nomes das colunas, facilitando a legibilidade.

Funções adaptadas:

'init_db()': Inicializa o banco e cria a tabela tarefas.

'adicionar_tarefa(titulo, descricao)': Insere uma nova tarefa.

'get_tarefas(status_filter)': Recupera tarefas com suporte a filtros dinâmicos.

'atualizar_status(tarefa_id, status)': Altera o status da tarefa.

'deletar_tarefa(tarefa_id)': Remove uma tarefa.

'get_tarefa(tarefa_id)': Busca uma tarefa única (usada na edição).

'editar_tarefa(tarefa_id, titulo, descricao)': Atualiza o conteúdo de uma tarefa existente.


## Código Principal (main.py) e Roteamento (rotas.py)

Para aprimorar a organização e evitar a repetição de código, evoluí a arquitetura para o padrão de Separação de Responsabilidades, pois não sabia sobre o conhecimento das rotas e adicionei um novo arquivo para melhor organização. 

'main.py': Tornou-se "compacto". Sua única responsabilidade é iniciar o servidor HTTP e o banco de dados. Ele atua como o "dono do restaurante", mantendo a infraestrutura funcionando.

'rotas.py': Este é o novo cérebro do sistema. Ele contém a classe GerenciadorTarefas (o Handler), que processa as requisições, e os Controladores. O roteamento é feito de forma dinâmica através de dicionários (ROTAS_GET e ROTAS_POST), o que torna a adição de novas funcionalidades muito mais simples.

Imports utilizados:

    http.server e socketserver: Para o servidor web.

    urllib.parse: Para manipular e organizar as rotas e os parâmetros das URLs.

    Jinja2: Para renderizar dinamicamente o HTML com os dados do banco.

## Frontend

A interface foi construída com foco em agilidade e integração. Utilizei a inteligencia artificial para conseguir realizar essa tarefa 

Estrutura: HTML5 estruturado com Bootstrap para design responsivo.

Dinâmica: Utilizamos o Jinja2 para injetar os dados do banco na tabela ({% for %}, {% if %}).

Edição "Inline": Implementamos a edição das tarefas diretamente na tabela do index.html. Cada linha da tabela é um formulário, permitindo alterar título e descrição e salvar a edição sem a necessidade de uma nova página, mantendo a experiência do usuário fluida e o código limpo.

## Estrutura Atualizada do Projeto

main.py: Inicializa o servidor.

rotas.py: Contém a classe GerenciadorTarefas, as rotas e a lógica de negócio (controladores).

database.py: Gerencia exclusivamente a comunicação com o SQLite.

Front_end/index.html: Template dinâmico com o formulário de listagem e edição das tarefas.


## Sobre o desenvolvimento
O desenvolvimento deste projeto foi realizado com o suporte de Inteligência Artificial, principalmente na parte de frontend na qual nunca tive contato nenhum, por mais que o descobrimento da bibliotca Jinja2 facilitou um pouco meu entendimento para o frontend, ainda tive dificuldades que foram sanadas pelo uso da IA. Busquei utilizar a IA como uma ferramenta de suporte técnico, auxiliando na compreensão de conceitos, na estrutura do código Python aonde tava errando, no uso e descobrimento de bibliotecas, e na implementação das classes do servidor HTTP. Busquei durante este processo não apenas entregar a funcionalidade, mas garantir que eu pudesse compreender a lógica de integração e a arquitetura do sistema, servindo como base para meus próximos passos. Irei correr átras do aprofundamento técnico da área. 