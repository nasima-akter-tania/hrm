from django import forms
from backend.models import TransferModel

class TransferForm(forms.ModelForm):
    class Meta:
        model=TransferModel
        fields='__all__'
        choices=(('','--Select--'),('Active','Active'),('Inactive','Inactive'))
        widgets={
            'employee_code':forms.TextInput(attrs={'class':'form-control input-circle','id':'employee_code_id'}),
            'issue_date':forms.DateInput(attrs={'class':'form-control input-circle','type':'date'}),
            'previous_branch':forms.TextInput(attrs={'class':'form-control input-circle','id':'previous_branch','readonly':'True'}),
            'previous_department':forms.TextInput(attrs={'class':'form-control input-circle','id':'previous_department','readonly':'True'}),
            'present_branch':forms.Select(attrs={'class':'form-control input-circle','id':'branch'}),
            'present_department':forms.Select(attrs={'class':'form-control input-circle','id':'department'})
        }
