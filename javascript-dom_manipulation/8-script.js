const FilmList = document.querySelector('#list_movies');

fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then((response) => response.json())
    .then((data) => {
        for (let index = 0; index < data.results.length; index++) {
            const NewFilm = document.createElement('li');
            NewFilm.textContent = data.results[index].title;
            FilmList.appendChild(NewFilm);
        }
    });