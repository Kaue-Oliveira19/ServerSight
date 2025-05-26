document.addEventListener("DOMContentLoaded", function () {
    const btnEntrar = document.getElementById("btnEntrar");

    btnEntrar.addEventListener("click", function (event) {
        event.preventDefault(); // Evita o envio do formulário

        const usuario = document.getElementById("usuario").value.trim();
        const senha = document.getElementById("senha").value.trim();

        if (usuario === "" || senha === "") {
            alert("Por favor, preencha todos os campos do login.");
        } else {
            alert("Login realizado com sucesso!");
            // Em Flask, o redirecionamento deve ser feito no backend após autenticação
            window.location.href = "{{ url_for('controller_form.exibir_index') }}";
        }
    });
});