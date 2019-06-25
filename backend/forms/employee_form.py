from django import forms
from backend.models import *

class EmployeePersonalForm(forms.ModelForm):
    class Meta:
        model=EmployeePersonalModel
        fields = '__all__'
        choices=(('','--Select--'),('Active','Active'),('Inactive','Inactive'))
        gender=(('','--Select--'),('Female','Female'),('Male','Male'))
        religion=(('','--Select--'),('Islam','Islam'),('Hinduism','Hinduism'),('Christianity','Christianity'),('Buddhism','Buddhism'))
        marital_status=(('','--Select--'),('Unmarried','Unmarried'),('Married','Married'))
        blood_group=(('','--Select--'),('O+','O+'),('O-','O-'),('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('AB+','AB+'),('AB-','AB-'))
        widgets={
            
            'employee_code':forms.TextInput(attrs={'class':'form-control input-circle','placeholder':'Employee Code'}),
            'employee_name':forms.TextInput(attrs={'class':'form-control input-circle','placeholder':'Employee Name'}),
            'branch':forms.Select(attrs={'class':'form-control input-circle','id':'branch'}),
            'department':forms.Select(attrs={'class':'form-control input-circle','id':'department'}),
            'designation':forms.Select(attrs={'class':'form-control input-circle','id':'designation'}),
            'father_name':forms.TextInput(attrs={'class':'form-control input-circle','placeholder':'Father Name'}),
            'mother_name':forms.TextInput(attrs={'class':'form-control input-circle','placeholder':'Mother Name'}),
            'date_of_birth':forms.DateInput(attrs={'class':'form-control input-circle', 'placeholder':'Select a date', 'type':'date'}),
            'gender':forms.Select(attrs={'class':'form-control input-circle'},choices=gender),
            'national_id':forms.TextInput(attrs={'class':'form-control input-circle','placeholder':'National Id'}),
            'nationality':forms.TextInput(attrs={'class':'form-control input-circle','placeholder':'Nationality'}),
            'blood_group':forms.Select(attrs={'class':'form-control input-circle','id':'designation'},choices=blood_group),
            'religion':forms.Select(attrs={'class':'form-control input-circle','id':'designation'},choices=religion),
            'marital_status':forms.Select(attrs={'class':'form-control input-circle','id':'designation'},choices=marital_status)
           
        }  
class FormContact(forms.ModelForm):
    class Meta:
        model=EmployeeContactModel
        fields=('contact_number','contact_email','present_address','permanent_address')
        exclude = ("emplyee_id",)
        widgets={
            'contact_number':forms.TextInput(attrs={'class':'form-control input-circle','placeholder':'Contact Number'}),
            'contact_email':forms.EmailInput(attrs={'class':'form-control input-circle','placeholder':'eg.: email@email.com'}),
            'present_address':forms.Textarea(attrs={'class':'form-control input-circle','rows':'2','cols':'3','placeholder':'Present Address'}),
            'permanent_address':forms.Textarea(attrs={'class':'form-control input-circle','rows':'2','cols':'3','placeholder':'Parmanent Address'})

        }   
class BankForm(forms.ModelForm):
       class Meta:
           model=EmployeeBankModel
           fields=('account_no','bank_name','branch_name')
           exclude = ("emplyee_id",)
           widgets={
             'account_no':forms.TextInput(attrs={'class':'form-control input-circle','placeholder':'Account No'}),
             'bank_name':forms.TextInput(attrs={'class':'form-control input-circle','placeholder':'Bank No'}),
             'branch_name':forms.TextInput(attrs={'class':'form-control input-circle','placeholder':'Branch Name'})
        
           }   
class EmployeeJoiningForm(forms.ModelForm):
    class Meta:
        model=EmployeeJoiningModel
        exclude = ("emplyee_id",)
        fields=('date_of_joining','offer_date','confirmation_date')
        widgets={
           'date_of_joining':forms.DateInput(attrs={'class':'form-control input-circle', 'placeholder':'Select a date', 'type':'date'}),
           'offer_date':forms.DateInput(attrs={'class':'form-control input-circle', 'placeholder':'Select a date', 'type':'date'}),
           'confirmation_date':forms.DateInput(attrs={'class':'form-control input-circle', 'placeholder':'Select a date', 'type':'date'})
           }

# class EmployeeQualificationForm(forms.ModelForm):
#         class Meta:
#             model=EmployeeQualificationModel
#             fields='__all__'
      
  
# class EmployeePreviousworkForm(forms.ModelForm):
#     class Meta:
#         model=EmployeePreviousworkModel
#         fields='__all__'
       
# class EmployeeBioForm():
#     class Meta:
#         model=EmployeePersonalbioModel
#         fields='__all__'
