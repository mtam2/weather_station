from flask import Flask, render_template, request
import subprocess
import threading

def poll():
    data = subprocess.check_output("sudo temper-poll", shell=True)
    data = data.replace("\xc2\xb0", "")
    c_temp = data[27:32]
    f_temp = data[33:38]
    return c_temp, f_temp 

app = Flask(__name__)

@app.route('/')
def home():
    c_temp, f_temp = poll()
    return render_template('index.html', c_temp=c_temp, f_temp=f_temp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
