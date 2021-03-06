import os

from sanic import Sanic
from sanic.response import json

app = Sanic()

@app.get('/')
async def test(request):
	return json({"hello": "world"})

if __name__ == "__main__":
	app.run(
		host = '0.0.0.0',
		port = os.environ.get('PORT', 9300),
	)