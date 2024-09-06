# Importa as bibliotecas necessárias
import webbrowser
from tkinter import Tk, Button, Label
import os
from tkinter import PhotoImage

# Função que abre uma URL no navegador web padrão
def abrir_url(url):
    webbrowser.open(url, new=2)

# Função para abrir a calculadora do Windows
def abrir_calculadora():
    os.system('calc')

def abrir_notepad():
    os.system('notepad')

# Cria a janela principal da interface gráfica
root = Tk()
root.title("ESPU - Eng. Computação - RU:1515161")  # Define o título da janela
window_width = 400
window_height = 800
root.geometry(f"{window_width}x{window_height}")  # Define o tamanho da janela

# Calcula a posição para centralizar a janela
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")  # Define a posição da janela

google_icon = PhotoImage(file="google_icon.gif")
whats = PhotoImage(file="whats.gif")
face = PhotoImage(file="face.gif")
insta_icon = PhotoImage(file="insta_icon.gif")
cnn_icon = PhotoImage(file="cnn_icon.gif")
youtube_icon = PhotoImage(file="youtube_icon.gif")
netflix_icon = PhotoImage(file="netflix_icon.gif")
gmail_icon = PhotoImage(file="gmail_icon.gif")
notepad_icon = PhotoImage(file="notepad_icon.gif")  # Carrega o ícone para o Bloco de Notas
calc_icon = PhotoImage(file="calc_icon.gif")  # Carrega o ícone para a Calculadora

# Cria o botão com o ícone
# Cria o botão com o ícone
b1 = Button(root,  command=lambda: abrir_url('https://www.google.com'), font=("Arial", 20),  width=20, height=2, image=google_icon, compound="left")
b1.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

b2 = Button(root, command=lambda: abrir_url('https://www.google.com/intl/pt_br/gmail/about/'),  font=("Arial", 20), width=20, height=2, image=gmail_icon, compound="left")
b2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

b3 = Button(root, command=lambda: abrir_url('https://www.instagram.com/'), font=("Arial", 20), width=20, height=2, image=insta_icon, compound="left")
b3.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

b4 = Button(root, command=lambda: abrir_url('https://facebook.com'), font=("Arial", 20), width=20, height=2, image=face, compound="left")
b4.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

b5 = Button(root, command=lambda: abrir_url('https://www.cnnbrasil.com.br/'), font=("Arial", 20), width=20, height=2, image=cnn_icon, compound="left")
b5.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

b6 = Button(root, command=lambda: abrir_url('https://www.youtube.com'), font=("Arial", 20), width=20, height=2, image=youtube_icon, compound="left")
b6.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)

b7 = Button(root,  command=lambda: abrir_url('https://www.netflix.com/br/'), font=("Arial", 20),  width=20, height=2, image=netflix_icon, compound="left")
b7.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)

b8 = Button(root, command=lambda: abrir_url('https://web.whatsapp.com'),  font=("Arial", 20), width=20, height=2, image=whats, compound="left")
b8.grid(row=3, column=1, sticky="nsew", padx=5, pady=5)

b9 = Button(root, command=abrir_notepad, font=("Arial", 20), width=20, height=2, image=notepad_icon, compound="left")
b9.grid(row=4, column=0, sticky="nsew", padx=5, pady=5)

b10 = Button(root, command=abrir_calculadora, font=("Arial", 20), width=20, height=2, image=calc_icon, compound="left")
b10.grid(row=4, column=1, sticky="nsew", padx=5, pady=5)

root.grid_rowconfigure((0,1,2,3,4), weight=1)  # Inclui a linha 4 no redimensionamento automático
root.grid_columnconfigure((0,1), weight=1) 

# Inicia o loop principal da interface gráfica
root.mainloop()
