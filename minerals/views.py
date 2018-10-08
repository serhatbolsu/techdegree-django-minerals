import random

from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Mineral


# Create your views here.

def mineral_list(request):
    minerals = Mineral.objects.all()
    return render(request, 'minerals/mineral_list.html', {'minerals': minerals})


def mineral_detail(request, pk):
    mineral = get_object_or_404(Mineral, pk=pk)
    attributes = vars(mineral)
    filter_attr = ['id', '_state', 'name', 'image_filename',
                   'image_caption', 'category', 'formula',
                   'strunz_classification']
    res = map(lambda x: (x[0].replace("_", " "), x[1]),
              filter(
                  lambda x: x[0] not in filter_attr and x[1], attributes.items()))
    attr = dict(res)
    return render(request, 'minerals/mineral_detail.html',
                  {'mineral': mineral, 'attr': attr})


def random_mineral(request):
    count = Mineral.objects.count()
    picked = random.randint(1,count)
    return mineral_detail(request, picked)



# class IndexView(generic.ListView):
#     template_name = 'minerals/index.html'
#     context_object_name = 'minerals'
#
#     def get_queryset(self):
#         """Returns all the minerals"""
#         return Mineral.objects.all()


# class DetailView(generic.DetailView):
#     model = Mineral
#
#     def get_context_data(self, **kwargs):
#         context = super(DetailView, self).get_context_data(**kwargs)
#         # print(context)
#         attributes = vars(context['mineral'])
#         filter_attr = ['id', '_state', 'name', 'image_filename',
#                        'image_caption']
#         res = map(lambda x: (x[0].replace("_", " ").title(),x[1]),
#                   filter(
#                       lambda x: x[0] not in filter_attr and x[1], attributes.items()))
#         context['attr'] = dict(res)
#
#         print(context['attr'])
#         return context

