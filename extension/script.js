fetch('https://icanhazdadjoke.com/', {
    headers: {
        'Accept': 'application/json'
    }
})
.then(response => response.json())
.then(data => {
    const jokeText = data.joke;
    const jokeElement = document.getElementById('jokeElement');
    jokeElement.innerText = jokeText;
})
.catch(error => {
    console.error('Error fetching joke:', error);
    const jokeElement = document.getElementById('jokeElement');
    jokeElement.innerText = 'Failed to fetch joke.';
});
