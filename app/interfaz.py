import tkinter as tk

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
            relief = "solid").grid(
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
                  relief = "solid").grid(
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
                  relief = "solid").grid(
                    column = 0,
                    columnspan = 4,
                    row = 5,
                    padx = 5,
                    pady = 5,
                    sticky = "nsew")

    # Ejecutar el loop de la ventana
    ventana.mainloop()
