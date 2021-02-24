from django.shortcuts import render
from .models import Food, Consume
# Create your views here.


def index(request):

    if request.method == "POST":
        food_consumed = request.POST.get('food_consumed')
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume.objects.create(user=user, food_consumed=consume)
        consume.save()
        foods = Food.objects.all()

    else:
        foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)
    return render(request, 'cc/index.html', {'foods': foods,    'consumed_food': consumed_food})