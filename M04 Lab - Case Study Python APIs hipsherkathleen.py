from flask import Flask

app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), unique=True, nullab)
    author = db.Column(db.String(100))
    publisher = db.Column(db.String(100))

    def __repr__(self):
        return {'id': self.id, 'book_name': self.book_name, 'author': self.author, 'publisher': self.publisher}


@app.route('/books')
def get_books():
    books = Book.query.all()

    output = []
    for book in books:
        book_data = {'id': book.id, 'name': book.name, 'author': book.author, 'publisher': book.publisher}

        output.append(book.data)

    return {"books": output}

@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {'id': book.id, 'name': book.name, 'author': book.author, 'publisher': book.publisher}

@app.rout('/books', methods=['POST'])
def add_book(id):
    book = Book(book_id=request.json['id'], book_name=request.json['name'], author=request.json['author'], publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return{'id': book.id, 'name': book.name, 'author': book.author, 'publisher': book.publisher}

@app route('/books'<id>, methods=['DELETE'])
def delete_book(id):
    book =  Book.query.get(id)
    if book is None:
        return{"error": "not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "No book found!"}