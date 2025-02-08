import tkinter as tk
from tkinter import font

root = tk.Tk()
root.title("Calculadora")
root.geometry("300x500")
root.configure(bg="#000000")

custom_font = font.Font(family="SF Pro Display", size=20)
expressao = ""


def atualizar_expressao(valor):
    global expressao
    expressao += str(valor)
    label_resultado.config(text=expressao)


def calcular():
    global expressao
    try:
        expressao = expressao.replace("x", "*")
        resultado = str(eval(expressao))
        label_resultado.config(text=resultado)
        expressao = resultado
    except:
        label_resultado.config(text="Erro")
        expressao = ""


def limpar():
    global expressao
    expressao = ""
    label_resultado.config(text="0")


def inverter_sinal():
    global expressao
    if expressao and expressao[0] == '-':
        expressao = expressao[1:]
    else:
        expressao = '-' + expressao if expressao else ""
    label_resultado.config(text=expressao)


def porcentagem():
    global expressao
    try:
        valor = float(eval(expressao))
        expressao = str(valor / 100)
        label_resultado.config(text=expressao)
    except:
        label_resultado.config(text="Erro")
        expressao = ""


label_resultado = tk.Label(root, text="0", font=custom_font, fg="#FFFFFF", bg="#000000", anchor="e", padx=20)
label_resultado.pack(fill=tk.BOTH, expand=True)

frame_botoes = tk.Frame(root, bg="#000000")
frame_botoes.pack(fill=tk.BOTH, expand=True)

botoes = [
    ("AC", 1, 0, "#A5A5A5", 1), ("+/-", 1, 1, "#A5A5A5", 1), ("%", 1, 2, "#A5A5A5", 1), ("/", 1, 3, "#FF9500", 1),
    ("7", 2, 0, "#333333", 1), ("8", 2, 1, "#333333", 1), ("9", 2, 2, "#333333", 1), ("x", 2, 3, "#FF9500", 1),
    ("4", 3, 0, "#333333", 1), ("5", 3, 1, "#333333", 1), ("6", 3, 2, "#333333", 1), ("-", 3, 3, "#FF9500", 1),
    ("1", 4, 0, "#333333", 1), ("2", 4, 1, "#333333", 1), ("3", 4, 2, "#333333", 1), ("+", 4, 3, "#FF9500", 1),
    ("0", 5, 0, "#333333", 2), (".", 5, 2, "#333333", 1), ("=", 5, 3, "#FF9500", 1)
]

for (texto, linha, coluna, cor, colspan) in botoes:
    cmd = lambda t=texto: atualizar_expressao(t) if t not in {"=", "AC", "+/-", "%"} else None
    if texto == "AC":
        cmd = limpar
    elif texto == "+/-":
        cmd = inverter_sinal
    elif texto == "%":
        cmd = porcentagem
    elif texto == "=":
        cmd = calcular

    botao = tk.Button(frame_botoes, text=texto, font=custom_font,
                      fg="#000000" if texto in {"AC", "+/-", "%"} else "#FFFFFF",
                      bg=cor, bd=0, highlightthickness=0, command=cmd)
    botao.grid(row=linha, column=coluna, columnspan=colspan, sticky="nsew", padx=2, pady=2)

for i in range(6): frame_botoes.rowconfigure(i, weight=1)
for j in range(4): frame_botoes.columnconfigure(j, weight=1)

root.mainloop()