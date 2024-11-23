from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, 'home.html')

def get_user_ip(request):
    # Check for the X-Forwarded-For header (set by proxies)
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()  # Get the first IP in the list
    else:
        ip = request.META.get('REMOTE_ADDR')  # Fallback to REMOTE_ADDR

    return render(request, 'ip_address.html', {'ip': ip})
