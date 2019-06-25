from django import forms
from backend.models import AttendanceModel


class AttendanceForm(forms.ModelForm):
    class Meta:
        model=AttendanceModel
        fields='__all__'
        widgets={
            'date':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control','type':'date','id':'get_date'}),
            'department':forms.Select(attrs={'class':'form-control','id':'department'})

        }
 