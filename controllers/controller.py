from flask import render_template, request, redirect
from app import app
from models.book_manager import books, add_new_book, remove_book
from models.book import Book

@app.route('/books')
def index():
    return render_template('index.html', title='Home', books=books)

@app.route('/books', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    checked_out = True if 'checked_out' in request.form else False
    new_book = Book(title, author, genre, checked_out)
    add_new_book(new_book)
    return render_template('index.html', title='Home', books=books)

@app.route('/books/delete/<index>', methods=['POST'])
def delete_event(index):
    remove_book(int(index))
    return redirect('/books')
