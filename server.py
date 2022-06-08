import socket
import asyncio
from hypercorn.asyncio import serve
from hypercorn.config import Config
from main import app

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
host = s.getsockname()[0]
s.close()

config = Config()
config.bind = [host+":12345"] 
config.use_reloader = True

asyncio.run(serve(app, config))

#https://pgjones.gitlab.io/hypercorn/how_to_guides/api_usage.html
