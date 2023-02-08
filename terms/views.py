from django.shortcuts import render
from django.views.generic import ListView
from terms.models import Keyword

# Create your views here.
# ***************************************
# def all_name(request):
#     keywords = Keyword.objects.all().order_by("name")
#     context = {
#         'keywords': keywords
#     }
#     return render(request, 'all_name.html', context)

class AllKeywordsView(ListView):
    model = Keyword
    template_name = "terms/all_name.html"