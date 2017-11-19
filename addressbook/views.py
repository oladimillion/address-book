from django.shortcuts import render, redirect
from django.db import IntegrityError

from .form import AddressForm
from .models import Models


def index(request, template_name='index.html'):
    return render(request, template_name, {"title": "WELCOME"})


def add(request, template_name='add.html', form_class=AddressForm):

    title = 'ADD TO RECORD'

    if request.method == 'POST':
        form = form_class(request.POST)

        context = {
            'form': form,
            'title': title,
        }

        if form.is_valid():
            name = request.POST["name"]
            email = request.POST["email"]
            models = Models(name=name, email=email)
            try:
                models.save()
                return redirect(list)
            except IntegrityError as err:
                if str(err).find("name") != -1:
                    return render(request, template_name, {
                            'form': form,
                            'title': title,
                            'unique_error': 'Name already taken'
                        })
                elif str(err).find("email") != -1:
                    return render(request, template_name, {
                            'form': form,
                            'title': title,
                            'unique_error': 'Email already taken'
                        })
                else:
                    return render(request, template_name, {
                            'form': form,
                            'title': title,
                            'unique_error': 'Error occurred'
                        })

        else:
            return render(request, template_name, context)

    else:
        form = form_class()
        context = {
            'form': form,
            'title': title,
        }
    return render(request, template_name, context)


def list(request, template_name='list.html'):
    lists = Models.objects.all()
    context = {
        "title": "RECORD",
        "lists": lists
    }
    return render(request, template_name, context) 


