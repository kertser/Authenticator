# Prototyping server v2
from flask import Flask, request, jsonify
import aiomysql
import asyncio

app = Flask(__name__)

# Настройки базы данных
db_host = 'your_db_host'
db_user = 'your_db_user'
db_password = 'your_db_password'
db_name = 'your_db_name'

async def get_db_connection():
    return await aiomysql.connect(host=db_host, user=db_user, password=db_password, db=db_name)

@app.route('/check_phone', methods=['POST'])
async def check_phone():
    try:
        # Получаем номер телефона из JSON запроса
        request_data = await request.get_json()
        phone_number = request_data.get('phone_number')

        # Выполняем асинхронный SQL-запрос для поиска номера телефона в базе данных
        async with get_db_connection() as conn:
            async with conn.cursor() as cursor:
                sql = "SELECT * FROM users WHERE phone_number = %s"
                await cursor.execute(sql, (phone_number,))
                result = await cursor.fetchone()

        # Если номер телефона найден, возвращаем код 200
        if result:
            return '', 200
        else:
            return '', 404

    except Exception as e:
        return str(e), 500

@app.route('/verify_code', methods=['POST'])
async def verify_code():
    try:
        # Получаем код из JSON запроса
        request_data = await request.get_json()
        code = request_data.get('code')

        # Выполняем асинхронный SQL-запрос для проверки кода
        async with get_db_connection() as conn:
            async with conn.cursor() as cursor:
                sql = "SELECT * FROM users WHERE code = %s"
                await cursor.execute(sql, (code,))
                result = await cursor.fetchone()

        # Если код совпадает, возвращаем токен
        if result:
            token = result.get('token')
            return jsonify({'token': token}), 200
        else:
            return '', 404

    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(aiomysql.create_pool(host=db_host, user=db_user, password=db_password, db=db_name))
    app.run()
