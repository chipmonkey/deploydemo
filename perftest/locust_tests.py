"""
Performance testing for CENtree API
"""

import os
import random
import names
from locust import HttpUser, task, between

# from requests.packages.urllib3.exceptions import InsecureRequestWarning
import urllib3


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
    def post_random_user_name(self):
        """ Posts a random userid and name to /user/
        """
        userid = random.randint(1, NUMUSERS)
        name = names.get_full_name()
        payload = {
            'userid': userid,
            'name': name
        }
        self.client.post(
            "/user/",
            json=payload,
            verify=False,
            allow_redirects=False,
        )

    @task
    def patch_random_user_name(self):
        """ PATCHes a random userid and name to /user/
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
        self.client.headers = {"Content-Type": "application/json"}
