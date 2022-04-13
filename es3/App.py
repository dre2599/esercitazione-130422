from clientiDAO import clientiDAO

class App():

    def __init__(self):
        n = int(input('scegli una query: '))

        __clientidao = clientiDAO()

        match n:
            case 1:
                __clientidao.getnumClientiForAgente()
            case 2:
                __clientidao.getClienti_byAgente()

if __name__ == "__main__":
    app = App()
