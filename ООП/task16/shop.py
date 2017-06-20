from datetime import datetime, date
from pony.orm import Database, Required, Optional, Set, sql_debug, db_session, select, delete

db = Database()


class Category(db.Entity):
    """Категория товара"""
    parent = Optional('Category', reverse='children')
    children = Set('Category', reverse='parent')
    title = Required(str)
    description = Optional(str)
    Product = Set('Product')


class Product(db.Entity):
    """Товар магазина"""
    title = Required(str)
    category = Required(Category)
    price = Required(float)
    description = Optional(str)
    code = Required(int)
    comments = Set('Comment')
    order_items = Set('OrderItem')


class Customer(db.Entity):
    """Покупатель"""
    name = Required(str)
    email = Required(str)
    phone = Required(str)
    login = Required(str)
    password = Required(str)
    address = Optional(str) # Может быть сущностью
    comments = Set('Comment')
    orders = Set('Order')
    cart = Optional('Cart')


class Comment(db.Entity):
    """Комментарий"""
    product = Required(Product)
    customer = Required(Customer)
    text = Required(str)
    created = Optional(datetime)
    rating = Optional(int)
    

class OrderItem(db.Entity):
    """Одна позиция в заказе"""
    product = Required(Product)
    order = Optional('Order')
    amount = Optional(int)


class Order(db.Entity):
    """Заказ"""
    customer = Required(Customer)
    order_items = Set('OrderItem')
    created = Optional(datetime)
    promo_code = Optional(str)
    histories = Set('OrderLog')


class Status(db.Entity):
    """Справочник статусов для других сущностей"""
    name = Required(str)
    order_logs = Set('OrderLog')


class OrderLog(db.Entity):
    """История измеения заказа"""
    order = Required(Order)
    status = Required(Status)
    created = Optional(datetime) #Дата изменения статуса заказа


class Cart(db.Entity):
    """Корзина"""
    customer = Required(Customer)
    products = Required(str) 

sql_debug(True)
db.bind('sqlite', 'shop.sqlite', create_db=True)
db.generate_mapping(create_tables=True)

######################################
##############ДОМАШКА#################
######################################

with db_session:
    #Добавим покупателей и их заказы
    customer1 = Customer(name='Вася Пупкин', email='vasya@yandex.ru', phone='89311111111', password='qwerty', address='spb', login = 'vasya92')
    customer2 = Customer(name='Вова Иванов', email='vova@gmail.com', phone='8931222222', password='qwerty123', address='msk', login = 'vova777')
    customer3 = Customer(name='Петя Сидоров', email='petya666@gmail.com', phone='89313333333', password='Qwerty12345', address='spb', login = 'PETYA')
    order1 = Order(customer = customer1, created = '2017-06-05', promo_code ='mmm')
    order2 = Order(customer = customer1, created = '2017-01-06', promo_code ='nnn')
    order3 = Order(customer = customer2, created = '2016-06-19', promo_code ='aaa')
    order4 = Order(customer = customer2, created = '2015-06-06', promo_code ='vvv')
    order5 = Order(customer = customer3, created = '2017-04-29', promo_code ='kkk')
    order6 = Order(customer = customer3, created = '2017-06-05', promo_code ='ddd')


    #Сделаем запросы
    for i in select(c for c in Order if c.customer.name == 'Вася Пупкин'): #Выведем промокоды из всех заказов у Васи Пупкина
        print(i.promo_code)
    for i in select(c.customer for c in Order if c.id == 1): #Выведем телефон у покупателя из первого заказа
        print(i.phone)
    for i in select(c.customer for c in Order if c.created > date(2017,4,1) and c.created < date(2017,6,30)):#Выведем имена покупателей в заказах из промежутка дат
        print(i.name)
    delete(c for c in Order if c.customer.address == 'spb') #Удалим все заказы у покупателей из СПб