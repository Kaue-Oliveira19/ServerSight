// Validação do formulário de envio de dúvidas
document.querySelector("form").addEventListener("submit", function (event) {
    const email = document.getElementById("email").value.trim();
    const duvida = document.getElementById("duvida").value.trim();

    if (!email || !duvida) {
        alert("Por favor, preencha todos os campos antes de enviar.");
        event.preventDefault(); // Impede o envio do formulário
    } else if (!validateEmail(email)) {
        alert("Por favor, insira um endereço de email válido.");
        event.preventDefault();
    } else {
        alert("Dúvida enviada com sucesso!");
    }
});

// Função para validar o formato do email
function validateEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

// Exemplo de manipulação do menu offcanvas
document.querySelectorAll(".navbar-toggler").forEach(button => {
    button.addEventListener("click", function () {
        const offcanvas = document.querySelector(this.getAttribute("data-bs-target"));
        if (offcanvas) {
            offcanvas.classList.toggle("show");
        }
    });
});