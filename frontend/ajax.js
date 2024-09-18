const form = document.getElementById('productForm');
const productTableBody = document.getElementById('productTableBody');

form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = new FormData(form);
    const response = await fetch('/api/products', {
        method: 'POST',
        body: formData
    });

    if (response.ok) {
        const data = await response.json();
        updateProductList();
        form.reset();
    } else {
        console.error('Ошибка при добавлении продукта');
    }
});

async function updateProductList() {
    const response = await fetch('/api/products');
    const data = await response.json();

    productTableBody.innerHTML = '';
    data.forEach(product => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${product.name}</td>
            <td>${product.description}</td>
            <td>${product.price}</td>
        `;
        productTableBody.appendChild(row);
    });
}

// Инициальная загрузка списка продуктов
updateProductList();