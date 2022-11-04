from flask import render_template, request, redirect
from app import app
from models.book_manager import books, add_new_book, remove_book
from models.book import Book

@app.route('/books')
def index():
    return render_template('index.html', title='Home', books=books)