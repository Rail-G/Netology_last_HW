from dotenv import find_dotenv
import json
from os import getenv
from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

find_dotenv()

dsn = getenv('DSN')
engine = create_engine(dsn)
sema = sessionmaker(engine)
session = sema()

create_table(engine)

with open('tests_data.json', 'r') as file:
    data = json.load(file)

# for i in data:
#     if i['model'] == 'publisher':
#         session.add(Publisher(id=i['pk'], **i['fields']))
#     elif i['model'] == 'book':
#         session.add(Book(id=i['pk'], **i['fields']))
#     elif i['model'] == 'shop':
#         session.add(Shop(id=i['pk'], **i['fields']))
#     elif i['model'] == 'stock':
#         session.add(Stock(id=i['pk'], **i['fields']))
#     elif i['model'] == 'sale':
#         session.add(Sale(id=i['pk'], **i['fields']))
#     session.commit()

for i in data:
    datas = {'publisher': Publisher, 'book': Book, 'shop': Shop, 'stock': Stock, 'sale': Sale}[i['model']]
    session.add(datas(id=i['pk'], **i['fields']))
    session.commit()


