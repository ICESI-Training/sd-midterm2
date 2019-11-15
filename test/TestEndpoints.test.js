const agent = require('superagent');
const statusCode = require('http-status-codes');
const chai = require('chai');

const { expect } = chai;

const requestBody = {
  name: "Daniel",
  lastname: "Quintero",
  idnumber: 11438747777
};

describe('Api Tests for Users endpoints', () => {
//Primera prueba de GET users, dónde se verifica que no se haya insertado ningún usuario
  it('GET users without any user created', async () =>{
    const response = await agent.get('http://localhost:4000/users');
    expect(response.status).to.equal(200);
    if(response.body.users.length == 0){
      expect(response.body.message).to.eql('List of users is empty');     
    }    

  });

    it('POST service', async () => {
     
  
      const response = await agent.post('http://localhost:4000/users').send(requestBody);
  
      expect(response.status).to.equal(statusCode.CREATED);
      expect(response.body.message).to.eql('A new user has been created');
      expect(response.body.user.name).to.eql(requestBody.name);
      expect(response.body.user.lastname).to.eql(requestBody.lastname);
      expect(response.body.user.idnumber).to.eql(requestBody.idnumber);
    });

    it('POST service with a user already created', async () => {
      const requestBody = {
        name: "Daniel",
        lastname: "Quintero",
        idnumber: 11438747777
      };
            
      await agent.post('http://localhost:4000/users').send(requestBody).then().catch(
            (response)=> {
                expect(response.status).to.equal(statusCode.BAD_REQUEST);
                expect(response.response.body.message).to.equal('A user has been created with that number');
            });
  
       
    });
          
      it('GET all users', async () =>{
      const response = await agent.get('http://localhost:4000/users');
      expect(response.status).to.equal(200);
      expect(response.body.message).to.eql('A list of all users');    
      expect(response.body.users.length).to.gt(0);

    });
     
    it('GET with a not existent route', async () =>{
      const response = await agent.get('http://localhost:4000/usersss');      
      expect(response.status).to.equal(200);      
      expect(response.body.message).to.eql('Welcome to our app :)');

    });
});
