from django.shortcuts import render, redirect, get_object_or_404
from .forms import BugForm
from .models import Bug, Project
from django.contrib.auth.decorators import login_required


@login_required
def report(request, slug):
    project = get_object_or_404(Project, slug=slug, members=request.user)
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.project = project
            bug.updated_by = request.user
            bug.created_by = request.user
            bug.save()
            return redirect('bug_list', slug=slug)
    else:
        form = BugForm()
    return render(request, 'bugs/report_form.html', {
        'form': form,
        'title': 'New bugreport from: {}'.format(request.user),
    })


@login_required
def bug_detail(request, slug, bug_id):
    bug = get_object_or_404(Bug, project__slug=slug, pk=bug_id)
    if request.method == 'POST':
        form = BugForm(request.POST, instance=bug)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.updated_by = request.user
            bug.save()
            return redirect('bug_list', slug=slug)
    else:
        form = BugForm(instance=bug)
    return render(request, 'bugs/report_form.html', {
        'form': form,
        'title': 'Edit bugreport: {}'.format(bug.description),
    })


@login_required
def bug_list(request, slug):
    project = get_object_or_404(Project, slug=slug)
    bug_list = Bug.objects.filter(project__slug=slug, project__members=request.user)
    return render(request, 'bugs/bug_list.html', {
        'bug_list': bug_list,
        'project': project,
        'title': '{} list of bugs'.format(project.name),
    })
