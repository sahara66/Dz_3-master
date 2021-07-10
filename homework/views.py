from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, redirect

from homework.forms import ProductForm, UserCreationForm, LoginForm
from homework.models import Product, Category


PAGE_SIZE = 3


def get_all_product(request):
    word = request.GET.get('search', '')
    page = int(request.GET.get('page', 1))

    category = Category.objects.filter(name__contains=word)
    count = category.count()
    print(count // PAGE_SIZE)
    if count % PAGE_SIZE == 0:
        buttons = count // PAGE_SIZE
    else:
        buttons = count // PAGE_SIZE + 1
        print([i for i in range(1, buttons + 1)])
    start = (page - 1) * PAGE_SIZE
    end = page * PAGE_SIZE
    data = {
        'all_product': category[start:end],
        'username': auth.get_user(request).username,
        'buttons': [i for i in range(1, buttons + 1)]
    }
    return render(request, 'product.html', context=data)


def get_one_product(request, id):
    category = Category.objects.get(id=id)
    product = Product.objects.filter(category_id=id)
    data = {
        'product': product,
        'category': category
    }
    return render(request, 'detail.html', context=data)


def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('product_name', '')
        Category.objects.create(name=name)
        return redirect('/product/')
    return render(request, 'add.html', context={
        'username': auth.get_user(request).username
    })


def add(request):
    if request.method == 'POST':
        print(request.POST)
        form = ProductForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/product/')
        else:
            return render(request, 'add1.html', context={
                'form': form
            })
    data = {
        'form': ProductForm()
    }
    return render(request, 'add1.html', context=data)


def main_page(request):
    data = {
        'username': auth.get_user(request).username
    }
    return render(request, "main.html", context=data)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            print('POST запрос без ошибок')
            return redirect('/admin/')
        else:
            print('POST запрос с ошибкой')
            return render(request, 'register.html', context={'form': form})

    data = {
        'form': UserCreationForm(),
        'username': auth.get_user(request).username
    }
    print('GET запрос')
    return render(request, 'register.html', context=data)


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = auth.authenticate(
                username=form.cleaned_data['username'], password=form.cleaned_data['password']
            )
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                return render(request, 'login.html', context={'form': form})
    data = {
        'form': LoginForm(),
        'username': auth.get_user(request).username
    }
    return render(request, 'login.html', context=data)


def logout(request):
    auth.logout(request)
    return redirect('/')


def add_products(request):
    if request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/students/')
        else:
            data = {
                'form': form,
                'username': auth.get_user(request).username
            }
            return render(request, 'add_products.html', context=data)
    data = {
        'form': ProductForm(),
        'username': auth.get_user(request).username
    }
    return render(request, 'add_products.html', context=data)


def products(request):
    data = {
        'products': Product.objects.all(),
        'username': auth.get_user(request).username
    }
    return render(request, 'products.html', context=data)