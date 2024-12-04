import tkinter as tk
from tkinter import messagebox


def press(key):
    """Adiciona o caractere pressionado ao visor."""
    if key == "=":
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception:
            messagebox.showerror("Erro", "Expressão inválida!")
            display.delete(0, tk.END)
    elif key == "C":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, key)


# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora")

# Personalização de cores
root.configure(bg="#1e1e2f")  # Fundo da janela
button_bg = "#282a36"        # Fundo dos botões
button_fg = "#f8f8f2"        # Cor do texto dos botões
display_bg = "#44475a"       # Fundo do display
display_fg = "#f8f8f2"       # Cor do texto do display

# Campo de entrada (visor)
display = tk.Entry(root, font=("Arial", 16), bd=5, insertwidth=4, width=14, justify="right",
                   bg=display_bg, fg=display_fg)
display.grid(row=0, column=0, columnspan=4)

# Botões da calculadora
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Criação e posicionamento dos botões
row_val = 1
col_val = 0
for button in buttons:
    def action(x=button): return press(x)
    tk.Button(
        root,
        text=button,
        padx=20,
        pady=20,
        font=("Arial", 14),
        bg=button_bg,
        fg=button_fg,
        activebackground="#6272a4",  # Cor ao clicar no botão
        activeforeground=button_fg,  # Cor do texto ao clicar no botão
        command=action
    ).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Inicia o loop da interface gráfica
root.mainloop()
