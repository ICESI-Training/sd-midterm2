import unittest
import requests
import json

class TestUsersApi(unittest.TestCase):

    API_URL = "http://apiflask-env.uuhyrnua83.us-east-2.elasticbeanstalk.com"

    def test_get_all_users(self):
    
        response = requests.get(self.API_URL+'/users',
        headers={'Accept': 'application/json'})

        self.assertEqual(response.status_code, 200, "Should be 200")
        

    def test_add_new_user(self):

        response = requests.post(self.API_URL+'/users/JesusPaz',
        headers={'Accept': 'application/json'})

        self.assertEqual(response.status_code, 200, "Should be 200")

        data = json.loads(response.content)
        aux = json.loads(data)
        userId = aux["id"]
        numRepos = aux["numRepos"]
        
        self.assertTrue(userId != "" and userId != None, "Can not be empty or None")
        self.assertEqual(numRepos, 22, "Number of repos should be 22")
      

if __name__ == '__main__':
    unittest.main()
