from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection
from .forms import ContactForm


def say_cyprus(request):
    return render(request, 'hello.html', {'name': 'Yakov'})


def say_cheese(request):
    submitted = False
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # assert False
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                cd['firstname'] + cd['lastname'],
                cd['message'],
                cd['email'],
                ['to@corporate.com'],
                cd['phonenum'],
                connection=con
            )
            return HttpResponseRedirect('/home/shalom?submitted=True')
        else:
            if 'submitted' in request.GET:
                submitted = True

    return render(request, 'shalom.html', {'form': form, 'submitted': submitted})
