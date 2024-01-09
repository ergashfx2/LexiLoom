const searchInput = document.getElementById('searchInput');
const suggestionsList = document.getElementById('suggestionsList');
const searchIcon = document.getElementById('searchIcon');

searchInput.addEventListener('input', function () {
    const userInput = this.value.toLowerCase();

    if (userInput.trim() === '') {
        // If input is empty, hide the suggestions list
        suggestionsList.innerHTML = '';
        suggestionsList.style.display = 'none';
        return;
    }

    fetch(`/get_english_word_suggestions/?term=${userInput}`)
        .then(response => response.json())
        .then(data => {
            renderSuggestions(data);
        })
        .catch(error => {
            console.error('Error fetching suggestions:', error);
        });
});

searchIcon.addEventListener('click', function () {
    // If the search icon is clicked, redirect to the view
    const selectedWord = searchInput.value.trim();
    window.location.href = `/get_word_definition/${selectedWord}/`;
});

searchInput.addEventListener('keydown', function (e) {
    if (e.key === 'Enter') {
        // If the user presses Enter, redirect to the view
        const selectedWord = this.value.trim();
        window.location.href = `/get_word_definition/${selectedWord}/`;
    }
});

function renderSuggestions(suggestions) {
    const html = suggestions.map(suggestion => `<a href="/get_word_definition/${suggestion}" class="suggestion">${suggestion}</a><br>`).join('');
    suggestionsList.innerHTML = html;

    // Show the suggestions list
    suggestionsList.style.display = 'block';

    // Add event listener to suggestionsList (if needed)
    // This could be used to handle click events on the entire suggestionsList
    suggestionsList.addEventListener('click', function (e) {
        // Handle clicks on the suggestionsList if needed
    });

    // Alternatively, you can add event listeners to each suggestion link
    const suggestionLinks = suggestionsList.querySelectorAll('.suggestion');
    suggestionLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const selectedWord = this.innerText;
            window.location.href = `/get_word_definition/${selectedWord}/`;
        });
    });
}
