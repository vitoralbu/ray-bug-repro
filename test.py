import ray

from fastapi import FastAPI
from ray import serve

app = FastAPI()
ray.init(address='auto')
serve.start(detached=True)

@serve.deployment(route_prefi)
class MyFastAPIDeployment:
    @app.get("/")
    def root(self):
        return "Hello, world!"


MyFastAPIDeployment.deploy()
