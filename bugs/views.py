from django.shortcuts import render, redirect
from .forms import BugForm
from .models import Bug
from django.contrib.auth.decorators import login_required
from django.http import Http404


@login_required
def report(request):
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.submitter = request.user
            bug.save()
            return redirect('/')
    else:
        form = BugForm()
    return render(request, 'bugs/report_form.html', {
        'form': form,
        'title': 'New bugreport from: {}'.format(request.user),
    })


@login_required
def bug_detail(request, bug_id):
    try:
        bug = Bug.objects.get(submitter=request.user, pk=bug_id)
    except Bug.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        form = BugForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BugForm(instance=bug)
    return render(request, 'bugs/report_form.html', {
        'form': form,
        'title': 'Edit bugreport: {}'.format(bug.pk),
    })


@login_required
def bug_list(request):
    bug_list = Bug.objects.filter(submitter=request.user)
    return render(request, 'bugs/bug_list.html', {
        'bug_list': bug_list,
    })
