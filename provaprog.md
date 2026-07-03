# Rubrica de Avaliação - Projeto: Sistema de Gerenciamento de Tarefas (Task Manager Web)

**Disciplina:** Programação / Desenvolvimento Web  
**Projeto:** Sistema de Gerenciamento de Tarefas com Interface Web  
**Nível esperado:** Intermediário (usando Python + HTTP Server)

---

## Objetivo do Projeto

Desenvolver um sistema web funcional de **Gerenciamento de Tarefas** (Task Manager) que permita ao usuário:

- Cadastrar novas tarefas
- Listar todas as tarefas
- Marcar tarefas como concluídas
- Editar e excluir tarefas
- Filtrar tarefas por status (pendentes / concluídas)
- Tudo acessível via navegador através de um servidor HTTP em Python

O projeto deve utilizar o modelo de servidor fornecido (`http.server` + `BaseHTTPRequestHandler`) como base, integrando banco de dados, responsividade, bibliotecas/frameworks e interatividade.

---

## Critérios de Avaliação

| Critério | Pontuação Máxima | Peso |
|----------|------------------|------|
| **1. Banco de Dados** | 25 pontos | 25% |
| **2. Código Responsivo** | 20 pontos | 20% |
| **3. Implementação de Bibliotecas/Frameworks** | 20 pontos | 20% |
| **4. Interatividade** | 25 pontos | 25% |
| **5. Funcionalidade Geral + Organização** | 10 pontos | 10% |
| **Total** | **100 pontos** | 100% |

---

## 1. Banco de Dados (25 pontos)

**Objetivo:** O sistema deve persistir as tarefas de forma correta e funcional.

### O que é necessário para pontuar:

| Nível | Descrição | Pontos |
|-------|-----------|--------|
| **Excelente** | Usa SQLite com tabelas bem estruturadas (`tarefas`, `categorias`). CRUD completo (Create, Read, Update, Delete). | 25 |
| **Bom** | Banco de dados com pelo menos uma tabela principal e operações básicas funcionando. | 18 |
| **Regular** | Banco de dados existe, mas com estrutura simples ou operações limitadas. | 10 |
| **Insuficiente** | Não utiliza banco de dados ou não persiste as tarefas. | 0 |

**Requisitos mínimos:**
- Tabela `tarefas` com campos: `id`, `titulo`, `descricao`, `status`, `data_criacao`
- Operações de inserir, listar, atualizar status e excluir

---

## 2. Código Responsivo (20 pontos)

**Objetivo:** A interface web deve funcionar bem em diferentes tamanhos de tela.

### O que é necessário para pontuar:

| Nível | Descrição | Pontos |
|-------|-----------|--------|
| **Excelente** | Usa Bootstrap 5 ou CSS responsivo bem implementado. Interface funcional e bonita em celular, tablet e desktop. | 20 |
| **Bom** | Interface se adapta na maioria dos tamanhos de tela. | 14 |
| **Regular** | Tem alguma responsividade, mas apresenta problemas em telas menores. | 8 |
| **Insuficiente** | Interface não é responsiva ou quebra em dispositivos móveis. | 0 |

**Recomendação:** Utilizar **Bootstrap 5 via CDN** para facilitar o desenvolvimento.

---

## 3. Implementação de Bibliotecas / Frameworks (20 pontos)

**Objetivo:** Demonstrar o uso adequado de bibliotecas e frameworks.

### O que é necessário para pontuar:

| Nível | Descrição | Pontos |
|-------|-----------|--------|
| **Excelente** | Utiliza pelo menos **duas** tecnologias:  
• Bootstrap (frontend)  
• Jinja2 (templates)  
• SQLite3  
• Outra biblioteca útil | 20 |
| **Bom** | Utiliza pelo menos uma biblioteca de forma correta (Bootstrap ou Jinja2). | 14 |
| **Regular** | Usa apenas o módulo `http.server` nativo. | 8 |
| **Insuficiente** | Não utiliza nenhuma biblioteca adicional. | 0 |

**Observação:** O `http.server` é obrigatório como base. O uso de outras bibliotecas é valorizado.

---

## 4. Interatividade (25 pontos)

**Objetivo:** O sistema deve permitir interação real do usuário com as tarefas.

### O que é necessário para pontuar:

| Nível | Descrição | Pontos |
|-------|-----------|--------|
| **Excelente** | Sistema completo com:  
• Formulário para adicionar tarefa  
• Listagem de tarefas  
• Marcar como concluída (checkbox ou botão)  
• Editar e excluir tarefas  
• Filtros (Todas / Pendentes / Concluídas) | 25 |
| **Bom** | Tem interatividade básica (adicionar + listar + marcar como concluída). | 18 |
| **Regular** | Alguma interatividade presente, mas com bugs ou funcionalidades incompletas. | 10 |
| **Insuficiente** | Interface estática sem interação funcional. | 0 |

**Funcionalidades esperadas:**
- Adicionar nova tarefa via formulário
- Atualizar status da tarefa
- Excluir tarefa
- Filtrar tarefas por status

---

## 5. Funcionalidade Geral + Organização do Código (10 pontos)

| Critério | Descrição | Pontos |
|----------|-----------|--------|
| **Funcionalidade** | O sistema roda sem erros e cumpre o objetivo principal | 5 |
| **Organização** | Código bem separado em arquivos (`main.py`, `database.py`, `routes.py`, etc.) | 3 |
| **Documentação** | Comentários claros e/ou README explicando como executar o projeto | 2 |


## Observações Importantes

- O servidor deve ser construído com base no código `http.server` + `BaseHTTPRequestHandler` fornecido.
