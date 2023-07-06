from random import randint
import httpx
import trio


async def foo(id_poke: str):
    url = 'https://pokeapi.co/api/v2/pokemon/{id_pokemon}'

    async with httpx.AsyncClient() as client:
        await trio.sleep(randint(0, 10))
        response = await client.get(
            url.format(id_pokemon=id_poke)
        )
        data = response.json()
        print('ID: ', id_poke, 'Pokemon: ', data.get('name'))


async def response_good_foo(msg):
    await trio.sleep(randint(0, 3))
    print('Chamada de retorno ao cliente ', msg)


async def bar():  # Vulgo MAIN
    print('Iniciou BAR')
    async with trio.open_nursery() as nursery:
        nursery.start_soon(response_good_foo, 'JOSE')
        for n in range(1, 15):
            nursery.start_soon(foo, n)
    print('Finalizou BAR')

if __name__ == "__main__":
    print('Inicio do main')
    trio.run(bar)
    print('Fim do main')


