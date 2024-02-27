from flask import Flask, render_template, request, jsonify, Response
import threading
import subprocess
import os

app = Flask(__name__)
sem = threading.Semaphore()

port = 4000

def start_instance(port):
    subprocess.run(["sh", "./run-compose.sh", f"instance{port}", port], cwd="/app")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['GET'])
def generate():
    global sem

    sem.acquire()
    global port
    thread = threading.Thread(target=start_instance, args=(port))
    thread.start()
    port += 1
    sem.release()

    return render_template('index.html', port=port)

    
@app.route('/', methods=['GET'])
def instancer():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)