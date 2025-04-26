from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

# Конфигурация Redis
redis_host = os.environ.get('REDIS_HOST', 'redis')
redis_port = int(os.environ.get('REDIS_PORT', 6379))
redis_client = redis.Redis(host=redis_host, port=redis_port, db=0)

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"status": "ok"})

@app.route('/count', methods=['GET'])
def count():
    try:
        # Увеличиваем счетчик и возвращаем значение
        visit_count = redis_client.incr('visit_counter')
        return jsonify({"count": visit_count})
    except redis.exceptions.ConnectionError:
        return jsonify({"error": "Redis connection failed"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0')