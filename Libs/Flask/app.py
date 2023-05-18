from flask import Flask, render_template
from random import randint


app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World!!"

@app.route("/teste/<name>")
def teste(name):
    # Logica
    num = [randint(1, 99), 3, 4,6,22]
    return render_template(
        'teste.html',
        numero=num,
        nome_user=name
        )
    

if __name__ == "__main__":
    app.run()
