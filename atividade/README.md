# Gerenciamento de Tarefas

Sistema web de gerenciamento de tarefas desenvolvido em Python com servidor HTTP, SQLite, Bootstrap e Jinja2.

## Relato de Desenvolvimento

Desenvolver este projeto foi um aprendizado intenso. A parte de HTML foi um pouco mais tranquila por conta de algumas experiências que já tive com desenvolvimento web básico. Isso ajudou a estruturar as páginas e montar o layout com Bootstrap sem grandes dificuldades.
Já a lógica do backend foi mais trabalhosa. Peguei parte do banco de dados do projeto da loja de exemplo (fornecedores, notas fiscais) e adaptei as estruturas para o sistema de tarefas. Implementar as rotas no Python foi diferente do que eu esperava, já tinha experiência com rotas em JavaScript, então a lógica geral não é tão diferente.
Criar as funções e pensar na lógica foi a parte mais trabalhosa, principalmente lidando com a biblioteca Jinja2. Entendi como ela funciona (substituir placeholders no HTML por loops e variáveis diretamente no template), mas de primeira senti dificuldade de entender o encaixe com o Python.
Utilizei IA no projeto quando travava em alguma parte e não conseguia achar um vídeo ou algo no StackOverflow que me ajudasse rapidamente, por conta do prazo de entrega. A IA ajudou a encontrar bugs e sugerir soluções de forma mais ágil.

## Tecnologias utilizadas

- **Python** — Servidor HTTP (`http.server`)
- **SQLite3** — Banco de dados
- **Jinja2** — Templates HTML
- **Bootstrap 5** — Frontend responsivo

## Como executar

1. Instale as dependências:
   ```
   pip install jinja2
   ```
2. Execute o servidor:
   ```
   python main.py
   ```
3. Acesse: [http://localhost:5000](http://localhost:5000)

## Estrutura do projeto

```
├── main.py          # Servidor HTTP (ponto de entrada)
├── routes.py        # Rotas e lógica do servidor
├── database.py      # CRUD SQLite
├── site/
│   ├── index.html   # Página principal
│   ├── editar.html  # Página de edição
│   └── style.css    # Estilos responsivos
└── README.md        # Documentação
```
