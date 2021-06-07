from base64 import b64decode
from flask import make_response, request, send_file
from config import logsAuthPassword, logsAuthUserName


def getLogs():
    if request.headers.get("Authorization"):
        login, password = b64decode(request.headers["Authorization"].split(" ")[-1]).decode("utf-8").split(":")
        if login == logsAuthUserName and password == logsAuthPassword:
            return send_file("logs/logs.txt")
    resp = make_response("There would be logs if you knew the username and password.", 401)
    resp.headers['WWW-Authenticate'] = 'Basic realm="How about authorization?"'
    return resp
