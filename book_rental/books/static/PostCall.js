//Post
const asyncPostCall = async (BookName,BookDescription) => {
    try {
        const response = await fetch('/api/books/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
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