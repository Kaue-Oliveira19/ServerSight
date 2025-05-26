class Servidores:
    def __init__(self, qtd_servers: int = 0, opcao_resfri: str = "", fator: float = 0.0):
        self.qtd_servers = qtd_servers
        self.opcao_resfri = opcao_resfri
        self.fator = fator

    # Método compatível com o controller
    def definirQtdServers(self, qtd_servers: int) -> int:
        self.qtd_servers = qtd_servers
        return self.qtd_servers

    # Método compatível com o controller
    def definirFator(self, opcao_resfri: str) -> float:
        if opcao_resfri == "opcaoCrac":
            self.fator = 1.3
        elif opcao_resfri == "opcaoInRow":
            self.fator = 1.1
        else:
            self.fator = 0.9
        self.opcao_resfri = opcao_resfri
        return self.fator

    # Getters e setters opcionais
    def get_qtd_servers(self) -> int:
        return self.qtd_servers

    def set_qtd_servers(self, qtd_servers: int) -> None:
        self.qtd_servers = qtd_servers

    def get_opcao_resfri(self) -> str:
        return self.opcao_resfri

    def set_opcao_resfri(self, opcao_resfri: str) -> None:
        self.opcao_resfri = opcao_resfri

    def get_fator(self) -> float:
        return self.fator

    def set_fator(self, fator: float) -> None:
        self.fator = fator