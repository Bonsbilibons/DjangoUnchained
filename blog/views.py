from django.shortcuts import render

def main_page(request):
    return render(request, 'blog/front_page.html')