from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import UserLoginForm
from django.contrib.auth.decorators import login_required
from api.models import Readings, Dustbins


# Create your views here.
# for logging in a user
def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        # print(request.user.is_authenticated())
        return redirect('/dashboard')
    if request.user.is_authenticated():
        return redirect('/dashboard')
    return render(request, 'login_form.html', {'form': form})


@login_required(login_url='/login/')
def dashboard_view(request):
    # latest_record = Readings.objects.order_by('-recorded_on')
    latest_record = Readings.objects.raw('SELECT * FROM api_readings WHERE (`recorded_on`) IN (SELECT MAX(`recorded_on`) FROM api_readings GROUP BY `dustbin_id`) ORDER BY dustbin_id ASC, recorded_on DESC')

    filled = []
    empty = []
    for rows in latest_record:
        filled.append(int(rows))
        empty.append(100 - int(rows))

    return render(request, 'dashboard/index.html', {'latest_record': latest_record , 'filled': filled, 'empty': empty })


@login_required(login_url='/login/')
def details_view(request, dustbin_id):
    location = Dustbins.objects.get(id=dustbin_id)
    # print(get_record.dustbin_id)
    get_record = Readings.objects.filter(dustbin_id=dustbin_id).order_by('-recorded_on')[0]
    level = get_record.level
    dustbin_id = get_record.dustbin_id
    empty = 100 - int(level)
    recorded_on = get_record.recorded_on
    location = location.location_name

    context = {}
    context['level'] = level
    context['dustbin_id'] = dustbin_id
    context['empty'] = empty
    context['recorded_on'] = recorded_on
    context['location'] = location

    return render(request, 'dashboard/details.html', context)

# for registering a user
# def register_view(request):
#     form = UserRegisterForm(request.POST or None)
#     if form.is_valid():
#         user = form.save(commit=False)
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#         user.set_password(password)
#         user.save()
#         # this is required step before login
#         user = authenticate(username=username, password=password)
#         login(request, user)
#     return render(request, 'register_form.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/login/')
