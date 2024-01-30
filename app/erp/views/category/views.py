
from django.shortcuts import render
from django.views.generic import ListView

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

    def queryset(self):
        #return Product.objects.all()
        #return Category.objects.all()
        return Category.objects.filter(name__startswith='B')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        #context['object_list'] = Product.objects.all()
        return context

