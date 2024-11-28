document.addEventListener('DOMContentLoaded', function() {
    const likeButton = document.querySelector('.like-button');
    const likesCount = document.querySelector('.likes-count');
    
    if (likeButton) {
        likeButton.addEventListener('click', function(e) {
            e.preventDefault(); // Zapobiegaj przeładowaniu strony
            
            const postId = likeButton.getAttribute('data-post-id');
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            // Wysłanie zapytania do serwera za pomocą fetch
            fetch(`/post/${postId}/like/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    'post_id': postId
                })
            })
            .then(response => response.text())  // Używamy .text() zamiast .json()
            .then(data => {
                console.log("Odpowiedź z serwera:", data);  // Sprawdzamy odpowiedź przed parsowaniem

                try {
                    const jsonResponse = JSON.parse(data);  // Parsujemy odpowiedź jako JSON

                    if (jsonResponse.liked !== undefined) {
                        likeButton.textContent = jsonResponse.liked ? 'Unlike' : 'Like';
                        likesCount.innerHTML = `<strong>Likes:</strong> ${jsonResponse.likes_count}`;
                    }
                } catch (error) {
                    console.error('Błąd parsowania JSON:', error);
                }
            })
            .catch(error => console.error('Błąd:', error));
        });
    }
});
