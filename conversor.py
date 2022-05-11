#importamos las librerias necesarias
import tkinter #tkinter para crear la interfaz grafica
import requests #requests para que funcione la API
from tkinter import *
from tkinter import messagebox 

#caracteristicas de nuestra interfaz
interfaz = Tk()
interfaz.title("conversor de euros a bitcoin")
interfaz.geometry("600x500+300+100")
interfaz.iconbitmap("bitcoins.ico")
interfaz.resizable(0,0)
interfaz.config(bg="black")
img = tkinter.PhotoImage(file="fondo.png")
lbl_img = tkinter.Label(interfaz, image = img)

#funcion para realizar nuestra operacion y mostarnos el resultado en la pantalla de la interfaz
def conv_bitcoin():
    conv_bitcoin = cantidad_euros.get() / float(cantidad_bitcoin)
    messagebox.showinfo(title="conversor de euros a bitcoin ", message=str( cantidad_euros.get())+" euros equivale a "+ (str("{:.8f}".format(conv_bitcoin)+ " XBT")))
   
#funcion para adquirir el valor del bitcoin en tiempo real a travez de una API
def valor_bitcoin():
    url = requests.get("https://www.bitstamp.net/api/v2/ticker/btceur")
    response = url.json()
    return str("{:.2f}".format(float(response["last"])))

#titulo de la interfaz
ventana_titulo = Label(text="€ CONVERSOR DE EUROS A BITCOIN €",fg='gold',bg='black', font = ("Courier",18)).pack()

#nuestras variables y su representacion para que se vean en la interfaz
ventana_pbitcoin  = Label(text= " Valor actual del bitcoin en euros: ",fg='gold',bg='black',font = ("Courier",15)).place(x=10,y=48)
cantidad_bitcoin = valor_bitcoin()
txt_Ingrese = Label(interfaz,text = cantidad_bitcoin,fg='gold',bg='black',font=(80)).place(x=450,y=50)
                                                                    
ventana_euros  = Label(text= "ingrese la cantidad de euros a convertir: ",fg='gold',bg='black',font = ("Courier",13)).place(x=10,y=90)
cantidad_euros = DoubleVar()
txt_Ingrese = Entry(interfaz,textvariable = cantidad_euros,fg='gold',bg='black',font=(10)).place(x=440,y=90)

boton_Resultado = Button(interfaz, text="Convertir",command=conv_bitcoin,fg='gold',bg='black',font=("Courier",14)).place(x=10,y=150)

lbl_img.pack()#metodo para nuestra imagen de fondo de la interfaz
interfaz.mainloop()#metodo para que  la interfaz quede abierta

#añadimos el resultado de nuestro programa a un archivo txt
conv_bitcoin = cantidad_euros.get() / float(valor_bitcoin())
result_bitcoin = (str( cantidad_euros.get())+" euros equivale a "+ (str("{:.8f}".format(conv_bitcoin)+ " XBT")))
reg_proyect = open("datos.txt","a")
print(result_bitcoin)
datos_proyect = result_bitcoin +"\n"
reg_proyect.write((datos_proyect))
reg_proyect.close()