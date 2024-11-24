from django import forms

class PredictionForm(forms.Form):
    contact_duration = forms.IntegerField(
        label='Contact Duration (days)',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter contract duration in days'
        }),
        min_value=1
    )
    
    employee_variation_rate = forms.FloatField(
        label='Employee Variation Rate',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter employee variation rate'
        })
    )
    
    client_age = forms.IntegerField(
        label='Client Age',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter client age'
        }),
        min_value=18,
        max_value=100
    )