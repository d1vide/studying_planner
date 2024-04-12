from django import forms

from .models import Plan


class PlanForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["description"].widget.attrs.update({'rows': 4})
        self.fields["deadline"].widget = forms.DateInput(attrs={'type': 'date'})

    class Meta:
        model = Plan
        fields = ('title', 'category', 'priority', 'time_required',
                  'description', 'deadline',)
