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

    # Operaciones permitidas
    lista_operaciones = {"/","*","+","-"}

    # Variables auxiliares
    lista_expresion = [""]
    resultado = False
    error = False

    # Agrega un valor a la lista de operaciones
    def agrega_valor(valor):
        lista_expresion[-1] += valor
        expresion.set("".join(lista_expresion))

    # Que hacer si se presiona un boton
    def boton_presionado(valor):
        nonlocal error
        nonlocal resultado
        # Si existio un error
        if error:
            if valor == "C":
                error = False
                resultado = False
                lista_expresion.clear()
                lista_expresion.append("")
                agrega_valor("")
        
        # Si se presiona un digito 
        elif valor.isdigit():
            if resultado:
                lista_expresion.clear()
                lista_expresion.append("")
                resultado = False
            elif lista_expresion[-1] in lista_operaciones:
                lista_expresion.append("")
            agrega_valor(valor)

        # Si se presiona un punto
        elif valor == "." and lista_expresion[-1].isdigit():
            if resultado:
                lista_expresion.clear()
                lista_expresion.append("")
                agrega_valor(".")
                resultado = False
            elif "." not in lista_expresion[-1]:
                if lista_expresion[-1] in lista_operaciones:
                    lista_expresion.append("")
                agrega_valor(valor)

        # Si se presiona una operacion
        elif valor in lista_operaciones and lista_expresion[-1] != "":
            if lista_expresion[-1][-1].isdigit():
                lista_expresion.append("")
                agrega_valor(valor)
            resultado = False

        # Si se presiona la tecla de borrado
        elif valor == "C":
            lista_expresion.clear()
            lista_expresion.append("")
            expresion.set("")
            resultado = False

        # Si se presiona la tecla =
        elif valor == "=" and len(lista_expresion) >= 3:
            resultado = resolver_expresion(lista_expresion)
            expresion.set("".join(resultado))
            lista_expresion.clear()
            lista_expresion.append(resultado)
            resultado = True
        print(lista_expresion)
    
    # Resuelve la expresion
    def resolver_expresion(lista_expresion):
        nonlocal error
        # Convierte a float los numeros para evitar problemas
        for i, num in enumerate(lista_expresion):
            if num not in lista_operaciones:
                lista_expresion[i] = float(num)

        # Recorre toda la lista hasta que solo quede 1 valor
        while len(lista_expresion) > 1:
            for i, elemento in enumerate(lista_expresion):
                # Primero verifica multiplicacion y division
                if elemento == "*":
                    lista_expresion[i] = lista_expresion[i - 1] * lista_expresion[i + 1]
                    lista_expresion.pop(i + 1)
                    lista_expresion.pop(i - 1)
                elif elemento == "/":
                    if (lista_expresion[ i+ 1]) == 0:
                        error = True
                        return "Error div por 0. C para continuar"
                    lista_expresion[i] = lista_expresion[i - 1] / lista_expresion[i + 1]
                    lista_expresion.pop(i + 1)
                    lista_expresion.pop(i - 1)
                # Luego verifica sumas y restas
                elif elemento == "+":
                    lista_expresion[i] = lista_expresion[i - 1] + lista_expresion[i + 1]
                    lista_expresion.pop(i + 1)
                    lista_expresion.pop(i - 1)
                elif elemento == "-":
                    lista_expresion[i] = lista_expresion[i - 1] - lista_expresion[i + 1]
                    lista_expresion.pop(i + 1)
                    lista_expresion.pop(i - 1)

        # Si es entero retiramos el punto decimal
        if lista_expresion[0].is_integer():
            return str(int(lista_expresion[0]))
        else:
            return str(lista_expresion[0])

    # Colores de los botones
    color1 = "lightblue"
    color2 = "purple"
    color3 = "blue"
    color4 = "lightgreen"

    # Fuente
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
