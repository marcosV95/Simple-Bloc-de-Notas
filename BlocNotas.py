from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


def nuevo():
    """Esta funcion limpia la caja de texto para iniciar una nueva nota"""
    option=messagebox.askquestion("Nuevo archivo", "Seguro que quieres crear un nuevo archivo?")
    if option=="yes":
        entradaTexto.delete(0.0, END)

def abrir():
    """Esta funcion abre un archivo .txt y coloca su contenido dentro de la caja de texto. Esta funcion almacena el nombre del archivo abierto en la variable 'guardado'"""
    #global guardado
    vent.filename=filedialog.askopenfilename(title="Seleccionar archivo",filetypes=(("archivos txt","*.txt"),))
    entradaTexto.delete(0.0, END)
    with open(f"{vent.filename}") as txt:
        contenido = txt.read()
    # label=Label(vent,text=contenido)
    # label.pack()
    entradaTexto.insert(END,f"{contenido}")
    guardado.set(f"{vent.filename}")
    

def guardar():
    """Esta funcion guarda el contenido dentro de la caja de texto dentro de un archivo. Si la variable 'guardado' almacena una ruta, esta funcion va a sobreescribir ese archivo con el contenido nuevo, y si la variable no almacena nada esta funcion creara un 'Nuevo_archivo'"""
    inputValue=entradaTexto.get("1.0","end-1c")
    if guardado.get()=="":
        with open("Nuevo_Documento.txt","w") as txt:
            txt.write(f"{inputValue}")
        guardado.set("Nuevo_Documento.txt")
    else:
        with open(f"{guardado.get()}","w") as txt:
            txt.write(f"{inputValue}")
        

def guardarComo():
    """Esta funcion guarda el archivo con formato .txt"""
    vent.filename=filedialog.asksaveasfilename(title="Guardar archivo como", filetypes=(("archivos txt","*.txt"),))
    posUltimoSlash=vent.filename.rfind("/")
    archivo=vent.filename[posUltimoSlash+1:]
    inputValue=entradaTexto.get("1.0","end-1c")
    with open(f"{archivo}","w") as txt:
        txt.write(f"{inputValue}")
    # label=Label(vent,text=vent.filename)
    # label.pack()    

def cortar():
    """Corta una parte seleccionada del texto por el usuario y lo guarda en una variable para poder pegarla con la funcion pegar()"""
    textoSeleccionado=entradaTexto.get(SEL_FIRST,SEL_LAST)#Esto consigue de la caja de texto toda la cadena seleccionada con el cursor
    textoCopiado.set(f"{textoSeleccionado}")
    entradaTexto.delete(SEL_FIRST,SEL_LAST)

def copiar():
    """Esta funcion copia una parte del texto seleccionado por el usuario y lo guarda en una variable de cadena para luego pegar su contenido con la funcion pegar()"""
    textoSeleccionado=entradaTexto.get(SEL_FIRST,SEL_LAST)
    textoCopiado.set(f"{textoSeleccionado}")

def pegar():
    """Pega el texto almacenado en 'textoCopiado'"""
    if textoCopiado.get()!="":
        posCursor=entradaTexto.index(INSERT)#Esto consigue la posicion actual del cursor dentro de la caja de texto
        entradaTexto.insert(posCursor,f"{textoCopiado.get()}")#Una vez teniendo la posicion del cursor, dentro de este metodo indico que apartir de la posicion actual del cursor quiero agregar el texto almacenado en 'textoGuardado'

def deshacer():
    """Deshace la ultima accion del usuario dentro de la caja de texto"""
    entradaTexto.edit_undo()

def rehacer():
    """Rehace la ultima accion del usuario dentro de la caja de texto"""
    entradaTexto.edit_redo()

#Aqui se define la ventana inicial
vent=Tk()
vent.title("Bloc de Notas")
#vent.resizable(False,False)
vent.geometry("620x510")
vent.iconbitmap("notas.ico")

#Aqui se definen todos los elementos dentro de la barra de menu
barraMenu=Menu(vent)
menuArchivo=Menu(barraMenu,tearoff=0)
menuArchivo.add_command(label="Nuevo",command=nuevo)
menuArchivo.add_command(label="Abrir",command=abrir)
menuArchivo.add_command(label="Guardar",command=guardar)
menuArchivo.add_command(label="Guardar como",command=guardarComo)

menuEditar=Menu(vent,tearoff=0)
menuEditar.add_command(label="Cortar",command=cortar)
menuEditar.add_command(label="Copiar",command=copiar)
menuEditar.add_command(label="Pegar",command=pegar)
menuEditar.add_command(label="Deshacer",command=deshacer)
menuEditar.add_command(label="Rehacer",command=rehacer)

barraMenu.add_cascade(label="Archivo",menu=menuArchivo)
barraMenu.add_separator()
barraMenu.add_cascade(label="Editar",menu=menuEditar)
vent.config(menu=barraMenu)

#Aqui se declaran las variables para almacenar informacion proveniente de las funciones
guardado=StringVar()#Esta variable almacena el nombre del archivo el cual se abre por medio de la funcion "abrir"
textoCopiado=StringVar()#Esta variable almacena el texto cortado o copiado por el usuario, para luego poder pegarlo mediante la funcion pegar()

#Aqui se define la caja de texto donde el usuario va a poder tipear su nota
entradaTexto=Text(vent,width=77,height=31,undo=True)
entradaTexto.pack(fill='both',expand=True)


# entradaTexto=Text(frm,width=77,height=31)
# #entradaTexto.place(height=510)
# entradaTexto.grid(column=0,row=0)

vent.mainloop()