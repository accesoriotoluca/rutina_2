"""
git add .
git commit -m ''
git push origin m

? VSCODE:
F1 : lista de opciones en vscode
'select interpreter' : establecer la terminal con el entorno virtual

-------------------------------

? TERMINAL:
'cls' : limpiar consola

-------------------------------

? VIRTUALENV:
'pip install virtualenv'
'virtualenv entorno_virtual' : CREAR ENTORNO (ESTO CREA UNA CARPETA)
".\entorno_virtual\Scripts\activate" : 'ACTIVAR ENTORNO

-------------------------------

? DJANGO:
'django-admin startproject nombre_proyecto_django .' : CREAR PROYECTO DJANGO ( ' .' AL FINAL HACE QUE NO CREE DOBLE CARPETA)
'__pycache__' : la carpeta guarda código que ya compilo python para que se ejecute mas rápido

? DJANGO ADMIN:
python manage.py createsuperuser
i44k3112


-------------------------------

? PARAMS:
recibir datos desde navegador para pasarlo por operaciones de una base de datos

-------------------------------

? SERVIDOR:
ORM? en cada cambio, vuelve a ejecutar todo el proyecto automaticamente

? BASE DE DATOS:
1. 'python manage.py makemigrations nombre_carpeta_app' inicialmente no sirve por que python ya tiene 'migraciones' hechas de database por defecto de ORM
1.1 pero el comando migra los datos de los modelos de las apps en general o la especificada y crea archivos migrations dentro de carpeta migrations de app
2. 'python manage.py migrate nombre_carpeta_app' ejecuta las 'migraciones' crea las tablas dentro de nuestra base de datos de apps en general o la especificada
2.1 el 'script' del archivo db.sqlite3 es el que ejecuta las migraciones, este proceso funciona en cualquier base de datos (sql: mysql, postgres, oracle, etc.) con la configuración correcta, para eso se crea un modelo en la carpeta de la app
2.2. para crear tablas (productos, categorías, etc.) es necesario crear un 'modelo' (código python que se va a transformar en una tabla SQL), dentro del archivo 'models.py', se crea una clase, que hera los modelos que da django, y de allí llama a la clase model, que permiten especificar las tablas

-------------------------------

? MINI CLASE SHELL? para interactuar con database
- 'python manage.py shell' iniciar la consola
- 'from app.models import proyectos, tareas': importar tablas desde archivo models de app
- 'proyectos(nombre = 'proyecto 1').save()': ingresa dato en fila en turno en columna nombre
- 'proyectos.objects.all()': obtiene set query de ids
- 'proyectos.objects.all().delete()': elimina todos los datos de proyectos
- 'proyectos.objects.get(id=1)': obtiene query con id, donde id=1
- 'proyectos.objects.get(id=1).delete()': elimina la fila donde id=1
- 'proyectos.objects.get(id=7).tareas_set.create(titulo = 'tarea 1')': crea dato en fila en turno en columna titulo de tabla tareas con referencia de la tabla proyectos con id 7.
- 'proyectos.objects.get(id=7).tareas_set.all()': obtiene set query de ids de tareas relacionados a proyectos con id 7
- 'proyectos.objects.get(id=7).tareas_set.all().delete()': elimina todos los datos de tareas relacionados a proyectos con id 7
- 'proyectos.objects.get(id=7).tareas_set.get(id=1)': obtiene dato donde id=1 de tareas relacionados a proyectos con id 7
- 'proyectos.objects.get(id=7).tareas_set.get(id=1).delete()': elimina dato donde id=1 de tareas relacionados a proyectos con id 7

-------------------------------

? CARPETAS:
si las carpetas que tiene un nombre reservado vscode las identifica?, o almenos la carpeta templeates tiene un nombre reservado // olvidalo si no tiene el nombre predeterminado django no la reconoce

? PROYECTO GLOBAL Y APLICACIONES
'python manage.py startapp carpeta_aplicacion_1' : crea carpeta de applicacion interna del proyecto global
    carpeta_proyecto_django : administra 'proyecto global'
    carpeta_aplicacion_1 : administra una parte del 'proyecto global'

? MIGRATIONS:
SE MODIFICA AUTOMATICAMENTE al llenar datos en la base de datos
django no requiere consultas SQL x modulo ORM base de datos interactua atraves de código de python

-------------------------------

? ORGANIGRAMA:
¿que otros pasos faltan?
¿en django como se le llama a este proceso? ¿existen otros metodos de trabajo?

? INSTALACIÓN DE HERRAMIENTAS:
. creamos un entorno virtual: virtualenv 'nombre' y lo activamos: .\'nombre'\Scripts\activate
. instalamos django en entorno: pip install django

? PROYECTO Y APP:
. creamos un proyecto con: django-admin startproject 'nombre' '.' para que no cree otra carpeta
. en proyecto creamos una app: python manage.py startapp 'nombre'
. en proyecto en archivo settings agregamos nombre de app a la lista de apps

? MODELOS:
. en app en archivo models creamos modelos y establecemos, clase, tipo de dato y relación
. migramos los datos de los modelos: python manage.py makemigrations 'app' 
. ejecutamos las migraciones: python manage.py migrate 'app'

? VIEWS:
. en app en archivo views creamos función para enviar contenido al navegador
. en app en archivo views creamos diccionario que relaciona los modelos y el archivo html

? TEMPLATES:
. en app creamos carpeta templates y archivo templete.html con etiquetas button, a, div, etc.
. en app en templates en archivo templete creamos jinja loop/conditionals para mostrar elementos de los modelos

? TEMPLETES BASE/NAVEGACIÓN:
. en app creamos carpeta diseños y archivo base y creamos con etiquetas nav,ul,li,a una navegación y con el metodo block/endblock de jinja referenciamos donde estará el contenido de archivo templete
. en app en templates en archivo templete usamos el método extends de jinja para referenciar la navegacion de archivo base y agregamos block/endblock para referenciar donde estara el contenido

? FORMULARIOS:
. an app creamos archivo formularios, donde creamos la clase para ingresar datos desde la clase forms de django, y lo referenciamos en en archivo templete, usando etiqueta form com method POST, y agregamos metodo csrf_token de jinja
. en app en views en la función agregamos una condicional if si el request method es igual a get renderizamos el contenido, de lo contrario se crearía un nuevo objeto en el modelo con los datos del input delformulario y con metodo redirect se redirecciona a la lista de proyectos

? ESTÁTICOS Y CSS
. en app creamos carpeta static para agregar imagenes, pdf, etc a archivo templete
. en app en static creamos carpeta css y archivo css y agregamos estilos
. en app en templete referenciamos con jinja load static/ static 'css/css.css' para agregar estilos al archivo html

? URLS:
. en app creamos archivo que aloja urls_app que ejecutan funciones importadas de views
. en proyecto en archivo urls incluimos urls_app con módulo include.

-------------------------------

? para despues:
. Creamos modelo dentro de app, ventas(#venta, cliente, producto, cantidad_venta, precio_venta)
. Creamos modelo dentro de app, productos(producto, sku, cantidad, precio)
. Creamos modelo dentro de app, clientes(nombre, telefono, direccion)
. migramos datos de modelos dentro de app a la base de datos

"""

""" 
* SE INSTALLA UNA EXTENCION APARTE:
    pip install django-crispy-forms
    pip install crispy-bootstrap4

* NUEVO CONTEXTO PARA AGREGAR DICCIONARIOS EN UNA VARIABLE:
    context = {'form': forms.UniuversityForm }
        return render(request,'index.html',context)

* REITERACION DE ".as_p" COMO HERRAMIENTA UTIL

* TUPLAS DE OPCIONES: 
    tupla que contiene tuplas anidadas, cada anidada representa una opción con un valor y una etiqueta correspondiente:

    OPCIÓN N: VALOR: 1 / ETIQUETA: 'Web Development'

    subject = forms.ChoiceField(choices=SUBJECT_CHOICES)

    SUBJECT_CHOICES = (
            (1, 'Web Development'),
            (2, 'System Programming'),
            (3, 'Data Science')
        )

* 'crispy_bootstrap4', 'crispy_forms',: 
    SE DEBE AGREGAR A LA LISTA DE APPS EN settings.py, DEBE SER UN TIPO DE APP O FUNCIONA COMO UNA APP DENTRO DE DJANGO

* CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
  CRISPY_TEMPLATE_PACK = 'bootstrap4': 
    has template packs for different libraries css frameworks 'we use bootstrap 4' template pack, this goes into settings.py

* {.% load crispy_forms_tags %}: 
    use crispy forms within our template 

* {.{ form.as_p }} >>> {.% crispy form %}: 
    render the form to use the crispy form tag

* agrega una fecha como en appsheet y puedes poner el maximo en fecha de agregado:

    necesita importar esto: from datetime import datetime

    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={
            'type':'date',
            'max': datetime.now().date()
        }
    ))

* agrega las opciones y los pone como opción multiple:

    subject = forms.ChoiceField(
        choices=SUBJECT_CHOICES, 
        widget=forms.RadioSelect()
    )

* SET FORM ACTION: in 'form action' use 'reverse lazy function' to url template tag
    . reference the index url
    . not submit the form in the view
    . inspect elements: we got a 'form element'
    . specify where the submission should be sent on server
    . looks up urls by name, turns them into proper path for url on server
    . gives a way of specifying that

    from django.urls import reverse_lazy
    from crispy_forms.helper import FormHelper

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    >>> self.helper.form_action = reverse_lazy('index')
    >>> AGREGA UNA ACCION: <form action="/"></form>

* AGREGAR UN BOTON SUBMIT AL CUESTIONARIO

    from crispy_forms.helper import FormHelper
    from crispy_forms.layout import Submit

    self.helper.add_input(Submit('submit','submit'))

    
"""