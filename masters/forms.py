from django import forms
from . models import CustomerMaster

class CustomerForm(forms.ModelForm):
    class Meta:
        model=CustomerMaster
        fields=['cuscode','cusname','cusemail']

