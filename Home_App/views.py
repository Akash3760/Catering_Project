from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

from Home_App.forms import ImageForm
from Home_App.models import BookNow, Comment, Image, Menu


# Create your views here.
def home(request):
    images = Image.objects.all()
    return render(request, 'home.html', {'images': images})


def about(request):
    return render(request, 'about.html')


def book_now(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        enquiry = request.POST.get('enquiry')
        person = request.POST.get('person')

        if name != '' and email != '' and number != '' and enquiry != '' and person != '':
            data = BookNow(Name=name, Email=email, Number=number, Enquiry=enquiry, Person=person)
            data.save()

        return render(request, 'success_page.html')

    return render(request, 'book_now.html')


def menu_list(request):
    category = request.GET.get('category', '')
    menus = Menu.objects.all()

    if category:
        menus = menus.filter(category=category)

    return render(request, 'menu_list.html', {'menus': menus, 'category': category})


def menu_search(request):
    query = request.GET.get('q', '')
    menus = Menu.objects.filter(name__icontains=query)
    return render(request, 'menu_list.html', {'menus': menus, 'query': query})


def chicken_items(request):
    menus = Menu.objects.filter(category='Chicken Items')
    return render(request, 'menu_list.html', {'menus': menus, 'category': 'Chicken Items'})


def mutton_items(request):
    menus = Menu.objects.filter(category='Mutton Items')
    return render(request, 'menu_list.html', {'menus': menus, 'category': 'Mutton Items'})


def fish_items(request):
    menus = Menu.objects.filter(category='Fish Items')
    return render(request, 'menu_list.html', {'menus': menus, 'category': 'Fish Items'})


def dal(request):
    menus = Menu.objects.filter(category='Dal')
    return render(request, 'menu_list.html', {'menus': menus, 'category': 'Dal'})


def rice(request):
    menus = Menu.objects.filter(category='Rice')
    return render(request, 'menu_list.html', {'menus': menus, 'category': 'Rice'})


def flourbased(request):
    menus = Menu.objects.filter(category='Flourbased')
    return render(request, 'menu_list.html', {'menus': menus, 'category': 'Flourbased'})


def veg(request):
    menus = Menu.objects.filter(category='Veg Menu')
    return render(request, 'menu_list.html', {'menus': menus, 'category': 'Veg Menu'})


def snacks(request):
    menus = Menu.objects.filter(category='Snacks')
    return render(request, 'menu_list.html', {'menus': menus, 'category': 'Snacks'})


def sweets(request):
    menus = Menu.objects.filter(category='Sweets')
    return render(request, 'menu_list.html', {'menus': menus, 'category': 'Sweets'})


def drinks(request):
    menus = Menu.objects.filter(category='Drinks')
    return render(request, 'menu_list.html', {'menus': menus, 'category': 'Drinks'})


def salads(request):
    menus = Menu.objects.filter(category='Salads')
    return render(request, 'menu_list.html', {'menus': menus, 'category': 'Salads'})


def papad(request):
    menus = Menu.objects.filter(category='Papad')
    return render(request, 'menu_list.html', {'menus': menus, 'category': 'Papad'})


def chutney(request):
    menus = Menu.objects.filter(category='Chutney')
    return render(request, 'menu_list.html', {'menus': menus, 'category': 'Chutney'})


def services(request):
    return render(request, 'services.html')


def gallery(request):
    images = Image.objects.all()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = ImageForm()
    return render(request, 'gallery.html', {'images': images, 'form': form})


def success_page(request):
    return render(request, 'success_page.html')


def blog(request):
    return render(request, 'blog.html')


def comment_views(request):
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        name = request.POST.get('name')
        email = request.POST.get('email')

        if comment_text and name and email:
            # Assuming you have a Comment model with fields 'comment_text', 'author', 'email'
            comment = Comment(comment_text=comment_text, author=name, email=email)
            comment.save()
            success_message = 'Comment submitted successfully'
        else:
            success_message = 'Please fill in all required fields'

        return render(request, 'blog.html', {'success_message': success_message})

    # Handle GET requests or rendering the form page
    return render(request, 'blog.html')
