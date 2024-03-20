import React, { useState, useEffect } from 'react';
import BASE_URL from './api';

function BookList() {
    const [books, setBooks] = useState([]);
    const [formData, setFormData] = useState({
        title: '',
        author: '',
        genre: 'Fantasy' // Default genre
    });
    const [csrfToken, setCsrfToken] = useState('');

    useEffect(() => {
        fetchCsrfToken();
        fetchBooks();
    }, []);

    const fetchCsrfToken = () => {
        fetch(`${BASE_URL}/api/csrf/`, { allowCredentials : 'true' }) // Ensure you set 'credentials: include' to send cookies
            .then(res => res.json())
            .then(data => setCsrfToken(data.csrfToken))
            .catch(error => console.error('Error fetching CSRF token:', error));
    };

    const fetchBooks = () => {
        fetch(`${BASE_URL}/books/`)
            .then(res => res.json())
            .then(data => setBooks(data))
            .catch(error => console.error('Error fetching books:', error));
    };

    const handleSubmit = (ev) => {
        ev.preventDefault();
        const data = {
            'title': formData.title,
            'author': formData.author,
            'genre': formData.genre
        };

        fetch(`${BASE_URL}/books/`, {
            body: JSON.stringify(data),
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
        })
            .then(() => {
                fetchBooks(); // Refresh book list after adding a new book
                setFormData({
                    title: '',
                    author: '',
                    genre: 'Fantasy' // Reset genre to default after adding a new book
                });
            })
            .catch(error => console.error('Error submitting book:', error));
    };

    const handleChange = (ev) => {
        setFormData({
            ...formData,
            [ev.target.name]: ev.target.value
        });
    };

    return (
        <div>
            <form onSubmit={handleSubmit} id="form-create-book">
                <input type="text" name="title" value={formData.title} onChange={handleChange} placeholder="Book Title" />
                <input type="text" name="author" value={formData.author} onChange={handleChange} placeholder="Book Author" />
                <select name="genre" value={formData.genre} onChange={handleChange}>
                    <option value="Fantasy">Fantasy</option>
                    <option value="SciFi">SciFi</option>
                </select>
                <button type="submit" id="btn-submit">Add Book</button>
            </form>
            <div>
                <h1>Book List</h1>
                <ul id="book-list">
                    {books.map(book => (
                        <li key={book.id}>{book.title}</li>
                    ))}
                </ul>
            </div>
        </div>
    );
}

export default BookList;