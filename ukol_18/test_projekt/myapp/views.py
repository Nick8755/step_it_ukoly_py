import datetime as dt
from django.shortcuts import render


def age(request):
    message = ""

    birth_year  = request.GET.get('birth_year', '')
    if birth_year.isdecimal():
        birth_year = int(birth_year)
        current_year = dt.datetime.now().year
        age = current_year - birth_year
        message = f"Je vám přibližně {age} let"

    else:
        message = "Zadejte prosím rok narození jako celé číslo."

    context = {
        'message': message

    }
    return render(request, 'age.html', context)




