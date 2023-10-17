from django import forms

'''
class OutpassForm(forms.Form):
    OUTPASS_REASON_CHOICES = (
        ('business', 'Business'),
        ('personal', 'Personal'),
    )

    outpass_time = forms.DateTimeField(
        label='Outpass Time',
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'],
    )
    outpass_reason = forms.ChoiceField(
        label='Reason for Outpass',
        choices=OUTPASS_REASON_CHOICES,
        widget=forms.Select,
    )
    remarks = forms.CharField(
        label='Remarks',
        widget=forms.Textarea(attrs={'rows': 4}),  # You can adjust rows as needed
        required=False  # Set this to True if you want the field to be required
    )

from django import forms
'''

from django import forms
from datetime import date


class OutpassForm(forms.Form):
    OUTPASS_REASON_CHOICES = (
        ('on-duty', 'On-Duty'),
        ('personal', 'Personal'),
    )

    RETURN_CHOICES = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )

    # Get the current date as the initial value for the outpass_date field
    current_date = date.today()
    
    outpass_date = forms.DateField(
        label='Outpass Date',
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d'],
        initial=current_date,  # Set the initial value to the current date
    )
    outpass_time = forms.TimeField(
        label='Outpass Time',
        widget=forms.TimeInput(attrs={'type': 'time'}),
        input_formats=['%H:%M'],
    )
    outpass_reason = forms.ChoiceField(
        label='Reason for Outpass',
        choices=OUTPASS_REASON_CHOICES,
        widget=forms.Select,
    )
    remarks = forms.CharField(
        label='Remarks',
        widget=forms.Textarea(attrs={'rows': 4}),  # You can adjust rows as needed
        required=False  # Set this to True if you want the field to be required
    )

    return_to_company = forms.ChoiceField(
        label='Return to Company',
        choices=RETURN_CHOICES,
        widget=forms.Select,
    )

    return_time = forms.TimeField(
        label='Return Time',
        widget=forms.TimeInput(attrs={'type': 'time'}),
        input_formats=['%H:%M'],
        required=False,
    )

'''

from django import forms

class OutpassForm(forms.Form):
    OUTPASS_REASON_CHOICES = (
        ('business', 'Business'),
        ('personal', 'Personal'),
    )

    outpass_date = forms.DateField(
        label='Outpass Date',
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d'],
        initial=forms.DateField.widget.attrs['value']
    )
    outpass_time = forms.TimeField(
        label='Outpass Time',
        widget=forms.TimeInput(attrs={'type': 'time'}),
        input_formats=['%H:%M'],
        initial=forms.TimeField.widget.attrs['value']
    )
    outpass_reason = forms.ChoiceField(
        label='Reason for Outpass',
        choices=OUTPASS_REASON_CHOICES,
        widget=forms.Select,
        initial='business'  # Set a default choice if needed
    )
    return_time = forms.TimeField(
        label='Return Time (Business)',
        widget=forms.TimeInput(attrs={'type': 'time'}),
        input_formats=['%H:%M'],
        required=False  # This field is required if 'business' is selected
    )
    remarks = forms.CharField(
        label='Remarks',
        widget=forms.Textarea(attrs={'rows': 4}),
        required=False
    )

class InpassForm(forms.Form):
    INPASS_REASON_CHOICES = (
        ('reason1', 'Reason 1'),
        ('reason2', 'Reason 2'),
        # Add more choices as needed
    )

    inpass_reason = forms.ChoiceField(
        label='Reason for Inpass',
        choices=INPASS_REASON_CHOICES,
        widget=forms.Select,
    )
    inpass_time = forms.TimeField(
        label='Inpass Time',
        widget=forms.TimeInput(attrs={'type': 'time'}),
        input_formats=['%H:%M'],
        initial=forms.TimeField.widget.attrs['value']
    )
'''

#for approval process
# forms.py


