const agent = require('superagent')
const statusCode = require('http-status-codes')
const chai = require('chai')
const expect = chai.expect

describe('API test', () => {
  it('Consume GET Service', async () => {
    const response = await agent.get('http://localhost:8080/movies')
    expect(response.status).to.equal(statusCode.OK)
  })
})
