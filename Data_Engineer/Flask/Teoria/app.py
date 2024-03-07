from flask import Flask

app = Flask(__name__) # Agarra el nombre app porque es el nombre del archivo.

@app.route('/')
def index():
    return "<h1>Hello World!</h1>"