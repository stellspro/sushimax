from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, ProductCategory, TestModel
from rest_framework import generics, viewsets
from .serializers import ProductSerializer, TestSerializer
from utils import DataMixin


# Create your views here.
class IndexPage(DataMixin, ListView):
    model = Product
    template_name = 'sitesushimax/index.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        con = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(con.items()))

    def get_queryset(self):
        return Product.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = TestSerializer

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = ProductCategory.objects.get(pk=pk)
        return Response({'cats': cats.name})

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
