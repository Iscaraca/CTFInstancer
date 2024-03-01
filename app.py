from flask import Flask, render_template, redirect, url_for, session
import threading
import subprocess
import random

app = Flask(__name__)
app.secret_key = 'change_me'
sem = threading.Semaphore()

ports = []

def start_instance(port):
    subprocess.run(["sh", "./run-compose.sh", f"instance{port}", port], cwd="/app")

@app.route('/generate', methods=['GET'])
def generate():
    global sem
    sem.acquire()

    global ports
    port = random.randint(1000, 10000)
    while port in ports:
        port = random.randint(1000, 10000)
    
    ports.append(port)
    port = str(port)

    thread = threading.Thread(target=start_instance, args=(port))
    thread.start()

    sem.release()

    session['port'] = port
    return redirect(url_for('instancer'))

    
@app.route('/', methods=['GET'])
def instancer():
    port = session.get('port')
    session.clear()
    return render_template('index.html', port=port)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)