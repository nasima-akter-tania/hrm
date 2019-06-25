from django import forms
from backend.models import SettingsModel

class SettingsForm(forms.ModelForm):
    class Meta:
        model=SettingsModel
        fields='__all__'
        choices=(('','--Select--'),('Active','Active'),('Inactive','Inactive'))
        widgets={
            'email':forms.TextInput(attrs={'class':'form-control input-circle'}),
            'contact_no':forms.TextInput(attrs={'class':'form-control input-circle'}),
            'company_name':forms.TextInput(attrs={'class':'form-control input-circle'}),
            'company_address':forms.Textarea(attrs={'class':'form-control input-circle','rows':'4','cols':'5'}),
                        
        }
