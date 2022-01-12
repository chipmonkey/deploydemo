"""
Performance testing for CENtree API
"""

import os
import random
import json
import names
from dotenv import load_dotenv
from locust import HttpUser, task, between

# from requests.packages.urllib3.exceptions import InsecureRequestWarning
import urllib3


load_dotenv()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

host = os.getenv("host", "localhost")
port = os.getenv("port", "8000")

NUMUSERS = 10

class QuickstartUser(HttpUser):
    """ Default locust test user.
        Contains API specific tests as @tasks
    """
    wait_time = between(1, 2.5)

    @task
    def change_random_user_name(self):
        """ Picks a random user_id and changes its name
        """
        user_id = random.randint(1, NUMUSERS)
        name = names.get_full_name()
        payload = {
            'user_id': user_id,
            'name': name
        }
        self.client.post(
            "/user/",
            json=payload,
            verify=False,
            allow_redirects=False,
        )


    def on_start(self):
        """ Set authorization headers for requests with JWT token (from environment)
        """
        # self.client.headers = {"Authorization": f"Bearer {api_token}"}
        self.client.headers = {"Content-Type": "application/json"}
