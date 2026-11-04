# Oficina de Lógica de Programação com Python

Duas horas, zero experiência prévia. Ao longo da aula o grupo constrói um **jogo de adivinhação de número**, e cada conceito entra porque o jogo precisa dele.

Ao final você deve saber: usar variáveis, tipos (`str`, `int`, `float`), `print` e `input`, tomar decisões com `if/elif/else`, combinar condições com `and`, `or` e `not`, e repetir ações com `while`.

---

## Como abrir o ambiente

Você **não precisa instalar nada**. O Python roda no navegador, dentro do GitHub Codespaces.

1. Entre na sua conta do GitHub (uma por grupo basta).
2. Abra a página deste repositório.
3. Clique no botão verde **Code**, aba **Codespaces**, e em **Create codespace**.
4. Espere carregar (de 1 a 3 minutos na primeira vez).
5. O arquivo `aulas/aula1.ipynb` abre sozinho. Clique na primeira célula de código e aperte `Shift + Enter`.
6. Se aparecer um pedido para escolher o **kernel**, escolha **Python 3.12** (ou o Python que aparecer na lista).

> **O codespace aparece como "offline" ou não carrega?** Quase sempre é um bloqueador de anúncios (como o uBlock Origin) ou a proteção contra rastreamento do navegador. Desative-os só para o site do codespace (`github.dev`) e recarregue a página, ou abra uma janela anônima sem extensões. Se ainda assim não funcionar, abra o codespace no **Visual Studio Code** instalado no computador (menu do codespace, **Open in Visual Studio Code**).

---

## Como a aula funciona

Cada etapa tem **dois arquivos**:

| Arquivo | Para que serve |
|---|---|
| `aulas/aulaN.ipynb` | Teoria. Rode as células, leia e mude valores onde estiver escrito **EXPERIMENTE**. |
| `exercicios/exercicioN.ipynb` | Exercícios. Resolva nas células marcadas e confira com o `checar`. |

**Para conferir os exercícios:**

1. Salve o notebook (`Ctrl + S`).
2. Abra o terminal (menu **Terminal → New Terminal**).
3. Rode:

```
checar exercicio1.ipynb
```

Você vê ✅ (certo), ❌ (errado, com uma dica) ou ⏳ (ainda não resolvido) para cada exercício.

Se o comando `checar` não existir, use `python checar.py exercicio1.ipynb`.

**Regras de grupo:**

- **Máximo 3 pessoas por notebook.** Quanto maior o grupo, menos gente realmente programa.
- **Troquem de quem digita a cada exercício.** Quem só olha acha que entendeu, e na hora de fazer sozinho trava.
- Antes de rodar, **prevejam em voz alta o que vai aparecer**. Errar a previsão é onde se aprende.

**Dicas rápidas:**

- Rode as células **de cima para baixo**. Pular células causa erros estranhos.
- Quando o programa usa `input()`, a caixa de digitação aparece **no topo da tela**.
- O Python usa **indentação** (4 espaços) para saber o que está dentro do `if` ou do `while`.
- Mensagem de erro não é bronca: leia a **última linha**, ela diz o que deu errado.
- `ValueError` ao digitar um número: você digitou letras ou um decimal onde o programa esperava um inteiro.
- Célula que não termina? Clique no botão **■ (Interromper)** ao lado dela.

---

## Roteiro (120 minutos)

| Tempo | Atividade | Arquivos |
|---|---|---|
| 0:00-0:03 | **Demonstração:** o instrutor roda `python jogo.py` no projetor, para a turma ver aonde vai chegar. | `jogo.py` |
| 0:03-0:10 | **Algoritmo sem computador:** um aluno é o "robô" e a turma dá instruções exatas para ele fazer uma tarefa simples. | nenhum |
| 0:10-0:25 | **Abrir o Codespace** em cada grupo, escolher o kernel e rodar a primeira célula. O instrutor mostra no projetor onde aparece o `input()` e como usar o `checar`. | `aula1` |
| 0:25-0:55 | **Etapa 1:** variáveis, tipos, `input` e `int()`. | `aula1`, `exercicio1` |
| 0:55-1:08 | **Etapa 2:** `if / elif / else`. | `aula2`, `exercicio2` |
| 1:08-1:20 | **Etapa 3:** `True/False`, `and`, `or`, `not`. | `aula3`, `exercicio3` |
| 1:20-1:30 | **Intervalo.** | |
| 1:30-1:52 | **Etapa 4:** `while`. | `aula4`, `exercicio4` |
| 1:52-2:00 | **Fechamento:** `import random` e o jogo completo. Os exercícios da etapa 5 ficam para casa. | `aula5`, `exercicio5` |

**Este roteiro é apertado.** Se o tempo estourar, corte nesta ordem:

1. O exercício 3 da etapa 4 (já é opcional) e os blocos **EXPERIMENTE** das etapas 2 e 3.
2. A etapa 5 vira só demonstração.
3. Nunca corte a etapa 4: o `while` fecha o jogo e é o que faz o aluno sentir que construiu algo.

---

## Preparação do instrutor

**Antes da oficina:**

- [ ] **Teste o Codespace de ponta a ponta com uma conta que não seja a sua.** É o maior risco da aula. Confirme que:
  - o `aula1.ipynb` abre sozinho;
  - a primeira célula roda (e veja se pede para escolher o kernel);
  - o `input()` funciona dentro do notebook;
  - `checar exercicio1.ipynb` funciona no terminal.
- [ ] Confirme se alunos que não são donos do repositório conseguem criar o Codespace. Se o repositório for privado, cada conta precisa ser colaboradora. Se pedir para criar uma cópia (fork), explique rapidamente ou use a opção de repositório modelo ("Use this template").
- [ ] Peça com antecedência que cada grupo **crie uma conta no GitHub**. Sem isso, a aula começa com 20 minutos de cadastro.
- [ ] Confira a **cota gratuita de horas do Codespaces** nas configurações do GitHub. Costuma bastar para 2 horas, mas o valor muda com o tempo.
- [ ] Confira Wi-Fi para todos ao mesmo tempo e se o projetor funciona.
- [ ] **Não publique a pasta `instrutor/` (gabarito).** Mantenha-a só no seu computador.
- [ ] Resolva você mesmo os exercícios uma vez e rode o `checar`, errando de propósito, para conhecer as mensagens que os alunos vão ver.

**Plano B se o Codespace não abrir para algum grupo:**

- O grupo entra junto com outro que funcionou.
- Ou abre os notebooks no Google Colab (*Arquivo → Abrir notebook → GitHub*). Lá o `checar` não funciona, então os exercícios são conferidos pela saída esperada escrita em cada enunciado.

---

## Depois da oficina

Sugestões de continuação, na ordem em que eu seguiria:

1. Terminar os exercícios da etapa 5.
2. Fazer um segundo programa por conta própria: uma calculadora de média ou um quiz de 5 perguntas.
3. Aprender a tratar entrada inválida (`try / except`) e **listas e funções**, que ficaram de fora desta oficina.
4. **Git de verdade** (`mkdir`, `git add`, `commit`, `push`): bom tema para um segundo encontro, agora que já têm código para versionar.

---

## Estrutura do repositório

```
.devcontainer/    configuração do Codespace (Python, Jupyter e atalho checar)
aulas/            aula1.ipynb ... aula5.ipynb (teoria)
exercicios/       exercicio1.ipynb ... exercicio5.ipynb
imagens/          tabelas e fluxogramas usados nas aulas
checar.py         verificador dos exercícios
jogo.py           o jogo completo, para rodar no terminal
README.md         este arquivo
```
