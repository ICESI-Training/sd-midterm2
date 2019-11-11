const express = require('express')
const app = express()
const morgan = require('morgan')

const movieRoutes = require('../routes/movies')
const reviewRoutes = require('../routes/reviewers')
const publicationRoutes = require('../routes/publications')

app.use(morgan('dev'))

// Routes which should handle request
app.use('/movies', movieRoutes)
app.use('/reviewers', reviewRoutes)
app.use('/publications', publicationRoutes)

module.exports = app
