import tkinter as tk
from tkinter import font

# Configurações da janela
root = tk.Tk()
root.title("Calculadora")
root.geometry("300x450")
root.configure(bg="#000000")

# Aqui alteramos a fonte
custom_font = font.Font(family="Helvetica", size=20)

# Para armazenar a expressão
expressao = ""

# Função para atualizar a expressão
def atualizar_expressao(valor):
    global expressao
    expressao += str(valor)
    label_resultado.config(text=expressao)

# Função para calcular o resultado
def calcular():
    global expressao
    try:
        resultado = str(eval(expressao))
        label_resultado.config(text=resultado)
        expressao = resultado
    except:
        label_resultado.config(text="Erro")
        expressao = ""

# Função para limpar a tela
def limpar():
    global expressao
    expressao = ""
    label_resultado.config(text="0")

# Label para exibir o resultado
label_resultado = tk.Label(root, text="0", font=custom_font, fg="#FFFFFF", bg="#000000", anchor="e", padx=20)
label_resultado.pack(fill=tk.BOTH, expand=True)

# Frame para os botões
frame_botoes = tk.Frame(root, bg="#000000")
frame_botoes.pack(fill=tk.BOTH, expand=True)

# Botões
botoes = [
    ("C", 1, 0, "#A5A5A5"), ("/", 1, 3, "#FF9500"),
    ("7", 2, 0, "#333333"), ("8", 2, 1, "#333333"), ("9", 2, 2, "#333333"), ("*", 2, 3, "#FF9500"),
    ("4", 3, 0, "#333333"), ("5", 3, 1, "#333333"), ("6", 3, 2, "#333333"), ("-", 3, 3, "#FF9500"),
    ("1", 4, 0, "#333333"), ("2", 4, 1, "#333333"), ("3", 4, 2, "#333333"), ("+", 4, 3, "#FF9500"),
    ("0", 5, 0, "#333333", 2), (".", 5, 2, "#333333"), ("=", 5, 3, "#FF9500")
]

for botao in botoes:
    if len(botao) == 4:  # Se não tiver colspan, adiciona o valor padrão 1
        botao = (*botao, 1)
    texto, linha, coluna, cor, colspan = botao

    botao_widget = tk.Button(
        frame_botoes, text=texto, font=custom_font, fg="#FFFFFF", bg=cor, bd=0, highlightthickness=0,
        command=lambda t=texto: atualizar_expressao(t) if t not in {"=", "C"} else calcular() if t == "=" else limpar()
    )
    botao_widget.grid(row=linha, column=coluna, columnspan=colspan, sticky="nsew", padx=5, pady=5)

# Ajustar o tamanho das linhas e colunas
for i in range(5):
    frame_botoes.rowconfigure(i, weight=1)
for j in range(4):
    frame_botoes.columnconfigure(j, weight=1)

# Iniciar a aplicação
root.mainloop()