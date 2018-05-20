from django.shortcuts import render, redirect
from django.utils import timezone
from .models import DogEntry
from .form import DogEntryForm


# Create your views here.
def dog_list(request):
    entries = DogEntry.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "dogentries.html", {'entries': entries})


def dog_entry(request):
    if request.method == "POST":
        form = DogEntryForm(request.POST, request.FILES)
        if form.is_valid():
            entries = form.save(commit=False)
            entries.author = request.user
            entries.published_date = timezone.now()
            entries.save()
            return redirect(dog_list)

    else:
        form = DogEntryForm()
    return render(request, 'dogentryform.html', {'form': form})
