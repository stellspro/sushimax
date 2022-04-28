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

    # carts = models.ManyToManyField('Cart')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ProductCategory(models.Model):
    name = models.CharField(max_length=120, verbose_name='Название категории')
    slug = models.SlugField(max_length=120, unique=True, db_index=True, verbose_name='URL')
    description = models.CharField(max_length=250, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория продуктов'
        verbose_name_plural = 'Категории продуктов'


class Order(models.Model):
    user_name = models.CharField(max_length=120, verbose_name='Имя покупателя')
    phone = models.CharField(max_length=15, verbose_name='Телефон')
    address = models.TextField(verbose_name='Адрес покупателя')
    payment = models.BooleanField(verbose_name='Способ оплаты')
    data = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Cart(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Номер заказа')
    product_id = models.OneToOneField(Product, on_delete=models.CASCADE, verbose_name='Номер продукта')
    coast = models.IntegerField(verbose_name='Количество')


    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


# Корзина + заказ
# class Order(db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     user_name = db.Column(db.String(80))
#     phone = db.Column(db.Integer())
#     address = db.Column(db.Text)
#     payment = db.Column(db.String(15))
#     date = db.Column(db.DateTime, default=datetime.now())
#     carts = db.relationship('Cart', backref='order', lazy='dynamic')
#
#     def __repr__(self):
#         return f'{self.user_name}, адрес: {self.address}, номер телефона: {self.phone}'
#
#
# class Cart(db.Model):
#     order_id = db.Column(db.Integer(), db.ForeignKey('order.id'), primary_key=True)
#     product_id = db.Column(db.Integer(), db.ForeignKey('product.id'), primary_key=True)
#     count = db.Column(db.Integer())


class TestModel(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name
