# loosely based off https://github.com/python/asyncio/blob/master/examples/simple_tcp_server.py

import sys
import asyncio
import asyncio.streams

from ... import chatFunctions

class chat_server:
	def __init__(self,serverName):
		self.server = None
		self.clients = {}
		self.name = serverName

	def add_client(self, cReader, cWriter):

	@asyncio.coroutine
	def handle_client(self, cReader, cWriter):
		while True:
			data = (yield from cReader.readline()).decode('utf-8')

			if not data:
				break
