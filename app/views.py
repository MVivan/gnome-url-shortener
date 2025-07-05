from django.shortcuts import render, redirect, get_object_or_404
from .models import ShortURL

# Create your views here.

def shorten_url(request):
    short_url = None

    if request.method == 'POST':
        original_url = request.POST.get('original_url')
        if original_url:
            obj, created = ShortURL.objects.get_or_create(original_url=original_url)
            short_url = request.build_absolute_uri('/') + obj.short_code

    return render(request, 'home.html', {'short_url': short_url})


def redirect_url(request, short_code):
    obj = get_object_or_404(ShortURL, short_code=short_code)
    obj.clicks += 1
    obj.save()
    return redirect(obj.original_url)
