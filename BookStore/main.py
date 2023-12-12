from dotenv import load_dotenv
from models import *
from os import getenv
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker



dsn = getenv('DSN')
engine = create_engine(dsn)

semaker = sessionmaker(engine)
session = semaker()

def _check(id_name):
    if id_name.isdigit():
        correct_publisher = session.query(Publisher.id).filter(Publisher.id == int(id_name)).all()
        for i in correct_publisher:
            if int(id_name) in i:
                return True

    else:
        correct_publisher = session.query(Publisher.name).filter(Publisher.name == id_name).all()
        for i in correct_publisher:
            if id_name in i:
                return True

def info():
    publish = input('Введите ID или имя издателя: ')
    list_ = []
    if _check(publish) == True:
        if publish.isdigit():
            shops = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).join(Stock, Stock.id_book == Book.id).join(Shop).join(Sale, Sale.id_stock == Stock.id).join(Publisher).filter(Publisher.id == int(publish)).all()
        else:
            shops = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).join(Stock, Stock.id_book == Book.id).join(Shop).join(Sale, Sale.id_stock == Stock.id).join(Publisher).filter(Publisher.name == publish).all()
        for i in shops:
            list_.append('{:<40} | {:<10} | {:<7} | {}'.format(i[0],i[1],i[2],i[3].strftime('%d/%B/%Y %H:%M:%S')))
    else:
        return 'Такого пользователя не существует!'
    return '\n'.join(list_)

if __name__ == '__main__':
    print(info())
