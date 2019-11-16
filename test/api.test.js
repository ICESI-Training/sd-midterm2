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
