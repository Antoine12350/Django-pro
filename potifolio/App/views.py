from django.shortcuts import render

def home(request):
    return render(request, 'portfolio/index.html')

def about(request):
    return render(request, 'portfolio/about.html')

def contact(request):
    return render(request, 'portfolio/contact.html')
from django.http import HttpResponse
from django.template import loader
from .models import Member

def all_members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('portfolio/all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


## forms Exercise

from django.shortcuts import render, redirect
from .models import Member
from .forms import UserForm

def all_members(request):
    users = Member.objects.all()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portfolio/all_members')
    else:
        form = UserForm()
    
    return render(request, 'portfolio/all_members.html', {'users': users, 'form': form})
