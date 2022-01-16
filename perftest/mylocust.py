# import time
from locust import HttpUser, task, between
from password_generator import PasswordGenerator

class QuickstartUser(HttpUser):

    wait_time = between(1, 2.5)

    @task
    def hello_world(self):
        pwo=PasswordGenerator()
        pwd = pwo.generate()
        self.client.get("/login.php")
        self.client.post("/login.php",
                {'username': 'random@chipmonkey.test',
                 'password': pwd})
        # time.sleep(0.05)

    def on_start(self):
        self.client.post("/login.php", json={"username":"foo", "password":"bar"})

