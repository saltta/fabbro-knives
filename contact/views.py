from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    """
    View function for displaying and processing the contact form.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent! We will \
                get back to you as soon as possible.')
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
