class Emergia:
    def __init__(self, energia=None, servers=None):
        """
        Construtor da classe.
        :param energia: Instância da classe Energia.
        :param servers: Instância da classe Servidores.
        """
        self.energia_total = 0.0   # Armazena a energia total consumida pelos servidores
        self.energia_resfri = 0.0  # Armazena a energia associada ao resfriamento
        self.energia = energia     # Agregação com a classe Energia
        self.servers = servers     # Agregação com a classe Servidores

    def calcEnergiaTotal(self) -> float:
        """
        Calcula a energia total consumida (kWh), multiplicando
        a quantidade de energia gasta por servidor pela quantidade de servidores.
        """
        qtd_energia = self.energia.get_qtd_energia() if self.energia is not None else 0
        qtd_servers = self.servers.get_qtd_servers() if self.servers is not None else 0

        self.energia_total = qtd_servers * qtd_energia
        return self.energia_total

    def calcEnergiaResfri(self) -> float:
        """
        Calcula a energia do resfriamento multiplicando o resultado
        da energia total pelo fator de resfriamento definido em servers.
        """
        energia_total = self.calcEnergiaTotal()
        fator = self.servers.get_fator() if self.servers is not None else 0

        self.energia_resfri = energia_total * fator
        return self.energia_resfri

    # Métodos getter
    def get_energia_total(self) -> float:
        return self.energia_total

    def get_energia_resfri(self) -> float:
        return self.energia_resfri

    # Métodos setter compatíveis com o controller
    def setEnergia(self, energia) -> None:
        self.energia = energia

    def setServers(self, servers) -> None:
        self.servers = servers