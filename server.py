# This is a server for the project.

from typing import Any
import tornado.ioloop
import tornado.web
from tornado import httputil
import aiomysql
import json

import token_generator  # generating and comparing sha256 hash tokens
import config  # general config

import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

# Base class for asynchronous handlers
class BaseHandler(tornado.web.RequestHandler):
    def __init__(
            self,
            application: tornado.web.Application,
            request: httputil.HTTPServerRequest,
            **kwargs: Any,
    ):
        super().__init__(application, request, **kwargs)
        self.cursor = None
        self.db = None

    async def prepare(self):
        self.db = await aiomysql.connect(**config.db_config)
        self.cursor = await self.db.cursor()

    async def on_finish(self):
        await self.cursor.close()
        await self.db.close()


# Phone number check class
class CheckPhoneHandler(BaseHandler):
    async def post(self):
        try:
            request_data = json.loads(self.request.body.decode('utf-8'))
            phone_number = request_data.get('phone_number')  # Getting phone number from request

            # Checking if phone number is already in the database
            sql = "SELECT * FROM users WHERE phone_number = %s"
            await self.cursor.execute(sql, (phone_number,))
            result = await self.cursor.fetchone()

            if result:
                self.set_status(200)  # It means that phone number is already in the database
            else:
                self.set_status(404)   # It means that phone number is not in the database

        except Exception as e:
            self.set_status(500)   # Internal server error
            self.write(str(e))

# Code verification class
class VerifyCodeHandler(BaseHandler):
    async def post(self):
        try:
            # Getting data from the request
            request_data = json.loads(self.request.body.decode('utf-8'))
            phone_number = request_data.get('phone_number')
            code = request_data.get('password')

            # Checking if the phone number and code match
            sql = "SELECT * FROM users WHERE phone_number = %s and password = %s"

            await self.cursor.execute(sql, (phone_number, code,))
            result = await self.cursor.fetchone()

            if result:  # if they are match
                token = token_generator.TokenGenerator().get_token()
                self.write(json.dumps({'token': token}))
                #  This is reserved for token check feature
                """
                token = result[4].decode('utf-8')
                if token == token_generator.TokenGenerator().generate_token_by_date("2023-09-15 00:00:00"):
                    self.write(json.dumps({'token': token}))
                """
            else:
                self.set_status(404)  # It means that phone number and code are not match

        except Exception as e:
            self.set_status(500)  # Internal server error
            self.write(str(e))


# Creating the application - entry point
def make_app():
    return tornado.web.Application([
        (r"/check_phone", CheckPhoneHandler),
        (r"/verify_code", VerifyCodeHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(5000)
    tornado.ioloop.IOLoop.current().start()
