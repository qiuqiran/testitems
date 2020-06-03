from locust import HttpLocust, TaskSet, task


class WebsiteTasks(TaskSet):
    def on_start(self):
        print('start')


    def login(self):
        self.client.post("/reptilian/login_action/", {
            "username": "admin",
            "password": "admin123456"
        })


    def index(self):
        s = self.client.get("/admin_0/")
        json = s.status_code
        print(json)

    def film(self):
        s = self.client.get("/film/")
        text = s.text
        print(text)

    @task(1)
    def start(self):
        self.index()
        self.film()



class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 15000
    host = "http://207.246.77.150:8000"
    # host = "https://www.baidu.com/"