from django.shortcuts import render, reverse, HttpResponseRedirect
from .forms import PopUpForm
from .models import Services, Time, Posts, Review,User
import users.models
from .models import HeaderThings


# Create your views here.

def main_page(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            form = PopUpForm(data=request.POST)
            if form.is_valid():
                user = users.models.User.objects.get(username=request.user.username)
                name = Services.objects.filter(name=form.data['service']).first()
                model_time = Time.objects.filter(time=form.data["time"]).first()
                model_posts = Posts.objects.filter(name=name, date=form.data['date'], time=model_time, user=user)
                if model_posts:
                    return HttpResponseRedirect(reverse('product:main'))
                else:
                    model_posts = Posts(user=user, name=name, pet_name=form.data['pet_name'], date=form.data['date'],
                                        phone=form.data['phone'], email=form.data['email'], time=model_time).save()

    form = Services.objects.all()[:3]
    form_time = Time.objects.all()
    review = Review.objects.all()[:3]
    things = HeaderThings
    admin = request.user
    context = {
        'services': form,
        'times': form_time,
        'review': review,
        'things': things,
        'admin':admin
    }
    return render(request, "product/index.html", context=context)


def services(request):
    services_model = Services.objects.filter(is_push=True)
    if request.method == 'POST':
        name = request.POST['search']
        list_res = []
        for el in services_model:
            if name in str(el.name).lower():
                list_res.append(el)
        things = HeaderThings
        context = {
            'model': list_res,
            'things': things
        }
        return render(request, 'product/catalog.html', context=context)
    things = HeaderThings
    admin = request.user
    context = {
        'model': services_model,
        'things':things,
        'admin':admin
    }
    return render(request, 'product/catalog.html', context=context)
