# Importa as bibliotecas necessárias
import webbrowser
from tkinter import Tk, Button, Label
import os
import sys
from tkinter import PhotoImage

# Ajusta o caminho da imagem para o executável compilado
if getattr(sys, 'frozen', False):
    img_google = os.path.join(sys._MEIPASS, "google_icon.gif")
    img_gmail = os.path.join(sys._MEIPASS, "gmail_icon.gif")
    img_instagram = os.path.join(sys._MEIPASS, "insta_icon.gif")
    img_whats = os.path.join(sys._MEIPASS, "whats.gif")
    img_face = os.path.join(sys._MEIPASS, "face.gif")
    img_cnn = os.path.join(sys._MEIPASS, "cnn_icon.gif")
    img_youtube = os.path.join(sys._MEIPASS, "youtube_icon.gif")
    img_netflix = os.path.join(sys._MEIPASS, "netflix_icon.gif")
    img_calc = os.path.join(sys._MEIPASS, "calc_icon.gif")
    img_notepad = os.path.join(sys._MEIPASS, "notepad_icon.gif")
    # adicione mais conforme necessário
else:
    img_google = "google_icon.gif"
    img_gmail = "gmail_icon.gif"
    img_instagram = "insta_icon.gif"
    img_whats ="whats.gif"
    img_face = "face.gif"
    img_cnn = "cnn_icon.gif"
    img_youtube = "youtube_icon.gif"
    img_netflix = "netflix_icon.gif"
    img_calc = "calc_icon.gif"
    img_notepad = "notepad_icon.gif"
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
root.title("ESPUninter - Eng. Computação - RU:151561")  # Define o título da janela
window_width = 400
window_height = 700
root.geometry(f"{window_width}x{window_height}")  # Define o tamanho da janela

# Calcula a posição para centralizar a janela
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")  # Define a posição da janela

google_icon = PhotoImage(file=img_google)
whats = PhotoImage(file=img_whats)
face = PhotoImage(file=img_face)
insta_icon = PhotoImage(file=img_instagram)
cnn_icon = PhotoImage(file=img_cnn)
youtube_icon = PhotoImage(file=img_youtube)
netflix_icon = PhotoImage(file=img_netflix)
gmail_icon = PhotoImage(file=img_gmail)
calc_icon = PhotoImage(file=img_calc)
notepad_icon = PhotoImage(file=img_notepad)

# Cria o botão com o ícone
b1 = Button(root,  command=lambda: abrir_url('https://www.google.com'), font=("Arial", 20),  width=20, height=2, image=google_icon, compound="left")
b1.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

b2 = Button(root, command=lambda: abrir_url('https://www.google.com/intl/pt_br/gmail/about/'),  font=("Arial", 20), width=20, height=2, image=gmail_icon, compound="left")
b2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

b3 = Button(root, command=lambda: abrir_url('https://instagram.com'), font=("Arial", 20), width=20, height=2, image=insta_icon, compound="left")
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

b9 = Button(root, command=lambda: abrir_calculadora(), font=("Arial", 20), width=20, height=2, image=calc_icon, compound="left")
b9.grid(row=4, column=0, sticky="nsew", padx=5, pady=5)

b10 = Button(root, command=lambda: abrir_notepad(), font=("Arial", 20), width=20, height=2, image=notepad_icon, compound="left")
b10.grid(row=4, column=1, sticky="nsew", padx=5, pady=5)

root.grid_rowconfigure((0,1,2,3,4), weight=1)
root.grid_columnconfigure((0,1), weight=1)

# Inicia o loop principal da interface gráfica
root.mainloop()

