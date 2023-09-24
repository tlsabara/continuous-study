matrix = [['maçã', 'banana', 'laranja', 'uva', 'morango'],
          ['abacaxi', 'pera', 'manga', 'uva', 'morango'],
          ['kiwi', 'banana', 'laranja', 'uva', 'pêssego'],
          ['abacate', 'banana', 'laranja', 'uva', 'morango'],
          ['maçã', 'banana', 'laranja', 'uva', 'morango']]


for frist, second, *rest in matrix:
    print(frist, second, "->", rest)