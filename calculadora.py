import tkinter as tk

# ------------ FUNCIONES ------------
def escribir_numero(valor):
    global primer_numero
    if (valor == "0" or valor=="x" or valor=="/" or valor=="+" or valor==".") and texto_en_pantalla.get() == "0":
        if valor==".":
            texto_en_pantalla.set(texto_en_pantalla.get() + valor)
            primer_numero = False
    elif texto_en_pantalla.get() == "ERROR":
        texto_en_pantalla.set("ERROR")
    else:
        if primer_numero:
            texto_en_pantalla.set("")
        primer_numero = False
        texto_en_pantalla.set(texto_en_pantalla.get() + valor)  
            
def calcular():
    global primer_numero
    calculo = texto_en_pantalla.get().replace("x","*")
    try: 
        resultado = eval(calculo)
        texto_en_pantalla.set(resultado)
        if resultado == 0:
            primer_numero = True
    except Exception:
        texto_en_pantalla.set("ERROR")
        raiz.after(1000, lambda: texto_en_pantalla.set("0"))
        primer_numero = True
    
def borrar_todo():
    global primer_numero
    texto_en_pantalla.set("0")
    primer_numero = True
    
def borrar_ultimo():
    nuevo_texto = texto_en_pantalla.get()[:-1]
    if len(texto_en_pantalla.get()) != 1:
        texto_en_pantalla.set(nuevo_texto)
        
def escribir_por_teclado(event):
    tecla = event.char
    if tecla == "0" or tecla == "1" or tecla == "2" or tecla == "3" or tecla == "4" or tecla == "5" or tecla == "6" or tecla == "7" or tecla == "8" or tecla == "9" or tecla == "+" or tecla == "-" or tecla == "/"  or tecla == "x" or tecla == ".":
        escribir_numero(event.char)
    if tecla == "\r":
        calcular()
    if tecla == "\x08":
        borrar_ultimo()
        
def cambiar_tema():
    if tema_apariencia.get() == 1: #Claro
        contenedor.config(bg=temas["claro"]["fondo"])
        display.config(bg=temas["claro"]["display"], fg=temas["claro"]["letra"])
        boton_0.config(bg=temas["claro"]["boton_numero"], fg=temas["claro"]["letra"])
        boton_1.config(bg=temas["claro"]["boton_numero"], fg=temas["claro"]["letra"])
        boton_2.config(bg=temas["claro"]["boton_numero"], fg=temas["claro"]["letra"])
        boton_3.config(bg=temas["claro"]["boton_numero"], fg=temas["claro"]["letra"])
        boton_4.config(bg=temas["claro"]["boton_numero"], fg=temas["claro"]["letra"])
        boton_5.config(bg=temas["claro"]["boton_numero"], fg=temas["claro"]["letra"])
        boton_6.config(bg=temas["claro"]["boton_numero"], fg=temas["claro"]["letra"])
        boton_7.config(bg=temas["claro"]["boton_numero"], fg=temas["claro"]["letra"])
        boton_8.config(bg=temas["claro"]["boton_numero"], fg=temas["claro"]["letra"])
        boton_9.config(bg=temas["claro"]["boton_numero"], fg=temas["claro"]["letra"])
        boton_punto.config(bg=temas["claro"]["boton_numero"], fg=temas["claro"]["letra"])
        boton_sumar.config(bg=temas["claro"]["boton_operacion"], fg=temas["claro"]["letra"])
        boton_restar.config(bg=temas["claro"]["boton_operacion"], fg=temas["claro"]["letra"])
        boton_multiplicar.config(bg=temas["claro"]["boton_operacion"], fg=temas["claro"]["letra"])
        boton_dividir.config(bg=temas["claro"]["boton_operacion"], fg=temas["claro"]["letra"])
        boton_igual.config(bg=temas["claro"]["boton_resaltado"], fg=temas["claro"]["letra"])
        boton_borrar_todo.config(bg=temas["claro"]["boton_resaltado"], fg=temas["claro"]["letra"])
        boton_borrar_ultimo.config(bg=temas["claro"]["boton_resaltado"], fg=temas["claro"]["letra"])
        boton_cambiar_tema_oscuro.config(bg=temas["claro"]["fondo"], fg=temas["claro"]["letra"], activebackground=temas["claro"]["fondo"], activeforeground=temas["claro"]["letra"])
        boton_cambiar_tema_claro.config(bg=temas["claro"]["fondo"], fg=temas["claro"]["letra"], activebackground=temas["claro"]["fondo"], activeforeground=temas["claro"]["letra"])
        boton_cambiar_tema_color.config(bg=temas["claro"]["fondo"], fg=temas["claro"]["letra"], activebackground=temas["claro"]["fondo"], activeforeground=temas["claro"]["letra"])
        
    if tema_apariencia.get() == 2: #Oscuro
        contenedor.config(bg=temas["oscuro"]["fondo"])
        display.config(bg=temas["oscuro"]["display"], fg=temas["oscuro"]["letra"])
        boton_0.config(bg=temas["oscuro"]["boton_numero"], fg=temas["oscuro"]["letra"])
        boton_1.config(bg=temas["oscuro"]["boton_numero"], fg=temas["oscuro"]["letra"])
        boton_2.config(bg=temas["oscuro"]["boton_numero"], fg=temas["oscuro"]["letra"])
        boton_3.config(bg=temas["oscuro"]["boton_numero"], fg=temas["oscuro"]["letra"])
        boton_4.config(bg=temas["oscuro"]["boton_numero"], fg=temas["oscuro"]["letra"])
        boton_5.config(bg=temas["oscuro"]["boton_numero"], fg=temas["oscuro"]["letra"])
        boton_6.config(bg=temas["oscuro"]["boton_numero"], fg=temas["oscuro"]["letra"])
        boton_7.config(bg=temas["oscuro"]["boton_numero"], fg=temas["oscuro"]["letra"])
        boton_8.config(bg=temas["oscuro"]["boton_numero"], fg=temas["oscuro"]["letra"])
        boton_9.config(bg=temas["oscuro"]["boton_numero"], fg=temas["oscuro"]["letra"])
        boton_punto.config(bg=temas["oscuro"]["boton_numero"], fg=temas["oscuro"]["letra"])
        boton_sumar.config(bg=temas["oscuro"]["boton_operacion"], fg=temas["oscuro"]["letra"])
        boton_restar.config(bg=temas["oscuro"]["boton_operacion"], fg=temas["oscuro"]["letra"])
        boton_multiplicar.config(bg=temas["oscuro"]["boton_operacion"], fg=temas["oscuro"]["letra"])
        boton_dividir.config(bg=temas["oscuro"]["boton_operacion"], fg=temas["oscuro"]["letra"])
        boton_igual.config(bg=temas["oscuro"]["boton_resaltado"], fg=temas["oscuro"]["letra"])
        boton_borrar_todo.config(bg=temas["oscuro"]["boton_resaltado"], fg=temas["oscuro"]["letra"])
        boton_borrar_ultimo.config(bg=temas["oscuro"]["boton_resaltado"], fg=temas["oscuro"]["letra"])
        boton_cambiar_tema_oscuro.config(bg=temas["oscuro"]["fondo"], fg=temas["oscuro"]["letra"], activebackground=temas["oscuro"]["fondo"], activeforeground=temas["oscuro"]["letra"])
        boton_cambiar_tema_claro.config(bg=temas["oscuro"]["fondo"], fg=temas["oscuro"]["letra"], activebackground=temas["oscuro"]["fondo"], activeforeground=temas["oscuro"]["letra"])
        boton_cambiar_tema_color.config(bg=temas["oscuro"]["fondo"], fg=temas["oscuro"]["letra"], activebackground=temas["oscuro"]["fondo"], activeforeground=temas["oscuro"]["letra"])
    
    if tema_apariencia.get() == 3: #Color
        contenedor.config(bg=temas["color"]["fondo"])
        display.config(bg=temas["color"]["display"], fg=temas["color"]["letra"])
        boton_0.config(bg=temas["color"]["boton_numero"], fg=temas["color"]["letra"])
        boton_1.config(bg=temas["color"]["boton_numero"], fg=temas["color"]["letra"])
        boton_2.config(bg=temas["color"]["boton_numero"], fg=temas["color"]["letra"])
        boton_3.config(bg=temas["color"]["boton_numero"], fg=temas["color"]["letra"])
        boton_4.config(bg=temas["color"]["boton_numero"], fg=temas["color"]["letra"])
        boton_5.config(bg=temas["color"]["boton_numero"], fg=temas["color"]["letra"])
        boton_6.config(bg=temas["color"]["boton_numero"], fg=temas["color"]["letra"])
        boton_7.config(bg=temas["color"]["boton_numero"], fg=temas["color"]["letra"])
        boton_8.config(bg=temas["color"]["boton_numero"], fg=temas["color"]["letra"])
        boton_9.config(bg=temas["color"]["boton_numero"], fg=temas["color"]["letra"])
        boton_punto.config(bg=temas["color"]["boton_numero"], fg=temas["color"]["letra"])
        boton_sumar.config(bg=temas["color"]["boton_operacion"], fg=temas["color"]["letra"])
        boton_restar.config(bg=temas["color"]["boton_operacion"], fg=temas["color"]["letra"])
        boton_multiplicar.config(bg=temas["color"]["boton_operacion"], fg=temas["color"]["letra"])
        boton_dividir.config(bg=temas["color"]["boton_operacion"], fg=temas["color"]["letra"])
        boton_igual.config(bg=temas["color"]["boton_resaltado"], fg=temas["color"]["letra"])
        boton_borrar_todo.config(bg=temas["color"]["boton_resaltado"], fg=temas["color"]["letra"])
        boton_borrar_ultimo.config(bg=temas["color"]["boton_resaltado"], fg=temas["color"]["letra"])
        boton_cambiar_tema_oscuro.config(bg=temas["color"]["fondo"], fg=temas["color"]["letra"], activebackground=temas["color"]["fondo"], activeforeground=temas["color"]["letra"])
        boton_cambiar_tema_claro.config(bg=temas["color"]["fondo"], fg=temas["color"]["letra"], activebackground=temas["color"]["fondo"], activeforeground=temas["color"]["letra"])
        boton_cambiar_tema_color.config(bg=temas["color"]["fondo"], fg=temas["color"]["letra"], activebackground=temas["color"]["fondo"], activeforeground=temas["color"]["letra"])
    
# ------------ PERSONALIZACION ------------
temas = {
    "oscuro":{
        "fondo": "#121212",             
        "display": "#272727",           
        "letra": "#FFFFFF",             
        "boton_resaltado": "#51524f",   
        "boton_numero": "#323232",      
        "boton_operacion": "#51524f"
    },
    "claro":{
        "fondo": "#F5F5F5",            
        "display": "#E0E0E0",           
        "letra": "#000000",            
        "boton_resaltado": "#c2c2be",   
        "boton_numero": "#E0E0E0",      
        "boton_operacion": "#c2c2be"
    },
    "color":{
        "fondo":"#333333",
        "display":"#B8C1A9",
        "letra":"white",
        "boton_resaltado":"#E24A10",
        "boton_numero":"#848484",
        "boton_operacion":"#59A12B"
    }
}
font=('Helvetica', 15)

# ------------ TKINTER ------------
raiz = tk.Tk()
raiz.title("Calculadora")
raiz.resizable(False, False)
raiz.iconbitmap("logo.ico")
contenedor = tk.Frame(raiz, bg=temas["color"]["fondo"])
contenedor.grid()

# ------------ PANTALLA CALCULADORA ------------
texto_en_pantalla = tk.StringVar()
texto_en_pantalla.set("0")
display = tk.Label(contenedor, anchor="e", font=font, textvariable=texto_en_pantalla, bg=temas["color"]["display"], fg=temas["color"]["letra"], justify="right", width=20)
display.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
primer_numero = True
tema_apariencia = tk.IntVar()
tema_apariencia.set(3)

# ------------ BOTONES FILA 1 ------------
boton_borrar_todo = tk.Button(contenedor, font=font, text="C", bg=temas["color"]["boton_resaltado"], fg="white", width=6, command=borrar_todo)
boton_borrar_ultimo = tk.Button(contenedor, font=font, text="⌫", bg=temas["color"]["boton_resaltado"], fg="white", width=6, command=borrar_ultimo)
# En pantalla:
boton_borrar_todo.grid(row=2, column=1, columnspan=2, pady=5)
boton_borrar_ultimo.grid(row=2, column=3, columnspan=2, pady=5)

# ------------ BOTONES FILA 2 ------------
boton_7 = tk.Button(contenedor, font=font, text="7", bg=temas["color"]["boton_numero"], fg=temas["color"]["letra"], width=3, command=lambda:escribir_numero("7"))
boton_8 = tk.Button(contenedor, font=font, text="8", bg=temas["color"]["boton_numero"], fg=temas["color"]["letra"], width=3, command=lambda:escribir_numero("8"))
boton_9 = tk.Button(contenedor, font=font, text="9", bg=temas["color"]["boton_numero"], fg=temas["color"]["letra"], width=3, command=lambda:escribir_numero("9"))
boton_dividir = tk.Button(contenedor, font=font, text="/", bg=temas["color"]["boton_operacion"], fg=temas["color"]["letra"], width=3, command=lambda:escribir_numero("/"))
# En pantalla:
boton_7.grid(row=3, column=1, padx=5)
boton_8.grid(row=3, column=2, padx=5)
boton_9.grid(row=3, column=3, padx=5)
boton_dividir.grid(row=3, column=4, padx=5)

# ------------ BOTONES FILA 3 ------------
boton_4 = tk.Button(contenedor, font=font, text="4", bg=temas["color"]["boton_numero"], fg=temas["color"]["letra"], width=3, command=lambda:escribir_numero("4"))
boton_5 = tk.Button(contenedor, font=font, text="5", bg=temas["color"]["boton_numero"], fg=temas["color"]["letra"], width=3, command=lambda:escribir_numero("5"))
boton_6 = tk.Button(contenedor, font=font, text="6", bg=temas["color"]["boton_numero"], fg=temas["color"]["letra"], width=3, command=lambda:escribir_numero("6"))
boton_multiplicar = tk.Button(contenedor, font=font, text="x", bg=temas["color"]["boton_operacion"], fg=temas["color"]["letra"], width=3, command=lambda:escribir_numero("x"))
# En pantalla:
boton_4.grid(row=4, column=1, padx=5, pady=5)
boton_5.grid(row=4, column=2, padx=5, pady=5)
boton_6.grid(row=4, column=3, padx=5, pady=5)
boton_multiplicar.grid(row=4, column=4, padx=5, pady=5)

# ------------ BOTONES FILA 4 ------------
boton_1 = tk.Button(contenedor, font=font, text="1", bg=temas["color"]["boton_numero"], fg=temas["color"]["letra"], width=3, command=lambda:escribir_numero("1"))
boton_2 = tk.Button(contenedor, font=font, text="2", bg=temas["color"]["boton_numero"], fg=temas["color"]["letra"], width=3, command=lambda:escribir_numero("2"))
boton_3 = tk.Button(contenedor, font=font, text="3", bg=temas["color"]["boton_numero"], fg=temas["color"]["letra"], width=3, command=lambda:escribir_numero("3"))
boton_restar = tk.Button(contenedor, font=font, text="-", bg=temas["color"]["boton_operacion"], fg=temas["color"]["letra"], width=3, command=lambda:escribir_numero("-"))
# En pantalla:
boton_1.grid(row=5, column=1, padx=5)
boton_2.grid(row=5, column=2, padx=5)
boton_3.grid(row=5, column=3, padx=5)
boton_restar.grid(row=5, column=4, padx=5)

# ------------ BOTONES FILA 5 ------------
boton_0 = tk.Button(contenedor, font=font, text="0", bg=temas["color"]["boton_numero"], fg=temas["color"]["letra"], width=3, command=lambda:escribir_numero("0"))
boton_punto = tk.Button(contenedor, font=font, text=".", bg=temas["color"]["boton_numero"], fg=temas["color"]["letra"], width=3, command=lambda:escribir_numero("."))
boton_sumar = tk.Button(contenedor, font=font, text="+", bg=temas["color"]["boton_operacion"], fg=temas["color"]["letra"], width=3, command=lambda:escribir_numero("+"))
boton_igual = tk.Button(contenedor, font=font, text="=", bg=temas["color"]["boton_resaltado"], fg=temas["color"]["letra"], width=3, command=calcular)
# En pantalla:
boton_0.grid(row=6, column=1, padx=5, pady=5)
boton_punto.grid(row=6, column=2, padx=5, pady=5)
boton_sumar.grid(row=6, column=3, padx=5, pady=5)
boton_igual.grid(row=6, column=4, padx=5, pady=5)

# ------------ CONFIGURACION ------------
contenedor_configuracion = tk.Frame(contenedor)
contenedor_configuracion.grid(row=7, column= 1, columnspan=4)
boton_cambiar_tema_claro = tk.Radiobutton(contenedor_configuracion, font=("Helvetica", 12), variable=tema_apariencia, value=1, command=cambiar_tema, text="Claro", bg=temas["color"]["fondo"], selectcolor="grey", fg=temas["color"]["letra"], activebackground=temas["color"]["fondo"], activeforeground=temas["color"]["letra"])
boton_cambiar_tema_oscuro = tk.Radiobutton(contenedor_configuracion, font=("Helvetica", 12), variable=tema_apariencia, value=2, command=cambiar_tema, text="Oscuro", bg=temas["color"]["fondo"], selectcolor="grey", fg=temas["color"]["letra"], activebackground=temas["color"]["fondo"], activeforeground=temas["color"]["letra"])
boton_cambiar_tema_color = tk.Radiobutton(contenedor_configuracion, font=("Helvetica", 12), variable=tema_apariencia, value=3, command=cambiar_tema, text="Color", bg=temas["color"]["fondo"], selectcolor="grey", fg=temas["color"]["letra"], activebackground=temas["color"]["fondo"], activeforeground=temas["color"]["letra"])
boton_cambiar_tema_claro.grid(row=1, column=1)
boton_cambiar_tema_oscuro.grid(row=1, column=2)
boton_cambiar_tema_color.grid(row=1, column=3)


raiz.bind("<Key>", escribir_por_teclado)
raiz.mainloop()
