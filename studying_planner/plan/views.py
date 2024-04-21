from django.shortcuts import get_object_or_404, redirect, render

from .forms import PlanForm
from .models import Plan


def index(request):
    template_name = 'plan/index.html'
    return render(request, template_name)


def plan_list(request):
    template_name = 'plan/plan_list.html'
    plan_list = Plan.objects.values('id', 'title', 'category__title', 'priority__title').filter(is_task=False)
    context = {'plan_list': plan_list}
    return render(request, template_name, context)


def plan_detail(request, pk):
    template_name = 'plan/plan_detail.html'
    plan = get_object_or_404(Plan, pk=pk, is_task=False)
    context = {'plan_detail': plan}
    return render(request, template_name, context)


def plan_create(request, pk=None):
    template_name = 'plan/plan_create.html'
    instance = None
    if pk:
        instance = get_object_or_404(Plan, pk=pk)
    form = PlanForm(request.POST or None, instance=instance)
    context = {'form': form}
    if form.is_valid():
        form.save()
        return redirect('plan:list')
    return render(request, template_name, context)


def plan_delete(request, pk):
    template_name = 'plan/plan_create.html'
    instance = get_object_or_404(Plan, pk=pk)
    form = PlanForm(instance=instance)
    context = {'form': form}
    if request.POST:
        instance.delete()
        return redirect('plan:list')
    return render(request, template_name, context)


def task_list(request):
    template_name = 'plan/task_list.html'
    task_list = Plan.objects.values('id', 'title', 'category__title', 'priority__title', 'is_task').filter(is_task=True)
    context = {'task_list': task_list}
    return render(request, template_name, context)


def task_detail(request, pk):
    pass


def do_task(request, pk):
    if request.POST:
        instance = get_object_or_404(Plan, pk=pk)
        instance.is_task = True
        instance.save()
        return redirect('plan:tasklist')


def finish_task_now(request, pk):
    if request.POST:
        instance = get_object_or_404(Plan, pk=pk)
        instance.is_task = False
        instance.is_over = True
        instance.save()
        return redirect('plan:tasklist')


def finish_task_later(request, pk):
    if request.POST:
        instance = get_object_or_404(Plan, pk=pk)
        instance.is_task = False
        instance.save()
        return redirect('plan:list')
