from django import forms
from backend.models import BranchModel

class BranchForm(forms.ModelForm):
    class Meta:
        model=BranchModel
        fields = '__all__'
        choices=(('','--Select--'),('Active','Active'),('Inactive','Inactive'))
        widgets={
            'branch_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Branch Name'}),
            'branch_status':forms.Select(attrs={'class':'form-control'},choices=choices)

        }