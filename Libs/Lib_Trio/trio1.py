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


async def bar():
    print('Iniciou BAR')
    async with trio.open_nursery() as nursery:
        for n in range(1, 15):
            nursery.start_soon(foo, n)
    print('Finalizou BAR')


trio.run(bar)

