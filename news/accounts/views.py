from django.shortcuts import render, redirect

from .forms import CreateUser


def signup(request):
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post:post_list')
    else:
        form = CreateUser()
        return render('accounts/singuu.html')
        
        

