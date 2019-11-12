const admin = require('firebase-admin')
const serviceAccount = require('./distribuidos-parcial-firebase-adminsdk-3cv6g-4a8a72776d.json')

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: 'https://distribuidos-parcial.firebaseio.com'
})

const db = admin.database()
const ref = db.ref('distribuidos-parcial')

const usersRef = ref.child('prueba')

const holi = usersRef.set({
  nombre: 'Juanes'
})

module.exports = admin.module('Holi', holi)
