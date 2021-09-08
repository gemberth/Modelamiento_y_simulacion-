from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from scipy.stats import poisson
from tkinter import filedialog
from tkinter import messagebox
from scipy.stats import chi2
from pandas import DataFrame
import scipy.stats as stats
import matplotlib as mpl
from math import sqrt
from tkinter import *
import pandas as pd
import numpy as np
import matplotlib
import random
import math
import sys
from tqdm.auto import tqdm
from PIL import ImageTk,Image
import tkinter as tk
#pyinstaller --windowed --onefile --icon=./logo.ico examen.py
raiz=Tk()
raiz.title('Modelamiento y Simulación')
#raiz.resizable(False, False)
raiz.geometry('500x200')
raiz.iconbitmap('C:/Users/Admin/AppData/Local/Programs/Python/Python39/Scripts
/logo.ico')
myFrame=Frame(raiz)
myFrame.pack()
Label(myFrame, text='DATOS PERSONALES', font=('Arial', 16)).grid(row=0,
column=0, pady=10, columnspan=5)
uleam=Label(myFrame, text='Universidad Laica Eloy Alfaro de
Manabí').grid(row=1, column=0, columnspan=5)
materia=Label(myFrame, text='Modelamiento y Simulación').grid(row=2, column=0,
columnspan=5)
nombre=Label(myFrame, text='Anderson Plua Toala').grid(row=3, column=0,
columnspan=5)
curso=Label(myFrame, text='Sexto "B"').grid(row=4, column=0, columnspan=5)
#aaa = PhotoImage(file="yo.jpg")
#aLa = Label(myFrame, image=aaa).place(x=500, y=500)
#aaa = ImageTk.PhotoImage(Image.open('yo.jpg'))
#aLa = Label(myFrame, image=aaa)
#aLa.grid(row=5, column=0)
#aLa.pack()
def estadistica():
 estadist=Tk()
 estadist.title('Estadística')
 estadist.resizable(False, False)
 def abrirArchivo():
 global datos
 archivo =
filedialog.askopenfilename(initialdir='C:/Users/Admin/Desktop/MODELAMIENTO_SIM
ULACION', title='Seleccione archivo',
 filetype=(('Excel', '*.xlsx*'),
('Csv', '*.csv*')))
 exporta = pd.read_excel(archivo)
 datos = exporta

 textCarga.config(text="¡Archivo cargado exitosamente!")
 with pd.option_context('display.max_rows', None,
'display.max_columns', None, 'display.width', None):
 texP.insert('1.0', datos)

 def graficaBarraCaso():
 x=datos["CASOS"] #CAMBIAR VARIABLE EN CASO INDICADO
 plt.figure(figsize=(8,5))
 plt.hist(x,bins=8,color='orange')
 plt.axvline(x.mean(),color='red',label='Media')
 plt.axvline(x.median(),color='yellow',label='Mediana')
 plt.axvline(x.mode()[0],color='green',label='Moda')
 plt.xlabel('Total de casos')
 plt.ylabel('Frecuencia')
 plt.legend()
 plt.show()

 def graficaBarraFallecido():
 x=datos["FALLECIDOS"] #CAMBIAR VARIABLE EN CASO INDICADO
 plt.figure(figsize=(8,5))
 plt.hist(x,bins=8,color='orange')
 plt.axvline(x.mean(),color='red',label='Media')
 plt.axvline(x.median(),color='yellow',label='Mediana')
 plt.axvline(x.mode()[0],color='green',label='Moda')
 plt.xlabel('Total de casos')
 plt.ylabel('Frecuencia')
 plt.legend()
 plt.show()
 def media():
 t1, t2, t3, t4, t5 = datos.mean() #CAMBIAR VARIABLE EN CASO INDICADO
 datMean = datos.mean()
 textMedia.config(text=datMean)
 #texP.insert('1.0', datMean)
 def mediana():
 m1, m2, m3, m4, m5 = datos.median() #CAMBIAR VARIABLE EN CASOINDICADO
 datMedian = datos.median()
 textMediana.config(text=datMedian)
 def moda():
 #mo1 = datos["CASOS"].mode()
 #mo2 = datos["FALLECIDOS"].mode()
 #VaPD = pd.DataFrame(mo1,mo2)
 datosGenerales = datos[['CASOS','FALLECIDOS']].describe()
 textModa.config(text=datosGenerales)
 def graficaLineal():
 x = datos["DIA"]
 t1 = datos["CASOS"]
 t2 = datos["FALLECIDOS"]
 plt.figure(figsize=(10,6))
 plt.plot(x,t1,x,t2,marker='o')
 plt.xlabel('Dias de incidencias')
 plt.ylabel('Cantidad de usuarios')
 plt.legend(('CASOS','FALLECIDOS', ''), prop = {'size':10},loc='upper
right')
 plt.show()
 def graficoVariasVentanas():
 x = range(284)
 plt.figure(figsize=(10,5))
 plt.subplot(131)
 t1 = datos["CASOS"]
 p1 = plt.plot(x,t1,'r-')
 plt.ylabel('USUARIOS')
 plt.title(' CASOS DE USUARIOS')
 plt.subplot(132)
 t2 = datos["FALLECIDOS"]
 p1 = plt.plot(x,t2,'g-')
 plt.title(' FALLECIDOS')
 plt.subplot(133)
 t3 = datos["DIA"]
 p1, = plt.plot(x,t3,'b-')
 plt.title(' DIA')
 plt.show()
 def tablaFrecuencia():
 global dfclases
 lis = datos["CASOS"].unique()
 lis
 dfclases=pd.DataFrame(lis,columns=["CASOS"])
 dfclases
 with pd.option_context('display.max_rows', None,
'display.max_columns', None):
 textTablaFrecuencia.insert('1.0', dfclases)
 def frecuenciaAbsoluta():
 datafi=pd.crosstab(index=datos["CASOS"], columns = "fi")
 # Creamos una lista con los valores de las frecuencias
 li = datafi.values
 # agregamos una columna al dataframe
 dfclases["fi"] = li
 #observamos dfclase
 dfclases
 with pd.option_context('display.max_rows', None,
'display.max_columns', None):
 textFrecuenciaAbsoluta.insert('1.0', dfclases)
 def frecuenciaRelativa():
 total = dfclases.sum(axis=0)
 datahi = dfclases["fi"]/total["fi"] # aqui calculamos la frecuencia
 datahi.values
 # agregamos nueva columna de frecuencia relativa
 dfclases["hi"] = datahi
 dfclases
 with pd.option_context('display.max_rows', None,
'display.max_columns', None):
 textFrecuenciaRelativa.insert('1.0', dfclases.round(3))
 def frecuenciaAcumulada():
 FA = dfclases["fi"].values
 # obtenemos FA
 a=[]
 b=0
 for c in FA:
 b = c + b
 a.append(b)
 dfclases["FA"] = a
 HI = dfclases["hi"].values
 # obtenemos HI
 a=[]
 b=0
 for c in HI:
 b = c + b
 a.append(b)
 dfclases["HI"] = a
 dfclases
 with pd.option_context('display.max_rows', None,
'display.max_columns', None):
 textFrecuenciaAcumulada.insert('1.0', dfclases.round(3))

 def limpiar():
 textMedia.config(text="")
 textMediana.config(text="")
 textModa.config(text="")
 textTablaFrecuencia.delete('1.0', END)
 textFrecuenciaAbsoluta.delete('1.0', END)
 textFrecuenciaRelativa.delete('1.0', END)
 textFrecuenciaAcumulada.delete('1.0', END)

 def limpiarTodo():
 textMedia.config(text="")
 textMediana.config(text="")
 textModa.config(text="")
 texP.delete('1.0', END)
 textTablaFrecuencia.delete('1.0', END)
 textFrecuenciaAbsoluta.delete('1.0', END)
 textFrecuenciaRelativa.delete('1.0', END)
 textFrecuenciaAcumulada.delete('1.0', END)
 textModa.config(text="")

 #BOTONES----------------------------------
 boton = Button(estadist, text="Cargar archivo", command=abrirArchivo,
padx=2, pady=2, bg='dodgerblue', fg="white").grid(column=0, columnspan=3,
row=0, sticky=(W,E))
textCarga=Label(estadist, text="")
 textCarga.grid(column=0, columnspan=3, row=1, sticky=(W,E))
 boton = Button(estadist, text="Gráfico Casos", command=graficaBarraCaso,
padx=1, pady=1, bg='green', fg="white").grid(column=0, row=2, sticky=(W,E))
 boton = Button(estadist, text="Gráfico Fallecidos",
command=graficaBarraFallecido, padx=1, pady=1, bg='green',
fg="white").grid(column=1, row=2, sticky=(W,E))
 boton = Button(estadist, text="Gráfico Lineal", command=graficaLineal,
padx=1, pady=1, bg='green', fg="white").grid(column=2, row=2, sticky=(W,E))
 boton = Button(estadist, text="Gráfico Varios",
command=graficoVariasVentanas, padx=1, pady=1, bg='green',
fg="white").grid(column=0, row=3, sticky=(W,E))
 boton = Button(estadist, text="Limpiar cálculos", command=limpiar, padx=1,
pady=1, bg='red').grid(column=1, row=3, sticky=(W,E))
 boton = Button(estadist, text="Limpiar Todo", command=limpiarTodo, padx=1,
pady=1, bg='red').grid(column=2, row=3, sticky=(W,E))

 boton = Button(estadist, text="Media", command=media, padx=1, pady=1,
bg='green', fg="white", width=28).grid(column=4, row=0, sticky=(W,E))
 textMedia=Label(estadist, text="", bg='white')
 textMedia.grid(column=4, rowspan=4, row=1, sticky=(N, S, W,E))
 boton = Button(estadist, text="Mediana", command=mediana, padx=1, pady=1,
bg='green', fg="white", width=28).grid(column=4, row=5, sticky=(W,E))
 textMediana=Label(estadist, text="", bg='white')
 textMediana.grid(column=4, rowspan=4, row=6, sticky=(N, S, W,E))
 boton = Button(estadist, text="Resumen General", command=moda, padx=1,
pady=1, bg='green', fg="white", width=28).grid(column=4, row=10, sticky=(W,E))
 textModa=Label(estadist, text="", bg='white')
 textModa.grid(column=4, rowspan=7, row=11, sticky=(N, S, W,E))
 boton = Button(estadist, text="Tabla Frecuencia", command=tablaFrecuencia,
padx=1, pady=1, bg='green', fg="white", width=12).grid(column=6, row=0,
sticky=(W,E))
 textTablaFrecuencia=Text(estadist, bg='white', width=12)
 textTablaFrecuencia.grid(column=6, rowspan=17, row=1, sticky=(N, S, W,E))
 scrP=Scrollbar(estadist, orient=VERTICAL,
command=textTablaFrecuencia.yview)
 scrP.grid(row=1, column=7, sticky=(N,S), rowspan=17)
 textTablaFrecuencia.config(yscrollcommand=scrP.set)
 boton = Button(estadist, text="Frecuencia Absoluta",
command=frecuenciaAbsoluta, padx=1, pady=1, bg='green', fg="white",
width=17).grid(column=8, row=0, sticky=(W,E))
 textFrecuenciaAbsoluta=Text(estadist, bg='white', width=17)
 textFrecuenciaAbsoluta.grid(column=8, rowspan=17, row=1, sticky=(N, S,
W,E))
 scrFrecAbs=Scrollbar(estadist, orient=VERTICAL,
command=textFrecuenciaAbsoluta.yview)
 scrFrecAbs.grid(row=1, column=9, sticky=(N,S), rowspan=17)
 textFrecuenciaAbsoluta.config(yscrollcommand=scrFrecAbs.set)
 boton = Button(estadist, text="Frecuencia Relativa",
command=frecuenciaRelativa, padx=1, pady=1, bg='green', fg="white",
width=22).grid(column=10, row=0, sticky=(W,E))
 textFrecuenciaRelativa=Text(estadist, bg='white', width=22)
 textFrecuenciaRelativa.grid(column=10, rowspan=17, row=1, sticky=(N, S,
W,E))
 scrFrecRel=Scrollbar(estadist, orient=VERTICAL,
command=textFrecuenciaRelativa.yview)
scrFrecRel.grid(row=1, column=11, sticky=(N,S), rowspan=17)
 textFrecuenciaRelativa.config(yscrollcommand=scrFrecRel.set)
 boton = Button(estadist, text="Frecuencia Acumulada",
command=frecuenciaAcumulada, padx=1, pady=1, bg='green', fg="white",
width=35).grid(column=12, row=0, sticky=(W,E))
 textFrecuenciaAcumulada=Text(estadist, bg='white', width=35)
 textFrecuenciaAcumulada.grid(column=12, rowspan=17, row=1, sticky=(N, S,
W,E))
 scrFrecAcum=Scrollbar(estadist, orient=VERTICAL,
command=textFrecuenciaAcumulada.yview)
 scrFrecAcum.grid(row=1, column=13, sticky=(N,S), rowspan=17)
 textFrecuenciaAcumulada.config(yscrollcommand=scrFrecAcum.set)
 #texP=Text(metCuaMe, wrap="none", width=40)
 #texP.grid(row=2, column=0, columnspan=4, sticky=(W,E))
 #MOSTRAR-------------------------------
 Label(estadist, text="DATOS CARGADOS:").grid(column=0, row=4,
columnspan=3, sticky=(W,E))
 texP=Text(estadist, wrap="none", width=50)
 texP.grid(row=5, column=0, columnspan=3, sticky=(W,E), rowspan=13)
 scrP=Scrollbar(estadist, orient=VERTICAL, command=texP.yview)
 scrP.grid(row=5, column=3, sticky=(N,S), rowspan=13)
 scrhP=Scrollbar(estadist, orient=HORIZONTAL, command=texP.xview)
 scrhP.grid(row=18, column=0, columnspan=3, sticky=(W,E))
 texP.config(yscrollcommand=scrP.set, xscrollcommand=scrhP.set)
 #texP.config(yscrollcommand=scrP.set)
 estadist.mainloop()

#METODO CUADRADO MEDIO--------------------------------------------------------
-------------------------
def metodoCuadradoMedio():
 metCuaMe=Tk()
 metCuaMe.title('Método Cuadrado Medio')
 metCuaMe.resizable(False, False)
 def calcular():
 n = int(entrada_texto.get())
 r = int(entrada_texto2.get())
 l=len(str(r)) # determinamos el número de dígitos
 lista = [] # almacenamos en una lista
 lista2 = []
 i=0
 global df
 while i < n:
 x=str(r*r) # Elevamos al cuadrado r
 if l % 2 == 0:
 x = x.zfill(l*2)
 else:
 x = x.zfill(l)
 y=(len(x)-l)/2
 y=int(y)
 r=int(x[y:y+l])
 lista.append(r)
 lista2.append(x)
 i=i+1
 df = pd.DataFrame({'X2':lista2,'Xi':lista})
 dfrac = df["Xi"]/10**l
 df["ri"] = dfrac
 df
 with pd.option_context('display.max_rows', None,
'display.max_columns', None, 'display.width', None):
 texP.insert('1.0', df)
 def grafico():
 #GRAFICA
 fig = Figure(figsize=(6,6), dpi=100)
 a = fig.add_subplot(111)
 x1=df['ri']
 plt.plot(x1)
 plt.title('Generador de Numeros Aleatorios Cuadrados Medios')
 plt.xlabel('Serie')
 plt.ylabel('Aleatorios')
 plt.show()
 def limpiar():
 texP.delete('1.0', END)
 #METODO CUADRADO MEDIO------------------
 valor = ""
 valor2 = ""
 entrada_texto = Label(metCuaMe, text="n:", width=5).grid(column=0, row=0)
 entrada_texto = Entry(metCuaMe, width=10, textvariable=valor)
 entrada_texto.grid(column=1, row=0)
 entrada_texto2 = Label(metCuaMe, text="r:", width=5).grid(column=2, row=0)
 entrada_texto2 = Entry(metCuaMe, width=10, textvariable=valor2)
 entrada_texto2.grid(column=3, row=0)
 #BOTON----------------------------------
 boton = Button(metCuaMe, text="Limpiar", command=limpiar, padx=1, pady=1,
bg='red').grid(column=3, row=1, sticky=(W,E))
 boton = Button(metCuaMe, text="Calcular", command=calcular, padx=1,
pady=1, bg='green', fg = "white").grid(column=0, columnspan=2, row=1,
sticky=(W,E))
 boton = Button(metCuaMe, text="Gráfico", command=grafico, padx=1, pady=1,
bg='dodgerblue', fg = "white").grid(column=2, row=1, sticky=(W,E))
 #MOSTRAR-------------------------------
 texP=Text(metCuaMe, wrap="none", width=35)
 texP.grid(row=2, column=0, columnspan=4, sticky=(W,E))
 scrP=Scrollbar(metCuaMe, orient=VERTICAL, command=texP.yview)
 scrP.grid(row=2, column=5, sticky=(N,S))
 #scrh=Scrollbar(metCuaMe, orient=HORIZONTAL, command=texP.xview)
 #scrh.grid(row=2, column=8, columnspan=8, sticky=(W,E))
 texP.config(yscrollcommand=scrP.set)
 metCuaMe.mainloop()
#METODO CONGRUENCIAL LINEAL---------------------------------------------------
------------------------------
def metodoCongruencialLinea():
 metConLin=Tk()
 metConLin.title('Método Congruencial Lineal')
 metConLin.resizable(False, False)
 def calcular():
 global r, df
 n = int(ent_n.get())
 mF = int(ent_m.get())
 pot = int(ent_pon.get()) #potencia opcional
 a = int(ent_a.get())
 x0 = int(ent_x0.get())
 c = int(ent_c.get())
 m = mF ** pot
 x = [1] * n
 r = [0.1] * n
 for i in range(0, n):
 x[i] = ((a*x0)+c) % m
 x0 = x[i]
 r[i] = x0 / m
 # llenamos nuestro DataFrame
 d = {'Xn': x, 'ri': r }
 df = pd.DataFrame(data=d)
 df
 with pd.option_context('display.max_rows', None,
'display.max_columns', None, 'display.width', None):
 texP.insert('1.0', df)
 #REVISA------------------------------------------------------------
 #dfMCL
 inv_xp = df[:1]
 inv_xp
 #CLIENTES POR HORA LANDA=(?)
 landa=4
 dfexp = df['ri']
 # calculamos a todos los elementos la inversa
 exp_x = dfexp.values*(-1/landa)*np.log(dfexp)
 # anexamos al Datafram dfMCL
 df["exp_x"] = exp_x
 # Mostramos el resultado
 #dfMCL.head()
 #resultado.config(text=df.head())
 #GRAFICA DE PULSOS
 #plt.plot(r,'r-', marker='o',)
 #plt.figure(figsize=(50,15))
 #dfgrafico = df.filter(items=['ri','inv_x','exp_x'])
 #plt.title("ALEATORIO")
 #dfgrafico.plot(figsize=(50,15))
 #plt.show()
 #GRAFICA
 def graficaNumerosGenerados ():
 plt.plot(r,marker='o')
 plt.title('Generador de Numeros Aleatorios ')
 plt.xlabel('Serie')
 plt.ylabel('Aleatorios')
 plt.show()
 #GRAFICA DE BARRAS
 def histograma ():
 rS= df['ri']
 #rS
 plt.figure(figsize=(10,5))
 plt.hist(rS,bins=20,color='blue')
 plt.xlabel('# Aleatorios generados')
 plt.ylabel('Ocurrencias en rangos')
 plt.show()
 #GRAFICA DE DISPERSION
 def graficaDispercion ():
 plt.scatter(df.index,df['ri'])
 plt.show()
 def limpiar():
 texP.delete('1.0', END)
 #VARIABLES------------------
 mCn = ""
 mCm = ""
 mCa = ""
 mCx0 = ""
 mCc = ""
 ent_n = Label(metConLin, text="n:", width=5).grid(column=0, row=0)
 ent_n = Entry(metConLin, width=10, textvariable=mCn)
 ent_n.grid(column=1, row=0)
 ent_m = Label(metConLin, text="m:", width=5).grid(column=2, row=0)
 ent_m = Entry(metConLin, width=10, textvariable=mCm)
 ent_m.grid(column=3, row=0)
 mCp = "1"
 ent_pon = Label(metConLin, text="^?:", width=5).grid(column=4, row=0)
 ent_pon = Entry(metConLin, width=10, textvariable=mCp)
 ent_pon.grid(column=5, row=0)
 ent_a = Label(metConLin, text="a:", width=5).grid(column=6, row=0)
 ent_a = Entry(metConLin, width=10, textvariable=mCa)
 ent_a.grid(column=7, row=0)
 ent_x0 = Label(metConLin, text="x0:", width=5).grid(column=8, row=0)
 ent_x0 = Entry(metConLin, width=10, textvariable=mCx0)
 ent_x0.grid(column=9, row=0)
 ent_c = Label(metConLin, text="c:", width=5).grid(column=10, row=0)
 ent_c = Entry(metConLin, width=10, textvariable=mCc)
 ent_c.grid(column=11, row=0)
 #BOTON----------------------------------
 boton = Button(metConLin, text="Calcular", command=calcular, padx=1,
pady=1, bg='green', fg = "white").grid(column=0, columnspan=4, row=1,
sticky=(W,E))
 boton = Button(metConLin, text="Gráfica n° generados",
command=graficaNumerosGenerados, padx=1, pady=1, bg='dodgerblue', fg =
"white").grid(column=4, columnspan=2, row=1, sticky=(W,E))
 boton = Button(metConLin, text="Histograma", command=histograma, padx=1,
pady=1, bg='dodgerblue', fg = "white").grid(column=6, columnspan=2, row=1,
sticky=(W,E))
 boton = Button(metConLin, text="Gráfica de disperción",
command=graficaDispercion, padx=1, pady=1, bg='dodgerblue', fg =
"white").grid(column=8, columnspan=2, row=1, sticky=(W,E))
 boton = Button(metConLin, text="Limpiar", command=limpiar, padx=1, pady=1,
bg='red').grid(column=10, columnspan=2, row=1, sticky=(W,E))
 #MOSTRAR-------------------------------
 texP=Text(metConLin, wrap="none")
 texP.grid(row=2, column=0, columnspan=12, sticky=(W,E))
 scrP=Scrollbar(metConLin, orient=VERTICAL, command=texP.yview)
 scrP.grid(row=2, column=13, sticky=(N,S))
 #scrh=Scrollbar(metCuaMe, orient=HORIZONTAL, command=texP.xview)
 #scrh.grid(row=2, column=8, columnspan=8, sticky=(W,E))
 texP.config(yscrollcommand=scrP.set)
 metConLin.mainloop()
#METODO CONGRUENCIAL MULTIPLICATIVO-------------------------------------------
--------------------------------------
def metodoCongruencialMultiplicativo():
 metConMul=Tk()
 metConMul.title('Método Congruencial Multiplicativo')
 metConMul.resizable(False, False)
 def calcular():
 global r, df
 n = int(ent_cn.get())
 m = int(ent_cm.get())
 a = int(ent_ca.get())
 x0 = int(ent_cx0.get())
 x = [1] * n
 r = [0.1] * n
 for i in range(0, n):
 x[i] = (a*x0) % m
 x0 = x[i]
 r[i] = x0 / m
 d = {'Xn': x, 'ri': r }
 df = pd.DataFrame(data=d)
 df
 with pd.option_context('display.max_rows', None,
'display.max_columns', None, 'display.width', None):
 texP.insert('1.0', df)
 #GRAFICA
 def graficaNumerosGenerados():
 plt.plot(r,'r-', marker='o',)
 plt.title('Grafica y área de números Aleatorios ')
 plt.xlabel('Serie')
 plt.ylabel('Aleatorios')
 plt.show()
 def graficaArea():
 #GRAFICA RELLENO DE AREA
 x1 = df["ri"]
 x1.plot.area()
 plt.show()
 #GRAFICA DE BARRAS
 def histograma():
 rS= df['ri']
 #rS
 plt.figure(figsize=(10,5))
 plt.hist(rS,bins=20,color='blue')
 plt.xlabel('# Aleatorios generados')
 plt.ylabel('Ocurrencias en rangos')
 plt.show()
 #GRAFICA DE DISPERSION
 def graficaDispercion():
 plt.scatter(df.index,df['ri'])
 plt.show()
 def limpiar():
 texP.delete('1.0', END)
 #VARIABLES------------------
 mCn = ""
 mCm = ""
 mCa = ""
 mCx0 = ""
 ent_cn = Label(metConMul, text="n:", width=5).grid(column=0, row=0)
 ent_cn = Entry(metConMul, width=10, textvariable=mCn)
 ent_cn.grid(column=1, row=0)
 ent_cm = Label(metConMul, text="m:", width=5).grid(column=2, row=0)
 ent_cm = Entry(metConMul, width=10, textvariable=mCm)
 ent_cm.grid(column=3, row=0)
 ent_ca = Label(metConMul, text="a:", width=5).grid(column=4, row=0)
 ent_ca = Entry(metConMul, width=10, textvariable=mCa)
 ent_ca.grid(column=5, row=0)
 ent_cx0 = Label(metConMul, text="x0:", width=5).grid(column=6, row=0)
 ent_cx0 = Entry(metConMul, width=10, textvariable=mCx0)
 ent_cx0.grid(column=7, row=0)
 #BOTON----------------------------------
 boton = Button(metConMul, text="Calcular", command=calcular, padx=1,
pady=1, bg='green', fg="white").grid(column=0, columnspan=2, row=1,
sticky=(W,E))
 boton = Button(metConMul, text="Gráfica # generados",
command=graficaNumerosGenerados, padx=1, pady=1, bg='dodgerblue',
fg="white").grid(column=2, row=1, sticky=(W,E))
 boton = Button(metConMul, text="Gráfica área", command=graficaArea,
padx=1, pady=1, bg='dodgerblue', fg="white").grid(column=3, row=1,
sticky=(W,E))
 boton = Button(metConMul, text="Histograma", command=histograma, padx=1,
pady=1, bg='dodgerblue', fg="white").grid(column=4, row=1, sticky=(W,E))
 boton = Button(metConMul, text="Gráfica disperción",
command=graficaDispercion, padx=1, pady=1, bg='dodgerblue',
fg="white").grid(column=5, row=1, sticky=(W,E))
 boton = Button(metConMul, text="Limpiar", command=limpiar, padx=1, pady=1,
bg='red').grid(column=6, columnspan=2, row=1, sticky=(W,E))
 #MOSTRAR-------------------------------
 texP=Text(metConMul, wrap="none")
 texP.grid(row=2, column=0, columnspan=8, sticky=(W,E))
 scrP=Scrollbar(metConMul, orient=VERTICAL, command=texP.yview)
 scrP.grid(row=2, column=8, sticky=(N,S))
 #scrh=Scrollbar(metCuaMe, orient=HORIZONTAL, command=texP.xview)
 #scrh.grid(row=2, column=8, columnspan=8, sticky=(W,E))
 texP.config(yscrollcommand=scrP.set)
 metConMul.mainloop()
 #GENERAR MATRIZ---------------------------------------------------------------
------------------
def generarMatriz():
 genMat=Tk()
 genMat.title('Generar matriz')
 genMat.resizable(False, False)
 def calcular():
 n1 = int(ent_nA1.get())
 n2 = int(ent_nA2.get())
 asd = np.random.rand(n1, n2)
 with pd.option_context('display.max_rows', None,
'display.max_columns', None, 'display.width', None):
 texP.insert('1.0', asd.round(3))
 def limpiar():
 texP.delete('1.0', END)
 #VARIABLES------------------
 ent_randint = ""
 ent_randint1 = ""
 ent_nA1 = Label(genMat, text="Fila(s):").grid(column=0, row=0)
 ent_nA1 = Entry(genMat, width=10, textvariable=ent_randint)
 ent_nA1.grid(column=1, row=0, sticky=(W,E))
 ent_nA2 = Label(genMat, text="Columana(s):").grid(column=2, row=0)
 ent_nA2 = Entry(genMat, width=10, textvariable=ent_randint1)
 ent_nA2.grid(column=3, row=0, sticky=(W,E))
 #BOTON----------------------------------
 boton = Button(genMat, text="Calcular", command=calcular, padx=1, pady=1,
bg='green', fg="white").grid(column=0, columnspan=3, row=1, sticky=(W,E))
 boton = Button(genMat, text="Limpiar", command=limpiar, padx=1, pady=1,
bg='red').grid(column=3, row=1, sticky=(W,E))
 #MOSTRAR-------------------------------
 texP=Text(genMat, height=15)
 texP.grid(row=2, column=0, columnspan=4, sticky=(W,E))
 scrP=Scrollbar(genMat, orient=VERTICAL, command=texP.yview)
 scrP.grid(row=2, column=4, sticky=(N,S))
 texP.config(yscrollcommand=scrP.set)

 genMat.mainloop()
#GENERAR NUMERO ALEATORIO RANDINT---------------------------------------------
------------------------------------
def generarNumeroRandint():
 genNumRan=Tk()
 genNumRan.title('Generar números aleatorios')
 genNumRan.resizable(False, False)
 def calcular():
 n = int(ent_randint.get())
 n1 = int(ent_randint1.get())
 numbers = list(np.random.randint(n+1, size=n1))
 print("numero", numbers)
 vector = []
 for i in range(len(numbers)):
 if numbers[i] == 0:
 a = numbers[i]+1
 vector.append(a)
 else:
 a = numbers[i]
 vector.append(a)
 texP.insert('1.0', vector)
 print("vector arreglado", vector)
 def limpiar():
 texP.delete('1.0', END)
 #VARIABLES------------------
 ent_randint = ""
 ent_randint1 = ""
 ent_randint = Label(genNumRan, text="1 y:").grid(column=0, row=0)
 ent_randint = Entry(genNumRan, width=10, textvariable=ent_randint)
 ent_randint.grid(column=1, row=0, sticky=(W,E))
 ent_randint1 = Label(genNumRan, text="mostrar:").grid(column=2, row=0)
 ent_randint1 = Entry(genNumRan, width=10, textvariable=ent_randint1)
 ent_randint1.grid(column=3, row=0, sticky=(W,E))
 #BOTON----------------------------------
 boton = Button(genNumRan, text="Calcular", command=calcular, padx=1,
pady=1, bg='green', fg="white").grid(column=0, columnspan=3, row=1,
sticky=(W,E))
 boton = Button(genNumRan, text="Limpiar", command=limpiar, padx=1, pady=1,
bg='red').grid(column=3, row=1, sticky=(W,E))
 #MOSTRAR-------------------------------
 texP=Text(genNumRan, width=40, height=10)
 texP.grid(row=2, column=0, columnspan=4, sticky=(W,E))
 scrP=Scrollbar(genNumRan, orient=VERTICAL, command=texP.yview)
 scrP.grid(row=2, column=4, sticky=(N,S))
 texP.config(yscrollcommand=scrP.set)

 genNumRan.mainloop()
#DISTRUBUCION NORMAL----------------------------------------------------------
-----------------------
def distribucionNormal():
 disNor=Tk()
 disNor.title('Distrubución Normal')
 disNor.resizable(False, False)
 def calcular():
 global dfl
 n = int(ent_nDisN.get())
 lista=np.random.randn(n)
 lista
 #lista.plot.area()
 dfl =pd.DataFrame({'X1':lista})
 #dfl.head()
 dfl
 with pd.option_context('display.max_rows', None,
'display.max_columns', None):
 texP.insert('1.0', dfl)
 def histograma():
 #x1.plot.hist()
 plt.figure(figsize=(10,5))
 plt.hist(dfl,bins=10,color='blue')
 plt.xlabel('# Aleatorios generados')
 plt.ylabel('Ocurrencias en rangos')
 plt.show()
 def limpiar():
 texP.delete('1.0', END)
 #VARIABLES------------------
 numDisN = ""
 ent_nDisN = Label(disNor, text="Cantidad:").grid(column=0, row=0)
 ent_nDisN = Entry(disNor, width=10, textvariable=numDisN)
 ent_nDisN.grid(column=1, row=0)
 #BOTON----------------------------------
 boton = Button(disNor, text="Calcular", command=calcular, padx=1, pady=1,
bg='green', fg="white").grid(column=0, columnspan=2, row=1, sticky=(W,E))
 boton = Button(disNor, text="Histograma", command=histograma, padx=1,
pady=1, bg='dodgerblue', fg="white").grid(column=2, row=1, sticky=(W,E))
 boton = Button(disNor, text="Limpiar", command=limpiar, padx=1, pady=1,
bg='red').grid(column=2, row=0, sticky=(W,E))
 #MOSTRAR-------------------------------
 texP=Text(disNor, wrap="none", width=40)
 texP.grid(row=2, column=0, columnspan=3, sticky=(W,E))
 scrP=Scrollbar(disNor, orient=VERTICAL, command=texP.yview)
 scrP.grid(row=2, column=3, sticky=(N,S))
 #scrh=Scrollbar(metCuaMe, orient=HORIZONTAL, command=texP.xview)
 #scrh.grid(row=2, column=8, columnspan=8, sticky=(W,E))
 texP.config(yscrollcommand=scrP.set)
 disNor.mainloop()
 chi2
#CHI 2------------------------------------------------------------------------
---------
def chi2():
 chi=Tk()
 chi.title('Chi cuadrado')
 chi.resizable(False, False)
 def calcular():
 matrix = np.random.rand(3, 6)
 matrix.sort()
 textDatos.insert('1.0', matrix)
 #Seleccion de filas de la matriz
 fila1=matrix[0]
 fila2=matrix[1]
 fila3=matrix[2]
 gradoLibertad=5
 # Establecer intervalos Fila 1
 bins = [0.00, 0.25, 0.50, 0.75, 0.99]
 counts, bin_edges = np.histogram(fila1, bins)
 M1 = []
 inter=[]
 # Calcular Frecuencias Fila 1
 #print(f"INTERVALO M1")
 for low, hight, count in zip(bin_edges, np.roll(bin_edges, -1),
counts):
 #print(f"{f'{low}-{hight}': <10} {count}")
 M1.append(count)
 inter.append(f'{low} - {hight}')
 # Calcular chi cuadrado Fila 1
 M1X1=(((M1[0]-5/4)**2)+((M1[1]-5/4)**2)+((M1[2]-5/4)**2)+((M1[3]-
5/4)**2))*4/5
 #print("Chi cuadrado del valor de la serie 3: " , M1X1)
 #Guardar dato de chi cuadrado
 intervalo1=M1X1
 #---------------------------------------------------------------------
-----------------
 counts, bin_edges = np.histogram(fila2, bins)
 M2 = []
 for low, hight, count in zip(bin_edges, np.roll(bin_edges, -1),
counts):
 M2.append(count)
 M2X1=(((M2[0]-5/4)**2)+((M2[1]-5/4)**2)+((M2[2]-5/4)**2)+((M2[3]-
5/4)**2))*4/5
 intervalo2=M2X1
 #---------------------------------------------------------------------
-----------------
 counts, bin_edges = np.histogram(fila3, bins)
 M3 = []
 for low, hight, count in zip(bin_edges, np.roll(bin_edges, -1),
counts):
 M3.append(count)
 M3X1=(((M3[0]-5/4)**2)+((M3[1]-5/4)**2)+((M3[2]-5/4)**2)+((M3[3]-
5/4)**2))*4/5
 intervalo3=M3X1
 df=pd.DataFrame({'Intervalos':inter,'m1':M1,'m2':M2,'m3':M3})
 df.loc[4]=['Chi',intervalo1,intervalo2,intervalo3]
 df
 texP.insert('1.0', df)
 def limpiar():
 textDatos.delete('1.0', END)
 texP.delete('1.0', END)
 #BOTON----------------------------------
 boton = Button(chi, text="Generar", command=calcular, padx=1, pady=1,
bg='green', fg="white").grid(column=0, columnspan=2, row=0, sticky=(W,E))
 boton = Button(chi, text="Limpiar", command=limpiar, padx=1, pady=1,
bg='red').grid(column=2, row=0, sticky=(W,E))
 #MOSTRAR-------------------------------
 Label(chi, text="DATOS GENERADOS F:3 x C:6:").grid(column=0, row=1,
columnspan=3, sticky=(W,E))
 textDatos=Text(chi, wrap="none", height=5)
 textDatos.grid(row=2, column=0, columnspan=3, sticky=(W,E))
 Label(chi, text="DATOS:").grid(column=0, row=3, columnspan=3,
sticky=(W,E))
 texP=Text(chi, wrap="none", height=10)
 texP.grid(row=4, column=0, columnspan=3, sticky=(W,E))
 chi.mainloop()
#DISTRIBUCION DE POISSON------------------------------------------------------
---------------------------
def distribucionPoisson():
 disPois=Tk()
 disPois.title('Distribución de Poisson')
 disPois.resizable(False, False)
 def calcular():
 global x, fmp
 landa = float(ent_poisson.get())
 poisson = stats.poisson(landa)
 x = np.arange(poisson.ppf(0.01), poisson.ppf(0.99))
 fmp = poisson.pmf(x)
 texP.insert('1.0', fmp)
 def graficaPoisson():
 plt.plot(x,fmp,'--')
 plt.vlines(x,0,fmp,colors='b',lw=5,alpha=0.5)
 plt.title('Distribución de Poisson')
 plt.ylabel('Probabilidad')
 plt.xlabel('Valores')
 plt.show()
 def limpiar():
 texP.delete('1.0', END)
 #VARIABLES------------------
 numPoisson = ""
 ent_poisson = Label(disPois, text="λ (lambda):").grid(column=0, row=0)
 ent_poisson = Entry(disPois, width=10, textvariable=numPoisson)
 ent_poisson.grid(column=1, row=0)
 #BOTON----------------------------------
 boton = Button(disPois, text="Calcular", command=calcular, padx=1, pady=1,
bg='green', fg="white").grid(column=0, columnspan=2, row=1, sticky=(W,E))
 boton = Button(disPois, text="Gráfica", command=graficaPoisson, padx=1,
pady=1, bg='dodgerblue', fg="white").grid(column=2, row=1, sticky=(W,E))
 boton = Button(disPois, text="Limpiar", command=limpiar, padx=1, pady=1,
bg='red').grid(column=2, row=0, sticky=(W,E))
 #MOSTRAR-------------------------------
 texP=Text(disPois, wrap="none")
 texP.grid(row=2, column=0, columnspan=3, sticky=(W,E))
 scrP=Scrollbar(disPois, orient=VERTICAL, command=texP.yview)
 scrP.grid(row=2, column=5, sticky=(N,S))
 #scrh=Scrollbar(metCuaMe, orient=HORIZONTAL, command=texP.xview)
 #scrh.grid(row=2, column=8, columnspan=8, sticky=(W,E))
 texP.config(yscrollcommand=scrP.set)
 disPois.mainloop()
#PROMEDIO MOVIL---------------------------------------------------------------
------------------
def promedioMovil():
 proMov=Tk()
 proMov.title('Promedio Móvil')
 proMov.resizable(False, False)
 def abrirArchivo():
 global archivo
 archivo =
filedialog.askopenfilename(initialdir='C:/Users/Admin/Desktop/MODELAMIENTO_SIMULACION', title='Seleccione archivo', filetype=(('Excel', '*.xlsx*'), ('Csv','*.csv*')))
 exporta = pd.read_excel(archivo)
 archivo = exporta
 datosOrig.insert('1.0', archivo)
 textCarga.config(text="¡Archivo cargado exitosamente!")

 def calcular():
 global a, varC, varP
 proyFinal = int(ent_pMovil.get())
 dataFrame = int(ent_pMovil1.get())
 exporta = archivo
 name = exporta.columns
 varC = name[0]
 varP = name[1]

 movil = pd.DataFrame(exporta)
 # mostramos los 5 primeros registros
 movil.head()
 # calculamos para la primera media móvil MMO_3
 for i in range(0,movil.shape[0]-2):
 movil.loc[movil.index[i+2],'MMO_3'] =
np.round(((movil.iloc[i,1]+movil.iloc[i+1,1]+movil.iloc[i+2,1])/3),1)
 # calculamos para la segunda media móvil MMO_4
 for i in range(0,movil.shape[0]-3):
 movil.loc[movil.index[i+3],'MMO_4'] =
np.round(((movil.iloc[i,1]+movil.iloc[i+1,1]+movil.iloc[i+2,1]+movil.iloc[i+3,
1])/4),1)
 # calculamos la proyeción final
 proyeccion = movil.iloc[ proyFinal :,[1,2,3]]
 p1,p2,p3 =proyeccion.mean()
 # incorporamos al DataFrame
 a = movil.append({ varC:dataFrame, varP:p1, 'MMO_3':p2,
'MMO_4':p3},ignore_index=True)
 # mostramos los resultados
 a['e_MM3'] = a[varP]-a['MMO_3']
 a['e_MM4'] = a[varP]-a['MMO_4']
 a
 texP.insert('1.0', a)
 #GRAFICA DE RESULTADOS
 def grafica():
 plt.figure(figsize=[8,8])
 plt.grid(True)
 plt.title('Gráfica promedio móvil')
 plt.plot(a[varP],label=varP,marker='o')
 plt.plot(a['MMO_3'],label='Media Móvil 3 años')
 plt.plot(a['MMO_4'],label='Media Móvil 4 años')
 plt.legend(loc=2)
 plt.show()
 def limpiar():
 texP.delete('1.0', END)
 datosOrig.delete('1.0', END)
 #VARIABLES------------------
 numPMov = ""
 numPMov1 = ""
 ent_pMovil = Label(proMov, text="proy:", width=5).grid(column=0, row=1)
 ent_pMovil = Entry(proMov, width=10, textvariable=numPMov)
 ent_pMovil.grid(column=1, row=1)
 ent_pMovil1 = Label(proMov, text="dataF:", width=5).grid(column=2, row=1)
 ent_pMovil1 = Entry(proMov, width=10, textvariable=numPMov1)
 ent_pMovil1.grid(column=3, row=1)
 #BOTON----------------------------------
 boton = Button(proMov, text="Cargar archivo", command=abrirArchivo,
padx=2, pady=2, bg='dodgerblue', fg="white").grid(column=0, columnspan=3,
row=0, sticky=(W,E))
 textCarga=Label(proMov, text="")
 textCarga.grid(column=3, columnspan=2, row=0, sticky=(W,E))
 boton = Button(proMov, text="Calcular", command=calcular, padx=1, pady=1,
bg='green', fg="white").grid(column=0, columnspan=4, row=2, sticky=(W,E))
 boton = Button(proMov, text="Gráfica", command=grafica, padx=1, pady=1,
bg='dodgerblue', fg="white").grid(column=4, row=2, sticky=(W,E))
 boton = Button(proMov, text="Limpiar", command=limpiar, padx=1, pady=1,
bg='red').grid(column=4, row=1, sticky=(W,E))
 #MOSTRAR-------------------------------
 Label(proMov, text="DATOS CARGADOS:").grid(column=0, row=3, columnspan=2,
sticky=(W,E))
 datosOrig=Text(proMov, width=30)
 datosOrig.grid(row=4, column=0, columnspan=2, sticky=(W,E))
 Label(proMov, text="DATOS PROMEDIO MOVIL:").grid(column=2, row=3,
columnspan=3, sticky=(W,E))
 texP=Text(proMov, wrap="none", width=70)
 texP.grid(row=4, column=2, columnspan=3, sticky=(W,E))
 scrP=Scrollbar(proMov, orient=VERTICAL, command=texP.yview)
 scrP.grid(row=4, column=5, sticky=(N,S))
 #scrh=Scrollbar(metCuaMe, orient=HORIZONTAL, command=texP.xview)
 #scrh.grid(row=2, column=8, columnspan=8, sticky=(W,E))
 texP.config(yscrollcommand=scrP.set)
 proMov.mainloop()
#SUAVIZACION EXPONENCIAL------------------------------------------------------
---------------------------
def suavizacionExponencial():
 suaExp=Tk()
 suaExp.title('Suavización Exponencial')
 suaExp.resizable(False, False)
 def abrirArchivo():
 global archivo
 archivo =
filedialog.askopenfilename(initialdir='C:/Users/Admin/Desktop/MODELAMIENTO_SIM
ULACION', title='Seleccione archivo', filetype=(('Excel', '*.xlsx*'), ('Csv',
'*.csv*')))
 exporta = pd.read_excel(archivo)
 archivo = exporta
 datosOrig.insert('1.0', archivo)
 textCarga.config(text="¡Archivo cargado exitosamente!")

 def calcular():
 numalfa = float(ent_sExp.get())
 dataFrame = int(ent_sExp1.get())
 exporta = archivo
 name = exporta.columns
 varC = name[0]
 varP = name[1]

 movil = pd.DataFrame(exporta)
 # mostramos los 5 primeros registros
 movil.head()
 alfa = numalfa
 unoalfa = 1 - alfa
 for i in range(0,movil.shape[0]-1):
 movil.loc[movil.index[i+1],'SN'] = np.round(movil.iloc[i,1],1)
 for i in range(2,movil.shape[0]):
 movil.loc[movil.index[i],'SN'] = np.round(movil.iloc[i1,1],1)*alfa + np.round(movil.iloc[i-1,2],1)*unoalfa
 i=i+1
 p1=0
 p2=np.round(movil.iloc[i-1,1],1)*alfa + np.round(movil.iloc[i1,2],1)*unoalfa
 a = movil.append({varC:dataFrame, varP:p1, 'SN':p2},ignore_index=True)
 a
 texP.insert('1.0', a)
 def limpiarTodo():
 texP.delete('1.0', END)
 datosOrig.delete('1.0', END)
 def limpiar():
 texP.delete('1.0', END)

 #VARIABLES------------------
 numSuExp = ""
 numSuExp1 = ""
 ent_sExp = Label(suaExp, text="α (alfa):", width=5).grid(column=0, row=1)
 ent_sExp = Entry(suaExp, width=10, textvariable=numSuExp)
 ent_sExp.grid(column=1, row=1)
 ent_sExp1 = Label(suaExp, text="dataF:", width=5).grid(column=2, row=1)
 ent_sExp1 = Entry(suaExp, width=10, textvariable=numSuExp1)
 ent_sExp1.grid(column=3, row=1)
 #BOTON----------------------------------
 boton = Button(suaExp, text="Cargar archivo", command=abrirArchivo,
padx=2, pady=2, bg='dodgerblue', fg="white").grid(column=0, columnspan=3,
row=0, sticky=(W,E))
 textCarga=Label(suaExp, text="")
 textCarga.grid(column=3, columnspan=2, row=0, sticky=(W,E))
 boton = Button(suaExp, text="Calcular", command=calcular, padx=1, pady=1,
bg='green', fg="white").grid(column=0, columnspan=4, row=2, sticky=(W,E))
 boton = Button(suaExp, text="Limpiar", command=limpiar, padx=1, pady=1,
bg='red', fg="white").grid(column=4, row=2, sticky=(W,E))
 boton = Button(suaExp, text="Limpiar todo", command=limpiarTodo, padx=1,
pady=1, bg='red').grid(column=4, row=1, sticky=(W,E))
 #MOSTRAR-------------------------------
 Label(suaExp, text="DATOS CARGADOS:").grid(column=0, row=3, columnspan=2,
sticky=(W,E))
datosOrig=Text(suaExp, width=30)
 datosOrig.grid(row=4, column=0, columnspan=2, sticky=(W,E))
 Label(suaExp, text="DATOS SUAVIZACION EXPONENCIAL:").grid(column=2, row=3,
columnspan=3, sticky=(W,E))
 texP=Text(suaExp, wrap="none", width=70)
 texP.grid(row=4, column=2, columnspan=3, sticky=(W,E))
 scrP=Scrollbar(suaExp, orient=VERTICAL, command=texP.yview)
 scrP.grid(row=4, column=5, sticky=(N,S))
 #scrh=Scrollbar(metCuaMe, orient=HORIZONTAL, command=texP.xview)
 #scrh.grid(row=2, column=8, columnspan=8, sticky=(W,E))
 texP.config(yscrollcommand=scrP.set)
 suaExp.mainloop()
#REGRESION LINEAL Y CUADRADA--------------------------------------------------
-------------------------------
def regresionLineaCuadrada():
 regLinCua=Tk()
 regLinCua.title('Regresión Lineal Y Cuadrada')
 regLinCua.resizable(False, False)
 def abrirArchivo():
 global archivo
 archivo =
filedialog.askopenfilename(initialdir='C:/Users/Admin/Desktop/MODELAMIENTO_SIM
ULACION', title='Seleccione archivo', filetype=(('Excel', '*.xlsx*'), ('Csv',
'*.csv*')))
 exporta = pd.read_excel(archivo)
 archivo = exporta
 datosOrig.insert('1.0', archivo)
 textCarga.config(text="¡Archivo cargado exitosamente!")

 def graficaLineal():
 global x, y, varC, varP, aA
 exporta = archivo
 name = exporta.columns
 varC = name[0]
 varP = name[1]
 a = pd.DataFrame(exporta)
 aA = a
 x = a.index.values
 y= a[varP]
 # ajuste de la recta (polinomio de grado 1 f(x) = ax + b)
 p = np.polyfit(x,y,1) # 1 para lineal, 2 para polinomio ...
 p0,p1 = p

 y_ajuste = p[0]*x + p[1]
 #print (y_ajuste)
 #tex1.insert('1.0', y_ajuste)
 # dibujamos los datos experimentales de la recta
 p_datos =plt.plot(x,y,'b.')
 # Dibujamos la recta de ajuste
 p_ajuste = plt.plot(x,y_ajuste, 'r-')
 plt.title('Ajuste lineal por mínimos cuadrados')
 plt.xlabel('Eje x')
 plt.ylabel('Eje y')
 plt.legend(('Datos experimentales','Ajuste lineal',), loc="upper
left")
plt.show()

 def graficaCuadrada():
 global p, yAjuste
 p = np.polyfit(x,y,2)
 p1,p2,p3 = p
 y_ajuste = p[0]*x*x + p[1]*x + p[2]
 yAjuste = y_ajuste
 # dibujamos los datos experimentales de la recta
 p_datos =plt.plot(x,y,'b.')
 # Dibujamos la curva de ajuste
 p_ajuste = plt.plot(x,y_ajuste, 'r-')
 plt.title('Ajuste Polinomial por mínimos cuadrados')
 plt.xlabel('Eje x')
 plt.ylabel('Eje y')
 plt.legend(('Datos experimentales','Ajuste Polinomial',), loc="upper
left")
 plt.show()
 #x

 def graficaPronostico():
 #n=x.size
 x1 = []
 x2 = []
 for i in [15,16,17]:
 y1_ajuste = p[0]*i*i + p[1]*i + p[2]
 #print (f" z = {i} w = {y1_ajuste}")
 x1.append(i)
 x2.append(y1_ajuste)

 y_ajuste = yAjuste
 a = aA
 a["y_ajuste"] = y_ajuste
 dp = pd.DataFrame({varC:["dato1","dato2","dato3"],
varP:[0,0,0],'y_ajuste':x2})
 dp
 a = a.append(dp,ignore_index=True)
 a
 texP.insert('1.0', a)
 x = a.index.values
 y_ajuste = a["y_ajuste"]
 y= a[varP]
 p_datos =plt.plot(y,'b.')
 p_ajuste = plt.plot(x,y_ajuste, 'r-')
 plt.title('Ajuste Polinomial por mínimos cuadrados')
 plt.xlabel('Eje x')
 plt.ylabel(varP)
 plt.axvspan(0,15,alpha=0.3,color='y') # encajonamos los datos
iniciales
 plt.legend(('Datos experimentales','Ajuste Polinomial',), loc="upper
left")
 plt.show()
 def limpiar():
 texP.delete('1.0', END)
 datosOrig.delete('1.0', END)
 #BOTON----------------------------------
 boton = Button(regLinCua, text="Cargar archivo", command=abrirArchivo,
padx=2, pady=2, bg='dodgerblue', fg="white").grid(column=0, columnspan=3,
row=0, sticky=(W,E))
 textCarga=Label(regLinCua, text="")
 textCarga.grid(column=3, columnspan=1, row=0, sticky=(W,E))
 boton = Button(regLinCua, text="Gráfico Líneal", command=graficaLineal,
padx=1, pady=1, bg='green', fg="white").grid(column=0, row=2, sticky=(W,E))
 boton = Button(regLinCua, text="Gráfico Cuadrada",
command=graficaCuadrada, padx=1, pady=1, bg='green',
fg="white").grid(column=1, row=2, sticky=(W,E))
 boton = Button(regLinCua, text="Gráfico Pronostico",
command=graficaPronostico, padx=1, pady=1, bg='green',
fg="white").grid(column=2, row=2, sticky=(W,E))
 boton = Button(regLinCua, text="Limpiar", command=limpiar, padx=1, pady=1,
bg='red').grid(column=3, row=2, sticky=(W,E))
 #MOSTRAR-------------------------------
 Label(regLinCua, text="DATOS CARGADOS:").grid(column=0, row=3,
columnspan=2, sticky=(W,E))
 datosOrig=Text(regLinCua, width=25)
 datosOrig.grid(row=4, column=0, columnspan=2, sticky=(W,E))
 Label(regLinCua, text="DATOS:").grid(column=2, row=3, columnspan=3,
sticky=(W,E))
 texP=Text(regLinCua, wrap="none", width=45)
 texP.grid(row=4, column=2, columnspan=2, sticky=(W,E))
 scrP=Scrollbar(regLinCua, orient=VERTICAL, command=texP.yview)
 scrP.grid(row=4, column=5, sticky=(N,S))
 scrh=Scrollbar(regLinCua, orient=HORIZONTAL, command=texP.xview)
 scrh.grid(row=5, column=2, columnspan=2, sticky=(W,E))
 texP.config(yscrollcommand=scrP.set, xscrollcommand=scrh.set)
 regLinCua.mainloop()
#SIMULACION MONTE CARLO-------------------------------------------------------
--------------------------
def simulacionMonteCarlo():
 simMonCar=Tk()
 simMonCar.title('Simulación Monte Carlo')
 simMonCar.resizable(False, False)
 def abrirArchivo():
 global archivo
 archivo =
filedialog.askopenfilename(initialdir='C:/Users/Admin/Desktop/MODELAMIENTO_SIM
ULACION', title='Seleccione archivo', filetype=(('Excel', '*.xlsx*'), ('Csv',
'*.csv*')))
 datos = pd.read_excel(archivo)
 archivo = datos
 datosOrig.insert('1.0', archivo)
 textCarga.config(text="¡Archivo cargado exitosamente!")

 def calcular():
 #numalfa = float(ent_sExp.get())
 nAlea = int(ent_mCa.get())
 datos = archivo

 name = datos.columns
 varC = name[0]
 varP = name[1]

 suma = datos[varP].sum()
 n=len(datos)
 suma
 x1 = datos.assign(Probabilidad=lambda x: x[varP] / suma)
 x2 = x1
 a=x2['Probabilidad']
 a1= np.cumsum(a) #Cálculo la suma acumulativa de las
probabilidades
 x2['FPA'] =a1
 x2['Min'] = x2['FPA']
 x2['Max'] = x2['FPA']
 lis = x2["Min"].values
 lis2 = x2['Max'].values
 lis[0]= 0
 for i in range(1,len(lis)):
 lis[i] = lis2[i-1]+0.001
 x2['Min'] = lis
 lis3 = x2["Max"].values
 for i in range(0,3): #3 minimo de datos
 lis3[i] = lis3[i]
 x2['Max'] = lis3
 with pd.option_context('display.max_rows', None,
'display.max_columns', None, 'display.width', None):
 texP.insert('1.0', x2)
 nDatos = ent_mCaDatos.get() #----------DATOS QUE INGRESA EL USUARIO--
-------
 if nDatos != "":
 contt = nDatos.split(',')
 for i in range(len(contt)):
 contt[i] = float(contt[i])
 contt
 nCant = len(contt)
 cantNumber = list(range(1, nCant+1))
 exporta = {'evento':cantNumber,
 'aleatorio':contt}
 exporta
 else:
 numAleatorio = np.random.rand(nAlea)
 cantNumber = list(range(1, nAlea+1))
 exporta = {'evento':cantNumber,
 'aleatorio':numAleatorio}
 exporta

 df = pd.DataFrame(data=exporta)
 #with pd.option_context('display.max_rows', None):
 #tex2.insert('1.0', df)
 vector = df["aleatorio"].values
 mini = x2["Min"].values
 maxi = x2["Max"].values
 cambioprecio = x2[varC].values
 accion = []
 err = 'false'
 acumulativa = 0
 for i in range(0,len(vector)):
 for j in range(0, len(mini)):
 err = 'false'
 if ( maxi[j] >= vector[i] >= mini[j]):
 accion.append(cambioprecio[j])
err = 'true'
break
 if(err == 'false'):
 accion.append(0)
 df['accion'] = accion
 acumulativa = sum(accion)
 #tex1.insert('1.0', acumulativa)
 with pd.option_context('display.max_rows', None):
 datos2.insert('1.0', df)
 def limpiar():
 texP.delete('1.0', END)
 datosOrig.delete('1.0', END)
 datos2.delete('1.0', END)
 #VARIABLES------------------
 numMonCa = ""
 numMonCaDatos = ""
 ent_mCa = Label(simMonCar, text="αleatorio:").grid(column=0, row=1)
 ent_mCa = Entry(simMonCar, width=10, textvariable=numMonCa)
 ent_mCa.grid(column=1, row=1)
 ent_mCaDatos = Label(simMonCar, text="Datos:", width=5).grid(column=2,
row=1)
 ent_mCaDatos = Entry(simMonCar, width=10, textvariable=numMonCaDatos)
 ent_mCaDatos.grid(column=3, row=1, columnspan=6, sticky=(W,E))
 #BOTON----------------------------------
 boton = Button(simMonCar, text="Cargar archivo", command=abrirArchivo,
padx=2, pady=2, bg='dodgerblue', fg="white").grid(column=0, columnspan=3,
row=0, sticky=(W,E))
 textCarga=Label(simMonCar, text="")
 textCarga.grid(column=3, columnspan=2, row=0, sticky=(W,E))
 boton = Button(simMonCar, text="Calcular", command=calcular, padx=1,
pady=1, bg='green', fg="white").grid(column=0, columnspan=6, row=2,
sticky=(W,E))
 boton = Button(simMonCar, text="Limpiar", command=limpiar, padx=1, pady=1,
bg='red').grid(column=7, row=2, sticky=(W,E), columnspan=2)
 #MOSTRAR-------------------------------
 Label(simMonCar, text="DATOS CARGADOS:").grid(column=0, row=3,
columnspan=2, sticky=(W,E))
 datosOrig=Text(simMonCar, width=30)
 datosOrig.grid(row=4, column=0, columnspan=2, sticky=(W,E))
 Label(simMonCar, text="DATOS SIMULACION MONTE CARLOS:").grid(column=2,
row=3, columnspan=4, sticky=(W,E))
 texP=Text(simMonCar, wrap="none", width=70)
 texP.grid(row=4, column=2, columnspan=4, sticky=(W,E))
 scrP=Scrollbar(simMonCar, orient=VERTICAL, command=texP.yview)
 scrP.grid(row=4, column=6, sticky=(N,S))
 scrh=Scrollbar(simMonCar, orient=HORIZONTAL, command=texP.xview)
 scrh.grid(row=5, column=2, columnspan=4, sticky=(W,E))
 texP.config(yscrollcommand=scrP.set, xscrollcommand=scrh.set)
 Label(simMonCar, text="¿DATOS?:").grid(column=7, row=3, columnspan=2,
sticky=(W,E))
 datos2=Text(simMonCar, width=30)
 datos2.grid(row=4, column=7, columnspan=2, sticky=(W,E))
 sdat2=Scrollbar(simMonCar, orient=VERTICAL, command=datos2.yview)
 sdat2.grid(row=4, column=9, sticky=(N,S))
 datos2.config(yscrollcommand=sdat2.set)
 simMonCar.mainloop()
#INVENTARIO-------------------------------------------------------------------
--------------
def inventario():
 inventa=Tk()
 inventa.title('Inventario')
 inventa.resizable(False, False)
 def calcular():
 global Q, dfQ
 D = float(ent_D.get())
 Co = float(ent_Co.get())
 Ch = float(ent_Ch.get())
 P = float(ent_P.get())
 Tespera = float(ent_Te.get())
 DiasAno = float(ent_Da.get())
 #D = 1400
 #Co = 25.00 #bien
 #Ch = 1
 #P = 2.50
 #Tespera = 3
 #DiasAno = 250
 Q = round(sqrt(((2*Co*D)/Ch)),2)
 N = round(D / Q,2)
 R = round((D / DiasAno) * Tespera,2)
 T = round(DiasAno / N,2)
 CoT = N * Co
 ChT = round(Q / 2 * Ch,2)
 MOQ = round(CoT + ChT,2)
 CTT = round(P * D + MOQ,2)
 datosOrig.insert('1.0', ('Cantidad Optima de Pedido(Q)', Q,"\n","Costo
total de Ordenar(CoT)", CoT,"\n", "Costo total de Mantener Inventario ChT =",
ChT,"\n",
 "Costo Total de Ordenar y Mantener Inventario
MO(O)", MOQ,"\n", "Costo Total del Sistema de Inventario CTT", CTT,"\n",
 "Número total de pedidos",N,"\n", "Punto de
reorden = R",R, "Tiempo de Pedido",T))

 indice =
['Q','Costo_ordenar','Costo_Mantenimiento','Costo_total','Diferencia_Costo_Tot
al']

 periodo = np.arange(1,19)
 def genera_lista(Q):
 n=18
 Q_Lista = []
 i=1
 Qi = Q
 Q_Lista.append(Qi)
 for i in range(1,9):
 Qi = Qi - 60
 Q_Lista.append(Qi)
 Qi = Q
 for i in range(9, n):
 Qi = Qi + 60
 Q_Lista.append(Qi)
 return Q_Lista
 Lista= genera_lista(Q)
 Lista.sort()
 dfQ = DataFrame(index=periodo, columns=indice).fillna(0)
 dfQ['Q'] = Lista

 for period in periodo:
 dfQ['Costo_ordenar'][period] = D * Co / dfQ['Q'][period]
 dfQ['Costo_Mantenimiento'][period] = dfQ['Q'][period] * Ch / 2
 dfQ['Costo_total'][period] = dfQ['Costo_ordenar'][period] +
dfQ['Costo_Mantenimiento'][period]
 dfQ['Diferencia_Costo_Total'][period] = dfQ['Costo_total'][period]
- MOQ
 dfQ
 with pd.option_context('display.max_rows', None,
'display.max_columns', None, 'display.width', None):
 texP.insert('1.0', dfQ)
#*****************************************************************************
******************************************************************************
**********
 def make_data(product, policy, periods):
 """ Returns dataframe with the details of the inventory
simulation.
 Keyword arguments:
 product -- Product object
 policy -- dict that contains the policy name and parameters. For
example:
 policy = {'method': "Qs",
 'param1': 20000,
 'param2': 10000
 }
 periods -- numbers of periods of the simulation
 """
 periods += 1
 # Create zero-filled Dataframe
 period_lst = np.arange(periods) # index
 # Abbreviations
 # INV_INICIAL: INV_NETO_INICIALtial inventory position
 # INV_NETO_INICIAL: INV_NETO_INICIALtial net inventory
 # D: Demand
 # INV_FINAL: Final inventory position
 # INV_FINAL_NETO: Final net inventory
 # LS: Lost sales
 # AVG: Average inventory
 # ORD: order quantity
 # LT: lead time
 header = ['INV_INICIAL','INV_NETO_INICIAL','DEMANDA', 'INV_FINAL',
 'INV_FINAL_NETO', 'VENTAS_PERDIDAS', 'INV_PROMEDIO',
'CANT_ORDENAR', 'TIEMPO_LLEGADA']
 df = DataFrame(index=period_lst, columns=header).fillna(0)
 # Create a list that will store each period order
 order_l = [Order(quantity=0, lead_time=0)
 for x in range(periods)]

 # Fill DataFrame
 for period in period_lst:
 if period == 0:
 df['INV_INICIAL'][period] = product.initial_inventory
df['INV_NETO_INICIAL'][period] = product.initial_inventory
df['INV_FINAL'][period] = product.initial_inventory
df['INV_FINAL_NETO'][period] = product.initial_inventory
 if period >= 1:
 df['INV_INICIAL'][period] = df['INV_FINAL'][period - 1] +
order_l[period - 1].quantity
 df['INV_NETO_INICIAL'][period] =
df['INV_FINAL_NETO'][period - 1] + pending_order(order_l, period)
 #demand = int(product.demand())
demand = 20
# We can't have negative demand
if demand > 0:
 df['DEMANDA'][period] = demand
 else:
 df['DEMANDA'][period] = 0
 if df['INV_INICIAL'][period] - df['DEMANDA'][period] < 0:
 df['INV_FINAL'][period] = 0
 else:
 df['INV_FINAL'][period] = df['INV_INICIAL'][period] -
df['DEMANDA'][period]

 order_l[period].quantity, order_l[period].lead_time =
placeorder(product, df['INV_FINAL'][period], policy, period)
 df['INV_FINAL_NETO'][period] =
df['INV_NETO_INICIAL'][period] - df['DEMANDA'][period] #Line 58
 if df['INV_FINAL_NETO'][period] < 0:
 df['VENTAS_PERDIDAS'][period] =
abs(df['INV_FINAL_NETO'][period])
 df['INV_FINAL_NETO'][period] = 0
 else:
 df['VENTAS_PERDIDAS'][period] = 0
 df['INV_PROMEDIO'][period] =
(df['INV_NETO_INICIAL'][period] + df['INV_FINAL_NETO'][period]) / 2.0
 df['CANT_ORDENAR'][period] = order_l[period].quantity
df['TIEMPO_LLEGADA'][period] = order_l[period].lead_time
 return df

 def pending_order(order_l, period):
 """Return the order that arrives in actual period"""
 indices = [i for i, order in enumerate(order_l) if order.quantity]
 sum = 0
 for i in indices:
 if period - (i + order_l[i].lead_time + 1) == 0:
 sum += order_l[i].quantity
 return sum
def demand(self):
 if self.demand_dist == "Constant":
 return self.demand_p1
 elif self.demand_dist == "Normal":
 return make_distribution(
 np.random.normal,
self.demand_p1,
self.demand_p2)()
 elif self.demand_dist == "Triangular":
 return make_distribution(
 np.random_triangular,
 self.demand_p1,
self.demand_p2,
self.demand_p3
)()

 def lead_time(self):
 if self.leadtime_dist == "Constant":
 return self.leadtime_p1
 elif self.leadtime_dist == "Normal":
 return make_distribution(
 np.random.normal,
self.leadtime_p1,
self.leadtime_p2)()
 if self.leadtime_dist == "Triangular":
 return make_distribution(
 np.random.triangular,
 self.leadtime_p1,
 self.leadtime_p2,
self.leadtime_p3
)()

 def __repr__(self):
 return '<Product %r>' % self.name

 def placeorder(product, final_inv_pos, policy, period):
 """Place the order according the inventory policy:
 Keywords arguments:
 product -- object Product
 final_inv_pos -- final inventory position of period
 policy -- chosen policy Qs or RS
 period -- actual period
 Return:
 quantity to order
 lead time
 """
 #lead_time = int(product.lead_time())
 lead_time = 3
 # Qs = if we hit the reorder point s, order Q units
 if policy['method'] == 'Qs' and \
 final_inv_pos <= policy['param2']:
 return policy['param1'], lead_time
 # RS = if we hit the review period R and the reorder point S,
order: (S -
 # final inventory pos)
 elif policy['method'] == 'RS' and \
 period % policy['param1'] == 0 and \
 final_inv_pos <= policy['param2']:
 return policy['param2'] - final_inv_pos, lead_time
 else:
 return 0, 0

 politica = {'method': "Qs", 'param1': 50, 'param2': 20 }

 class Order(object):
 """Object that stores basic data of an order"""
 def __init__(self, quantity, lead_time):
 self.quantity = quantity
 self.lead_time = lead_time
 class product(object):

 def __init__
(self,name,price,order_cost,initial_inventory,demand_dist,demand_p1,

demand_p2,demand_p3,leadtime_dist,leadtime_p1,leadtime_p2,leadtime_p3):
 self.name=name
 self.price=price
 self.order_cost=order_cost
 self.initial_inventory=initial_inventory
 self.demand_dist=demand_dist
 self.demand_p1=demand_p1
 self.demand_p2=demand_p2
 self.demand_p3=demand_p3
 self.leadtime_dist=leadtime_dist
 self.leadtime_p1=leadtime_p1
 self.leadtime_p2=leadtime_p2
 self.leadtime_p3=leadtime_p3
 producto = product("Mesa",
18.0,20.0,100,"Constant",80.0,0.0,0.0,"Constant",1.0,0.0,0.0)
 df = make_data(producto, politica, 18)
 with pd.option_context('display.max_rows', None,
'display.max_columns', None, 'display.width', None):
 datos2.insert('1.0', df)
#*****************************************************************************
******************************************************************************
**********
 def grafico():
 dfG = dfQ.loc[:,'Costo_ordenar':'Costo_total']
 dfG
 dfG.plot()
 plt.show()
 def limpiar():
 texP.delete('1.0', END)
 datosOrig.delete('1.0', END)
 datos2.delete('1.0', END)
 #VARIABLES------------------
 numD = "1400"
 numCo = "25"
 numCh = "1"
 numP = "2.50"
 numTE = "3"
 numDA = "250"
 ent_D = Label(inventa, text="d:").grid(column=0, row=0)
 ent_D = Entry(inventa, width=10, textvariable=numD)
 ent_D.grid(column=1, row=0)
 ent_Co = Label(inventa, text="Co").grid(column=2, row=0)
 ent_Co = Entry(inventa, width=10, textvariable=numCo)
 ent_Co.grid(column=3, row=0)
 ent_Ch = Label(inventa, text="Ch:").grid(column=4, row=0)
 ent_Ch = Entry(inventa, width=10, textvariable=numCh)
 ent_Ch.grid(column=5, row=0)
 ent_P = Label(inventa, text="P:").grid(column=6, row=0)
 ent_P = Entry(inventa, width=10, textvariable=numP)
 ent_P.grid(column=7, row=0)
 ent_Te = Label(inventa, text="T. espera").grid(column=8, row=0)
 ent_Te = Entry(inventa, width=10, textvariable=numTE)
 ent_Te.grid(column=9, row=0)
 ent_Da = Label(inventa, text="Dias Año:").grid(column=10, row=0)
 ent_Da = Entry(inventa, width=10, textvariable=numDA)
 ent_Da.grid(column=11, row=0)
 #BOTON----------------------------------
 boton = Button(inventa, text="Calcular", command=calcular, padx=1, pady=1,
bg='green', fg="white").grid(column=0, columnspan=4, row=3, sticky=(W,E))
 boton = Button(inventa, text="Gráfico", command=grafico, padx=1, pady=1,
bg='dodgerblue', fg="white").grid(column=7, columnspan=2, row=3, sticky=(W,E))
 boton = Button(inventa, text="Limpiar", command=limpiar, padx=1, pady=1,
bg='red').grid(column=10, columnspan=2, row=3, sticky=(W,E))
 #MOSTRAR-------------------------------
 Label(inventa, text="DATOS:").grid(column=0, row=4, columnspan=2,
sticky=(W,E))
 datosOrig=Text(inventa, width=20, height=16)
 datosOrig.grid(row=5, column=0, columnspan=2, sticky=(W,E))
 Label(inventa, text="DATOS PERIODO:").grid(column=2, row=4, columnspan=10,
sticky=(W,E))
 texP=Text(inventa, wrap="none", width=100, height=16)
 texP.grid(row=5, column=2, columnspan=10, sticky=(W,E))
 scrP=Scrollbar(inventa, orient=VERTICAL, command=texP.yview)
 scrP.grid(row=5, column=12, sticky=(N,S))
 scrh=Scrollbar(inventa, orient=HORIZONTAL, command=texP.xview)
 scrh.grid(row=6, column=2, columnspan=10, sticky=(W,E))
 texP.config(yscrollcommand=scrP.set, xscrollcommand=scrh.set)

 Label(inventa, text="RESUMEN:").grid(column=2, row=7, columnspan=10,
sticky=(W,E))
 datos2=Text(inventa, wrap="none", width=30, height=16)
 datos2.grid(row=8, column=2, columnspan=10, sticky=(W,E))
 sdat2=Scrollbar(inventa, orient=VERTICAL, command=datos2.yview)
 sdat2.grid(row=8, column=12, sticky=(N,S))
 scrh2=Scrollbar(inventa, orient=HORIZONTAL, command=datos2.xview)
 scrh2.grid(row=9, column=2, columnspan=10, sticky=(W,E))
 datos2.config(yscrollcommand=sdat2.set, xscrollcommand=scrh2.set)
 inventa.mainloop()
#LINEA TIEMPO DE ESPERA-------------------------------------------------------
--------------------------
def lineaTiempoEspera():
linTiEsp=Tk()
 linTiEsp.title('Línea Tiempo De Espera')
 linTiEsp.resizable(False, False)
 def abrirArchivo():
 global archivo
 archivo =
filedialog.askopenfilename(initialdir='C:/Users/Admin/Desktop/MODELAMIENTO_SIM
ULACION', title='Seleccione archivo', filetype=(('Excel', '*.xlsx*'), ('Csv',
'*.csv*')))
 datos = pd.read_excel(archivo)
 archivo = datos
 datosOrig.insert('1.0', archivo)
 textCarga.config(text="¡Archivo cargado exitosamente!")

 def calcular():
 varLanda = float(ent_ltimeLanda.get())
 varNiu = float(ent_ltimeNiu.get())

 landa = varLanda
 #1.3333 - 10
 nu = varNiu
 #4.0 - 12
 #La probabilidad de hallar el sistema ocupado o utilización del
sistema:
 p=landa/nu
 #L#a probabilidad de que no haya unidades en el sistema este vacía
u ocioso :
 Po = 1.0 - (landa/nu)
 #Longitud esperada en cola, promedio de unidades en la línea de
espera:
 Lq = landa*landa / (nu * (nu - landa))
 #/ (nu * (nu - landa))
 # Número esperado de clientes en el sistema(cola y servicio) :
 L = landa /(nu - landa)
 #El tiempo promedio que una unidad pasa en el sistema:
 W = 1 / (nu - landa)
 #Tiempo de espera en cola:
 Wq = W - (1.0 / nu)
 #La probabilidad de que haya n unidades en el sistema:
 n = 1
 Pn = (landa/nu)*n*Po
 global dfLE

 datosOrig.insert('1.0', ("Pn: ", round(Pn,3)))
 datosOrig.insert('1.0', ("Wq: ", round(Wq,3), "\n"))
 datosOrig.insert('1.0', ("W: " , round(W,3), "\n"))
 datosOrig.insert('1.0', ("L: ", round(L,1), "\n"))
 datosOrig.insert('1.0', ( "Lq: ", round(Lq,3), "\n"))
 datosOrig.insert('1.0', ( "Po: ", round(Po,3), "\n"))
 datosOrig.insert('1.0', ("Nu: ", nu, "\n"))
 datosOrig.insert('1.0', ("Landa: ", round(landa,3), "\n"))
 datosOrig.insert('1.0', (Wq, "\n"))
 numsAle1 = ent_ltimeOne.get()
 numsAle2 = ent_ltimeTwo.get()

 nDatos = ent_ltimeCant.get()
 if numsAle1 != "" or numsAle2 != "":
 contt = numsAle1.split(',')
 contt2 = numsAle2.split(',')

 for i in range(len(contt)):
 contt[i] = float(contt[i])
 contt
 for j in range(len(contt2)):
 contt2[j] = float(contt2[j])
 contt2

 nCant = len(contt)
 numClientes = nCant
 randomNumbersOne = contt
 randomNumbersTwo = contt2
 else:
 varTimeCant = int(ent_ltimeCant.get())
 numClientes = varTimeCant
 randomNumbersOne = list(np.random.rand(numClientes))
 randomNumbersTwo = list(np.random.rand(numClientes))

 i = 0
 #ent_ltimeOne
 #variablesRamdom = random.random()
 indice =
['ALL','ASE','TILL','TISE','TIRLL','TIISE','TIFSE','TIESP','TIESA']
 Clientes = np.arange(numClientes)
 dfLE = pd.DataFrame(index=Clientes, columns=indice).fillna(0.000)
 np.random.seed(100)
 for i in Clientes:
 if i == 0:
 dfLE['ALL'] = randomNumbersOne
 dfLE['ASE'] = randomNumbersTwo
 dfLE['TILL'][i] = -1/landa*np.log(dfLE['ALL'][i])
 dfLE['TISE'][i] = -1/nu*np.log(dfLE['ASE'][i])
 dfLE['TIRLL'][i] = dfLE['TILL'][i]
 dfLE['TIISE'][i] = dfLE['TIRLL'][i]
 dfLE['TIFSE'][i] = dfLE['TIISE'][i] + dfLE['TISE'][i]
 dfLE['TIESA'][i] = dfLE['TIESP'][i] + dfLE['TISE'][i]
 else:
 dfLE['ALL'] = randomNumbersOne
 dfLE['ASE'] = randomNumbersTwo
 dfLE['TILL'][i] = -1/landa*np.log(dfLE['ALL'][i])
 dfLE['TISE'][i] = -1/nu*np.log(dfLE['ASE'][i])
 dfLE['TIRLL'][i] = dfLE['TILL'][i] + dfLE['TIRLL'][i-1]
 dfLE['TIISE'][i] = max(dfLE['TIRLL'][i],dfLE['TIFSE'][i-1])
 dfLE['TIFSE'][i] = dfLE['TIISE'][i] + dfLE['TISE'][i]
 dfLE['TIESP'][i] = dfLE['TIISE'][i] - dfLE['TIRLL'][i]
 dfLE['TIESA'][i] = dfLE['TIESP'][i] + dfLE['TISE'][i]
 nuevas_columnas =
pd.core.indexes.base.Index(["A_LLEGA","A_SERV","T_LLEGA","T_SERV",

"T_EXACT_LLEGA","T_INI_SERV", "T_FIN_SERV","T_ESPERA",
 "T_EN_SISTE"])
 dfLE.columns = nuevas_columnas
 dfLE = dfLE.round(3)
 dfLE
 with pd.option_context('display.max_rows', None,
'display.max_columns', None, 'display.width', None):
 texP.insert('1.0', dfLE)

 zxc = dfLE.describe()
 most = zxc.round(3)
 with pd.option_context('display.max_rows', None,
'display.max_columns', None, 'display.width', None):
 datos2.insert('1.0', most)
 def grafico():
 dFlee = dfLE
 dFlee
 dFlee.plot()
 plt.show()
 def limpiar():
 texP.delete('1.0', END)
 datosOrig.delete('1.0', END)
 datos2.delete('1.0', END)
 #VARIABLES------------------
 numEsperaLanda = ""
 numEsperaNiu = ""
 numTimeCant = ""
 ent_ltimeLanda = Label(linTiEsp, text="λ (lambda):").grid(column=0, row=1)
 ent_ltimeLanda = Entry(linTiEsp, width=10, textvariable=numEsperaLanda)
 ent_ltimeLanda.grid(column=1, row=1)
 ent_ltimeNiu = Label(linTiEsp, text="μ (mi):").grid(column=2, row=1)
 ent_ltimeNiu = Entry(linTiEsp, width=10, textvariable=numEsperaNiu)
 ent_ltimeNiu.grid(column=3, row=1)
 ent_ltimeCant = Label(linTiEsp, text="Cantidad:").grid(column=4, row=1)
 ent_ltimeCant = Entry(linTiEsp, width=10, textvariable=numTimeCant)
 ent_ltimeCant.grid(column=5, row=1)
 #datosIngresar------
 numTimeOne=""
 numTimeTwo=""
 ent_ltimeOne = Label(linTiEsp, text="Dat1:").grid(column=0, row=2)
 ent_ltimeOne = Entry(linTiEsp, textvariable=numTimeOne, width=45)
 ent_ltimeOne.grid(column=1, row=2, columnspan=3, sticky=(W,E))
 ent_ltimeTwo = Label(linTiEsp, text="Dat2:").grid(column=4, row=2)
 ent_ltimeTwo = Entry(linTiEsp, textvariable=numTimeTwo, width=45)
 ent_ltimeTwo.grid(column=5, row=2, columnspan=3, sticky=(W,E))
 #BOTON----------------------------------
 #boton = Button(linTiEsp, text="Cargar archivo", command=abrirArchivo,
padx=2, pady=2, bg='dodgerblue', fg="white").grid(column=0, columnspan=3,
row=0, sticky=(W,E))
 textCarga=Label(linTiEsp, text="")
 textCarga.grid(column=3, columnspan=2, row=0, sticky=(W,E))
 boton = Button(linTiEsp, text="Calcular", command=calcular, padx=1,
pady=1, bg='green', fg="white").grid(column=0, columnspan=4, row=3,
sticky=(W,E))
 boton = Button(linTiEsp, text="Gráfico", command=grafico, padx=1, pady=1,
bg='dodgerblue', fg="white").grid(column=4, columnspan=2, row=3, sticky=(W,E))
 boton = Button(linTiEsp, text="Limpiar", command=limpiar, padx=1, pady=1,
bg='red').grid(column=6, row=3, sticky=(W,E), columnspan=2)
 #MOSTRAR-------------------------------
 Label(linTiEsp, text="DATOS:").grid(column=0, row=4, columnspan=2,
sticky=(W,E))
 datosOrig=Text(linTiEsp, width=20, height=16)
 datosOrig.grid(row=5, column=0, columnspan=2, sticky=(W,E))
 Label(linTiEsp, text="DATOS LINEA TIEMPO ESPERA:").grid(column=2, row=4,
columnspan=7, sticky=(W,E))
 texP=Text(linTiEsp, wrap="none", width=100, height=16)
 texP.grid(row=5, column=2, columnspan=6, sticky=(W,E))
 scrP=Scrollbar(linTiEsp, orient=VERTICAL, command=texP.yview)
 scrP.grid(row=5, column=9, sticky=(N,S))
 scrh=Scrollbar(linTiEsp, orient=HORIZONTAL, command=texP.xview)
 scrh.grid(row=6, column=2, columnspan=6, sticky=(W,E))
 texP.config(yscrollcommand=scrP.set, xscrollcommand=scrh.set)

 Label(linTiEsp, text="RESUMEN DE LINEA TIEMPO ESPERA:").grid(column=2,
row=7, columnspan=7, sticky=(W,E))
 datos2=Text(linTiEsp, wrap="none", width=30, height=10)
 datos2.grid(row=8, column=2, columnspan=6, sticky=(W,E))
 sdat2=Scrollbar(linTiEsp, orient=VERTICAL, command=datos2.yview)
 sdat2.grid(row=8, column=9, sticky=(N,S))
 scrh2=Scrollbar(linTiEsp, orient=HORIZONTAL, command=datos2.xview)
 scrh2.grid(row=9, column=2, columnspan=6, sticky=(W,E))
 datos2.config(yscrollcommand=sdat2.set, xscrollcommand=scrh2.set)
 linTiEsp.mainloop()
#SALIR------------------------------------------------------------------------
--------------------------
def salir():
 exit = messagebox.askquestion("SALIR", "¿Deseas salir?")
 #exit = messagebox.askokcancel("SALIR", "¿Deseas salir?")
 if exit=="yes":
 raiz.destroy()
#-----------------------------------------------------------------------------
--------------------------
barraMenu=Menu(raiz)
raiz.config(menu=barraMenu, width=300, height=300)
unidad2=Menu(barraMenu, tearoff=0)
unidad2.add_command(label="Estadística", command=estadistica)
unidad3=Menu(barraMenu, tearoff=0)
unidad3.add_command(label="Metodo cuadrado medio",
command=metodoCuadradoMedio)
unidad3.add_command(label="Métodos congruención lineales",
command=metodoCongruencialLinea)
unidad3.add_command(label="Congruenciales multiplicativo",
command=metodoCongruencialMultiplicativo)
unidad3.add_separator()
unidad3.add_command(label="Generador matriz", command=generarMatriz)
unidad3.add_command(label="Generador de números aleatorios",
command=generarNumeroRandint)
unidad3.add_command(label="Número aleatorio con distribución normal",
command=distribucionNormal)
unidad3.add_separator()
unidad3.add_command(label="Chi2", command=chi2)
unidad3.add_command(label="Distribución de Poisson",
command=distribucionPoisson)
unidad4=Menu(barraMenu, tearoff=0)
unidad4.add_command(label="Promedio Móvil", command=promedioMovil)
unidad4.add_separator()
unidad4.add_command(label="Suavización exponencial",
command=suavizacionExponencial)
unidad4.add_separator()
unidad4.add_command(label="Regresión Lineal y Cuadrada",
command=regresionLineaCuadrada)
unidad4.add_separator()
unidad4.add_command(label="Simulación Monte Carlo",
command=simulacionMonteCarlo)
unidad5=Menu(barraMenu, tearoff=0)
unidad5.add_command(label="Inventario", command=inventario)
unidad5.add_command(label="Línea Tiempo de Espera", command=lineaTiempoEspera)
opciones=Menu(barraMenu, tearoff=0)
opciones.add_command(label="Salir", command=salir)
barraMenu.add_cascade(label="Capitulo 2", menu=unidad2)
barraMenu.add_cascade(label="Capitulo 3", menu=unidad3)
barraMenu.add_cascade(label="Capitulo 4", menu=unidad4)
barraMenu.add_cascade(label="Capitulo 5", menu=unidad5)
barraMenu.add_cascade(label="Opciones", menu=opciones)
raiz.mainloop()