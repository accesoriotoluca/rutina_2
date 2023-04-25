"""
! ARCHIVO ORIGINAL CREADO POR STARTAPP DJANGO:
RELACIÓN: MODELOS, VAR URLS, DICCIONARIOS TEMPLETES
define que envia al cliente/navegador para ver en pantalla (archivos html) """

# Jasonresponse, formato q entiende navegador, representar conjunto elementos (queryset)
# ctrl + space : mostrar sugerencias
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from app_rutina import rutina_forms
from app_rutina import models

"""
? funcion convencional con parámetro que envía repuesta HTTP
. función retorna HttpResponse, y cuando ejecute devuelve al navegador ('texto: hola isaac')
. var var_params_ruta es una variable dentro de la ruta y debe tener el mismo nombre para su referencia
. %s concatena un texto con una variante (crea un parametro que ira cambiando conforme cambio de una url a otra)
. HttpResponse devuelve strings (etiquetas, archivos,templates: html) q navegador interpreta
. HttpResponse sirve para probar una respuesta sencilla al cliente """
# Create your views here.

#?funciones de datos:
# pasar variable var_titulo al segundo parametro de render para visualizarlo en alguna parte del archivo html, no es necesario procesar el archivo html o leerlo con modulos del sistema o modulos de lectura de archivos de python, ya viene integrado en django, atravez del 3er parametro en forma de 'diccionario: pares de clave/valor' y declarando ''diccionario_titulo': var_titulo', el archivo html ya tiene referencia clave = referencia al html / valor = variable en este caso (pueden ser string, int, boolean), diccinarios y listas los transforma a strings, ya que html solo espera texto y lo procesa, poir lo tanto la lista de proyectos quedaria mal

def f_inicio(i):
    return render(i, 'inicio.html')

#? funciones que mostrarán y obtendran datos de proyectos y tareas

"""
? queryset para ser visto debe convertirse en lista y establecer el parametro "safe" a False
. El clase .all() todos los "datos" y .values() solo los valores
. queryset_proyectos = list(clase_proyectos.objects.values())
. funcionalidad template engine 'for': de 'listas' generar multiples elementos, lista ul, multiples tarjetas, etc. /interpretar código a modo de condicionales """

def f_cuerpo(i):
    q = models.t_cuerpo.objects.all()
    return render(i, 'cuerpo/cuerpo.html',{
        'f_cuerpo': q
    })

def ff_cuerpo(i):
    if i.method == 'GET':
        return render(i, 'cuerpo/ff_cuerpo.html',
                      {'ff_cuerpo': rutina_forms.tf_cuerpo})
    else:
        models.t_cuerpo.objects.create(cuerpo = i.POST['cuerpo'])
        return redirect('f_cuerpo')
    
def d_cuerpo(i, id):
    d_cuerpo = get_object_or_404(models.t_cuerpo,id=id)
    d_ejercicio = models.t_ejercicio.objects.filter(cuerpo_id=id)
    return render(i, 'cuerpo/d_cuerpo.html',{
        'd_cuerpo':d_cuerpo,
        'd_ejercicio':d_ejercicio
    })

"""
? como el get_object_or_404 remplaza el buscar el objeto especificando el modelo
. var_get_titulo_tarea = tabla_tareas.objects.get(id = var_url_id)
. en la ruta el espacio se cambia a %20 por que hace un encode, esta codificando la url
. antes de usar render solo hemos devuelto strings copn httpresponse
. buscar, enviar, mostrar, etc. datos de database con params, vars en ruta
. def view_funcion_tareas(view_funcion_tareas_param_request, var_url_id):
. var_get_titulo_tarea = get_object_or_404(tabla_tareas, id = var_url_id)
. () #paréntesis al final 'ejecuta la clase/modelo/tabla' pero no lo necesitaba en este caso

print(view_funcion_crear_tarea_param_request.GET['crear_tarea_col_titulo'])
print(view_funcion_crear_tarea_param_request.GET['crear_tarea_col_descripcion']) """

def f_ejercicio(i):
    q = models.t_ejercicio.objects.all()
    return render(i, 'ejercicio/ejercicio.html',{
        'f_ejercicio': q
    })

"""
? cuando visita la página de esta forma no existe el título descripción
. si visitamos 'create task' sin parámetros me indica 'título no existe' entonces al momento de insertar da error 
. no debemos insertar datos con método GET este sirve para mostrar datos en la interfaz
. metodo POST para q servidor reciba datos (cuando el formulario va a enviar los datos)
. en archivo crear tarea en el formulario establecemos método post en ves de action
. en views establecemos si request.método == GET (sirve para mostrar) voy a renderizar la interfaz
. caso contrario si visita otra vez otro método (ELSE/cualquier otro metodo) voy a procesar/guardar/insertan los datos a la base de datos 
. cuando termine de guarda voy a cambiar de página
. por el momento en vez de usar el metodo GET lo cambia a POST por que así lo establecimos en el formulario """
def ff_ejercicio(i):
    if i.method == 'GET':
        return render(i, 'ejercicio/ff_ejercicio.html',
                      {'ff_ejercicio': rutina_forms.tf_ejercicio})
    else:
        models.t_ejercicio.objects.create(
            repeticiones = i.POST['repeticiones'],
            ejercicio = i.POST['ejercicio'],
            posicion = i.POST['posicion'],
            cuerpo_id = i.POST['cuerpo'],
            tipo = i.POST['tipo'],
        )
        return redirect('f_cuerpo')