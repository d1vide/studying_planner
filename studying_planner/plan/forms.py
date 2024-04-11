from django import forms

from .models import Plan


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ('title', 'category', 'priority', 'time_required', 'description')
