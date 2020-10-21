# Create your views here.

from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Articulo # importamos la clase articulo para usar sus atributos
from miapp.forms import FormArticulo # Se importa la clase del formulario articulo
from django.contrib import messages # Libreria Para mostrar mensajes flash 

#Creamos una variable para mostrarla en el index
nombre_autor_web="Vladimir Guajardo"

# se crea una lista 
lenguajes = ['python', 'C#', 'Java', 'PHP', 'Type Script', 'JavaScript']

def index(request):
    return render ( request, 'index.html', {
        'mi_variable':'soy un datos que esta en la vista',
        'titulo':'Bienvenidos',
        'nombre_autor': nombre_autor_web,
        'lenguajes':lenguajes
    })


def hola_mundo (request):
    return render (request, 'hola_mundo.html', {
        'numero1':'2',
        'numero2':'4'
    })

def contacto(request):
    return render (request, 'contacto.html', {
        'contacto': 'Vladimir Guajardo'
    }
    )

#En este metodo estamos enviando tres parametros,el ultimo es un diccionario
def quienes_somos(request):
    return render (request,'quienes_somos.html',{
        'Nombre_empresa':'Somos una empresa de desarrollo en Python'
    }
    )

# Vista para la creacion de articulos
def crear_articulo(request, title, content, public):
        articulo  = Articulo(
            titulo = title,
            contenido= content,
            publicado = public
        )
        # Para guardar el articulo en la bbdd se utiliza el siguiente metodo
        articulo.save()

        return HttpResponse(f"El articulo {articulo.titulo} se almaceno en la BBDD. ")

############################################### trabajo con formularios ################################################

# Vista para la creacion de articulos
def save_article(request):

    if request.method == 'POST':      

        # Recogemos los datos enviados por post

        titulo = request.POST['titulo']
        contenido = request.POST['contenido']
        publicado = request.POST['publicado']

        # Validar que el titulo no venga en blanco
       # if len(titulo) == 0 or len(contenido) == 0 :
        #    return HttpResponse("Debe completar el formulario")

        articulo  = Articulo(
            titulo = titulo,
            contenido= contenido,
            publicado = publicado                    
        )
        # Para guardar el articulo en la bbdd se utiliza el siguiente metodo
        articulo.save()
        return HttpResponse(f"El articulo {articulo.titulo} se almaceno en la BBDD. ")
    else:
        return HttpResponse("No se ha podido guardar el artículo ")


def create_article(request):

    return render (request,'create_article.html')


######################################################################################################################


# Vista para obtener un articulo en particular
def articulo (request):

#excepción
    try:
         articulo = Articulo.objects.get(id=2 , publicado=True)
         response = f"El nombre del Articulo es:<strong> {articulo.titulo} </strong> <br> y su contenido:<strong>{articulo.contenido}</strong>"
        
    except:
        response = f"No se encontro el articulo"

    return HttpResponse (response)

# Vista para actualizar un articulo
def editar_articulo(request, id):

    try:
        articulo = Articulo.objects.get(id=id)
        articulo.titulo = 'editado'
        articulo.contenido = 'contenido editado'
        articulo.save()
        response = f"El articulo Nº: {articulo.id} ha sido editado."
    
    except:
        response = f"El articulo no existe."

    return HttpResponse(response)

# Listar todos los articulos 
def listar_articulos(request):
    
    #articulos = Articulo.objects.all() Todos los articulos 

    articulos = Articulo.objects.order_by('-id') #Ordenado por ID


    return render(request, 'articulos.html', {
        'articulos': articulos
    })

# Borrar articulos
def borrar_articulos (request, id):

    articulo = Articulo.objects.get(pk=id)
    articulo.delete()

    return redirect('listado_articulos')

################################################# FORMS a traves de la clase Forms #####################
#PARA USAR LOS FORMS A TRAVES DE CLASES SE DEBE IMPORTAR
#from miapp.forms import FormArticulo

def creacion_full_articulo (request):

    if request.method == 'POST':
        formulario = FormArticulo(request.POST)

        if formulario.is_valid():
            datos_formulario = formulario.cleaned_data #Si el formulario es valido, recogo los datos  

            title = datos_formulario.get('titulo')
            content = datos_formulario.get('contenido')
            public = datos_formulario.get('publicado')

            articulo = Articulo(
                titulo = title,
                contenido = content,
                publicado = public
            )
            # Para guardar el articulo en la bbdd se utiliza el siguiente metodo
            articulo.save()

            #Crear mensaje flash (solo se muestra una vez)
            messages.success(request, f'Has creado correctamete el articulo: {articulo.titulo}')



            return redirect ('listado_articulos')
           # return HttpResponse (articulo.titulo + ' ' + articulo.contenido + ' '+ str(articulo.publicado) )

    else:
        formulario = FormArticulo()

    return render (request, 'creacion_full_articulo.html',{
        'form': formulario # se pasa el fomulario instanciado
    })

