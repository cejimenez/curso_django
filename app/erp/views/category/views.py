from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView

from erp.forms import CategoryForm
from erp.models import Category, Product


def category_list(request):
    data = {
        'title': 'Listado de Categorías',
        'categories': Category.objects.all()
    }
    return render(request, 'category/list.html', data)

class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Category.objects.get(pk=request.POST['id']).toJSON()

        except Exception as error:
            data['error'] = str(error)

        return JsonResponse(data)

    def queryset(self):
        #return Product.objects.all()
        return Category.objects.all()
        #return Category.objects.filter(name__startswith='B')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        #context['object_list'] = Product.objects.all()
        return context


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('erp:category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear una Categoría'
        return context




