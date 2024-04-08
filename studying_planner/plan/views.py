from django.shortcuts import get_object_or_404, render

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