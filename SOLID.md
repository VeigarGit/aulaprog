# S.O.L.I.D: Os 5 Princípios da Programação Orientada a Objetos

Os princípios **SOLID** são um conjunto de 5 diretrizes de design de software que ajudam a criar sistemas mais **flexíveis**, **manuteníveis** e **escaláveis**. Eles foram introduzidos por Robert C. Martin (Uncle Bob).

> **Objetivo**: Escrever código que seja fácil de entender, modificar e estender ao longo do tempo.

---

## S — Single Responsibility Principle  
**Princípio da Responsabilidade Única**

> Uma classe deve ter **apenas uma razão para mudar**.

### ❌ Violando o princípio

```python
class Pedido:
    def calcular_total(self): ...
    def salvar_no_banco(self): ...           # Responsabilidade de persistência
    def enviar_email_confirmacao(self): ...  # Responsabilidade de comunicação
```

### ✅ Respeitando o princípio

```python
class Pedido:
    def calcular_total(self): ...

class PedidoRepository:
    def salvar(self, pedido): ...

class EmailService:
    def enviar_confirmacao(self, pedido): ...
```

**Analogia**: Um cozinheiro não deve ser responsável por lavar a louça, atender o telefone e fazer a contabilidade ao mesmo tempo.

---

## O — Open-Closed Principle  
**Princípio Aberto-Fechado**

> Entidades de software devem estar **abertas para extensão**, mas **fechadas para modificação**.

### ❌ Violando o princípio

Toda vez que surge um novo tipo de desconto, precisamos modificar a classe existente.

### ✅ Respeitando o princípio

```python
from abc import ABC, abstractmethod

class Desconto(ABC):
    @abstractmethod
    def calcular(self, valor: float) -> float:
        pass

class DescontoBlackFriday(Desconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.30

class DescontoNatal(Desconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.15
```

**Vantagem**: Podemos criar novos descontos sem alterar o código existente.

---

## L — Liskov Substitution Principle  
**Princípio da Substituição de Liskov**

> Objetos de uma classe derivada devem poder **substituir** objetos da classe base **sem alterar** o comportamento esperado do programa.

### ❌ Violando o princípio (Clássico)

```python
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

class Quadrado(Retangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)  # Quebra o comportamento!
```

Se o código espera que `Retangulo` tenha largura e altura independentes, o `Quadrado` quebra essa expectativa.

### ✅ Boa prática

Use composição ou crie hierarquias mais coerentes.

```python
class Forma:
    def area(self):
        pass

class Retangulo(Forma):
    ...

class Quadrado(Forma):
    ...
```

---

## I — Interface Segregation Principle  
**Princípio da Segregação de Interface**

> Clientes não devem ser forçados a depender de métodos que não utilizam.

### ❌ Violando o princípio

```python
class ImpressoraMultifuncional:
    def imprimir(self): ...
    def escanear(self): ...
    def faxear(self): ...
    def fotocopiar(self): ...
```

Se uma classe só precisa imprimir, ela ainda é obrigada a implementar os outros métodos.

### ✅ Respeitando o princípio

```python
class Impressora:
    def imprimir(self): ...

class Scanner:
    def escanear(self): ...

class Multifuncional(Impressora, Scanner):
    pass
```

**Regra de ouro**: Prefira **muitas interfaces específicas** do que uma interface grande e genérica.

---

## D — Dependency Inversion Principle  
**Princípio da Inversão de Dependência**

> Módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de **abstrações**.

### ❌ Violando o princípio

```python
class PedidoService:
    def __init__(self):
        self.repository = PedidoRepository()  # Dependência direta
```

### ✅ Respeitando o princípio

```python
from abc import ABC, abstractmethod

class PedidoRepositoryInterface(ABC):
    @abstractmethod
    def salvar(self, pedido): pass

class PedidoService:
    def __init__(self, repository: PedidoRepositoryInterface):
        self.repository = repository  # Depende da abstração
```

Agora podemos trocar o repositório (banco de dados, arquivo, memória) sem modificar o `PedidoService`.

---

## Resumo dos 5 Princípios

| Letra | Princípio                          | Foco Principal                     | Benefício Principal             |
|-------|------------------------------------|------------------------------------|---------------------------------|
| **S** | Responsabilidade Única             | Uma classe = uma responsabilidade  | Facilita manutenção             |
| **O** | Aberto-Fechado                     | Extensão sem modificação           | Código mais flexível            |
| **L** | Substituição de Liskov             | Subtipos devem ser substituíveis   | Evita bugs inesperados          |
| **I** | Segregação de Interface            | Interfaces pequenas e específicas  | Reduz acoplamento               |
| **D** | Inversão de Dependência            | Depender de abstrações             | Facilita testes e trocas        |

---

## Por que aprender SOLID?

- Código mais **limpo** e organizado
- Mais fácil de **testar** (unit tests)
- Facilita a **evolução** do sistema
- Reduz **acoplamento** e aumenta **coesão**
- Essencial para trabalhar com **arquitetura limpa** e **DDD**

