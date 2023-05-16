from stanfordkarel import *
from sys import argv

comandos_proibidos = {
    "return ": "return",
    "==": "Comparação (==)",
    "=": "Aribuição (=)",
    "break": "break",
    "continue": "continue",
    " global ": "global",
    "yield": "yield",
    "True": "Valor lógico (True)",
    "False": "Valor lógico (False)",
    "[": "Listas ([...])",
    "]": "Listas ([...])",
    "{": "Dicionários ({...})",
    "}": "Dicionários ({...})",
}


class ComandoInvalido(Exception):

    def __init__(self, erros):
        mensagens = [comandos_proibidos[erro] for erro in erros]
        mensagens = list(dict.fromkeys(mensagens))
        mensagem = ", \n  -> ".join(mensagens)
        super().__init__(f"Recurso(s) não permitido(s):\n  -> {mensagem}")


class MuitosImports(Exception):

    def __init__(self):
        super().__init__("Apenas o 'from KarelCAP import *' é permitido")


def verifique_arquivo():
    contador_import = 0
    with open(argv[0], "r") as fonte:
        for linha in fonte:
            erros = [erro for erro in comandos_proibidos.keys()
                     if erro in linha]
            if len(erros) > 0:
                raise ComandoInvalido(erros)
            if "import " in linha or " import " in linha:
                contador_import += 1
    if contador_import > 1:
        raise MuitosImports()


executou = False


def Execute(mundo = ""):
    global executou
    verifique_arquivo()
    if not executou:
        executou = True
        run_karel_program(mundo)
