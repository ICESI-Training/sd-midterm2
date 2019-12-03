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
            url: 'http://localhost:8082/movies/' + doc._id
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
          url: 'http://localhost:8082/movies/' + result._id
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
          url: 'http://localhost:8082/movies/'
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
        url: 'http://localhost:8082/movies/' + id
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
