class FilaNormal:
    codigo: int = 0
    fila = []
    clientes_atendidos = []
    senha_atual: str = ""

    def gera_senha_atual(self) -> None:
        self.senha_atual = f'NW{self.codigo}'

    def reseta_fila(self):
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.fila.append(self.senha_atual)

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual = self.fila.pop()
        self.clientes_atendidos.append(cliente_atual)
        return f'cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}'
