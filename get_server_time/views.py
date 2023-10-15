from datetime import datetime
from django.http import HttpResponse

def current_time(request):
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")  
    response_text = f"Current Time: {current_time}"
    return HttpResponse(response_text)
