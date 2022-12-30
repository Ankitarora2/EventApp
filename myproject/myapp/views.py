from django.shortcuts import render
from django.http import JsonResponse
from .models import Event, Interest, Rating


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Validate email and password
        # ...
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failure'})


def event_list(request):
    events = Event.objects.all()
    data = []
    for event in events:
        interest_count = Interest.objects.filter(event=event).count()
        rating_count = Rating.objects.filter(event=event).count()
        avg_rating = 0
        if rating_count > 0:
            total_rating = 0
            ratings = Rating.objects.filter(event=event)
            for rating in ratings:
                total_rating += rating.rating
            avg_rating = total_rating / rating_count
        data.append({
            'id': event.id,
            'name': event.name,
            'location': event.location,
            'date': event.date,
            'interest_count': interest_count,
            'rating_count': rating_count,
            'avg_rating': avg_rating,
        })
    return JsonResponse({'events': data})


def show_interest(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        event_id = request.POST.get('event_id')
        # Validate user_id and event_id
        # ...
        Interest.objects.create(user_id=user_id, event_id=event_id)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failure'})


def rate_event(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        event_id = request.POST.get('event_id')
        rating = request.POST.get('rating')
        # Validate user_id, event_id, and rating
        # ...
        Rating.objects.create(user_id=user_id, event_id=event_id, rating=rating)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failure'})
