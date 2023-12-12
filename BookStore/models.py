from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column as Col, Integer as Int, String as Str, ForeignKey as FK, TIMESTAMP

Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publisher'

    id = Col(Int, primary_key=True)
    name = Col(Str(40), unique=True)

    def __str__(self):
        return f"Издатель: {self.name}"


class Book(Base):
    __tablename__ = 'book'

    id = Col(Int, primary_key=True)
    title = Col(Str(40), nullable=False)
    id_publisher = Col(Int, FK('publisher.id', ondelete='CASCADE'), nullable=False)

    publisher = relationship(Publisher, backref='book')

    def __str__(self):
        return f'Книга: {self.title}'

class Shop(Base):
    __tablename__ = 'shop'

    id = Col(Int, primary_key=True)
    name = Col(Str(40), unique=True)

    def __str__(self):
        return f"Магазин: {self.name}"

class Stock(Base):
    __tablename__ = 'stock'

    id = Col(Int, primary_key=True)
    id_book = Col(Int, FK('book.id', ondelete='CASCADE'), nullable=False)
    id_shop = Col(Int, FK('shop.id', ondelete='CASCADE'), nullable=False)
    count = Col(Int, nullable=False)

    book = relationship(Book, backref='stock')
    shop = relationship(Shop, backref='stock')

    def __str__(self):
        return f"Количество на складе: {self.count}"


class Sale(Base):
    __tablename__ = 'sale'

    id = Col(Int, primary_key=True)
    price = Col(Str(20), nullable=False)
    date_sale = Col(TIMESTAMP, nullable=False)
    id_stock = Col(Int, FK('stock.id', ondelete='CASCADE'), nullable=False)
    count = Col(Int, nullable=False)

    stock = relationship(Stock, backref='sale')

    def __str__(self):
        return f"Цена: {self.price}, Количество к закупке: {self.count}"
    


def create_table(eng):
    Base.metadata.drop_all(eng)
    Base.metadata.create_all(eng)

