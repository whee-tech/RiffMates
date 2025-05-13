from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def credits(request):
    content = "Nicky\nVadim"
    return HttpResponse(content, content_type="text/plain")

def news(request):
    data = {"news": [
        "现在我们有一个报纸了!",
        "但是现在我们没有钱了!"
    ]}
    return render(request, "news.html", data)

