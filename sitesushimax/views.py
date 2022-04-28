import json

from django.forms import model_to_dict
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import ListView, CreateView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, ProductCategory, TestModel, Order, Cart
from rest_framework import generics, viewsets
from .serializers import ProductSerializer, TestSerializer
from .utils import DataMixin
from .forms import OrderingForm


class IndexPage(DataMixin, ListView):
    """Главная страница"""
    # model = Product
    template_name = 'sitesushimax/index.html'

    # context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        con = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(con.items()))

    def get_queryset(self):
        return Product.objects.all()


class PizzaPage(DataMixin, ListView):
    """Страница - пиццы"""
    template_name = 'sitesushimax/pizza.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        con = self.get_user_context(title='Пиццы')
        return dict(list(context.items()) + list(con.items()))

    def get_queryset(self):
        return Product.objects.all()


class SushiPage(DataMixin, ListView):
    """Страница - роллы"""
    template_name = 'sitesushimax/sushi.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        con = self.get_user_context(title='Суши')
        return dict(list(context.items()) + list(con.items()))

    def get_queryset(self):
        return Product.objects.all()


class SnacksPage(DataMixin, ListView):
    """Страница - казуски"""
    template_name = 'sitesushimax/snacks.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        con = self.get_user_context(title='Закуски')
        return dict(list(context.items()) + list(con.items()))

    def get_queryset(self):
        return Product.objects.all()


class SaladsPage(DataMixin, ListView):
    """Страница - салаты"""
    template_name = 'sitesushimax/salads.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        con = self.get_user_context(title='Салаты')
        return dict(list(context.items()) + list(con.items()))

    def get_queryset(self):
        return Product.objects.all()


class CartPage(DataMixin, ListView):
    """Страница - корзина"""
    template_name = 'sitesushimax/my_cart.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        con = self.get_user_context(title='Корзина')
        return dict(list(context.items()) + list(con.items()))

    def get_queryset(self):
        return Product.objects.all()


@csrf_exempt
def checkout(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        print(data)
        print(data['id'])
    # s = x.decode()
    # print(type(s))
        name = data['user_name']
        phone = data['phone']
        address = data['address']
        payment = data['payment']
        products_id = data['id']
        products_coast = data['coast']
        # product = Product.objects.all().order_by('id')
        order = Order(user_name=name, phone=phone, address=address, payment=payment)
        order.save()
        print(products_id, products_coast)
        for i in range(len(products_id)):
            product = Product.objects.get(pk=products_id[i])
            cart = Cart(order_id=order, product_id=product, coast=products_coast[i])
            cart.save()
            print('Успешно')
    return render(request, 'sitesushimax/index.html')


class OrderingPage(CreateView):
    form_class = OrderingForm
    template_name = 'sitesushimax/order.html'
    success_url = reverse_lazy('home')


class ProductViewSet(viewsets.ModelViewSet):
    """Отображение всех продуктов"""
    queryset = Product.objects.all().order_by('pk')
    serializer_class = TestSerializer

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = ProductCategory.objects.get(pk=pk)
        return Response({'cats': cats.name})


class PizzaViewSet(viewsets.ModelViewSet):
    """Отображение - пиццы"""
    queryset = Product.objects.filter(category_id=1)
    serializer_class = TestSerializer

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = ProductCategory.objects.get(pk=pk)
        return Response({'cats': cats.name})


class SushiViewSet(viewsets.ModelViewSet):
    """Отображение - роллы"""
    queryset = Product.objects.filter(category_id=2)
    serializer_class = TestSerializer

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = ProductCategory.objects.get(pk=pk)
        return Response({'cats': cats.name})


class SnacksViewSet(viewsets.ModelViewSet):
    """Отображение - закуски"""
    queryset = Product.objects.filter(category_id=3)
    serializer_class = TestSerializer

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = ProductCategory.objects.get(pk=pk)
        return Response({'cats': cats.name})


class SaladsViewSet(viewsets.ModelViewSet):
    """Отображение - салаты"""
    queryset = Product.objects.filter(category_id=4)
    serializer_class = TestSerializer

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = ProductCategory.objects.get(pk=pk)
        return Response({'cats': cats.name})

# def show_salads(requests):
#     products = {}
#     salads = Product.objects.filter(category_id=4)
#     for i in salads:
#         b = {'id': f'{i.id}', 'name': f'{i.name}', 'description': f'{i.description}', 'price': f'{int(i.price)}',
#              'image': f'{i.image}'}
#         products[i.id] = b
#     json_products = json.dumps(products)
#     return json_products

# class IndexListAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = TestSerializer
#
#
# class IndexAPIUpdate(generics.UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = TestSerializer
#
#
# class ProductAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = TestSerializer


# class IndexAPIView(APIView):
#     def get(self, request):
#         product_list = TestModel.objects.all().values()
#         return Response({'products': list(product_list)})
#
#     def post(self, request):
#         serializer = TestSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method PUT not allowed'})
#
#         try:
#             instance = TestModel.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Объект не найден'})
#
#         serializer = TestSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method DELETE not allowed'})
#
#         try:
#             instance = TestModel.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Объект не найден'})
#
#         instance.delete()
#         return Response({'post': f'Запись {instance.pk} успешно удалена'})
