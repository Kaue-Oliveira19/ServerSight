import io
from flask import Blueprint, request, render_template, make_response
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

class ControllerForm:
    def __init__(self, emergia, energia, servers):
        self.emergia = emergia
        self.energia = energia
        self.servers = servers

        self.blueprint = Blueprint("controller_form", __name__)
        self.__register_routes()

    def __register_routes(self):
        self.blueprint.add_url_rule("/", view_func=self.exibir_index)
        self.blueprint.add_url_rule("/index", view_func=self.exibir_index)
        self.blueprint.add_url_rule("/calcular_emergia", methods=["GET", "POST"], view_func=self.calcular_emergia)
        self.blueprint.add_url_rule("/usuarios", view_func=self.exibir_usuarios)
        self.blueprint.add_url_rule("/sobre", view_func=self.exibir_sobre)
        self.blueprint.add_url_rule("/login", view_func=self.exibir_login)
        self.blueprint.add_url_rule("/cadastrar", view_func=self.exibir_cadastrar)
        self.blueprint.add_url_rule("/redefinir_senha", view_func=self.exibir_redefinir_senha)

    def exibir_index(self):
        return render_template("index.html")

    def exibir_usuarios(self):
        return render_template("usuarios.html")

    def exibir_sobre(self):
        return render_template("sobre.html")

    def exibir_login(self):
        return render_template("login.html")

    def exibir_cadastrar(self):
        return render_template("cadastrar.html")

    def exibir_redefinir_senha(self):
        return render_template("redefinir_senha.html")

    def calcular_emergia(self):
        if request.method == "GET":
            return render_template("calcular_emergia.html")
        try:
            # Pegando os nomes dos campos conforme o HTML correto (modelo antigo)
            qtdServers = int(request.form.get("qtdServers", 0))
            qtdTempo = int(request.form.get("qtdTempo", 0))
            opcaoTempo = request.form.get("opcaoTempo", "")
            opcaoResfri = request.form.get("opcaoResfri", "")

            # Debug: print para checar os valores recebidos
            print("DEBUG:", qtdServers, qtdTempo, opcaoTempo, opcaoResfri)

            self.energia.definirQtdTempo(qtdTempo)
            self.energia.definirConsumo(opcaoTempo)
            self.servers.definirQtdServers(qtdServers)
            self.servers.definirFator(opcaoResfri)

            self.emergia.setEnergia(self.energia)
            self.emergia.setServers(self.servers)

            resultado5 = self.emergia.calcEnergiaTotal()
            resultado6 = self.emergia.calcEnergiaResfri()

            buffer = io.BytesIO()
            pdf = canvas.Canvas(buffer, pagesize=letter)
            width, height = letter

            x = 50
            y = height - 50
            pdf.drawString(x, y, "Relatório Calculadora de Emergia")
            y -= 30
            pdf.drawString(x, y, f"Quantidade de servidor(es) selecionado(s): {qtdServers}")
            y -= 20
            pdf.drawString(x, y, f"Quantidade de {opcaoTempo} selecionado: {qtdTempo}")
            y -= 20
            pdf.drawString(x, y, f"Fator de resfriamento selecionado: {opcaoResfri}")
            y -= 20
            pdf.drawString(x, y, f"Resultado Energia Total: {resultado5}")
            y -= 20
            pdf.drawString(x, y, f"Resultado Fator Resfriamento: {resultado6}")
            pdf.showPage()
            pdf.save()

            pdf_bytes = buffer.getvalue()
            buffer.close()

            response = make_response(pdf_bytes)
            response.headers.set("Content-Type", "application/pdf")
            response.headers.set("Content-Disposition", "attachment; filename=relatorio_emergia.pdf")
            return response

        except Exception as e:
            return f"Ocorreu um erro: {str(e)}", 500