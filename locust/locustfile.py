from locust import HttpUser, task


class HelloWorldUser(HttpUser):

    @task
    def post_list(self):
        self.client.get("/blog/api/v1/post/")
