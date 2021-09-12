from fila_base import FilaBase


class FilaPrioritaria(FilaBase):
    def gera_senha_atual(self) -> None:
        self.senha_atual = f'PR{self.codigo}'

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual = self.fila.pop()
        self.clientes_atendidos.append(cliente_atual)
        return f'cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}'

    def estatisticas(self, dia: str, agencia: int, flag: str) -> dict:
        if flag != 'detail':
            estatistica = {f'{agencia}-{dia}': len(self.clientes_atendidos)}
        else:
            estatistica = {}
            estatistica['dia'] = dia
            estatistica['agencia'] = agencia
            estatistica['clientes_atendidos'] = self.clientes_atendidos
            estatistica['quantidade_clientes_atendidos'] = len(self.clientes_atendidos)

        return estatistica
