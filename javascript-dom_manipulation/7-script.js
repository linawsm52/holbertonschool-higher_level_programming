fetch('https://hbtn.io')
  .then(response => response.json())
  .then(data => {
    const movies = data.results;
    const listElement = document.querySelector('#list_movies');
    
    movies.forEach(movie => {
      const listItem = document.createElement('li');
      listItem.textContent = movie.title;
      listElement.appendChild(listItem);
    });
  });
