from random import randint
from time import sleep
import trio
from flask import Flask

app = Flask(__name__)

async def corroutine(n1):
    for n2 in range(1, n1):
        sleep(n2)
        print(f"Fazendo algo no background {n2}")
    print('Finalizando corroutine')
async def response_good_foo():
    times = randint(0, 3)
    await trio.sleep(times)
    val = 'Chamada de retorno ao cliente ' + str(times)
    async with trio.open_nursery() as nsy:
        nsy.start_soon(corroutine, times)
    return val

@app.route('/')
def index():
    return "Olá, mundo! Esta é a página inicial da minha aplicação."

@app.route('/about')
async def about():
    var = await response_good_foo()
    return "Esta é a página 'Sobre' executando:\n" + str(var)


async def application_exec():
    async with trio.open_nursery() as nsy:
        nsy.start_soon(app.run, '0.0.0.0', 5000)

if __name__ == '__main__':
    trio.run(application_exec)