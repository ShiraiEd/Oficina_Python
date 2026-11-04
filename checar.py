#!/usr/bin/env python3
"""Verificador dos exercícios da oficina.

Uso (no terminal):

    checar exercicio1.ipynb

Se o atalho "checar" não existir, use:  python checar.py exercicio1.ipynb

Antes de rodar, SALVE o notebook (Ctrl+S). O verificador lê o arquivo salvo,
encontra a célula de cada exercício, roda o código dela sozinho com entradas
simuladas e diz se a saída está certa.
"""
import json
import os
import re
import subprocess
import sys
import time

# Cada caso de teste:
#   entrada:  o que será "digitado" (uma resposta por linha)
#   esperado: trechos que devem aparecer na saída, NESTA ORDEM
#   proibido: trechos que NÃO podem aparecer
#   exato:    se presente, a saída inteira (ignorando espaços) deve ser igual
TESTES = {
    "exercicio1": {
        "ex1": {
            "titulo": "Exercício 1 - boas-vindas",
            "casos": [
                {"entrada": "Carlos\n", "esperado": ["Bem-vindo ao jogo, Carlos"]},
                {"entrada": "Ana\n", "esperado": ["Bem-vindo ao jogo, Ana"]},
            ],
        },
        "ex2": {
            "titulo": "Exercício 2 - converter a idade",
            "casos": [
                {"entrada": "20\n", "esperado": ["Ano que vem: 21"]},
                {"entrada": "0\n", "esperado": ["Ano que vem: 1"]},
            ],
        },
        "ex3": {
            "titulo": "Exercício 3 - anos em 2026",
            "casos": [
                {"entrada": "2000\n", "esperado": ["Você faz 26 anos em 2026"]},
                {"entrada": "1990\n", "esperado": ["Você faz 36 anos em 2026"]},
            ],
        },
    },
    "exercicio2": {
        "ex1": {
            "titulo": "Exercício 1 - palpite baixo",
            "casos": [
                {"entrada": "10\n", "esperado": ["Muito baixo!"], "proibido": ["Não está baixo"]},
                {"entrada": "50\n", "esperado": ["Não está baixo"], "proibido": ["Muito baixo!"]},
                {"entrada": "42\n", "esperado": ["Não está baixo"], "proibido": ["Muito baixo!"]},
            ],
        },
        "ex2": {
            "titulo": "Exercício 2 - if / elif / else do jogo",
            "casos": [
                {"entrada": "42\n", "esperado": ["Acertou!"], "proibido": ["Muito"]},
                {"entrada": "7\n", "esperado": ["Muito baixo!"], "proibido": ["Acertou!", "Muito alto!"]},
                {"entrada": "99\n", "esperado": ["Muito alto!"], "proibido": ["Acertou!", "Muito baixo!"]},
            ],
        },
    },
    "exercicio3": {
        "ex1": {
            "titulo": "Exercício 1 - palpite no intervalo",
            "casos": [
                {"entrada": "50\n", "esperado": ["Palpite válido"], "proibido": ["fora"]},
                {"entrada": "1\n", "esperado": ["Palpite válido"], "proibido": ["fora"]},
                {"entrada": "100\n", "esperado": ["Palpite válido"], "proibido": ["fora"]},
                {"entrada": "150\n", "esperado": ["Palpite fora do intervalo"], "proibido": ["válido"]},
                {"entrada": "0\n", "esperado": ["Palpite fora do intervalo"], "proibido": ["válido"]},
            ],
            "dica": "Os dois lados precisam ser verdadeiros ao mesmo tempo.",
        },
        "ex2": {
            "titulo": "Exercício 2 - adulto",
            "casos": [
                {"entrada": "25\n", "esperado": ["Adulto"], "proibido": ["Fora da faixa"]},
                {"entrada": "18\n", "esperado": ["Adulto"], "proibido": ["Fora da faixa"]},
                {"entrada": "17\n", "esperado": ["Fora da faixa"], "proibido": ["Adulto"]},
                {"entrada": "60\n", "esperado": ["Fora da faixa"], "proibido": ["Adulto"]},
                {"entrada": "70\n", "esperado": ["Fora da faixa"], "proibido": ["Adulto"]},
            ],
            "dica": "Confira os limites: 18 é adulto, 60 não é.",
        },
    },
    "exercicio4": {
        "ex1": {
            "titulo": "Exercício 1 - de 1 a 5",
            "casos": [{"entrada": "", "exato": "1 2 3 4 5"}],
        },
        "ex2": {
            "titulo": "Exercício 2 - senha",
            "casos": [
                {"entrada": "abc\npython\n", "esperado": ["Senha incorreta", "Acesso liberado"]},
                {"entrada": "abc\nxyz\npython\n",
                 "esperado": ["Senha incorreta", "Senha incorreta", "Acesso liberado"]},
                {"entrada": "python\n", "esperado": ["Acesso liberado"], "proibido": ["Senha incorreta"]},
            ],
        },
        "ex3": {
            "titulo": "Exercício 3 - contagem regressiva (opcional)",
            "casos": [{"entrada": "", "exato": "5 4 3 2 1 Fogo!"}],
        },
    },
    "exercicio5": {
        "ex1": {
            "titulo": "Exercício 1 - avaliação",
            "casos": [
                {"entrada": "3\n", "esperado": ["Excelente!"], "proibido": ["Bom!", "melhorar"]},
                {"entrada": "5\n", "esperado": ["Excelente!"], "proibido": ["Bom!", "melhorar"]},
                {"entrada": "6\n", "esperado": ["Bom!"], "proibido": ["Excelente!", "melhorar"]},
                {"entrada": "8\n", "esperado": ["Bom!"], "proibido": ["Excelente!", "melhorar"]},
                {"entrada": "9\n", "esperado": ["Dá para melhorar!"], "proibido": ["Excelente!", "Bom!"]},
            ],
            "dica": "Confira os limites: 5 é Excelente, 6 e 8 são Bom.",
        },
        "ex2": {
            "titulo": "Exercício 2 - limite de 7 tentativas",
            "casos": [
                {"entrada": "1\n2\n3\n4\n5\n6\n7\n",
                 "esperado": ["Acabaram as tentativas! O número era 42"]},
                {"entrada": "50\n42\n", "esperado": ["Acertou em 2 tentativas!"],
                 "proibido": ["Acabaram"]},
                {"entrada": "500\n1\n2\n3\n4\n5\n6\n42\n", "esperado": ["Acertou em 7 tentativas!"],
                 "proibido": ["Acabaram"]},
            ],
            "dica": "O while precisa parar quando acertar OU quando chegar a 7 tentativas.",
        },
    },
}

DICAS = {
    "SyntaxError": "Erro de escrita: confira parênteses, aspas e dois-pontos.",
    "IndentationError": "A indentação está errada. Use 4 espaços dentro do if/while.",
    "NameError": "Você usou um nome que não existe. Confira o nome das variáveis e se ainda sobrou algum ___.",
    "TypeError": "Misturou texto com número. Lembre do int() e do str().",
    "ValueError": "O int() recebeu algo que não é um número inteiro.",
    "EOFError": "O programa pediu mais respostas (input) do que deveria. Algum laço não parou?",
}

PLACEHOLDER = re.compile(r"(?<![A-Za-z0-9_])___(?![A-Za-z0-9_])")
LIMITE_SEGUNDOS = 5


def normalizar(texto):
    return " ".join(texto.split())


def fonte_da_celula(celula):
    src = celula.get("source", "")
    return "".join(src) if isinstance(src, list) else src


def tem_codigo(fonte):
    return any(l.strip() and not l.strip().startswith("#") for l in fonte.splitlines())


def achar_celula(nb, exercicio):
    for c in nb.get("cells", []):
        if c.get("cell_type") == "code" and c.get("metadata", {}).get("exercicio") == exercicio:
            return fonte_da_celula(c)
    return None


def executar(codigo, entrada):
    try:
        r = subprocess.run(
            [sys.executable, "-I", "-X", "utf8", "-c", codigo],
            input=entrada, capture_output=True, text=True,
            encoding="utf-8", timeout=LIMITE_SEGUNDOS,
        )
        return r.stdout, r.stderr, False
    except subprocess.TimeoutExpired:
        return "", "", True


def ultima_linha(texto):
    linhas = [l for l in texto.strip().splitlines() if l.strip()]
    return linhas[-1] if linhas else ""


def falta_em_ordem(saida, esperados):
    """Devolve o primeiro trecho esperado que não aparece na ordem certa."""
    pos = 0
    for e in esperados:
        alvo = normalizar(e)
        i = saida.find(alvo, pos)
        if i < 0:
            return e
        pos = i + len(alvo)
    return None


def checar_exercicio(codigo, ex):
    """Devolve (status, linhas_de_mensagem). status: ok, pendente ou erro."""
    if not tem_codigo(codigo):
        return "pendente", ["Ainda não resolvido (a célula está vazia)."]
    if PLACEHOLDER.search(codigo):
        return "pendente", ["Ainda há um ___ para preencher."]

    for caso in ex["casos"]:
        entrada = caso.get("entrada", "")
        saida, erro, estourou = executar(codigo, entrada)
        digitado = entrada.strip().replace("\n", " | ")
        contexto = f"Quando digito: {digitado}" if digitado else "Rodando a célula:"
        saida_n = normalizar(saida)
        obtido = saida_n[-200:] if saida_n else "(nada foi impresso)"

        if estourou:
            return "erro", [
                contexto,
                f"O programa não terminou em {LIMITE_SEGUNDOS} segundos.",
                "Dica: confira se há um laço (while) que nunca termina.",
            ]

        if erro.strip():
            linha = ultima_linha(erro)
            nome_erro = linha.split(":")[0].strip()
            msg = [contexto, f"Erro: {linha}"]
            if nome_erro in DICAS:
                msg.append("Dica: " + DICAS[nome_erro])
            return "erro", msg

        problema = None
        if "exato" in caso and saida_n != normalizar(caso["exato"]):
            problema = f"Esperado exatamente: {caso['exato']}"
        if problema is None:
            faltou = falta_em_ordem(saida_n, caso.get("esperado", []))
            if faltou is not None:
                problema = f"Esperado na saída: {faltou}"
        if problema is None:
            for p in caso.get("proibido", []):
                if normalizar(p) in saida_n:
                    problema = f"Não deveria aparecer: {p}"
                    break

        if problema:
            msg = [contexto, problema, f"Obtido: {obtido}"]
            if ex.get("dica"):
                msg.append("Dica: " + ex["dica"])
            return "erro", msg

    return "ok", []


def localizar(arg):
    """Aceita exercicio1, exercicio1.ipynb ou um caminho; procura em exercicios/."""
    pasta_repo = os.path.dirname(os.path.realpath(__file__))
    nome = arg if arg.endswith(".ipynb") else arg + ".ipynb"
    candidatos = [nome, arg, os.path.join(pasta_repo, "exercicios", os.path.basename(nome))]
    for c in candidatos:
        if os.path.isfile(c):
            return c
    return None


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    if len(sys.argv) != 2:
        print("Uso: checar exercicio1.ipynb")
        return 2

    caminho = localizar(sys.argv[1])
    if caminho is None:
        print(f"Não encontrei o arquivo: {sys.argv[1]}")
        print("Os exercícios são exercicio1.ipynb até exercicio5.ipynb.")
        return 2

    nome = os.path.splitext(os.path.basename(caminho))[0]
    if nome not in TESTES:
        print(f"Não há testes para '{nome}'. Use um arquivo de exercicios/ (exercicio1 a exercicio5).")
        return 2

    try:
        with open(caminho, encoding="utf-8") as f:
            nb = json.load(f)
    except Exception as e:
        print(f"Não consegui ler o notebook ({e}). Ele foi salvo corretamente?")
        return 2

    salvo = time.strftime("%H:%M:%S", time.localtime(os.path.getmtime(caminho)))
    print(f"Checando {os.path.basename(caminho)} (salvo às {salvo})")
    print("Se você mexeu agora, salve com Ctrl+S e rode de novo.\n")

    corretos = 0
    total = len(TESTES[nome])

    for chave, ex in TESTES[nome].items():
        codigo = achar_celula(nb, chave)
        if codigo is None:
            status, msg = "erro", ["Não encontrei a célula deste exercício. Ela foi apagada?"]
        else:
            status, msg = checar_exercicio(codigo, ex)

        icone = {"ok": "✅", "pendente": "⏳", "erro": "❌"}[status]
        print(f"{icone} {ex['titulo']}")
        for linha in msg:
            print(f"   {linha}")
        if status == "ok":
            corretos += 1

    print(f"\n{corretos}/{total} exercícios corretos.")
    return 0 if corretos == total else 1


if __name__ == "__main__":
    sys.exit(main())
