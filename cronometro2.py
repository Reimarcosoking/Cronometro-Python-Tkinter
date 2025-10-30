from tkinter import *
from tkinter import ttk

# Configurando janela
janela = Tk()
janela.geometry("318x192")
janela.title("Cronômetro")
janela.configure(bg="black")
janela.resizable(False, False)


# Variáveis globais
contador = 0
rodar = False

# Funções
def iniciar():
    global contador
    if rodar:
        # cálculo baseado em segundos totais
        h = contador // 3600
        m = (contador % 3600) // 60
        s = contador % 60

        label_tempo.config(text=f"{h:02}:{m:02}:{s:02}")
        contador += 1
        label_tempo.after(1000, iniciar)

def start():
    global rodar
    rodar = True
    iniciar()

def pausar():
    global rodar
    rodar = False

def reiniciar():
    global contador, rodar
    rodar = False
    contador = 0
    label_tempo.config(text="00:00:00")

# Label
label_tempo = Label(janela, text="00:00:00", font=("Times", 58, "bold"), bg="black", fg="blue")
label_tempo.place(x=16, y=25)

# Botões
Button(janela, text="Iniciar", command=start, width=8, height=2,
       font="Ivy 9 bold", relief="raised", overrelief="groove",
       bg="black", fg="white").place(x=16, y=118)

Button(janela, text="Pausar", command=pausar, width=8, height=2,
       font="Ivy 9 bold", relief="raised", overrelief="groove",
       bg="black", fg="white").place(x=116, y=118)

Button(janela, text="Reiniciar", command=reiniciar, width=8, height=2,
       font="Ivy 9 bold", relief="raised", overrelief="groove",
       bg="black", fg="white").place(x=216, y=118)

janela.mainloop()
