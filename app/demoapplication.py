from flask import Flask

class DemoApplication:
    def __init__(self):
        # Cria a instância da aplicação Flask
        self.app = Flask(__name__)
        self.register_routes()

    def register_routes(self):
        # Exemplo de rota raiz
        @self.app.route("/")
        def index():
            return "Hello, Flask Demo Application!"

    def run(self, **kwargs):
        # Configura e inicia o servidor web
        self.app.run(**kwargs)


if __name__ == '__main__':
    # Instancia a aplicação e a executa, similar ao SpringApplication.run()
    demo_app = DemoApplication()
    demo_app.run(debug=True)
