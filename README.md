# Exam 2

## Description

**Universidad ICESI**  
**Course:** Distributed systems  
**Teacher:** Juan M Álvarez Q.  
**Topic:** Microservices Architecture design  
**email:** juan.alvarez8 at correo.icesi.edu.co

### Learning goals
* Design a microservices architecture application

### Suggested technologies for the midterm development
* [Open API](https://openapi.tools/)
* Github repository
* Flask and [connexion](https://connexion.readthedocs.io/en/latest/)
* Mongo db and [mlab](https://mlab.com/)
* [travis-ci](https://travis-ci.org/)

### Description

For this exam you should redesing the application developed in midterm 1 into a REST-based microservices arquitecture. Your aplication must comply the following:

* Must have a Github repository which is a fork of the **[sd-mdterm2](https://github.com/ICESI-Training/sd-midterm2)** repository.
* It is suggested to use mlab for data storage: mlab is a database as a service provider for mongo databases.
* The system must accept HTTP requests from CURL (you can use other REST clients like postman, insomnia or postwoman).
* The application must have an endpoint to insert data in the database.
* The application must have an endpoint to retrieve all the registers from a database collection or table.
* The design must have continous integration unit tests for all microservices.


### Actividades (EN español para evitar ambigüedades)
1. Documento README.md en formato markdown:  
  * Formato markdown (5%).
  * Nombre y código del estudiante (5%).
  * Ortografía y redacción (5%).
2. Documentación de la API de conformidad con el estándar [OpenAPI](https://github.com/OAI/OpenAPI-Specification). (15%)
3. Pruebas unitarias de cada microservicio ara el proceso de integración contínua (10%). Evidencia del código pasando dichas pruebas(5%).
4. Archivos fuentes en el repositorio de los microservicios implementados (15%).
5. Documentación de las tareas para desplegar los microservicios en una máquina local (10%). Evidencias del despliegue (peticiones cURL o similares)(10%).
6. El informe debe publicarse en un repositorio de github el cual debe ser un fork de https://github.com/ICESI-Training/sd-midterm2 y para la entrega deberá hacer un Pull Request (PR) al upstream (10%). Tenga en cuenta que el repositorio debe contener todos los archivos necesarios para el despliegue.
7. Documente algunos de los problemas encontrados y las acciones efectuadas para su solución (10%).

---

## Desarrollo

### Equipo de trabajo:
* Cristian Alejandro Morales López - A00328064
* Juan Esteban Quinayás Gaitán - A00027548

### Inicialización

Lo primero que hacemos es un **fork** al repositorio de Github **sd-midterm2**. Dicho repositorio cuenta con tres archivos: .gitignore, LICENSE y README.md (vacío).

A continuación, editamos el archivo **.gitignore** que se encuentra en la raíz del proyecto. Para ello, ingresamos a la página https://www.gitignore.io/ y en el área de texto agregamos el sistema operativo (Windows), IDE's (Visual Studio Code) y el lenguaje (NodeJS). Damos clic en **Create** para generar el archivo. Una vez creado, lo copiamos y lo anexamos dentro del archivo .gitignore.

Creamos la carpeta **api** en la raíz del proyecto.

Inicializamos el proyecto ejecutando el siguiente comando en la terminal de Visual Studio Code:

~~~
npm init
~~~

Después de ejecutarlo aparecen una serie de campos que dejamos en default, excepto por el campo *description* que le pusimos *Parcial 2 - Distribuidos*. Al finalizar se habrá configurado el archivo **package.json**, se habrá creado el archivo **package-lock.json** y se habrá creado el directorio **node_modules**.

Antes de escribir cualquier línea de código, instalamos y guardamos las dependencias que vamos a utilizar. Con ese fin, ejecutamos el siguiente comando por la terminal de Visual Studio Code:

~~~
npm install express express-jwt auth0-api-jwt-rsa-validation --save
~~~

La dependencia **express** desplegará el framework express, la librería **express-jwt** nos dará funciones para trabajar con Web Tokens JSON, y finalmente la validación **auth0-api-jwt-rsa** proporcionará una función de ayuda para obtener nuestra clave secreta.

### Métodos de petición HTTP 

https://developer.mozilla.org/es/docs/Web/HTTP/Methods

**GET:** solicita una representación de un recurso específico. Las peticiones que usan el método GET sólo deben recuperar datos.

**HEAD:** pide una respuesta idéntica a la de una petición GET, pero sin el cuerpo de la respuesta.

**POST:** se utiliza para enviar una entidad a un recurso específico, causando a menudo un cambio en el estado o efectos secundarios en el servidor.

**PUT** reemplaza todas las representaciones actuales del recurso de destino con la carga útil de la petición.

**DELETE** borra un recurso específico.

**PATCH** es utilizado para aplicar modificaciones parciales a un recurso.

### Implementación

#### Backend

Creamos el archivo **server.js** en la raíz del proyecto.

~~~
// Insertar código aquí después de entender cómo funciona
~~~

#### Database

### Pruebas unitarias

BLA

### Despliegue

Para desplegar nuestra API ejecutamos el siguiente comando en la terminal de Visual Studio Code:

~~~
node server
~~~

Después abrimos el navegador web de nuestra preferencia y accedemos al siguiente endpoint:

~~~
localhost:8080/movies
~~~

Como resultado obtendremos el siguiente JSON con la lista de reseñas de películas y sus datos asociados.

---

### Referencias

https://scotch.io/tutorials/building-and-securing-a-modern-backend-api

https://developer.mozilla.org/es/docs/Web/HTTP/Methods
