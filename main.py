import logging
from datetime import datetime
from flask import Flask, redirect, request

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.WARNING)  # Отключаем логирование от Flask (werkzeug)

# Замените эту ссылку на ссылку, на которую вы хотите перенаправлять все GET-запросы
redirect_url = "https://t.me/+zcxMTHSYKEYxZDcy"

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    user_ip = request.headers.get('X-Real-IP', request.remote_addr)
    user_agent = request.headers.get('User-Agent')
    accept_language = request.headers.get('Accept-Language')
    print(f"{current_time} | {user_ip} | {accept_language} | {user_agent}")

    return redirect(redirect_url, code=302)

if __name__ == '__main__':
    # Устанавливаем хост '0.0.0.0' для прослушивания всех доступных IP-адресов на сервере
    app.run(host='0.0.0.0', port=5051)
