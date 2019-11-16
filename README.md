# Examen 1 - Sistemas Distribuidos

## Integrantes
- Juan David Bolaños - A00077464
- Andrés Zapata - A00077512

## 0. Sobre el proyecto

Este proyecto consta de una aplicación en python que levanta una API Rest cuya documentación tiene conformidad con el estándar OpenAPI, esta API cuenta con diferentes servicios que permiten la gestión de una base de datos de usuarios alojada en un cluster de MongoDB a través de peticiones HTTP.

A continuación se muestra la base de datos y la colección a la que se conectan los servicios de la API.

![Alt text](images/atlas.png?raw=true "MongoDB Atlas DB")

Las peticiones HTTP implementadas por esta API son:

* **GET**: Solicita una representación de un recurso específico
* **POST**: Se utiliza para enviar una entidad a un recurso en específico, causando a menudo un cambio en el estado o efectos secundarios en el servidor
* **DELETE**: Borra un recurso en específico

Los servicios ofrecidos por la API son:

* get_users(): Retorna todos los ususarios mediante una petición GET
* get_user(cc): Retorna el usuario con valor cc igual al pasado por parámetro mediante una petición GET
* insert_user(cc,username): Inserta un usuario con los valores de cc y username pasados por parámetro mediante una petición POST
* delete_user(cc): Borra el usuario con valor cc igual pasado por parámetro mediante una petición DELETE

A continuación se presentan las tareas necesarias para desplegar los microservicios en una máquina local, cada tarea muestra evidencias de los resultados e información detallada de lo que se debe realizar su despliegue y pruebas.

## 1. Preparación proyecto

Este proyecto requiere instalar python 3.7 junto a su manejador de paquetes pip, una vez se tiene instalado, se deben correr los siguientes comandos para instalar las librerías necesarias, las cuales se encuentran en el archivo [requirements.txt](https://github.com/gaearaz/sd-midterm2/blob/master/requirements.txt), para ejecutar la aplicación en localhost por el puerto 5000. 

~~~
    bash
    python3 -m pip install -r requirements.txt
    python3 src/handlers.py
~~~

Si surge un error al ejecutar la API, ejecutar los siguientes comandos que instalan algunas librerías que pueden no haber quedado instaladas adecuadamente debido al interprete de comandos usado.

~~~
    python3 -m pip install pymongo[srv]
    python3 src/handlers.py
~~~

Una vez ejectuado esos comandos se espera ver lo siguiente:

![Alt text](images/python_run.png?raw=true "App running")

## 2. Documentación de la API con OpenAPI

En el archivo [indexer.yaml](https://github.com/gaearaz/sd-midterm2/blob/master/src/openapi/indexer.yaml) se encuentra toda la documentación de la API, en este se declaran todos los paths (end points) de los servicios, los tipos de petición HTTP y sus posibles respuestas, así como la función del archivo [handlers.py](https://github.com/gaearaz/sd-midterm2/blob/master/src/handlers.py) a la que se llama. A continuación se presenta un fragmento del archivo *handlers.py* donde se levanta el servidor mediante **Flask** y **Connexion**.

![Alt text](images/main.png?raw=true "main")

> Todos los servicios de la API mencionados en el punto 0 están detallados y especificados en *indexer.yaml*, además, se implementaron las validaciones necesarias para cada uno de los servicios con sus respectivas excepciones y respuestas HTTP.

Para visualizar todos los servicios que ofrece la API se debe ingresar en un navegador la dirección http://0.0.0.0:5000/ui, una interfaz web ofrecida por OpenAPI, donde se puede observar lo siguiente.

![Alt text](images/swagger_ui.png?raw=true "Swagger UI")

## 3. Conexión con MongoDB

Para la conexión con MongoDB se utilizó la librería pymongo que permite inicializar un MongoClient a través de un string de conexión provisto por MongoDB Atlas en el cual se encuentran el cluster, la base de datos, el usuario y la contraseña, este cliente representa el cluster desde el que se puede acceder a sus base de datos y sus colecciones. A continuación se muesta dicha conexión la cual se encuentra en *handlers.py*.

![Alt text](images/pymongo.png?raw=true "MongoDB Connection from python")

## 4. Implementación de los servicios de la API

A continuación de muestra la información del servicio *get_user(cc)*.

![Alt text](images/get_user.png?raw=true "get_user()")

En la anterior captura se puede observar toda la información que fue definida previamente en *indexer.yaml*, estos son:

* El tipo de petición HTTP (GET)
* El end point del servicio (/users/{cc})
* Los parámetros, que en este caso es solamente *cc* el cual es obligatorio y se encuentra en el path
* Las respuestas posibles del servicio
    * 200: Sucessful Response, lo que quiere decir que se retornó el usuario
    * 400: Bad Request, lo que quiere decir que el parámetro no fue ingresado correctamente
    * 404: Not Found, lo que quiere decir que el usuario con dicha *cc* no fue encontrado
* El Schema, es decir, los atributos respuesta esperados del servicio con sus tipos de datos

Todo lo anterior, es configurado por cada servicio en *handlers.py*

## 5. Evidencias del funcionamiento de los servicios API

Al hacer la petición al servicio, ingresando el valor '123' como *cc* a un documento que existe en la colección de la base de datos, la API responde un 200 y retorna un json que contiene el usuario con toda su información tal como se puede observar en la siguiente captura.

![Alt text](images/get_user_good.png?raw=true "get_user(): 200")

Para la validación de excepciones, se valida que ninguni de los parametros ingresados por el usuario sea una cadena vacía o de solo espacios, al suceder esto, la API responde con un 404 informando que el parametro no debe ser vacío, esto se puede ver a continucación.

![Alt text](images/get_user_error_404.png?raw=true "get_user(): 404")

Por otro lado, si se hace la petición de un usuario que no existe, se retorna un error 400 en la descripción.

![Alt text](images/get_user_error_400.png?raw=true "get_user(): 400")

## 6. Pruebas unitarias con integración contínua}

El orden de las pruebas se hizo pensando en un continuo flujo de transacciones sobre la base de datos para la gestión de los usuarios, así como los tipos de peticiones, de manera que se pudieran evidenciar todas las posibles respuestas de los servicios de la API

![Alt text](images/taverns.png?raw=true "Tavern syntax")

Se utiliza Tavern, un plugin de pytest para volver más fácil la creación y ejecución de los test. El flujo para los test está determinado por el levantamiento del servidor en handlers.py seguido de la ejecución de un script bash que llama a este plugin y que prueba las diferentes peticiones a la API con sus respuestas correspondientes.

Travis instala las dependencias necesarias y ejecuta los test con normalidad, además de que vuelve más natural la manera de diseñar el código de los test

## 7. Problemas encontrados y sus soluciones

* Uno de los primeros problemas encontrados fue al intentar instalar todos los paquetes ya que hubo ciertas librerías que no se instalaban correctamente, al ejectuar el *pip install* se mostraba que todo había quedado instalado satisfactoriamente, sin embargo, cuando se ejecutaba la API esta librería sacaba errores. Este error era debido a que nos encontrabamos usando el interprete de comandos zsh y este no lograba instalar adecuadamente los plugins de ciertas librerías, es por esto, que en las tareas para el despliegue se declara que se debe utilizar el interprete bash.

* Fue un poco complejo establecer la conexión entre python y el cluster en MongoDB Atlas, pese a que la librería pymongo es bastante intuitiva para la conexión con Mongo, es distinto relizarla con una base de datos local a una base de datos alojada en un cluster en la nube. Esto implicó investigación para dicha conexión e instalar nuevos paquetes, fue de gran ayuda el que la plataforma web de MongoDB Atlas brinda el string de conexión para distintos lenguajes.

* Al comienzo no se tenía mucho conocimiento a la hora de manipular un API basado en Open API, se probaron implementaciones basadas en síntaxis pura de Open API y en python y nos quedamos con python. Al tener similitudes con herramientas antes utilizadas se tuvo un plus a la hora de agilizar la producción de resultados, al mismo tiempo que optimizó la gestión de dependencias. 










## Referencias

https://github.com/ICESI/so-microservices-python
https://developer.mozilla.org/es/docs/Web/HTTP/Methods
https://developer.mozilla.org/es/docs/Web/HTTP/Status
https://medium.com/@MicroPyramid/mongodb-crud-operations-with-python-pymongo-a26883af4d09
https://github.com/zalando/connexion
