document.addEventListener('DOMContentLoaded', function () {
  fetch('https://stefanbohacek.com')
    .then(response => response.json())
    .then(data => {
      document.querySelector('#hello').textContent = data.hello;
    });
});
