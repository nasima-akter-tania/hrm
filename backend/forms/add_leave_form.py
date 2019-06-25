from django import forms
from backend.models import AddLeaveModel

class AddLeaveForm(forms.ModelForm):
    class Meta:
        model=AddLeaveModel
        fields = '__all__'
        choices=(('','--Select--'),('Active','Active'),('Inactive','Inactive'))
        widgets={
            'employee_code':forms.TextInput(attrs={'class':'form-control input-circle'}),
            'leave_type':forms.Select(attrs={'class':'form-control input-circle'}),
            'from_date':forms.DateInput(attrs={'class':'form-control input-circle','type':'date'}),
            'to_date':forms.DateInput(attrs={'class':'form-control input-circle','type':'date'}),
            'reason':forms.Textarea(attrs={'class':'form-control input-circle','rows':'4','cols':'5'}),
            'status':forms.Select(attrs={'class':'form-control input-circle'},choices=choices)
        }
