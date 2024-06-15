import asyncio

import arrow
import requests


class Tinyalowda:
    params = {
        "clients": 10,
        "runtime": 300,
        "target": "http://localhost:8000/test-get/0",
    }
    codes = []
    sizes = []
    times = []

    def __init__(self, params):
        self.params = params

    def run(self):
        loop = asyncio.new_event_loop()
        try:
            loop.run_until_complete(self.run_tasks(loop))
        finally:
            loop.run_until_complete(loop.shutdown_asyncgens())
            loop.close()

        return self.codes, self.sizes, self.times

    async def run_tasks(self, loop):
        tasks = set()

        start = arrow.utcnow()
        while (arrow.utcnow() - start).total_seconds() < self.params["runtime"]:
            if len(tasks) >= self.params["clients"]:
                # Wait for some download to finish before adding a new one
                _done, tasks = await asyncio.wait(
                    tasks, return_when=asyncio.FIRST_COMPLETED
                )
            tasks.add(loop.create_task(self.test_get()))

        await asyncio.wait(tasks)

    async def test_get(self):
        start = arrow.utcnow()
        resp = requests.get(self.params["target"])
        stop = arrow.utcnow()

        self.codes.append(resp.status_code)
        self.sizes.append(len(resp.content))
        self.times.append((stop - start).total_seconds() * 1000)
