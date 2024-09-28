console.log('Página cargada con éxito');
const form = document.querySelector('form');
form.addEventListener('submit', function(event) {
  event.preventDefault();
  alert('¡Gracias por contactarnos! Hemos recibido tu mensaje.');
  form.reset();
});

<script>
  function redirectToCalendar(psicologo) {
    // Redirigir a la página del calendario del psicólogo
    window.location.href = '/calendario?psicologo=' + psicologo
  }
</script>

