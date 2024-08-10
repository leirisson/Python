document.getElementById('fetch-vendas-btn').addEventListener('click', fetchVendas);

function fetchVendas() {
    axios.get('http://127.0.0.1:8000/vendas')
    .then(response => {
        const vendasContainer = document.getElementById('vendas-container');
        vendasContainer.innerHTML = ''; // Limpa o container antes de adicionar os itens

        response.data.forEach(venda => {
            const vendaCard = document.createElement('div');
            vendaCard.className = 'venda-card';

            vendaCard.innerHTML = `
                <h3>${venda.produto}</h3>
                <p>ID: ${venda.id}</p>
                <p>Quantidade: ${venda.quantidade}</p>
                <p>Valor: R$ ${venda.valor.toFixed(2)}</p>
            `;

            vendasContainer.appendChild(vendaCard);
        });
    })
    .catch(error => {
        console.error('Erro na requisição:', error);
    });
}
