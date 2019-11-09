

# Examen 2 - Sistemas Distribuidos
## Integrantes
- Jesús Paz - A00022240
- William


## Nota:
Para este proyecto se utilizó python 3.7


## 1. Documentación de la API de conformidad con el estándar

Para el desarrollo de este trabajo se utilizó el micro framework llamado Flask. Para el desarrollo de la API se utilizo el paquete llamado connexion (https://connexion.readthedocs.io/en/latest/quickstart.html), de esta manera, lo relacionado con la documentacion se encuentra en el archivo src/swagger.yml. 

En este archivo se definen los servicios que expone la API, junto con la manera en la que se accede correctamente a esta función, de la misma manera se definen las formas en las que puede responder el servidor.

Para ver de una manera grafica esta documentacion lo podemos hacer accediendo al siguiente link (http://apiflask-env.uuhyrnua83.us-east-2.elasticbeanstalk.com/ui/), podemos apreciar lo siguiente:

En esta imagen podemos ver que el servicio se llama Users y que tiene diferentes métodos.

A continuación vamos a proceder a explicar uno de los métodos que se pueden utilizar, en esta API.

En la imagen podemos ver que tenemos muchos datos que son:
* Implementation Notes: Es la descripción de lo que hace el servicio.
* Response Class: Lo que debería responder el servicio
* Model: El modelo que debería retornar el servicio.
* Parameters: Los parámetros que entrar a la consulta.
* Response Messages: Las posibles respuestas que puede dar el servidor, en este caso corresponden a los errores.
* Try it out!: Es un botón, para que funcione correctamente es necesario llenar los parámetros primero. Al pulsarlo se puede ver el resultado de la consulta justo abajo.




## 2.1 Pruebas unitarias de cada microservicio para el proceso de integración contínua. 

Para el proceso de integración continua se utilizó travis y GitHub Actions

### Travis

Se agregó travis al repositorio y se creó un archivo llamado travis.yml, en donde se instalan en python los paquetes necesarios y luego se ejecuta el archivo test/tests.py, en donde se hacen todas las peticiones para probar los servicios de la API desplegada en AWS.

### Actions

De la misma manera, se creó un archivo en donde se aprovisiona python con los paquetes necesarios, posteriormente se ejecuta el archivo test/tests.py.


## 2.2 Evidencia del código pasando dichas pruebas.

En la siguiente imagen se pueden ver como pasan las pruebas en la consola de travis.

En la siguiente imagen se pueden ver como pasan las pruebas en la consola de Actions.


## 3. Archivos fuentes en el repositorio de los microservicios implementados.

## 4.1 Documentación de las tareas para desplegar los microservicios en una máquina local.

Para desplegar los servicios en la máquina local se debe hacer lo siguiente:
  1. Instalar las dependencias necesarias para el funcionamiento de la API, debe ubicarse en la raíz del proyecto y ejecutar el siguiente comando:
  ~~~
    pip install -r src/requirements.txt
  ~~~
  2. Se debe ejecutar el servidor, se realiza de la siguiente manera:
  ~~~
    export mongoURL="mongodb+srv://admin:admin@cluster0-n5sgi.mongodb.net"
    python src/application.py
  ~~~
  3. Desde el navegador se ingresa a [localhost](localhost:5000) por el puerto 5000.
  

## 4.2 Evidencias del despliegue.

## 5. Problemas encontrados y las acciones efectuadas para su solución.

El mayor problema fue desplegar la API en la nube. Para esto intente las siguientes opciones:

1. Heroku: fue mi primer intento ya que tenía ciertos conocimientos sobre esta aplicación. Presente los siguientes problemas:

  * Debía instalar algún tipo de paquete para ejecutar el servidor (gunicorn o wsgi), esto generó problemas. Al final termine utilizando wsgi y desplegar la aplicación en Heroku.

  * b. La aplicación estaba desplegada, pero al momento de hacer la petición de los usuarios, la base de datos (Mongo Atlas) no respondía. Intenté solucionar este error pero no lo logré, por lo tanto migre a AWS.
    
2. AWS: fue la plataforma final de despliegue, pero tuve también muchos problemas. Use Elastic Beanstalk y para python    tiene configurado que el servidor se llame application.py, mientras el mio se llamada app.py. La solución fue buscar tutoriales, ver como ellos desplegaba y les funcionaba y tratar de replicar lo que hacían. La solución fue cambiar los nombres que era necesarios y agregar solo los archivos importantes en un .zip, para posteriormente agregarlo directamente desde la web de AWS.










