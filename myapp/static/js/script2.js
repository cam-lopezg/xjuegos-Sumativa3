document.addEventListener('DOMContentLoaded', function () {
   
    const registrationButton = document.getElementById('registration');
    const loginButton = document.getElementById('login');
    const shoppingCartButton = document.getElementById('shoppingCart');
    


 
    // Agregar evento clic al botón "Registrate!"
    registrationButton.addEventListener('click', function () {
        // Redirigir a la página de registro (Form.html)
        window.location.href = 'Form.html';
    });

    // Agregar evento clic al botón "Iniciar sesión"
    loginButton.addEventListener('click', function () {
        // Redirigir a la página de inicio de sesión (Login.html)
        window.location.href = 'Login.html';
    });

    shoppingCartButton.addEventListener('click', function () {
        // Redirigir a la página del carrito
        window.location.href = 'carrito.html';
    });

});
