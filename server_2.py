import tornado.ioloop
import tornado.web
import aiomysql
import json

import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning)

# Database configuration
db_config = {
    'host': '46.243.233.79',
    'port': 3306,
    'user': 'mike',
    'password': '123456',
    'db': 'users',
    'charset': 'utf8mb4',
}


class BaseHandler(tornado.web.RequestHandler):
    async def prepare(self):
        self.db = await aiomysql.connect(**db_config)
        self.cursor = await self.db.cursor()

    async def on_finish(self):
        await self.cursor.close()
        await self.db.close()


class CheckPhoneHandler(BaseHandler):
    async def post(self):
        try:
            request_data = json.loads(self.request.body.decode('utf-8'))
            phone_number = request_data.get('phone_number')

            sql = "SELECT * FROM users WHERE phone_number = %s"
            await self.cursor.execute(sql, (phone_number,))
            result = await self.cursor.fetchone()

            if result:
                self.set_status(200)
            else:
                self.set_status(404)

        except Exception as e:
            self.set_status(500)
            self.write(str(e))


class VerifyCodeHandler(BaseHandler):
    async def post(self):
        try:
            request_data = json.loads(self.request.body.decode('utf-8'))
            code = request_data.get('password')

            sql = "SELECT * FROM users WHERE password = %s"  # Need to check the phone number too

            await self.cursor.execute(sql, (code,))
            result = await self.cursor.fetchone()

            if result:
                token = result[4].decode('utf-8')  # Adjust this index to match your token field
                self.write(json.dumps({'token': token}))
            else:
                self.set_status(404)

        except Exception as e:
            self.set_status(500)
            self.write(str(e))


def make_app():
    return tornado.web.Application([
        (r"/check_phone", CheckPhoneHandler),
        (r"/verify_code", VerifyCodeHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(5000)
    tornado.ioloop.IOLoop.current().start()
