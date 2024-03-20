import React, { useState, useEffect } from 'react';

function BookList() {
    const [books, setBooks] = useState([]);

    useEffect(() => {
        fetch('/books/')
            .then(response => response.json())
            .then(data => setBooks(data))
            .catch(error => console.error('Error fetching books:', error));
    }, []);

    return (
        <div>
            <h1>Book List</h1>
            <ul>
                {books.map(book => (
                    <li key={book.id}>
                        <strong>{book.title}</strong> by {book.author}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default BookList;