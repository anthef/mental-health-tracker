from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306165654',
        'name': 'Anthony Edbert Feriyanto',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)