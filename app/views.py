from django.shortcuts import render, get_object_or_404,redirect
from .models import Item
from django.views.generic import ListView,DetailView
from django.db.models import Q
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Sum
# Create your views here.
# def home(request):
#     context = {
#         'contacts': Contact.objects.all()
#     }
#     return render(request,'index.html', context)

# def detail(request,id):
#     context ={
#         'contact':get_object_or_404(Contact,pk=id)

#     }
#     return render(request,'detail.html',context)



class HomePageView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    model = Item
    context_object_name = 'items'
    

    def get_queryset(self):
        items = super().get_queryset()
        
        return items.filter(manager = self.request.user)
    
    @login_required
    def total(self):
        context = {
        'total_cost': Item.objects.all().aggregate(Sum('cost'))      
        }
        return render(self,'index.html',context)
    
    # def total(self):
    #     return Item.objects.aggregate(Sum('cost'))

class ItemDetailView(LoginRequiredMixin, DetailView):
    template_name = "detail.html"
    model = Item
    context_object_name = 'item'
    
@login_required
def search(request):   
    if request.GET:
        search_term = request.GET['search_term']
        search_results = Item.objects.filter(
            Q(name__icontains=search_term) |
            Q(category__icontains=search_term) |
            Q(info__icontains=search_term) | 
            Q(cost__iexact=search_term) 
        )
        context = {
        'search_term':search_term,
        'items':search_results.filter(manager=request.user)
        }
        return render(request,'search.html',context)
    else:
        return redirect('home')

class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    template_name =  'create.html'
    fields = ['name','category','info','image','cost']

    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.manager = self.request.user
        instance.save()
        messages.success(self.request,"Your Item has been created!")
        return redirect('home')

class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    template_name =  'update.html'
    fields = ['name','category','info','image','cost']
    success_url = '/'

    def form_valid(self,form):
        instance = form.save()
        messages.success(self.request,"Your Item has been Updated!")
        return redirect('detail',instance.pk)
    
class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    template_name = 'delete.html'
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,"Your Item has been deleted!")
        return super().delete(self, request, *args, **kwargs)

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')
