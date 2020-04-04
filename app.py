from flask import Flask
from flask import jsonify
import socket

app=Flask(__name__)

@app.route("/")
def retorna_ip():
	mensagem_ip = {'ip': socket.gethostbyname(socket.gethostname())}
	return jsonify(mensagem_ip)

app.run(host="0.0.0.0", port=80)
