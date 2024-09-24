console.log('Página cargada con éxito');
const form = document.querySelector('form');
form.addEventListener('submit', function(event) {
  event.preventDefault();
  alert('¡Gracias por contactarnos! Hemos recibido tu mensaje.');
  form.reset();
});
