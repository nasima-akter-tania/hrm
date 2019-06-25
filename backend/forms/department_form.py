from django import forms
from backend.models import DepartmentModel

class DepartmentForm(forms.ModelForm):
    class Meta:
        model=DepartmentModel
        fields = '__all__'
        choices=(('','--Select--'),('Active','Active'),('Inactive','Inactive'))
        widgets={
            'department_name':forms.TextInput(attrs={'class':'form-control'}),
            'department_status':forms.Select(attrs={'class':'form-control'},choices=choices)

        }