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
