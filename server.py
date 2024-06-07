from flask import Flask

app = Flask(__name__)

@app.route("/")
def server_info():
    # Замените "example.aternos.me" на реальный IP-адрес вашего сервера
    server_ip = "raota_kopatel.aternos.me"
    return f"IP-адрес сервера: {server_ip}"

if __name__ == "__main__":
    app.run()
