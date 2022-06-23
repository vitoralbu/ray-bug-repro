Steps to reproduce:

1. Install deps: `poetry install`
2. Start a shell in the virtualenv: `poetry shell`
3. Start ray: `ray start --head`
4. Run app with `uvicorn test:app --reload --port 8001`
5. Sending request: `curl http://localhost:8001/`

Error I get is:
```
INFO:     Will watch for changes in these directories: ['/home/vilma/github.com/trident/test-ray']
INFO:     Uvicorn running on http://127.0.0.1:8001 (Press CTRL+C to quit)
INFO:     Started reloader process [856404] using statreload
(ServeController pid=856442) INFO 2022-06-23 17:29:56,805 controller 856442 checkpoint_path.py:17 - Using RayInternalKVStore for controller checkpoint and recovery.
(ServeController pid=856442) INFO 2022-06-23 17:29:56,913 controller 856442 http_state.py:112 - Starting HTTP proxy with name 'SERVE_CONTROLLER_ACTOR:SERVE_PROXY_ACTOR-node:10.0.0.209-0' on node 'node:10.0.0.209-0' listening on '127.0.0.1:8000'
(ServeController pid=856442) INFO 2022-06-23 17:29:57,901 controller 856442 deployment_state.py:1216 - Adding 1 replicas to deployment 'MyFastAPIDeployment'.
(HTTPProxyActor pid=856472) INFO:     Started server process [856472]
INFO:     Started server process [856406]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:49160 - "GET / HTTP/1.1" 500 Internal Server Error
ERROR:    Exception in ASGI application
Traceback (most recent call last):
  File "/home/vilma/.cache/pypoetry/virtualenvs/test-ray-1A-bV5of-py3.9/lib/python3.9/site-packages/uvicorn/protocols/http/h11_impl.py", line 373, in run_asgi
    result = await app(self.scope, self.receive, self.send)
  File "/home/vilma/.cache/pypoetry/virtualenvs/test-ray-1A-bV5of-py3.9/lib/python3.9/site-packages/uvicorn/middleware/proxy_headers.py", line 75, in __call__
    return await self.app(scope, receive, send)
  File "/home/vilma/.cache/pypoetry/virtualenvs/test-ray-1A-bV5of-py3.9/lib/python3.9/site-packages/fastapi/applications.py", line 269, in __call__
    await super().__call__(scope, receive, send)
  File "/home/vilma/.cache/pypoetry/virtualenvs/test-ray-1A-bV5of-py3.9/lib/python3.9/site-packages/starlette/applications.py", line 124, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/home/vilma/.cache/pypoetry/virtualenvs/test-ray-1A-bV5of-py3.9/lib/python3.9/site-packages/starlette/middleware/errors.py", line 184, in __call__
    raise exc
  File "/home/vilma/.cache/pypoetry/virtualenvs/test-ray-1A-bV5of-py3.9/lib/python3.9/site-packages/starlette/middleware/errors.py", line 162, in __call__
    await self.app(scope, receive, _send)
  File "/home/vilma/.cache/pypoetry/virtualenvs/test-ray-1A-bV5of-py3.9/lib/python3.9/site-packages/starlette/exceptions.py", line 93, in __call__
    raise exc
  File "/home/vilma/.cache/pypoetry/virtualenvs/test-ray-1A-bV5of-py3.9/lib/python3.9/site-packages/starlette/exceptions.py", line 82, in __call__
    await self.app(scope, receive, sender)
  File "/home/vilma/.cache/pypoetry/virtualenvs/test-ray-1A-bV5of-py3.9/lib/python3.9/site-packages/fastapi/middleware/asyncexitstack.py", line 21, in __call__
    raise e
  File "/home/vilma/.cache/pypoetry/virtualenvs/test-ray-1A-bV5of-py3.9/lib/python3.9/site-packages/fastapi/middleware/asyncexitstack.py", line 18, in __call__
    await self.app(scope, receive, send)
  File "/home/vilma/.cache/pypoetry/virtualenvs/test-ray-1A-bV5of-py3.9/lib/python3.9/site-packages/starlette/routing.py", line 670, in __call__
    await route.handle(scope, receive, send)
  File "/home/vilma/.cache/pypoetry/virtualenvs/test-ray-1A-bV5of-py3.9/lib/python3.9/site-packages/starlette/routing.py", line 266, in handle
    await self.app(scope, receive, send)
  File "/home/vilma/.cache/pypoetry/virtualenvs/test-ray-1A-bV5of-py3.9/lib/python3.9/site-packages/starlette/routing.py", line 65, in app
    response = await func(request)
  File "/home/vilma/.cache/pypoetry/virtualenvs/test-ray-1A-bV5of-py3.9/lib/python3.9/site-packages/fastapi/routing.py", line 217, in app
    solved_result = await solve_dependencies(
  File "/home/vilma/.cache/pypoetry/virtualenvs/test-ray-1A-bV5of-py3.9/lib/python3.9/site-packages/fastapi/dependencies/utils.py", line 531, in solve_dependencies
    solved = await run_in_threadpool(call, **sub_values)
  File "/home/vilma/.cache/pypoetry/virtualenvs/test-ray-1A-bV5of-py3.9/lib/python3.9/site-packages/starlette/concurrency.py", line 41, in run_in_threadpool
    return await anyio.to_thread.run_sync(func, *args)
  File "/home/vilma/.cache/pypoetry/virtualenvs/test-ray-1A-bV5of-py3.9/lib/python3.9/site-packages/anyio/to_thread.py", line 31, in run_sync
    return await get_asynclib().run_sync_in_worker_thread(
  File "/home/vilma/.cache/pypoetry/virtualenvs/test-ray-1A-bV5of-py3.9/lib/python3.9/site-packages/anyio/_backends/_asyncio.py", line 937, in run_sync_in_worker_thread
    return await future
  File "/home/vilma/.cache/pypoetry/virtualenvs/test-ray-1A-bV5of-py3.9/lib/python3.9/site-packages/anyio/_backends/_asyncio.py", line 867, in run
    result = context.run(func, *args)
  File "/home/vilma/.cache/pypoetry/virtualenvs/test-ray-1A-bV5of-py3.9/lib/python3.9/site-packages/ray/serve/http_util.py", line 177, in get_current_servable_instance
    return serve.get_replica_context().servable_object
  File "/home/vilma/.cache/pypoetry/virtualenvs/test-ray-1A-bV5of-py3.9/lib/python3.9/site-packages/ray/serve/api.py", line 240, in get_replica_context
    raise RayServeException(
ray.serve.exceptions.RayServeException: `serve.get_replica_context()` may only be called from within a Ray Serve deployment.
```
