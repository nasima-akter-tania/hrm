from django import forms
from backend.models import DesignationModel

class DesignationForm(forms.ModelForm):
    class Meta:
        model=DesignationModel
        fields = '__all__'
        choices=(('','--Select--'),('Active','Active'),('Inactive','Inactive'))
        widgets={
            'department_name':forms.Select(attrs={'class':'form-control'}),
            'designation_name':forms.TextInput(attrs={'class':'form-control'}),
            'designation_status':forms.Select(attrs={'class':'form-control'},choices=choices)

        }