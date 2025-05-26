document.addEventListener("DOMContentLoaded", function () {
    // Adiciona um campo de busca acima da tabela
    const tabelaContainer = document.querySelector(".Tabela1");
    if (tabelaContainer) {
        const searchContainer = document.createElement("div");
        searchContainer.innerHTML = `
            <div class="mb-3">
                <label for="searchInput" class="form-label">Buscar Usuário:</label>
                <input type="text" id="searchInput" class="form-control" placeholder="Digite o nome do usuário ou email">
            </div>
        `;
        tabelaContainer.insertBefore(searchContainer, tabelaContainer.firstChild);

        // Adiciona evento de busca dinâmica
        const searchInput = document.getElementById("searchInput");
        searchInput.addEventListener("input", function () {
            const searchValue = searchInput.value.toLowerCase();
            const rows = document.querySelectorAll(".LinhaTabela");

            rows.forEach((row, idx) => {
                // Ignora o cabeçalho (primeira linha)
                if (idx === 0) return;
                const username = row.children[1]?.textContent.toLowerCase() || "";
                const email = row.children[2]?.textContent.toLowerCase() || "";

                if (username.includes(searchValue) || email.includes(searchValue)) {
                    row.style.display = "";
                    row.style.backgroundColor = "#d1e7dd";
                } else {
                    row.style.display = "none";
                    row.style.backgroundColor = "";
                }
            });
        });
    }
});