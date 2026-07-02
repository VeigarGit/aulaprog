# 📚 Material Completo - Aula de Programação

**Aula de 1 hora** sobre conceitos fundamentais de programação, com foco em boas práticas e estruturas de dados básicas.

---

## 🎯 Objetivo da Aula

Ao final desta aula, o aluno será capaz de:

- Utilizar operadores lógicos e estruturas de controle
- Entender os principais paradigmas de programação
- Conhecer as estruturas de dados básicas
- Diferenciar biblioteca de framework
- Aplicar os princípios **SOLID** no dia a dia

---

## 🛠️ Configurando o Repositório (Git)

### Forma Recomendada

1. Crie um repositório novo no GitHub
2. Clone o repositório:

```bash
git clone https://github.com/VeigarGit/aulaprog.git
cd aulaprog

## Git: Fundamentos Essenciais para Desenvolvedores

O **Git** é uma das ferramentas mais importantes no dia a dia de qualquer desenvolvedor. Abaixo você encontra explicações claras e práticas sobre os principais conceitos e comandos.

### O que é o Git e para que ele serve?

**Git** é um sistema de controle de versão distribuído. Ele permite que você:

- Salve o histórico completo do seu código ao longo do tempo
- Volte para versões anteriores facilmente
- Trabalhe em equipe sem sobrescrever o trabalho dos outros
- Experimente novas funcionalidades sem medo de quebrar o código principal

Resumindo: Git é como um "máquina do tempo" para o seu código.

### Como o Git funciona?

O Git possui **três áreas principais**:

1. **Working Directory** (Diretório de Trabalho)  
   Onde você edita seus arquivos normalmente.

2. **Staging Area** (Área de Preparação)  
   Onde você prepara os arquivos que serão salvos no próximo commit.

3. **Repository** (Repositório Local)  
   Onde o Git guarda o histórico dos commits.

Fluxo básico:
```
Working Directory → git add → Staging Area → git commit → Repository
```

### O que são Branches?

**Branch** é uma linha independente de desenvolvimento.

- A branch principal costuma se chamar `main` ou `master`
- Você pode criar branches para desenvolver novas funcionalidades, corrigir bugs ou testar ideias
- Cada branch tem seu próprio histórico de commits
- Depois você pode unir (merge) a branch de volta na principal

**Vantagem**: Permite trabalhar em várias coisas ao mesmo tempo sem interferir no código que está em produção.

### Comandos Básicos do Git

| Comando                        | Descrição                                      | Exemplo                              |
|--------------------------------|------------------------------------------------|--------------------------------------|
| `git init`                     | Inicializa um repositório Git                  | `git init`                           |
| `git clone`                    | Clona um repositório remoto                    | `git clone https://github.com/...`   |
| `git status`                   | Mostra o estado atual dos arquivos             | `git status`                         |
| `git add`                      | Adiciona arquivos à Staging Area               | `git add .` ou `git add arquivo.py`  |
| `git commit -m "mensagem"`     | Salva as alterações no repositório             | `git commit -m "Adiciona login"`     |
| `git push`                     | Envia commits para o repositório remoto        | `git push origin main`               |
| `git pull`                     | Baixa e mescla alterações do remoto            | `git pull origin main`               |
| `git branch`                   | Lista as branches                              | `git branch`                         |
| `git checkout -b nome`         | Cria e muda para uma nova branch               | `git checkout -b feature/login`      |
| `git log`                      | Mostra o histórico de commits                  | `git log --oneline`                  |
| `git merge`                    | Une uma branch na branch atual                 | `git merge feature/login`            |

### Diferença entre Git e GitHub

| Aspecto          | **Git**                                      | **GitHub**                                      |
|------------------|----------------------------------------------|-------------------------------------------------|
| O que é?         | Sistema de controle de versão (software)     | Plataforma online para hospedar repositórios    |
| Onde roda?       | No seu computador (local)                    | Na nuvem (servidor)                             |
| Função principal | Controlar versões do código                  | Hospedar, colaborar, revisar código (Pull Requests) |
| É obrigatório?   | Não (pode usar Git sem GitHub)               | Não (é apenas um dos muitos serviços)           |

**Resumo**: Git = ferramenta local. GitHub = plataforma na internet que usa Git.

### O que é um Merge?

**Merge** é o processo de **unir** o conteúdo de uma branch com outra.

Exemplo comum:
- Você está na branch `main`
- Terminou o desenvolvimento na branch `feature/login`
- Executa `git merge feature/login`

O Git tenta combinar automaticamente as alterações.  
Se houver conflito (duas pessoas editaram o mesmo arquivo), você precisa resolver manualmente.

### O que é o .gitignore?

O arquivo **`.gitignore`** é usado para dizer ao Git quais arquivos e pastas ele **deve ignorar**.

Exemplos comuns de arquivos que devem ser ignorados:
- `node_modules/`
- `__pycache__/`
- `.env`
- `*.log`
- `dist/`, `build/`
- Pastas de IDE (`.vscode/`, `.idea/`)

**Exemplo de .gitignore**:

```gitignore
# Ambientes virtuais
venv/
env/

# Cache do Python
__pycache__/
*.pyc

# Arquivos de ambiente
.env
.env.local

# Dependências
node_modules/

# Builds
dist/
build/
```

### Git Flow

**Git Flow** é um modelo de trabalho (workflow) que organiza o uso de branches de forma padronizada.

Branches principais:
- `main` / `master` → Código pronto para produção
- `develop` → Branch de desenvolvimento principal

Branches de suporte:
- `feature/` → Novas funcionalidades
- `release/` → Preparação para lançamento
- `hotfix/` → Correções urgentes em produção

Embora o Git Flow seja muito usado, muitos times hoje preferem workflows mais simples como **GitHub Flow** (main + feature branches + Pull Request).

### Padrões de Commit (Conventional Commits)

Usar um padrão nos commits facilita muito a leitura do histórico e a automação de changelogs.

**Formato recomendado** (Conventional Commits):

```
tipo(escopo): descrição curta

[corpo opcional]
```

**Tipos mais usados**:

| Tipo       | Significado                              | Exemplo                              |
|------------|------------------------------------------|--------------------------------------|
| `feat`     | Nova funcionalidade                      | `feat: adiciona sistema de login`    |
| `fix`      | Correção de bug                          | `fix: corrige erro ao salvar pedido` |
| `docs`     | Alteração na documentação                | `docs: atualiza README do SOLID`     |
| `refactor` | Refatoração sem mudar comportamento      | `refactor: melhora estrutura do service` |
| `test`     | Adiciona ou modifica testes              | `test: adiciona testes do repositório` |
| `chore`    | Tarefas de manutenção                    | `chore: atualiza dependências`       |

**Exemplo bom**:
```bash
git commit -m "feat(auth): implementa login com JWT"
```

**Exemplo ruim**:
```bash
git commit -m "fiz umas coisas"
```

---

**Dica final**: Comece simples. Use `main` + branches de feature + Pull Requests. Quando o projeto crescer, adote um fluxo mais estruturado.
