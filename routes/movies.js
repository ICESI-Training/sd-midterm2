const express = require('express')
const router = express.Router()

// Handle incoming GET request to /movies
router.get('/', (req, res, next) => {
  res.status(200).json({
    message: 'Handling GET request to /movies'
  })
})

router.post('/', (req, res, next) => {
  res.status(201).json({
    message: 'Handling POST request to /movies'
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
