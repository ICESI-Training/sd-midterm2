# Distributed Systems exam 2
Examen 2

Universidad ICESI
Curso: Sistemas Operativos
Docente: Juan Manuel Alvarez
Tema: Diseño de arquitectura de Microservicios

## Integrantes

Estudiante: Sebastian Calero
Código: A00065884

Estudiante: Felipe Cortés 
Código: A00077528

Objetivo: Diseñar una aplicación que cuente con una arquitectura de microservicios.


## Tecnologías utilizadas 


    Open API
    Flask y connexion
    Mongo db y mlab
    travis-ci


Solución

[ Referencia : https://juanda.gitbooks.io/webapps/content/api/arquitectura-api-rest.html ]

**Qué es una API**

    Es una forma de describir como los programas o los sitios webs intercambian datos.
    El formato de intercambio de datos normalmente es JSON o XML.

**¿Para qué necesitamos una API?**

    Ofrecer datos a aplicaciones que se ejecutan en un movil
    Ofrecer datos a otros desarrolladores con un formato más o menos estándar.
    Ofrecer datos a nuestra propia web/aplicación
    Consumir datos de otras aplicaciones o sitios Web

**Provedores de APIs**

    Algunos ejemplos de sitios web que proveen de APIS son:
        Twitter: acceso a datos de usuarios, estado
        Google: por ejemplo para consumir un mapa de Google
    Pero hay muchos más: Facebook, YouTube, Amazon, foursquare..

**Qué significa API REST**

    REST viene de, REpresentational State Transfer
    Es un tipo de arquitectura de desarrollo web que se apoya totalmente en el estándar HTTP.
    REST se compone de una lista de reglas que se deben cumplir en el diseño de la arquitectura de una API.
    Hablaremos de servicios web restful si cumplen la arquitectura REST.
    Restful = adjetivo, Rest = Nombre


## Como funciona REST

****Llamadas al API

    *Las llamadas al API se implementan como peticiones HTTP, en las que:*
        La URL representa el recurso
		http://www.formandome.es/api/cursos/1

    El método (HTTP Verbs) representa la operación:

GET http://www.formandome.es/api/cursos/1



    El código de estado HTTP representa el resultado:

200 OK HTTP/1.1
404 NOT FOUND HTTP/1.1


****Creación de recursos****

    La URL estará “abierta” (el recurso todavía no existe y por tanto no tiene id)
    El método debe ser POST

http://eventos.com/api/eventos/3/comentarios


****Respuesta a la creación de recursos****

    Resultados posibles:
        403 (Acceso prohibido)
        400 (petición incorrecta, p.ej. falta un campo o su valor no es válido)
        500 (Error del lado del servidor al intentar crear el recurso, p.ej. se ha caído la BD)
        201 (Recurso creado correctamente)
    ¿Qué URL tiene el recurso recién creado?
        La convención en REST es devolverla en la respuesta como valor de la cabecera HTTP Location

****Actualización de recursos****

    Método PUT
        Según la ortodoxia REST, actualizar significaría cambiar TODOS los datos
        PATCH es un nuevo método estándar HTTP (2010) pensado para cambiar solo ciertos datos. Muchos frameworks de programación REST todavía no lo soportan
    Resultados posibles
        Errores ya vistos con POST
        201 (Recurso creado, cuando le pasamos el id deseado al servidor)
        200 (Recurso modificado correctamente)

****Eliminar recursos****

    Método DELETE
    Algunos resultados posibles:
        200 OK
        404 Not found
        500 Server error
    Tras ejecutar el DELETE con éxito, las siguientes peticiones GET a la URL del recurso deberían devolver 404


****HTTP verbs****

    Si realizamos CRUD, debemos utilizar los HTTP verbs de forma adecuada para cuidar la semántica.
        GET: Obtener datos. Ej: GET /v1/empleados/1234
        PUT: Actualizar datos. Ej: PUT /v1/empleados/1234
        POST: Crear un nuevo recurso. Ej: POST /v1/empleados
        DELETE: Borrar el recurso. Ej: DELETE /v1/empleados/1234

****Nombre de los recursos****

    Plural mejor que singular, para lograr uniformidad:
        Obtenemos un listado de clientes: GET /v1/clientes
        Obtenemos un cliente en partícular: GET /v1/clientes/1234
    Url's lo más cortas posibles
    Evita guión y guiones bajos
    Utiliza nombres y no verbos

****Documentación de la API de conformidad con el estándar****

Para el presente trabajo cabe aclarar que se utilizó Python 3.6. De la misma manera, se hizo uso de un Framework más pequeño llamado Flask para realizar el Api.
Para lo anteriormente mencionado se usó el paquete connexion y la especificación de su uso se realiza en el archivo openapi.yaml.

En detalle, **openapi.yaml** tienes los servicios de la api ( los métodos con cada una de sus rutas ) y cada método cuenta con sus respectivas respuestas.

Se utilizó la aplicación con interfaz gráfica que ofrece Swagger para ver más detalladamente la información y esto fue lo que se obtuvo.


****Evidencias de la documentación de la API de conformidad con el estándar****


## [ Imagen de Swagger ]

Evidencia de los métodos http del Swagger UI y la colección de Users

![Alt text](capturas/swagger1.png?raw=true "Swagger")

![Alt text](capturas/swagger2.png?raw=true "Swagger")

Evidencia de lo que muestra Swagger cuando se le oprime al método get.

## [ Imagen de Swagger del Get ]**

![Alt text](capturas/get1.png?raw=true "get")

![Alt text](capturas/get2.png?raw=true "get")

Evidencia de lo que muestra Swagger cuando se le oprime al método post, al de actualizar y al de crear .

## [ Imagen de Swagger del Post ]

![Alt text](capturas/post-crear.png?raw=true "post-crear")

![Alt text](capturas/post-actualizar.png?raw=true "post-actualizar")


Evidencia de lo que muestra Swagger cuando se le oprime al método delete.

## [ Imagen de Swagger del Delete ]

![Alt text](capturas/delete.png?raw=true "post-delete")


****Pruebas de cada servicio con Travis-CI****

[ Referencia de travis CI https://www.federico-toledo.com/travis-ci-para-integracion-continua/ ]

Travis-CI es un sistema de Integración Continua, gratuita para proyectos Open Source y de pago para proyectos privados. Se integra sin problemas con GitHub y automáticamente ejecuta el pipeline definido en cada push o pull requests. Testea y buildea aplicaciones escritas en Ruby, Node, Objective-C, Go, Java, C# y F#, entre otras (que corran en Linux).

Para esto se creo el archivo *travis.yml* en el cual se ingresa la documentación para poder realizar el proceso de pruebas automáticas con travis, se define que el lenguaje utilizado fue python, que no se quiere recibir notificaciones por correo, luego se define también la versión del python que es 3.6, se instala el tox-travis ( se va a utilizar tox con travis ).
-------------------------------------------------------------------------
[ Documentación de Tox ]

[ Referencia de Tox https://mviera.io/blog/automatizando-con-tox/ ]

Tox es un gestor de virtualenvs y una herramienta para realizar tests en linea de comandos. Según su documentación se puede utilizar para:

    Probar que tu paquete se instala correctamente con diferentes versiones de Python.
    Ejecutar los tests de tu proyecto en cada uno de los entornos.
    Integración Continua (CI = Continuous Integration).
------------------------------------------------------------------------- 
Siguiendo con el parcial y el archivo ***travis.yml***, se corre un script que realiza los test.

## Evidencia de las pruebas en travis

![Alt text](capturas/travis1.png?raw=true "Travis")

![Alt text](capturas/travis2.png?raw=true "Travis")

![Alt text](capturas/travis3.png?raw=true "Travis")



##  Archivos fuentes en el repositorio de los microservicios implementados

##[ App ]

	[ __init__.py ] Código de inicialización de Flask

	[ helpers.py ] Toma la url completa y parsea los queries.

	[ openapi.yaml ] Documentación con Swagger

	[ usersData.py ] Lógica de la aplicación. Clase en la que se encuentra la implementación del backend de la api.

--------

##[ Test ]

	[ test_userData.py ] Clase en la cual se prueba los métodos de la api.

-------

##[ travis.yml ] Archivo detallado de travis

##[ config.py ] Archivo en el cual se configura la base de datos ( con el nombre students ) , en este caso mongo.

##[ requierements.txt ] Archivo que define lo que se debe instalar para el proyecto, los requerimientos.

##[ requierements_dev.txt ] Archivo que define lo que se debe instalar para el proyecto en desarrollo, los requerimientos.

##[ run.py ] Archivo donde se inicializa la aplicación y se configuran logs.

##[ tox.init ] Archivo donde está la configuración de tox para las pruebas.

[ deploy.sh ] Script que ejecuta la aplicación.


**** Documentación de las tareas para desplegar los microservicios en una máquina local. ****

Para hacer el despliegue de los servicios en una máquina local se debe seguir el siguiente procedimiento:

1. Instalar las dependencias necesarias para el funcionamiento de la API, debe ubicarse en la raíz del proyecto y ejecutar el siguiente comando:

  pip install -r requirements.txt


2. Se debe correr el script deploy.sh, así que en la carpeta raíz de la aplicación hacer lo siguiente

  sudo /deploy.sh

3. 
    Desde el navegador se ingresa a localhost por el puerto 5000.

![Alt text](capturas/localhost.png?raw=true "Localhost")


##  Evidencias del despliegue 

Para ver un poco de peticios cURL sobre la api, nos direccionaremos a la página de la interfaz gráfica de Swagger, daremos click en uno de los métodos y luego daremos click en Try it out!

## Curl de get

![Alt text](capturas/curl-get.png?raw=true "curl")

## Curl de post para crear

![Alt text](capturas/post-crear.png?raw=true "curl")

## Curl de delete

![Alt text](capturas/curl-delete1.png?raw=true "curl")

![Alt text](capturas/curl-delete2.png?raw=true "curl")


*****Problemas encontrados y las acciones efectuadas para darles solucion******
