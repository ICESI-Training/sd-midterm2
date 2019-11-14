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

---

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

---

### Métodos de petición HTTP 

https://developer.mozilla.org/es/docs/Web/HTTP/Methods

**GET:** solicita una representación de un recurso específico. Las peticiones que usan el método GET sólo deben recuperar datos.

**POST:** se utiliza para enviar una entidad a un recurso específico, causando a menudo un cambio en el estado o efectos secundarios en el servidor.

**DELETE:** borra un recurso específico.

**PATCH:** es utilizado para aplicar modificaciones parciales a un recurso.

***Estos son los métodos HTTP que utilizaremos en nuestra API.***

---

### Implementación

#### Backend

Vamos a instalar las dependencias **nodemon**, **morgan** y **body-parser**.

Para instalar **nodemon**, dependencia de desarollo, ejecutamos el siguiente comando en la terminal de Visual Studio Code:

~~~
npm install --save-dev nodemon
~~~

**nodemon** un monitor de cambios en nuestro código que nos recarga el servidor cada vez que hacemos algún cambio.

Dado que el comando *nodemon* no va a ser reconocido, nos dirigimos al archivo **package.json**, buscamos el objeto **scripts** (en nuestro caso ubicado en la línea 6), abajo del objeto **test** (en nuestro caso ubicado en la línea 7) y agregamos el objeto **start** con el contenido *nodemon ./api/server.js*.

Debería quedar así:

~~~
"scripts":{
    "test": "...",
    "start": "nodemon ./api/server.js"
}
~~~

Cabe resaltar que por el momento no le pusimos cuidado al contenido de **test**, por eso le pusimos tres puntos. 

Para instalar **morgan** ejecutamos el siguiente comando en la terminal de Visual Studio Code:

~~~
npm install --save morgan
~~~

**morgan** middleware del logger de petición HTTP para node.js. Básicamente, imprime por consola las peticiones que hacen al servidor con su estatus correspondiente.

Para instalar **body-parser** ejecutamos el siguiente comando en la terminal de Visual Studio Code:

~~~
npm install --save body-parser
~~~

**body-parser** nos permite convertir los datos que nos lleguen en las peticiones al servidor en objetos json.

Creamos la carpeta **api** y dentro creamos dos archivos: **app.js** y **server.js**.

Dentro del archivo **app.js** añadimos el siguiente contenido:

~~~
const express = require('express')
const app = express()
const morgan = require('morgan')
const bodyParser = require('body-parser')

const movieRoutes = require('../routes/movies')
const reviewRoutes = require('../routes/reviewers')
const publicationRoutes = require('../routes/publications')

app.use(morgan('dev'))
app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())

// Routes which should handle request
app.use('/movies', movieRoutes)
app.use('/reviewers', reviewRoutes)
app.use('/publications', publicationRoutes)

module.exports = app
~~~

Primero, importamos las dependencias. Segundo, inicializamos los archivos (*los crearemos más adelante*) que contienen los *endpoints* de nuestra API. Tercero, ponemos unos parámetros para que las dependencias funcionen. Cuarto, inicializamos las rutas que manejarán las solicitudes. Y finalmente, exportamos la variable *app* para ser utilizada en otro modulo que la requiera.

Dentro del archivo **server.js** añadimos el siguiente contenido:

~~~
const http = require('http')
const app = require('./app')
const port = 8080

const server = http.createServer(app)

server.listen(port)
~~~

Lo que estamos haciendo es poner a correr el servidor de nuestra API, para lo cual inicializamos la aplicación (archivo **app.js**), asignamos la dirección IP (en este caso, la opción default que es *localhost*) sobre la que va a correr y asignamos el puerto (*8080*) por el que va a escuchar.

Creamos la carpeta **routes** y dentro creamos tres archivos: **movies.js**, **reviewers.js** y **publications.js*.

Dentro del archivo **movies.js** añadimos el siguiente contenido:

~~~
const express = require('express')
const router = express.Router()

// Handle incoming GET request to /movies
router.get('/', (req, res, next) => {
  res.status(200).json({
    message: 'Handling GET request to /movies'
  })
})

router.post('/', (req, res, next) => {
  const movie = {
    name: req.body.name,
    price: req.body.price
  }
  res.status(201).json({
    message: 'Handling POST request to /movies',
    createdMovie: movie
  })
})

router.get('/:movieID', (req, res, next) => {
  const id = req.params.movieID
  if (id === 'holi') {
    res.status(200).json({
      message: 'You discovered the holi ID'
    })
  } else {
    res.status(200).json({
      message: 'You passed an ID'
    })
  }
})

router.patch('/:movieID', (req, res, next) => {
  res.status(200).json({
    message: 'Updated movie!'
  })
})

router.delete('/:movieID', (req, res, next) => {
  res.status(200).json({
    message: 'Deleted movie!'
  })
})

module.exports = router
~~~

Lo que hicimos fue crear todos los *endpoint* que definimos en un principio, es decir: GET, POST, PATCH y DELETE. Y como contenido agregamos unos mensajes para hacer la prueba.

Dentro del archivo **reviewers.js** añadimos el mismo contenido de **movies.js**, cambiando *movies* por *reviewers*.

Dentro del archivo **publications.js** añadimos el mismo contenido de **movies.js**, cambiando *movies* por *publications*.

**Nota:** por ahora nos centramos en crear nuestros *endpoints* y verificar que funcionan adecuadamente mostrando simples mensajes.

A continuación, vamos a mostrar el resultado de hacer petición a todos los *endpoints* definidos utilizando **postman**.

![Prueba GET](/images/implementacionBackend/GET.png)

![Prueba GET con ID](/images/implementacionBackend/GETwithID.png)

![Prueba POST](/images/implementacionBackend/POST.png)

![Prueba PATCH](/images/implementacionBackend/PATCH.png)

![Prueba DELETE](/images/implementacionBackend/DELETE.png)

#### Database

Usamos Mongodb Atlas, que básicamente, es mongodb en la nube.

Instalamos la dependencia **mongoose** ejecutando el siguiente comando por la terminal de Visual Studio Code:

~~~
npm install --save mongoose
~~~

**password.txt** para la contraseña

Como es información confidencial, no se deben subir al repositorio por ningún motivo. Lo que hacemos es agregar el archivo **password.txt** al archivo **.gitignore**, de la siguiente manera.

~~~
## Mongodb Atlas authentication ##
password.txt
password.json
~~~

Vamos a la carpeta **api** e ingresamos al archivo **app.js**.

~~~
const mongoose = require('mongoose')

mongoose.connect('mongodb+srv://admin:PASSWORD@clusterparcial2-vrxdh.mongodb.net/test?retryWrites=true&w=majority', { useNewUrlParser: true, useFindAndModify: false, useCreateIndex: true, useUnifiedTopology: true }).then(() => {
  console.log('connection to database establish')
}).catch(err => {
  console.log(err)
  process.exit(-1)
})
~~~

Mongo (maybe mongoose) manera models..
Creamos la carpeta **models** en la raíz del proyecto y dentro creamos el archivo **movies.js**.

~~~
<código>
~~~

En la carpeta **routes**, ingresamos al archivo **movies.js**.

~~~
const mongoose = require('mongoose')
const Movie = require('../models/movies')
~~~

<Hacer una descripción de cada método y poner el código>

<Poner el código completo>

<Insertar imágenes de postman>

---

### Pruebas unitarias

Instalamos las dependencias de desarrollo **mocha** y **chai**.

~~~
npm install --save-dev mocha chai
~~~

**mocha** es un framework de pruebas de JavaScript que se ejecuta en NodeJS. Nos da la posibilidad de crear tanto tests síncronos como asíncronos de una forma muy sencilla. Nos proporciona muchas utilidades para la ejecución y el reporte de los tests.

**chai** es una librería de aserciones, la cual se puede emparejar con cualquier marco de pruebas de Javascript. Chai tiene varias interfaces: assert, expect y should, que permite al desarrollador elegir el estilo que le resulte más legible y cómodo a la hora de desarrollar sus tests.

Instalamos la dependencia de desarrollo **http-status-codes**.

~~~
npm install --save-dev http-status-codes
~~~

**http-status-codes** es una librería que contiene un enumerador de los principales códigos de respuesta de los métodos HTTP.

Instalamos las dependencias **superagent** y **superagent-promise**.

~~~
npm install --save superagent superagent-promise
~~~

**superagent** es una librería cliente. Es usada principalmente para hacer peticiones AJAX en el navegador, pero también trabaja en NodeJS.

Para ejecutar las pruebas unitarias sobre nuestra API, utilizamos el siguiente comando en la terminal de Visual Studio Code:

~~~
npm test
~~~

---

### Despliegue

Para desplegar nuestra API ejecutamos el siguiente comando en la terminal de Visual Studio Code:

~~~
npm start
~~~

Después abrimos el navegador web de nuestra preferencia y accedemos al siguiente endpoint:

~~~
localhost:8080/movies
~~~

Como resultado obtendremos el siguiente JSON con la lista de reseñas de películas y sus datos asociados.

---

### Integración Continua

Creamos el archivo **.travis.yml** en la raíz del proyecto.

Dentro de dicho archivo agregamos el siguiente contenido:

~~~
language: node_js
cache:
directories:
- node_modules
notifications:
email: false
branches:
except:
- "/^v\\d+\\.\\d+\\.\\d+$/"
~~~

Habilitamos Travis en el repositorio

<Insertar imagen>

Vamos al archivo **package.json**, buscamos el objeto **scripts** (en nuestro caso ubicado en la línea 6), dentro buscamos el objeto **test** (en nuestro caso ubicado en la línea 7) y agregamos a su contenido *-t 5000*.

Debería quedarnos así:

~~~
"scripts":{
    "test": "mocha -t 5000"
}
~~~

Lo siguiente es verificar que la ejecución en Travis termine correctamente.

<Siento que falta algo, verificar sobre la marcha>

#### Reporte de pruebas

Adicionalmente, quisimos generar un reporte con interfaz gráfica (reporte HTML) para ver los resultados de las pruebas de una forma más amena.

Primero, instalamos la dependencia de desarrollo **mochawesome**.

~~~
npm install --save mochawesome
~~~

Segundo, vamos al archivo **package.json**, buscamos el objeto **scripts**, dentro buscamos el objeto **test** y agregamos a su contenido *--reporter mochawesome --reporter-options reportDir=report,reportFilename=ApiTesting*.

Debería quedarnos así:

~~~
"scripts": {
    "test": "mocha -t 5000 --reporter mochawesome --reporter-options reportDir=report,reportFilename=ApiTesting"
}
~~~

Tercero, agregamos las siguientes líneas dentro del archivo **.gitignore**:

~~~
## Reports ##
report
~~~

Para que se genere el reporte es necesario correr las pruebas, es decir, ejecutar el siguiente comando por la terminal de Visual Studio Code:

~~~
npm test
~~~

Se creará automáticamente una carpeta **report** con el reporte HTML. Para visualizarlo basta con copiar la ruta (terminada en **.html**) que sale en la consola, como por ejemplo: *D:\JUANES\9no Semestre\Distribuidos\sd-midterm2\report\ApiTesting.html*, y pegarla en el navegador.

<Insertar imagen>

---

### Problemas encontrados

1. Cuando olvidabamos poner *module.exports = <componente>* se generaba un error en el archivo *.js* que esta haciendo una importación de dicho componente.

2. En la conexión con la base de datos tuvimos varios problemas. ***Primero:*** planteamos utilizar Firebase como nuestra base de datos, pero nos estaba costando bastante trabajo. Al utilizar Mongodb Atlas se nos facilitó bastante avanzar dado que es bastante intuitiva. ***Segundo:*** no estabamos creando una variable de entorno con la contraseña, por ende, decía que no entraba la variable. ***Tercero:*** el tutorial con el que nos ayudamos tenía una versión vieja de mongoose: entonces la línea de código encargada de hacer la conexión tiraba error y decía que estaba deprecated.

---

### Referencias

https://scotch.io/tutorials/building-and-securing-a-modern-backend-api

https://github.com/holgiosalos/workshop-api-testing-js/

https://developer.mozilla.org/es/docs/Web/HTTP/Methods

https://victorroblesweb.es/2018/01/02/instalar-dependencias-con-npm-api-restful-nodejs/

https://www.paradigmadigital.com/dev/testeando-javascript-mocha-chai/

https://www.youtube.com/watch?v=0oXYLzuucwE&list=PL55RiY5tL51q4D-B63KBnygU6opNPFk_q&index=1
