document.addEventListener('DOMContentLoaded', function () {
    const logoButton = document.getElementById('logoButton');

    logoButton.addEventListener('click', function () {
        // Redirigir a la página principal (principal.html)
        window.location.href = 'principal.html';
    });
});


document.addEventListener('DOMContentLoaded', function() {
    const addToCartButtons = document.querySelectorAll('.add-to-cart');
    addToCartButtons.forEach(button => {
        button.addEventListener('click', function() {
            const nombre = this.getAttribute('data-nombre');
            const precio = this.getAttribute('data-precio');
            console.log("llamada a agregar carrito")
            fetch('/agregar-al-carrito/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')  // Asegúrate de incluir el CSRF token
                },
                body: JSON.stringify({nombre: nombre, precio: precio})
            })
            .then(response => response.json())
            .then(data => {
                alert('Producto agregado al carrito!');
                // Actualiza el contador del carrito aquí si es necesario
            })
            .catch(error => console.error('Error:', error));
        });
    });
});

// Función para obtener el valor de una cookie por nombre
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
