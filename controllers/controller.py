from flask import render_template, request, redirect
from app import app
from models.book_manager import books, add_new_book, remove_book, check_in_book, check_out_book
from models.book import Book

@app.route('/books')
def index():
    return render_template('index.html', title='Home', books=books)

@app.route('/books/<index>')
def single_book(index):
  chosen_book = books[int(index)]
  return render_template('book.html', title= 'Book Information', books=books, book=chosen_book)

#   order=orders[int(order_id)]

@app.route('/books', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    checked_out = True if 'checked_out' in request.form else False
    description = request.form['description']
    new_book = Book(title, author, genre, checked_out, description)
    add_new_book(new_book)
    return render_template('index.html', title='Home', books=books)

@app.route('/books/delete/<index>', methods=['POST'])
def delete_book(index):
    remove_book(int(index))
    return redirect('/books')

@app.route('/books/check_out/<index>', methods=['POST'])
def checkout_book(index):
    check_out_book(int(index))
    return redirect(request.referrer)

@app.route('/books/check_in/<index>', methods=['POST'])
def checkin_book(index):
    check_in_book(int(index))
    return redirect(request.referrer)

