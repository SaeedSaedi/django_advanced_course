from locust import HttpUser, task


class HelloWorldUser(HttpUser):

    def on_start(self):
        response = self.client.post(
            "/accounts/api/v1/jwt/create/",
            data={"email": "saeed@saeed.com", "password": "test"},
        ).json()
        self.client.headers = {
            "Authorization": f"Bearer {response.get('access', None)}"
        }
        return super().on_start()

    @task
    def post_list(self):
        self.client.get("/blog/api/v1/post/")
