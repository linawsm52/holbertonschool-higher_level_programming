fetch('https://hbtn.io')
  .then(response => response.json())
  .then(data => {
    document.querySelector('#character').textContent = data.name;
  });
