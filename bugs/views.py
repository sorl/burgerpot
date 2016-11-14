from django.shortcuts import render, redirect
from .forms import BugForm
from .models import Bug
from django.contrib.auth.decorators import login_required


@login_required
def report(request):
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.submitter = request.user
            bug.save()
            return redirect('/')
        print(form.errors)
    else:
        print(form.errors)
        form = BugForm()
    return render(request, 'bugs/report_form.html', {
        'form': form,
        'title': 'New bugreport from: {}'.format(request.user),
    })


@login_required
def bugs_list(request):
    bugs_list = Bug.objects.filter(submitter=request.user)
    return render(request, 'bugs/bugs_list.html', {
        'bugs_list': bugs_list,
    })
