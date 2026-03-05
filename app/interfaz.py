import tkinter as tk
from app.logica import *

def iniciar_app():
    # Crea ventana principal
    ventana = tk.Tk()

    # Titulo de la ventana
    ventana.title("Calculadora")

    # Tamaño de la vetana
    ventana.geometry("400x600")

    # Icono de la ventana
    ventana.iconbitmap("assets/calculadora.ico")

    # Configuracion del grid de la ventana
    for n in range(4):
        ventana.grid_columnconfigure(n, weight = 1)
    
    for n in range(6):
        ventana.grid_rowconfigure(n, weight = 1)
    
    # Variable de expresion del visor
    expresion = tk.StringVar()

    # Operaciones permitidas
    lista_operaciones = ["/","*","+","-"]
    lista_expresion = [""]

    def agrega_valor(valor):
        lista_expresion[-1] += valor
        expresion.set("".join(lista_expresion))

    def boton_presionado(valor):
        # Si se presiona un digito 
        if valor.isdigit():
            if lista_expresion[-1] in lista_operaciones:
                lista_expresion.append("")
            agrega_valor(valor)

        # Si se presiona un punto
        if valor == ".":
            if lista_expresion[-1] not in lista_operaciones and "." not in lista_expresion[-1]:
                agrega_valor(valor)

        # Si se presiona una operacion
        if valor in lista_operaciones and lista_expresion[-1] != "":
            if lista_expresion[-1][-1].isdigit():
                lista_expresion.append("")
                agrega_valor(valor)

        # Si se presiona la tecla de borrado
        if valor == "C":
            lista_expresion.clear()
            lista_expresion.append("")
            expresion.set("")

        # Si se presiona la tecla =
        if valor == "=":
            expresion.set("".join(resolver_expresion(lista_expresion)))
            lista_expresion.clear()
            lista_expresion.append("")

    def resolver_expresion(lista_expresion):
        for num in lista_expresion:
            if num not in lista_operaciones:
                lista_expresion[lista_expresion.index(num)] = float(num)
    
        while len(lista_expresion) > 1:
            for elemento in lista_expresion:
                if elemento == "*":
                    indice = lista_expresion.index(elemento)
                    lista_expresion[indice] = lista_expresion[indice - 1] * lista_expresion[indice + 1]
                    lista_expresion.pop(indice + 1)
                    lista_expresion.pop(indice - 1)
                elif elemento == "/":
                    indice = lista_expresion.index(elemento)
                    lista_expresion[indice] = lista_expresion[indice - 1] / lista_expresion[indice + 1]
                    lista_expresion.pop(indice + 1)
                    lista_expresion.pop(indice - 1)
                elif elemento == "+":
                    indice = lista_expresion.index(elemento)
                    lista_expresion[indice] = lista_expresion[indice - 1] + lista_expresion[indice + 1]
                    lista_expresion.pop(indice + 1)
                    lista_expresion.pop(indice - 1)
                elif elemento == "-":
                    indice = lista_expresion.index(elemento)
                    lista_expresion[indice] = lista_expresion[indice - 1] - lista_expresion[indice + 1]
                    lista_expresion.pop(indice + 1)
                    lista_expresion.pop(indice - 1)
        
        if lista_expresion[0].is_integer():
            return str(int(lista_expresion[0]))
        else:
            return str(lista_expresion[0])

    # Colores de los botones
    color1 = "lightblue"
    color2 = "purple"
    color3 = "blue"
    color4 = "lightgreen"
    fuente = ("Helvetica", 24)

    # Lista de valores de los botones
    lista_botones = [("7",0,1,color1),("8",1,1,color1),("9",2,1,color1),("/",3,1,color2),
                    ("4",0,2,color1),("5",1,2,color1),("6",2,2,color1),("*",3,2,color2),
                    ("1",0,3,color1),("2",1,3,color1),("3",2,3,color1),("-",3,3,color2),
                    ("0",0,4,color1),(".",1,4,color3),("C",2,4,color3),("+",3,4,color2)]

    # Visor de resultados
    tk.Label(ventana, 
            textvariable = expresion, 
            font = fuente,
            bg = "white",
            bd = 5,
            relief = "solid",
            anchor = "e").grid(
                column = 0,
                row = 0,
                columnspan = 4,
                padx = 5,
                pady = 5,
                sticky = "nsew")
    
    # Botones de numeros y operaciones
    for valor, col, ren, color in lista_botones:
        tk.Button(ventana,
                  text = valor,
                  font = fuente,
                  bg = color,
                  bd = 5,
                  relief = "solid",
                  command = lambda valor=valor: boton_presionado(valor)).grid(
                    column = col,
                    row = ren,
                    padx = 5,
                    pady = 5,
                    sticky = "nsew")
    
    # Boton de resultado
    tk.Button(ventana,
                  text = "=",
                  font = fuente,
                  bg = color4,
                  bd = 5,
                  relief = "solid",
                  command = lambda: boton_presionado("=")).grid(
                    column = 0,
                    columnspan = 4,
                    row = 5,
                    padx = 5,
                    pady = 5,
                    sticky = "nsew")

    # Ejecutar el loop de la ventana
    ventana.mainloop()
