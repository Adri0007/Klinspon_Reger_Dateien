from flask import Flask, request, render_template, redirect, url_for
import datetime

app = Flask(__name__)
LOG_FILE = "/home/pi/Level3/logs/logins.txt"


@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def catch_all(path):
    if request.method == 'POST' and path == 'login':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        ip = request.remote_addr
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(LOG_FILE, "a") as f:
            f.write(f"[{timestamp}] IP: {ip} - User: {username} - Pass: {password}\n")

        if username == "admin" and password == "SuperSecretPassword!":
            return render_template('success.html', token="CTF{br04dc4st_cr3d5_c4tch3d}")
        else:
            return render_template('login.html', error="Benutzername oder Passwort falsch.")

    if path != 'login':
        return redirect(url_for('catch_all', path='login'))

    return render_template('login.html')


if __name__ == '__main__':
    app.run(host='192.168.43.1', port=8080, debug=False)
