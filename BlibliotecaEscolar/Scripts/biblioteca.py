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