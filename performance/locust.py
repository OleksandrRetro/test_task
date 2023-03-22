import time

from locust import HttpUser, task, between


class LocustPerfTest(HttpUser):
    wait_time = between(1, 5)
    host = "http://localhost:8000"

    @task
    def get_peoples(self):
        self.client.get("/people")

    @task
    def get_peoples_by_id(self):
        for item_id in range(5):
            self.client.get(f"/people/{item_id}")
            time.sleep(1)

    @task
    def get_planets(self):
        self.client.get("/planets")

    @task
    def get_planets_by_id(self):
        for item_id in range(5):
            self.client.get(f"/planets/{item_id}")
            time.sleep(1)

    @task
    def get_starships(self):
        self.client.get("/starships")

    @task
    def get_starships_by_id(self):
        for item_id in range(5):
            self.client.get(f"/starships/{item_id}")
            time.sleep(1)
