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

La dependencia **express** desplegará el framework express. Un framework sobre Node.js que nos permite trabajar con el protocolo HTTP, rutas, etc.

---

### Métodos de petición HTTP 

https://developer.mozilla.org/es/docs/Web/HTTP/Methods

**GET:** solicita una representación de un recurso específico. Las peticiones que usan el método GET sólo deben recuperar datos.

**POST:** se utiliza para enviar una entidad a un recurso específico, causando a menudo un cambio en el estado o efectos secundarios en el servidor.

**DELETE:** borra un recurso específico.

**PATCH:** es utilizado para aplicar modificaciones parciales a un recurso.

***Estos son los métodos HTTP que utilizamos en nuestra API.***

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

app.use(morgan('dev'))
app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())

// Routes which should handle request
app.use('/movies', movieRoutes)

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

Creamos la carpeta **routes** y dentro creamos el archivo **movies.js**. Dentro de este último, añadimos el siguiente contenido:

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

**Nota:** por ahora nos centramos en crear nuestros *endpoints* y verificar que funcionan adecuadamente mostrando simples mensajes.

A continuación, vamos a mostrar el resultado de hacer petición a todos los *endpoints* definidos utilizando **postman**.

![Prueba GET](/images/implementacionBackend/GET.png)

![Prueba GET con ID](/images/implementacionBackend/GETwithID.png)

![Prueba POST](/images/implementacionBackend/POST.png)

![Prueba PATCH](/images/implementacionBackend/PATCH.png)

![Prueba DELETE](/images/implementacionBackend/DELETE.png)

#### Database

Usamos MongoDB Atlas, que básicamente, es MongoDB en la nube.

Instalamos la dependencia **mongoose** ejecutando el siguiente comando por la terminal de Visual Studio Code:

~~~
npm install --save mongoose
~~~

**mongoose** es una especie de ORM (Object-Relational Mapping) que nos provee de métodos y funcionalidades para trabajar de mejor manera con MongoDB.

Creamos una cuenta en MongoDB y proseguimos a crear nuestro clúster de almacenamiento.

Primero: elegimos nuestro proveedor y la región.

![1](/images/database/1.png)

Segundo: le ponemos nombre a nuestro clúster y dejamos los demás parámetros que nos permite la capa gratuita de MongoDB Atlas.

![2](/images/database/2.png)

Tercero: creamos un usuario, en este caso *admin* para poder acceder a la base de datos. Además, configuramos los permisos que iba a tener dicho usuario. La contraseña del usuario la asignamos nostros mismos, pero bien se podría generar automáticamente. 

Creamos el archivo **password.txt** para guardar la contraseña en caso de se nos olvide.

![3](/images/database/3.png)

Como es información confidencial, no se deben subir al repositorio por ningún motivo. Lo que hacemos es agregar el archivo **password.txt** al archivo **.gitignore**, de la siguiente manera.

~~~
## Mongodb Atlas authentication ##
password.txt
~~~

Cuarto: creamos una whitelist, es decir, configuramos quién puede acceder a nuestra base de datos. Lo dejamos todo en 0 para no tener restricciones de acceso con la IP y porque esto es un ejercico de aprendizaje (es decir, no es algo crítico).

![4](/images/database/4.png)

Quinto: para poder conectarse a la base de datos, seleccionamos el lenguaje por el que nos vamos a conectar, su respectiva versión y MongoDB no da una línea servirá para dicho propósito.

![5](/images/database/5.png)

Ahora vamos a la carpeta **api** e ingresamos al archivo **app.js** para añadir el código que nos permitirá conectarnos a la base de datos.

~~~
const mongoose = require('mongoose')

mongoose.connect('mongodb+srv://admin:PASSWORD@clusterparcial2-vrxdh.mongodb.net/test?retryWrites=true&w=majority', { useNewUrlParser: true, useFindAndModify: false, useCreateIndex: true, useUnifiedTopology: true }).then(() => {
  console.log('connection to database establish')
}).catch(err => {
  console.log(err)
  process.exit(-1)
})
~~~

Como mongoose maneja unos esquemas, creamos la carpeta **models** en la raíz del proyecto y dentro creamos el archivo **movies.js**.

~~~
const mongoose = require('mongoose')

const movieSchema = mongoose.Schema({
  _id: mongoose.Schema.Types.ObjectId,
  title: { type: String, required: true },
  release: { type: Number, required: true },
  score: { type: Number, required: true },
  reviewer: { type: String, required: true },
  publication: { type: String, required: true }
})

module.exports = mongoose.model('Movie', movieSchema)
~~~

Este archivo lo que hace es importar la dependencia de **mongoose**, crear un esquema y luego importarlo. El esquema nos permite definir los atributos que tendrá el objeto (*movie*), de qué tipo, si son obligatorios para crear los objeto, entre otras.

Como ya tenemos nuestro esquema de *movies*, nos dirijimos a la carpeta **routes**, ingresamos al archivo **movies.js**. Añadimos el siguiente código para poder usar el esquema anteriormente creado.

~~~
// Database Mongo
const mongoose = require('mongoose')
// Model of mongoose for movies
const Movie = require('../models/movies')
~~~

Paulatinamente vamos agregando el código correspondiente a cada *endpoint* dentro del archivo **/routes/movies.js**.

**GET:** este *endpoint* no requiere de parámetros. Se encarga de buscar todas las películas en la base de datos, pero solo trae los atributos que ponemos dentro del método *select()*. Para hacer la lectura de la respuesta más agradable estructuramos el json para que diga el número total de películas en la base de datos, cada película con sus respectivos atributos y dejamos un request adicional, lo que permite abrir otra pestaña en el postman y agilizar un poco la ejecución de las pruebas, en este caso dejamos el url para hacer una petición *GET* de la película que se desee con su correspondiente *ID*.

~~~
// Handle incoming GET request to /movies
router.get('/', (req, res, next) => {
  // find() method without params find all elements
  Movie.find().select('title release score reviewer publication _id').exec().then(docs => {
    console.log(docs)
    const response = {
      count: docs.length,
      movies: docs.map(doc => {
        return {
          title: doc.title,
          release: doc.release,
          score: doc.score,
          reviewer: doc.reviewer,
          publication: doc.publication,
          _id: doc._id,
          request: {
            type: 'GET',
            url: 'http://localhost:8080/movies/' + doc._id
          }
        }
      })
    }
    if (docs.length > 0) {
      res.status(200).json(response)
    } else {
      res.status(404).json({
        message: 'Database is empty'
      })
    }
  }).catch(err => {
    console.log(err)
    res.status(500).json({ error: err })
  })
})
~~~

**POST:*** este *endpoint* no requiere parámetros, pero si requiere un body. El body es el encargado de pasar los atributos para la nueva película a crear. Una vez se crea, se almacena en la base de datos. Y finalmente responde con un mensaje de satisfacción (sí todo salió bien), el objeto que creó (y almacenó) y un request adicional para poder buscar dicho objeto en la base de datos con su *ID*.

~~~
router.post('/', (req, res, next) => {
  const movie = new Movie({
    _id: new mongoose.Types.ObjectId(),
    title: req.body.title,
    release: req.body.release,
    score: req.body.score,
    reviewer: req.body.reviewer,
    publication: req.body.publication
  })
  // save() method is for save the object in the database
  // then() is a promise
  movie.save().then(result => {
    console.log(result)
    // response
    res.status(201).json({
      message: 'Created movie successfully',
      createdMovie: {
        title: result.title,
        release: result.release,
        score: result.score,
        reviewer: result.reviewer,
        publication: result.publication,
        _id: result._id,
        request: {
          type: 'GET',
          url: 'http://localhost:8080/movies/' + result._id
        }
      }
    })
  }).catch(err => {
    console.log(err)
    res.status(500).json({ error: err })
  })
})
~~~

**GET con ID:** este *endpoint* requiere un parámetro, el ID de la película que se desea buscar en la base de datos. Retorna la película buscada.

~~~
router.get('/:movieID', (req, res, next) => {
  const id = req.params.movieID
  Movie.findById(id).select('title release score reviewer publication _id').exec().then(doc => {
    console.log('From database', doc)
    // if doc NOT null response 200, else 404
    if (doc) {
      res.status(200).json({
        movie: doc,
        request: {
          type: 'GET',
          url: 'http://localhost:8080/movies/'
        }
      })
    } else {
      res.status(404).json({ message: 'No valid entry found for provided ID' })
    }
  }).catch(err => {
    console.log(err)
    res.status(500).json({ error: err })
  })
  // 200: found id.
  // 404: invalid id.
  // 500: invalid object id.
})
~~~

**PATCH:** este *endpoint* requiere un parámetro, el ID de la película que se desea modificar y un body. El body es un *Array* de atributos de la película, es decir, se puede modificar desde *1* atributo hasta *n* atributos. Retorna un mensaje de satisfacción (sí todo salió bien) y un request adicional por si se quiere buscar dicha película y verificar los cambios.

~~~
router.patch('/:movieID', (req, res, next) => {
  const id = req.params.movieID
  // $set is by mongoose. Its not and arbitrary name
  // Movie.update({ _id: id }, { $set: { name: req.body.newName, price: req.body.newPrice } })
  // In this example: mongoose asume that we will pass both params to be change
  const updateOps = {}
  for (const ops of req.body) {
    updateOps[ops.propName] = ops.value
  }
  Movie.update({ _id: id }, { $set: updateOps }).exec().then(result => {
    console.log(result)
    res.status(200).json({
      message: 'Updated movie successfully',
      request: {
        type: 'GET',
        url: 'http://localhost:8080/movies/' + id
      }
    })
  }).catch(err => {
    console.log(err)
    res.status(404).json({
      error: err
    })
  })
})
~~~

**DELETE:** este *endpoint* requiere un parámetro, el ID de la película que se desea eliminar de la base de datos. Retorna un mensaje de satisfacción (sí todo salió bien) y un request adicional que permite crear una nueva película, en caso de ser necesario, y un objeto con los atributos de una película y de qué tipo son.

~~~
router.delete('/:movieID', (req, res, next) => {
  const id = req.params.movieID
  Movie.remove({ _id: id }).exec().then(result => {
    res.status(200).json({
      message: 'Movie deleted',
      request: {
        type: 'POST',
        url: 'http://localhost:8080/movies/',
        body: {
          title: 'String',
          release: 'Number',
          score: 'Number',
          reviewer: 'String',
          publication: 'String'
        }
      }
    })
  }).catch(err => {
    console.log(err)
    res.status(500).json({
      error: err
    })
  })
})
~~~

La documentación estricta se realizó en OpenApi versión 3, la cual se puede acceder por medio del siguiente link:

https://app.swaggerhub.com/apis/CristianMoralesLopez/sd-midterm2/1.0.0#/developers/buscarTodasLasPeliculas

Adicionalmente se puede observar el archivo *.yaml* en la carpeta **openapi3**, que se encuentra ubicada en la raíz del proyecto.

El código completo de **/routes/movies.js** queda de la siguiente manera:

~~~
const express = require('express')
const router = express.Router()
// Database Mongo
const mongoose = require('mongoose')
// Model of mongoose for movies
const Movie = require('../models/movies')

// Handle incoming GET request to /movies
router.get('/', (req, res, next) => {
  // find() method without params find all elements
  Movie.find().select('title release score reviewer publication _id').exec().then(docs => {
    console.log(docs)
    const response = {
      count: docs.length,
      movies: docs.map(doc => {
        return {
          title: doc.title,
          release: doc.release,
          score: doc.score,
          reviewer: doc.reviewer,
          publication: doc.publication,
          _id: doc._id,
          request: {
            type: 'GET',
            url: 'http://localhost:8080/movies/' + doc._id
          }
        }
      })
    }
    if (docs.length > 0) {
      res.status(200).json(response)
    } else {
      res.status(404).json({
        message: 'Database is empty'
      })
    }
  }).catch(err => {
    console.log(err)
    res.status(500).json({ error: err })
  })
})

router.post('/', (req, res, next) => {
  const movie = new Movie({
    _id: new mongoose.Types.ObjectId(),
    title: req.body.title,
    release: req.body.release,
    score: req.body.score,
    reviewer: req.body.reviewer,
    publication: req.body.publication
  })
  // save() method is for save the object in the database
  // then() is a promise
  movie.save().then(result => {
    console.log(result)
    // response
    res.status(201).json({
      message: 'Created movie successfully',
      createdMovie: {
        title: result.title,
        release: result.release,
        score: result.score,
        reviewer: result.reviewer,
        publication: result.publication,
        _id: result._id,
        request: {
          type: 'GET',
          url: 'http://localhost:8080/movies/' + result._id
        }
      }
    })
  }).catch(err => {
    console.log(err)
    res.status(500).json({ error: err })
  })
})

router.get('/:movieID', (req, res, next) => {
  const id = req.params.movieID
  Movie.findById(id).select('title release score reviewer publication _id').exec().then(doc => {
    console.log('From database', doc)
    // if doc NOT null response 200, else 404
    if (doc) {
      res.status(200).json({
        movie: doc,
        request: {
          type: 'GET',
          url: 'http://localhost:8080/movies/'
        }
      })
    } else {
      res.status(404).json({ message: 'No valid entry found for provided ID' })
    }
  }).catch(err => {
    console.log(err)
    res.status(500).json({ error: err })
  })
  // 200: found id.
  // 404: invalid id.
  // 500: invalid object id.
})

router.patch('/:movieID', (req, res, next) => {
  const id = req.params.movieID
  // $set is by mongoose. Its not and arbitrary name
  // Movie.update({ _id: id }, { $set: { name: req.body.newName, price: req.body.newPrice } })
  // In this example: mongoose asume that we will pass both params to be change
  const updateOps = {}
  for (const ops of req.body) {
    updateOps[ops.propName] = ops.value
  }
  Movie.update({ _id: id }, { $set: updateOps }).exec().then(result => {
    console.log(result)
    res.status(200).json({
      message: 'Updated movie successfully',
      request: {
        type: 'GET',
        url: 'http://localhost:8080/movies/' + id
      }
    })
  }).catch(err => {
    console.log(err)
    res.status(404).json({
      error: err
    })
  })
})

router.delete('/:movieID', (req, res, next) => {
  const id = req.params.movieID
  Movie.remove({ _id: id }).exec().then(result => {
    res.status(200).json({
      message: 'Movie deleted',
      request: {
        type: 'POST',
        url: 'http://localhost:8080/movies/',
        body: {
          title: 'String',
          release: 'Number',
          score: 'Number',
          reviewer: 'String',
          publication: 'String'
        }
      }
    })
  }).catch(err => {
    console.log(err)
    res.status(500).json({
      error: err
    })
  })
})

module.exports = router
~~~

A continuación, mostraremos una pequeña prueba utilizando **postman**. Las pruebas más profundas se explican en la sección de pruebas unitarias.

Ejecutamos el proyecto con el siguiente comando:

~~~
npm start
~~~

Abrimos **postman** y empezamos!

![1](/images/postman/1.png)

Ejecutamos el método GET (sin parámetro), teniendo en cuenta que la base de datos esta vacía. El status de respuesta es 200 y el body muestra el número de películas que hay en la base de datos y los respectivos objetos película. 

![2](/images/postman/2.png)

Ejecutamos el método POST. Lo que hacemos es agregar una película, para lo cual envíamos un body con sus respectivos 5 parámetros: *title*, *release*, *score*, *review* y *publication*. En caso, de que omitamos alguno, tendremos un mensaje de respuesta erróneo y esto se debe a la configuración que le dimos al Schema de mongoose.

![3](/images/postman/3.png)
![4](/images/postman/4.png)

Ejecutamos el método GET con el ID de la película que creamos para validar que efectivamente se guardó en la base de datos.

![5](/images/postman/5.png)

Ejecutamos el método GET (sin parámetro) como segunda validación de que efectivamente se guardó en la base de datos.

![6](/images/postman/6.png)

Ejecutamos el método PATH con el ID de la película que queramos modificarle uno o más atributos, en este caso solo cambiamos uno (*title*).

![7](/images/postman/7.png)

Ejecutamos el método GET con el ID de la película que modificamos para validar que efectivamente se realizaron los cambios en la base de datos.

![8](/images/postman/8.png)

Ejecutamos el método DELETE para eliminar la película con el ID que pasamos por parámetro.

![9](/images/postman/9.png)

Ejecutamos el método GET (sin parámetro) para validar que se realizó la eliminación de la película de la base de datos.

![10](/images/postman/10.png)

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

Creamos la carpeta **test** en la raíz del proyecto y dentro el archivo **api.test.js** con el siguiente contenido:

~~~
const agent = require('superagent')
const statusCode = require('http-status-codes')
const chai = require('chai')
const { expect } = chai

describe('GET | success', () => {
  it('success', async () => {
    const response = await agent.get('http://localhost:8080/movies/')
    expect(response.status).to.equal(statusCode.OK)
  })
})

describe('GET | not found', () => {
  it('not found', async () => {
    const response = await agent.get('http://localhost:8080/movies/')
    if (response.body.count.length === 0) {
      expect(response.status).to.equal(statusCode.NOT_FOUND)
    }
  })
})

describe('GET with ID | success', async () => {
  it('success', async () => {
    const response = await agent.get('http://localhost:8080/movies/5dcf2e450b0afa342c1d8fa6')
    expect(response.status).to.equal(statusCode.OK)
  })
})

describe('GET with ID | error', async () => {
  it('error', async () => {
    await agent.get('http://localhost:8080/movies/5dcf2e450b0afa342').then().catch(
      (response) => {
        expect(response.status).to.equal(statusCode.INTERNAL_SERVER_ERROR)
      }
    )
  })
})

describe('POST | success', () => {
  it('success', async () => {
    const query = {
      title: 'Doctor Strange',
      release: 2016,
      score: 9,
      reviewer: 'Anthony Miller',
      publication: 'ComicBookHero.com'
    }

    const response = await agent.post('http://localhost:8080/movies/').send(query)
    expect(response.status).to.equal(statusCode.CREATED)
  })
})

describe('POST | error', () => {
  it('error', async () => {
    const query = {
      title: 'Doctor Strange',
      release: '2016',
      score: '9',
      reviewer: 'Anthony Miller',
      publication: 'ComicBookHero.com'
    }

    await agent.post('http://localhost:8080/movies/5dcf2e450b0afa342c1d8fa6').send(query).then().catch(
      (response) => {
        expect(response.status).to.equal(statusCode.NOT_FOUND)
      }
    )
  })
})

describe('PATCH | success', () => {
  it('success', async () => {
    const query = [
      { propName: 'title', value: 'IT' }
    ]

    const response = await agent.patch('http://localhost:8080/movies/5dcf2e450b0afa342c1d8fa6').send(query)
    expect(response.status).to.equal(statusCode.OK)
  })
})

describe('PATCH | error', () => {
  it('error', async () => {
    const query = {
      propName: 'title',
      value: 'IT'
    }

    await agent.patch('http://localhost:8080/movies/5dcf2e450b0afa342c1d8fa6').send(query).then().catch(
      (response) => {
        expect(response.status).to.equal(statusCode.INTERNAL_SERVER_ERROR)
      }
    )
  })
})

describe('DELETE | success', () => {
  it('success', async () => {
    const response = await agent.delete('http://localhost:8080/movies/5dcf300d0b0afa342c1d8fa9')
    expect(response.status).to.equal(statusCode.OK)
  })
})

describe('DELETE | error', () => {
  it('error', async () => {
    await agent.delete('http://localhost:8080/movies/5dcf300d0b0a').then().catch(
      (response) => {
        expect(response.status).to.equal(statusCode.INTERNAL_SERVER_ERROR)
      }
    )
  })
})
~~~

Dicho código lo que hace es importar las dependencias explicada y necesarias, y después probar cada *endpoint* como se definió en ***openapi***.

Vamos al archivo **package.json**, buscamos el objeto **scripts** (en nuestro caso ubicado en la línea 6), dentro buscamos el objeto **test** (en nuestro caso ubicado en la línea 7) y agregamos a su contenido *-t 5000*.

Debería quedarnos así:

~~~
"scripts":{
    "test": "mocha -t 5000"
}
~~~

Para ejecutar las pruebas unitarias sobre nuestra API, utilizamos el siguiente comando en la terminal de Visual Studio Code:

~~~
npm test
~~~

---

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

![1](/images/reportes/1.png)

![2](/images/reportes/2.png)

![3](/images/reportes/3.png)

![4](/images/reportes/4.png)
 
 **Nota:** para que las pruebas se ejecuten, debe estar desplegado el proyecto.
 
 **Nota2:** la carpeta que contiene el html del reporte quedó en el **.gitignore** y por ende, no se puede ver.

---

### Despliegue

Para desplegar nuestra API ejecutamos el siguiente comando en la terminal de Visual Studio Code:

~~~
npm start
~~~

Por debajo lo que se ejecuta es el comando:

~~~
nodemon ./api/server.js
~~~

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
script:
  - node ./api/server.js &
  - sleep 5000
  - npm test
~~~

Básicamente copiamos el archivo **.travis.yml** de un taller que hicimos con PSL (el repositorio se encuentra entre nuestras referencias). Le añadimos la sección de script porque travis, al igual que nosotros a nivel local, el travis no puede correr las pruebas sin desplegar el backend.

Habilitamos Travis en el repositorio.

![1](/images/travis/1.png)

Lo siguiente es verificar que la ejecución en Travis termine correctamente.

![2](/images/travis/2.png)

![3](/images/travis/3.png)

A pesar de que funcionaron tanto las pruebas con postman como las pruebas unitarias, el travis no logró funcionar.

---

### Tareas de integración

Como no manejabamos las tecnologías, nos íbamos turnando en cada una de las etapas que describimos (programación peer to peer). Entonces se puede decir que ambos integrantes hicimos algo de cada fase.

---

### Problemas encontrados

1. Cuando olvidabamos poner *module.exports = <componente>* se generaba un error en el archivo *.js* que esta haciendo una importación de dicho componente.

2. En la conexión con la base de datos tuvimos varios problemas. ***Primero:*** planteamos utilizar Firebase como nuestra base de datos, pero nos estaba costando bastante trabajo. Al utilizar Mongodb Atlas se nos facilitó bastante avanzar dado que es bastante intuitiva. ***Segundo:*** no estabamos creando una variable de entorno con la contraseña, por ende, decía que no entraba la variable. ***Tercero:*** el tutorial con el que nos ayudamos tenía una versión vieja de mongoose: entonces la línea de código encargada de hacer la conexión tiraba error y decía que estaba deprecated.

3. No pudimos hacer que el travis diera exitosamente, pese a las pruebas con el postman funcionarán y también las pruebas unitarias. Tuvimos que lidiar con varios problemas, entre ellos: (1) tiraba error por la función lambda que escribía por consola si la conexión a la base de datos había sido exitosa y (2) diferentes problemas de la carpeta **node_modules** que es la que se crea cuando se inicializa el proyecto, después de intentar una y otra vez, no pudimos.

---

### Referencias

https://scotch.io/tutorials/building-and-securing-a-modern-backend-api

https://github.com/holgiosalos/workshop-api-testing-js/

https://developer.mozilla.org/es/docs/Web/HTTP/Methods

https://victorroblesweb.es/2018/01/02/instalar-dependencias-con-npm-api-restful-nodejs/

https://www.paradigmadigital.com/dev/testeando-javascript-mocha-chai/

https://www.youtube.com/watch?v=0oXYLzuucwE&list=PL55RiY5tL51q4D-B63KBnygU6opNPFk_q&index=1
