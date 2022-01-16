"""
Performance testing for CENtree API
"""

import os
import random
import names
from dotenv import load_dotenv
from locust import HttpUser, task, between

# from requests.packages.urllib3.exceptions import InsecureRequestWarning
import urllib3


load_dotenv()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

host = os.getenv("host", "localhost")
port = os.getenv("port", "8000")

NUMUSERS = 50

class QuickstartUser(HttpUser):
    """ Default locust test user.
        Contains API specific tests as @tasks
    """
    wait_time = between(1, 2.5)

    @task
    def change_name_v2(self):
        """ Picks a random userid and changes its name
        """
        userid = random.randint(1, NUMUSERS)
        name = names.get_full_name()
        (first, last) = name.split(' ')
        payload = {
            'userid': userid,
            'first': first,
            'last': last
        }
        self.client.patch(
            "/v2/user/",
            json=payload,
            verify=False,
            allow_redirects=False,
        )


    @task
    def change_random_user_name(self):
        """ Picks a random userid and changes its name
        """
        userid = random.randint(1, NUMUSERS)
        name = names.get_full_name()
        payload = {
            'userid': userid,
            'name': name
        }
        self.client.patch(
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
