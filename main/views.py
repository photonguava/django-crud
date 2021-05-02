from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Exhibit
from django.core import serializers
from django.views.generic import TemplateView,UpdateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.

def index(request):
    context={
        'exhibits':Exhibit.objects.all()
    }
    return render(request,'art-home.html',context=context)


class AddExhibitView(TemplateView):
    template_name = 'index.html'
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        title = request.POST['title']
        artist = request.POST['artist']
        description = request.POST['description']
        if 'sale' in request.POST:
            for_sale = request.POST['sale']
        else:
            for_sale = False
        date = request.POST['date']
        price = float(request.POST['price'])
        quantity = int(request.POST['quantity'])
        image = request.FILES['image']
        newExhibit = Exhibit(
            title=title,
            artist=artist,
            description=description,
            for_sale=for_sale,
            image=image,
            date=date,
            price=price,
            quantity=quantity
        )
        newExhibit.save()
        return render(request,self.template_name)
    
@method_decorator(csrf_exempt, name='dispatch')
class APIView(TemplateView):
    template_name = 'crud.html'
    def get(self,request,pk=''):
        exhibits = Exhibit.objects.all()
        exhibits = serializers.serialize('json',exhibits)
        return HttpResponse(exhibits,content_type="text/json-comment-filtered")
    def delete(self,request,pk):
        to_delete = Exhibit.objects.get(pk=pk)
        to_delete.delete()
        return HttpResponse('Success')



class ListExhibitView(TemplateView):
    template_name = 'crud.html'
    def get(self,request):
        return render(request, self.template_name)

class DeleteExhibitView(TemplateView):
    def get(self,request,pk):
        to_delete = Exhibit.objects.get(pk=pk)
        to_delete.delete()
        return redirect('list-exhibit')


class UpdateExhibitView(TemplateView):
    template_name = 'update.html'
    def get(self,request,pk):
        to_update = Exhibit.objects.get(pk=pk)
        context = {
            'exhibit': to_update
        }
        return render(request,self.template_name,context)
    def post(self,request,pk):
        title = request.POST['title']
        artist = request.POST['artist']
        description = request.POST['description']
        if 'sale' in request.POST:
            for_sale = request.POST['sale']
        else:
            for_sale = False
        
        to_update = Exhibit.objects.get(pk=pk)
        to_update.title = title
        to_update.artist = artist
        to_update.description = description
        if 'image' in request.FILES:
            to_update.image = request.FILES['image']
        else:
            pass
        if 'sale' in request.POST:
            to_update.for_sale = True
        else:
            to_update.for_sale = False
        to_update.save()
        return redirect('list-exhibit')