import unittest
import requests
import json

class TestUsersApi(unittest.TestCase):

    API_URL = "http://apiflask-env.uuhyrnua83.us-east-2.elasticbeanstalk.com"

    def test_get_all_users(self):
    
        response = requests.get(self.API_URL+'/users',
        headers={'Accept': 'application/json'})

        self.assertEqual(response.status_code, 200, "Should be 200")
        

    def test_path_not_found(self):
        response = requests.get(self.API_URL+'/user',
        headers={'Accept': 'application/json'})

        self.assertEqual(response.status_code, 404, "Should be 404")
    

    def test_add_new_user(self):

        response = requests.post(self.API_URL+'/users/JesusPaz',
        headers={'Accept': 'application/json'})

        self.assertEqual(response.status_code, 200, "Should be 200")

        data = json.loads(response.content)
        aux = json.loads(data)
        userId = aux["id"]
        numRepos = aux["numRepos"]

        # Used to delete the user and can try the test again
        response = requests.delete(self.API_URL+'/users/JesusPaz',
        headers={'Accept': 'application/json'})

        # test deleted ok
        self.assertEqual(response.status_code, 200, "Should be 200")

        self.assertTrue(userId != "" and userId != None, "Can not be empty or None")
        self.assertEqual(numRepos, 22, "Number of repos should be 22")
      
    def test_add_new_user_empty_name(self):

        response = requests.post(self.API_URL+'/users/ ',
        headers={'Accept': 'application/json'})
        
        self.assertEqual(response.status_code, 400, "Should be 400")

    def test_add_new_user_exists_in_database(self):

        response = requests.post(self.API_URL+'/users/danielq97',
        headers={'Accept': 'application/json'})
        
        self.assertEqual(response.status_code, 400, "Should be 400")

    def test_add_new_user_dont_exists_in_github(self):

        response = requests.post(self.API_URL+'/users/atdgps85632s',
        headers={'Accept': 'application/json'})
        
        self.assertEqual(response.status_code, 400, "Should be 400")
    
    def test_delete_user_dont_exist(self):

        response = requests.delete(self.API_URL+'/users/atdgps85632s',
        headers={'Accept': 'application/json'})
        
        self.assertEqual(response.status_code, 400, "Should be 400")

    def test_delete_user_empty_name(self):

        response = requests.delete(self.API_URL+'/users/ ',
        headers={'Accept': 'application/json'})
        
        self.assertEqual(response.status_code, 400, "Should be 400")

    

if __name__ == '__main__':
    unittest.main()
