class Energia:
    def __init__(self, qtd_energia: float = 0.0, qtd_tempo: int = 0, opcao_tempo: str = ""):
        self.qtd_energia = qtd_energia
        self.qtd_tempo = qtd_tempo
        self.opcao_tempo = opcao_tempo

    # Método compatível com o controller
    def definirQtdTempo(self, qtd_tempo: int) -> int:
        self.qtd_tempo = qtd_tempo
        return self.qtd_tempo

    # Método compatível com o controller
    def definirConsumo(self, opcao_tempo: str) -> float:
        self.opcao_tempo = opcao_tempo
        if opcao_tempo == "opcaoHora":
            self.qtd_energia = self.qtd_tempo * (1 * 850)
        elif opcao_tempo == "opcaoDia":
            self.qtd_energia = self.qtd_tempo * (24 * 850)
        elif opcao_tempo == "opcaoSemana":
            self.qtd_energia = self.qtd_tempo * (7 * (24 * 850))
        else:
            self.qtd_energia = self.qtd_tempo * (30 * (24 * 850))
        return self.qtd_energia

    # Getters e setters (opcionais)
    def get_qtd_energia(self) -> float:
        return self.qtd_energia

    def set_qtd_energia(self, qtd_energia: float) -> None:
        self.qtd_energia = qtd_energia

    def get_tempo(self) -> int:
        return self.qtd_tempo

    def set_tempo(self, tempo: int) -> None:
        self.qtd_tempo = tempo

    def get_opcao_consumo(self) -> str:
        return self.opcao_tempo

    def set_opcao_consumo(self, opcao_tempo: str) -> None:
        self.opcao_tempo = opcao_tempo