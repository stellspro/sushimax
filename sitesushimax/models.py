from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=120, verbose_name='Название продукта')
    description = models.CharField(max_length=255, verbose_name='Описание продукта')
    slug = models.SlugField(max_length=120, unique=True, db_index=True, verbose_name='URL')
    price = models.CharField(max_length=30, verbose_name='Цена')
    discount_price = models.CharField(max_length=30, verbose_name='Цена со скидкой')
    image = models.ImageField(upload_to='images/', blank=True, verbose_name='Изображение')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE, verbose_name='Категория')
    carts = db.relationship('Cart', backref='product', lazy='dynamic')

    def __repr__(self):
        return '{}'.format(self.name)


class Category(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(255))

    def __repr__(self):
        return '{}'.format(self.name)


# Корзина + заказ
class Order(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_name = db.Column(db.String(80))
    phone = db.Column(db.Integer())
    address = db.Column(db.Text)
    payment = db.Column(db.String(15))
    date = db.Column(db.DateTime, default=datetime.now())
    carts = db.relationship('Cart', backref='order', lazy='dynamic')

    def __repr__(self):
        return f'{self.user_name}, адрес: {self.address}, номер телефона: {self.phone}'


class Cart(db.Model):
    order_id = db.Column(db.Integer(), db.ForeignKey('order.id'), primary_key=True)
    product_id = db.Column(db.Integer(), db.ForeignKey('product.id'), primary_key=True)
    count = db.Column(db.Integer())
