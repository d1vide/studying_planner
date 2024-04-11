from django.shortcuts import get_object_or_404, redirect, render

from .forms import PlanForm
from .models import Plan


def index(request):
    template_name = 'plan/index.html'
    return render(request, template_name)


def plan_list(request):
    template_name = 'plan/plan_list.html'
    plan_list = Plan.objects.values('id', 'title', 'category__title', 'priority__title')
    context = {'plan_list': plan_list}
    return render(request, template_name, context)


def plan_detail(request, pk):
    template_name = 'plan/plan_detail.html'
    plan = get_object_or_404(Plan, pk=pk)
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
        return redirect('plan:planlist')
    return render(request, template_name, context)


def plan_delete(request, pk):
    template_name = 'plan/plan_create.html'
    instance = get_object_or_404(Plan, pk=pk)
    form = PlanForm(instance=instance)
    context = {'form': form}
    if request.POST:
        instance.delete()
        return redirect('plan:planlist')
    return render(request, template_name, context)
