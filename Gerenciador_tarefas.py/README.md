## trabalho da aula 1 do intensivão de desenvolvimento 

## Banco de Dados
Para a realização do banco de dados usei como base o código exemplo "gerenciador_banco.py" localizado na pasta loja para a realização do banco de dados do gerenciador de tarefas. Estudei o basico da nomeclatura de SQlite3 para defenir as funções e utilizando e entendi o funcionamento de um cursor e seus comandos de executar. Funções do sqlite3,como o connect() que cria o arquivo se ele não existir, e o cursor é o objeto que executa os comandos SQL. Por meio da IA(Gemini web) aprendi uma forma de segurança ao utilizar o placeholder "?" e também a configuração do `row_factory` para permitir o acesso aos resultados do banco por meio do nome das colunas, melhorando a legibilidade do código no restante da aplicação. Aprendi também que Commit salva as alterações em cada função e o close fecha a função para não travar no arquivo, e pelo que entendi, o método execute() do sqlite3 exige que os argumentos dos placeholders (?) sejam passados dentro de uma tupla ou lista e para não dar erro em Python, se você escrever apenas (status_filter), o Python interpreta apenas como parênteses envolvendo uma string, para isso defini que aquilo é uma tupla de um único elemento, colocando a vírgula no final (status_filter,).  

Funções que adaptei da loja para os parametros definidos no comando do trabalho:
`init_db()`: Inicializa o banco de dados e cria a tabela `tarefas` caso ela ainda não exista no sistema.
`adicionar_tarefa(titulo, descricao)`: Insere uma nova tarefa com o status inicial `pendente` e registra automaticamente o carimbo de data/hora atual.
`get_tarefas(status_filter)`: Recupera as tarefas do banco de dados ordenadas pelas mais recentes. Permite filtragem dinâmica por status (`pendente` ou `concluida`).
`atualizar_status(tarefa_id, status)`: Modifica o status de uma tarefa específica utilizando o seu ID identificador.
`deletar_tarefa(tarefa_id)`: Remove permanentemente uma tarefa do banco de dados pelo ID.

## Código princial (main.py)
Para realizar o sistema pensei em que através de uma plataforma web realizamos um pedido e o sistema busca a informação na base de dados e traz a resposta de volta para web. Para solução usei como base duas funções a função get foi criada para pegar a informação realizando os comandos simples que serão o de se a tarefa esta completa ou não e exclui-la se requisitado, e a outra função foi a post em que guardo a informação colocada na tarefa sendo usado exclusivamente quando o usuário preenche o formulário para adicionar uma nova tarefa. 

Imports: 
Para fazer a o funcionameto é importado o protocolo HTTP reponsável pelo processamento dos pedidos no navegador buscando e processando a logica do backend, enquanto o  socketserver é o canal de comunicação das solicitações. 

Pesquisando formas de organizar e criar essa conexão entre a linguagem pythone e HTML, com ajuda da IA encontrei o urllib.parse que é um módulo embutido na biblioteca padrão do Python usado para manipular URLs organizando esses endereços e analisando-os. Ele divide o endereço em componentes para melhor analise deixando mais organizado os ednereços. Link da documentação oficial: https://www.google.com/url?sa=i&source=web&rct=j&url=https://docs.python.org/pt-br/3/library/urllib.parse.html&ved=2ahUKEwiNgavYwbmVAxXfuZUCHTUiNKgQy_kOegoIAggACAAIDxAC&opi=89978449&cd&psig=AOvVaw3zXou_srrLO7WfW1AuXwnw&ust=1783271375643000

Como forma de deixar o frontend mais dinâmico estudei sobre a biblioteca Jinja2 em que posso utilizar fundamentos do Python no HTML montando a página antes de enviá-la pronta para o navegador do usuário. 
Link da documentação oficial: https://jinja.palletsprojects.com/en/stable/

## Frontend 
A interface gráfica (arquivo `index.html`) marca o meu primeiro contato prático com o desenvolvimento Front-end. Para viabilizar a criação desta interface de forma ágil e focar no aprendizado da lógica de integração com o Back-end (Python), utilizei ferramentas de Inteligência Artificial como suporte na geração do código HTML e CSS.

Eu aprendi e apliquei com a ajuda da IA neste Front-end, a estruturação HTML5, criação de formulários (`<form>`) estruturados corretamente para enviar requisições do tipo `POST` para o servidor Python.  Estilização com Bootstrap, utilizando o Bootstrap para aplicar um design limpo e responsivo rapidamente, usando classes prontas para tabelas e botões. Integração com Jinja2, compreendendo como utilizar a sintaxe do Jinja2 (`{% for %}`, `{% if %}`, `{{ variavel }}`) direto no HTML para gerar listas dinâmicas e renderizar elementos condicionais. No entanto, foi minha primeira vez e utilizei a inteligencia artifical para a geração do codigo.  

## Estrutura do Projeto

 `main.py`: O coração do projeto. Contém as rotas, a lógica do servidor HTTP e a conexão entre o front-end e o banco de dados.
 `database.py`: Módulo responsável por interagir com os dados (adicionar, buscar, atualizar e deletar).
 `Front_end/index.html`: O template HTML que recebe as variáveis dinâmicas injetadas pelo Jinja2.

## Para executar o projeto

1. Certifique-se de ter o Python na máquina.
2. Instale a biblioteca Jinja2 (caso não tenha):
   ```bash
   pip install Jinja2