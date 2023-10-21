import time


class Pessoa:

    def __init__(self, **kwargs):
        self.olhos = kwargs.get("olhos")
        self.nariz = kwargs.get("nariz")
        self.boca = kwargs.get("boca")
        self.nome = kwargs.get("nome")
        self.idade = kwargs.get("idade")

    def quem_e_voce(self):
        print(f"ME CHAMO {self.nome}, E TENHO {self.idade} ANOS.")


    def conte_ate_10_e_fale_seu_nome(self):
        print("VOU CONTAR ATÉ 10!!")
        input()
        for i in range(11):
            print(f"{i}...")
            time.sleep(1)

        print()
        print(self.nome)
        print()


if __name__ == '__main__':
    catarrenta = Pessoa(
        nome="SARAH",
        idade=7,
        olhos="CASTANHOS",
        nariz="MEDIO",
        boca="MEDIA"
    )

    catarrenta.quem_e_voce()
    catarrenta.conte_ate_10_e_fale_seu_nome()