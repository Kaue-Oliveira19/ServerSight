// Validação do formulário de redefinição de senha
document.getElementById("btnCriar").addEventListener("click", function (event) {
    const email = document.getElementById("email").value.trim();

    if (!email) {
        alert("Por favor, insira o email para recuperação.");
        event.preventDefault(); // Impede o envio do formulário
    } else if (!validateEmail(email)) {
        alert("Por favor, insira um endereço de email válido.");
        event.preventDefault();
    } else {
        alert("Solicitação de redefinição de senha enviada com sucesso!");
    }
});

// Função para validar o formato do email
function validateEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}