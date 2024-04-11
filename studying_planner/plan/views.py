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


def plan_create(request):
    template_name = 'plan/plan_create.html'
    form = PlanForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        form.save()
        return redirect('plan:planlist')
    return render(request, template_name, context)
