from abc import abstractmethod, ABCMeta


class FilaBase(metaclass=ABCMeta):
    codigo: int = 0
    fila = []
    clientes_atendidos = []
    senha_atual: str = ""

    def reseta_fila(self):
        if self.codigo >= 200:
            self.codigo = 0
        else:
            self.codigo += 1

    def inseri_cliente(self):
        self.fila.append(self.senha_atual)

    @abstractmethod
    def gera_senha_atual(self):
        ...

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.inseri_cliente()

    @abstractmethod
    def chama_cliente(self, caixa: int):
        ...
