from django.shortcuts import render

def main_page(request):
    return render(request, 'userpage/base_userpage.html')
