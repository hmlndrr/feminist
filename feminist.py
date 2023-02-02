from flask import Flask, render_template, request
from subprocess import PIPE, Popen


app = Flask(__name__)


def exec(q):
    p = Popen(q, shell=True, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate()
    if stdout:
        return stdout.decode()
    return stderr.decode()

@app.get("/")
def index():
    return render_template('index.html', output="")

@app.post("/")
def query():
    q = request.form['q']
    q = ["she" + word for word in q.split(' ')]
    q = ' '.join(q)
    result = exec(q)
    return render_template('index.html', output=result)

@app.get("/code")
def code():
    return open(__file__).read()