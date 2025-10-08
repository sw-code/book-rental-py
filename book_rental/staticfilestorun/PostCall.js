//Post
const asyncPostCall = async (BookName,BookDescription) => {
const csrfToken = document.getElementById('csrf').getAttribute('content');

    try {
        console.log(csrfToken);
        const response = await fetch('/api/books/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify({
                BookName: BookName,
                BookDescription: BookDescription
            })
        });
        const data = await response.json();
        console.log(data);
    } catch(error) {
        console.log(error)
    }
}
//asyncPostCall()