from catalogo.models import Genero, Autor, Libro, EjemplarLibro
from datetime import date

# Crear géneros
g1 = Genero.objects.create(nombre="Novela")
g2 = Genero.objects.create(nombre="Fantasía")
g3 = Genero.objects.create(nombre="Ciencia Ficción")
g4 = Genero.objects.create(nombre="Clásico")

# Crear autores
a1 = Autor.objects.create(nombre="Gabriel", apellido="García Márquez", fecha_nacimiento="1927-03-06", fecha_fallecimiento="2014-04-17")
a2 = Autor.objects.create(nombre="Miguel", apellido="de Cervantes", fecha_nacimiento="1547-09-29", fecha_fallecimiento="1616-04-22")
a3 = Autor.objects.create(nombre="Isaac", apellido="Asimov", fecha_nacimiento="1920-01-02", fecha_fallecimiento="1992-04-06")
a4 = Autor.objects.create(nombre="Agatha", apellido="Christie", fecha_nacimiento="1890-09-15")

# Crear libros
l1 = Libro.objects.create(titulo="Cien Años de Soledad", autor=a1, resumen="Una gran novela latinoamericana", isbn="1234567890123", idioma="Español")
l1.genero.set([g1])

l2 = Libro.objects.create(titulo="Don Quijote de la Mancha", autor=a2, resumen="La obra más importante de la literatura española", isbn="9876543210987", idioma="Español")
l2.genero.set([g2])

l3 = Libro.objects.create(titulo="Fundación", autor=a3, resumen="Una saga épica sobre la caída y resurgimiento de un imperio galáctico.",isbn="1111111111111", idioma="Español")
l3.genero.set([g3])

l4 = Libro.objects.create(titulo="Asesinato en el Orient Express", autor=a4, resumen="Un misterioso asesinato ocurre a bordo de un tren de lujo.",isbn="2222222222222",idioma="Español")
l4.genero.set([g4])

# Crear ejemplares
EjemplarLibro.objects.create(libro=l1, estado='d', fecha_adquisicion=date.today())
EjemplarLibro.objects.create(libro=l2, estado='p', fecha_adquisicion=date.today())
EjemplarLibro.objects.create(libro=l3, estado='d', fecha_adquisicion=date(2022, 10, 10))
EjemplarLibro.objects.create(libro=l4, estado='p', fecha_adquisicion=date(2023, 3, 15))

#admin
#12345
