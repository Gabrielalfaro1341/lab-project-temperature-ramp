
from tkinter import *
from tkinter import filedialog
from graficador_de_rampas import graficadorrampa

raiz=Tk()
raiz.wm_title('Graficador de rampas')
def abrirarchivo():
    archivo=filedialog.askopenfilename(title='abrir',initialdir='/home/gabito/Escritorio/Muestras/')
    figura=graficadorrampa(archivo)

Button(raiz, text='Ingrese archivo para rampa',command=abrirarchivo).pack()


raiz.mainloop()