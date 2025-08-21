libros = [] #Creación de lista 

#Creación de función en python 

def agregar_libros(titulo, autor, año, indice):
    #Diccionario en Python 

    libro = {
        'titulo' : titulo,
        'autor' : autor, 
        'año' : año, 
        'indice' : indice
    }
    libros.append(libro) #append --> para agregar libros a la lista 
    print(f"Se ha agregado el libro con exito Libro'{titulo}'")

    def Eliminar_libro(titulo):
        for libro in libros:
            #condicional 
            if libro['titulo'] == titulo:
                #Eliminar libro
                libros.remove(libro)
                print("Libro eliminado")
                return
            print("Libro eliminado")
    
    def Editar_Libros(titulo, tituloNuevo, autor, autorNuevo, año, añoNuevo, indice, indiceNuevo):
        for libro in libros:
            if libro['tituloNuevo'] == titulo:
                libro['autorNuevo'] == autor,
                libro['añoNuevo'] == año,
                libro['indiceNuevo'] == indice

                #Editar libro
                tituloNuevo = input("Digite el nombre del nuevo libro")
                autorNuevo = input("Digite el autor nuevo")
                añoNuevo = input("Digite el nuevo año")
                indiceNuevo = input("Digite el indice nuevo")

                
            