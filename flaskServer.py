from flask import Flask, render_template, request
import subprocess
import threading

def poll():
    Threading.Timer(5.0, poll).start()
    data = subprocess.check_output( "sudo temper-poll", shell=True)
    data.replace("","")

app = Flask(__name__)

@app.route('/')
def home():
    poll()
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
