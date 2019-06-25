from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib import messages
from .models import *
from .forms.branch_form import BranchForm
from .forms.department_form import DepartmentForm
from .forms.leave_form import LeaveTypeForm
from .forms.add_leave_form import AddLeaveForm
from .forms.designation_form import DesignationForm
from .forms.transfer_form import TransferForm
from .forms.employee_form import *
from django.core import serializers
from .forms.attendance_form import AttendanceForm
from .forms.settings_form import SettingsForm
import os
# Create your views here.
#Start login method

def hrmlogin(request):
        if request.method=='GET':
                return render(request,'backend/login.html')
        elif request.method=='POST':
                username = request.POST.get('username',None)
                password = request.POST.get('password',None)
                user = authenticate(username=username,password=password)
                if user is not None:
                        login(request,user)
                        return HttpResponseRedirect(reverse("home"))
                else:
                        return HttpResponseRedirect(reverse("login"))

@login_required
def hrmlogout(request):
        logout(request)
        messages.success(request, 'Logged Out Successfully')
        return HttpResponseRedirect(reverse('login'))
#End login method
# Start home method
@login_required
def homeView(request):
        if request.method =='GET':
                count_employee =EmployeePersonalModel.objects.all().count()
                count_department=DepartmentModel.objects.filter(department_status='Active').count()
                count_branch=BranchModel.objects.filter(branch_status='Active').count()
                count_designation=DesignationModel.objects.filter(designation_status='Active').count()
                branch=BranchModel.objects.filter(branch_status='Active')[:9]

                context={
                        'count_employee':count_employee,
                        'count_department':count_department,
                        'count_branch':count_branch,
                        'count_designation':count_designation,
                        'branch':branch
                }
                return render(request,'backend/index.html',context)
# End home method  

#Start Branch method
@login_required    
def branchView(request):
        branch_all_data= BranchModel.objects.all()
        if request.method =='POST':
                branch=BranchForm(request.POST)
                if branch.is_valid():
                        branch.save()
                        messages.success(request,'Branch Form submission successful')
                        return HttpResponseRedirect(reverse('branch'))
                
        else:
                branch=BranchForm()
        context={
                'form':branch,
                'branch':branch_all_data
        }        
        return render(request,'backend/branch/branch.html',context) 
@login_required
def branch_delete(request,pk):
        branch_delete_data=get_object_or_404(BranchModel,pk=pk)
        branch_delete_data.delete()
        messages.info(request,'Branch Deleted')
        return HttpResponseRedirect(reverse('branch')) 
@login_required
def branch_update(request,pk):
        branch_edit_data=get_object_or_404(BranchModel,pk=pk)
        if request.method == 'POST':
                form=BranchForm(request.POST or None,instance=branch_edit_data)
                if form.is_valid():
                        form.save()
                        messages.success(request,"Branch data updated successfully")
                        return HttpResponseRedirect(reverse('branch'))
        else:
                form=BranchForm(instance=branch_edit_data)
        context={
                'form':form,
                
        }        
        return render(request,'backend/branch/branch_edit.html',context)
#End Branch method 

#Start Department method 
@login_required   
def departmentView(request):
        department_all_data=DepartmentModel.objects.all()
        if request.method =='POST':
                department=DepartmentForm(request.POST)
                if department.is_valid():
                        department.save()
                        messages.success(request,'Departmentform submission successful')
                        return HttpResponseRedirect(reverse('department'))
                
        else:
                department=DepartmentForm()
        context={
                'form':department,
                'department':department_all_data
        }        
        return render(request,'backend/department/department.html',context) 
@login_required
def department_delete(request,pk):
        department_delete_data=get_object_or_404(DepartmentModel,pk=pk)
        department_delete_data.delete()
        messages.info(request,'Department Deleted')
        return HttpResponseRedirect(reverse('department')) 
@login_required
def department_update(request,pk):
        department_edit_data=get_object_or_404(DepartmentModel,pk=pk)
        if request.method == 'POST':
                form=DepartmentForm(request.POST or None,instance=department_edit_data)
                if form.is_valid():
                        form.save()
                        messages.success(request,"department data updated successfully")
                        return HttpResponseRedirect(reverse('department'))
        else:
                form=DepartmentForm(instance=department_edit_data)
        context={
                'form':form,
                
        }        
        return render(request,'backend/department/department_edit.html',context)

#End Department method 


#Start Designation method    
@login_required
def designationView(request):
        designation_all_data=DesignationModel.objects.all()
        if request.method =='POST':
                designation=DesignationForm(request.POST)
                if designation.is_valid():
                        designation.save()
                        messages.success(request,'designation Form submission successful')
                        return HttpResponseRedirect(reverse('designation'))
                
        else:
                designation=DesignationForm()
        context={
                'form':designation,
                'designation':designation_all_data
        }        
        return render(request,'backend/designation/designation.html',context) 
@login_required
def designation_delete(request,pk):
        designation_delete_data=get_object_or_404(DesignationModel,pk=pk)
        designation_delete_data.delete()
        messages.info(request,'designation Deleted')
        return HttpResponseRedirect(reverse('designation')) 
@login_required
def designation_update(request,pk):
        designation_edit_data=get_object_or_404(DesignationModel,pk=pk)
        if request.method == 'POST':
                form=DesignationForm(request.POST or None,instance=designation_edit_data)
                if form.is_valid():
                        form.save()
                        messages.success(request,"designation data updated successfully")
                        return HttpResponseRedirect(reverse('designation'))
        else:
                form=DesignationForm(instance=designation_edit_data)
        context={
                'form':form,
                
        }        
        return render(request,'backend/designation/designation_edit.html',context)



#Start Designation method    
@login_required
def employeeReportView(request):
        employee_data=EmployeePersonalModel.objects.all()
        context={
                'employee_data':employee_data
                }
       
       
        return render(request,'backend/employee/employee.html',context)

#End Designation method 

#Start Employee method 
@login_required   
def employeeAddView(request):
        if request.method == 'POST':
                 basic_info=EmployeePersonalForm(request.POST,request.FILES)
                 contact_info=FormContact(request.POST or None)
                 bank_info=BankForm(request.POST or None)
                 joining_info=EmployeeJoiningForm(request.POST or None)
                 name_of_exam=request.POST.getlist('name_of_exam[]')
                 year_of_passing=request.POST.getlist('year_of_passing[]')
                 board=request.POST.getlist('board[]')
                 grade=request.POST.getlist('grade[]')
                 company_name=request.POST.getlist('company_name[]')
                 company_address=request.POST.getlist('company_address[]')
                 designation=request.POST.getlist('designation[]')
                 duration=request.POST.getlist('duration[]')
                 file_of_cv= request.FILES.get('cv_file')
                 if basic_info.is_valid():
                         get_pk=basic_info.save()
                         contact_save = contact_info.save(commit=False)
                         bank_save = bank_info.save(commit=False)
                         joining_save= joining_info.save(commit=False)
                         contact_save.emplyee_id=get_pk
                         bank_save.emplyee_id=get_pk
                         joining_save.emplyee_id=get_pk
                        
                         if contact_info.is_valid():
                                 contact_save.save()
                                 if bank_info.is_valid():
                                         bank_save.save()
                                         if joining_info.is_valid():
                                                 joining_save.save()
                                                 if name_of_exam and year_of_passing and  board and grade:
                                                         if len(name_of_exam) !=0:
                                                                 for i in range(len(name_of_exam)):
                                                                         qualification=EmployeeQualificationModel()
                                                                         qualification.emplyee_id=get_pk
                                                                         qualification.name_of_exam=name_of_exam[i]
                                                                         qualification.year_of_passing=year_of_passing[i]
                                                                         qualification.board=board[i]
                                                                         qualification.grade=grade[i]
                                                                         qualification.save()
                                                 if  company_name and  company_address and designation and duration:
                                                         if len(company_name) !=0:
                                                                 for j in range(len(company_name)):
                                                                         previouswork=EmployeePreviousworkModel()
                                                                         previouswork.emplyee_id=get_pk
                                                                         previouswork.company_name=company_name[j] 
                                                                         previouswork.company_address=company_address[j]
                                                                         previouswork.designation=designation[j]
                                                                         previouswork.duration=duration[j]
                                                                         previouswork.save()
                                                 if file_of_cv:
                                                         bio_info=EmployeePersonalbioModel() 
                                                         bio_info.emplyee_id=get_pk
                                                         bio_info.cv_file=file_of_cv
                                                         bio_info.save()
                                                         messages.success(request,'Data Save Succsessfully')
                                                         return HttpResponseRedirect(reverse('addemployee'))
          
        else:
                basic_info=EmployeePersonalForm()
                contact_info=FormContact()
                bank_info=BankForm()
                joining_info=EmployeeJoiningForm()
        context={
                'basic_info':basic_info,
                'contact_info':contact_info,
                'bank_info':bank_info,
                'joining_info':joining_info
        }
        return render(request,'backend/employee/createemployee.html',context)

@login_required
def employeeDesination(request):
        department=request.POST.get('department')
        designation=DesignationModel.objects.filter(department_name=department)
        value=serializers.serialize('json',designation)
        return HttpResponse(value,content_type='application/json')   


#End Employee method

#Start transfer method
@login_required
def transfer(request):
        transfer_all_data= TransferModel.objects.all()
        if request.method =='POST':
                transfer=TransferForm(request.POST)
                if transfer.is_valid():
                        transfer.save()
                        messages.success(request,'Transfer Form submission successful')
                        return HttpResponseRedirect(reverse('transfer'))
                
        else:
                transfer=TransferForm()
        context={
                'form':transfer,
                'transfer':transfer_all_data
        }        
        return render(request,'backend/employee/transfer.html',context)
@login_required
def transfer_delete(request,pk):
        transfer_delete_data=get_object_or_404(TransferModel,pk=pk)
        transfer_delete_data.delete()
        messages.info(request,'Transfer Deleted')
        return HttpResponseRedirect(reverse('transfer')) 
@login_required
def transfer_update(request,pk):
        transfer_edit_data=get_object_or_404(TransferModel,pk=pk)
        if request.method == 'POST':
                form=TransferForm(request.POST or None,instance=transfer_edit_data)
                if form.is_valid():
                        form.save()
                        messages.success(request,"Transfer data updated successfully")
                        return HttpResponseRedirect(reverse('transfer'))
        else:
                form=TransferForm(instance=transfer_edit_data)
        context={
                'form':form,
                
        }        
        return render(request,'backend/employee/transfer_edit.html',context) 
#End Transfer method 

#End Designation method 



# start attendance report method
@login_required
def atttendanceReportView(request):
        department=DepartmentModel.objects.all()
        context={
                'department':department
        }
        return render(request,'backend/attendance/attendance_report.html',context)

def getAttendance(request):
        department=request.POST.get('department')
        date=request.POST.get('date')
        parent_data=get_object_or_404(AttendanceModel,department=department,date=date)
        attendance_data=AttendanceChildModel.objects.filter(attendance=parent_data.pk)
        serialize_data=serializers.serialize('json',attendance_data)
        return HttpResponse(serialize_data,content_type='application/json') 

@login_required   
def addAttendanceView(request):
        # department=DepartmentModel.objects.all()
        if request.method == "POST":
                attendance_form=AttendanceForm(request.POST or None)
                check_employee=request.POST.getlist('check_employee[]')
                all_employee=request.POST.getlist('employee_code[]')
                if attendance_form.is_valid():

                        attendance_id=attendance_form.save()      
                        if  check_employee:
                                for i in range(len(check_employee)):
                                        all_employee.remove(check_employee[i])
                                        attendance_child=AttendanceChildModel()
                                        attendance_child.attendance=attendance_id
                                        attendance_child.employee_code=check_employee[i]
                                        attendance_child.status='Present'
                                        attendance_child.save()    
                                     
                        if all_employee:
                                for j in range(len(all_employee)):
                                        attendance_child=AttendanceChildModel()
                                        attendance_child.attendance=attendance_id
                                        attendance_child.employee_code=all_employee[j]
                                        attendance_child.status='Absent'
                                        attendance_child.save()
                        messages.success(request,'Attendance Add Operation Successful')                  
                        return HttpResponseRedirect(reverse('add_attendance'))
                              
        else:
                attendance_form=AttendanceForm()
               
        context={
                'attendance_form':attendance_form
        }               
        return render(request,'backend/attendance/add_attendance.html',context)
@login_required
def getEmployee(request):
        department=request.POST.get('department');
        employee_data=EmployeePersonalModel.objects.filter(department=department)
        serialize_data=serializers.serialize('json',employee_data)
        return HttpResponse(serialize_data,content_type='application/json')



# Start Leavetype method   
@login_required      
def leaveTypeView(request):
        leave_type_all_data= LeaveTypeModel.objects.all()
        if request.method =='POST':
                leave_type=LeaveTypeForm(request.POST)
                if leave_type.is_valid():
                        leave_type.save()
                        messages.success(request,'Leave Type Form submission successful')
                        return HttpResponseRedirect(reverse('leave_type'))
                
        else:
                leave_type=LeaveTypeForm()
        context={
                'form':leave_type,
                'leave_type':leave_type_all_data
        }        
        return render(request,'backend/leave/leave_type.html',context) 
@login_required
def leave_type_delete(request,pk):
        leave_type_delete_data=get_object_or_404(LeaveTypeModel,pk=pk)
        leave_type_delete_data.delete()

        messages.info(request,'leave Type Deleted')
        return HttpResponseRedirect(reverse('leave_type')) 
@login_required
def leave_type_update(request,pk):
        leave_type_edit_data=get_object_or_404(LeaveTypeModel,pk=pk)
        if request.method == 'POST':
                form=LeaveTypeForm(request.POST or None,instance=leave_type_edit_data)
                if form.is_valid():
                        form.save()
                        messages.success(request,"Leave Type data updated successfully")
                        return HttpResponseRedirect(reverse('leave_type'))
        else:
                form=LeaveTypeForm(instance=leave_type_edit_data)
        context={
                'form':form,
                
        }        
        return render(request,'backend/leave/leave_type_edit.html',context) 

#End Leavetype method

#Start AddLeave method
@login_required
def addLeaveView(request):
        add_leave_all_data= AddLeaveModel.objects.all()
        if request.method =='POST':
                add_leave=AddLeaveForm(request.POST)
                if add_leave.is_valid():
                        add_leave.save()
                        messages.success(request,'Leave Form submission successful')
                        return HttpResponseRedirect(reverse('add_leave'))
                
        else:
                add_leave=AddLeaveForm()
        context={
                'form':add_leave,
                'add_leave':add_leave_all_data
        }        
        return render(request,'backend/leave/add_leave.html',context) 
@login_required
def add_leave_delete(request,pk):
        add_leave_delete_data=get_object_or_404(AddLeaveModel,pk=pk)
        add_leave_delete_data.delete()
        messages.info(request,'leave Deleted')
        return HttpResponseRedirect(reverse('add_leave')) 
@login_required
def add_leave_update(request,pk):
        add_leave_edit_data=get_object_or_404(AddLeaveModel,pk=pk)
        if request.method == 'POST':
                form=AddLeaveForm(request.POST or None,instance=add_leave_edit_data)
                if form.is_valid():
                        form.save()
                        messages.success(request,"Leave data updated successfully")
                        return HttpResponseRedirect(reverse('add_leave'))
        else:
                form=AddLeaveForm(instance=add_leave_edit_data)
        context={
                'form':form,
                
        }        
        return render(request,'backend/leave/add_leave_edit.html',context) 

#End AddLeave method
#Start generalsettings method
@login_required
def generalsettingsView(request,pk):
        settings_data=get_object_or_404(SettingsModel,pk=pk)
        old_file = settings_data.logo
        if request.method == "POST":
                 form = SettingsForm(request.POST,request.FILES,instance=settings_data)
                 if form.is_valid():
                         if request.FILES:
                                 new_file = request.FILES.get('logo')
                                 if not old_file == new_file:
                                          if os.path.isfile(old_file.path):
                                                  os.remove(old_file.path)
                         form.save()
                         messages.success(request, 'Product Updated Successfully')
                         return redirect('general_settings', pk=pk)
        else:
                form=SettingsForm(instance=settings_data)

        context={
                'form':form,
                'settings_data':settings_data
        }
        return render(request,'backend/settings/general_settings.html',context)
        

#End generalsettings method
@login_required
def totalEmployeeReport(request):
        # return HttpResponse('ok')
        if request.method == 'POST':
                branch_name = request.POST.get('branch_name', None)
                department = request.POST.get('department', None)
               
                today = date.today()
                employee_data=EmployeePersonalModel.objects.all()
                if branch_name:
                       employee_data=EmployeePersonalModel.objects.filter(branch=branch_name)
                if department:
                        employee_data=EmployeePersonalModel.objects.filter(department=department)
                if branch_name and department:
                        employee_data=EmployeePersonalModel.objects.filter(branch=branch_name,department=department)
               
                count = employee_data.count()
                context = {
                     
                        'values':request.POST,
                        'employee_data': employee_data,
                        'today': today,
                        'count': count

                        }
                return render(request, 'backend/reports/total_employee_report.html',context);

        else:
                department=DepartmentModel.objects.all()
                branch=BranchModel.objects.all()
        context={
                'department':department,
                'branch':branch

        }
        return render(request,'backend/reports/employee_report_header.html',context)
@login_required
def totalAttendanceReport(request):
        return HttpResponse('ok') 
@login_required                              
def getEmployeeData(request):
        get_employee_code=request.POST.get('employee_code')
        employee_data=EmployeePersonalModel.objects.filter(employee_code=get_employee_code)
        value=serializers.serialize('json',employee_data)
        return HttpResponse(value,content_type="application/json")
    
@login_required
def employeeView(request,pk):
        employee_personal=get_object_or_404(EmployeePersonalModel,pk=pk)
        employee_contact=get_object_or_404(EmployeeContactModel,emplyee_id=pk)
        qualification=EmployeeQualificationModel.objects.filter(emplyee_id=pk)
        work_experience=EmployeePreviousworkModel.objects.filter(emplyee_id=pk)
        joining_info=get_object_or_404(EmployeeJoiningModel,emplyee_id=pk)
        bank_info=get_object_or_404(EmployeeBankModel,emplyee_id=pk)
        print(qualification)
        context={
                'employee_personal':employee_personal,
                'employee_contact':employee_contact,
                'qualification':qualification,
                'work_experience':work_experience,
                'joining_info':joining_info,
                'bank_info':bank_info
        }
        return render(request,'backend/employee/employee_view.html',context)
                                 

def employeeDelete(request,pk):
        basic_info=get_object_or_404(EmployeePersonalModel,pk=pk)
        if basic_info.photo:
                if os.path.isfile(basic_info.photo.path):
                        os.remove(basic_info.photo.path)
        employee_contact=get_object_or_404(EmployeeContactModel,emplyee_id=pk)
        qualification=EmployeeQualificationModel.objects.filter(emplyee_id=pk)
        work_experience=EmployeePreviousworkModel.objects.filter(emplyee_id=pk)
        joining_info=get_object_or_404(EmployeeJoiningModel,emplyee_id=pk)
        bank_info=get_object_or_404(EmployeeBankModel,emplyee_id=pk)
        bio_info=get_object_or_404(EmployeePersonalbioModel,emplyee_id=pk)
        if bio_info.cv_file:
                if os.path.isfile(bio_info.cv_file.path):
                        os.remove(bio_info.cv_file.path)
        basic_info.delete()
        employee_contact.delete()
        joining_info.delete()
        bank_info.delete()
        bio_info.delete()
        qualification.delete()
        work_experience.delete()
        messages.info(request,'Delete Operation Successfull')
        return HttpResponseRedirect(reverse('employee'))      
def employeeEdit(request,pk):
        basic_data_get = get_object_or_404(EmployeePersonalModel,pk=pk)
        contact_info_get=get_object_or_404(EmployeeContactModel,emplyee_id=pk)
        bank_info_get=get_object_or_404(EmployeeBankModel,emplyee_id=pk)
        joining_info_get=get_object_or_404(EmployeeJoiningModel,emplyee_id=pk)
        old_file = basic_data_get.photo
        qualification_data=EmployeeQualificationModel.objects.filter(emplyee_id=pk)
        work_experience_data=EmployeePreviousworkModel.objects.filter(emplyee_id=pk)
        bio_info=get_object_or_404(EmployeePersonalbioModel,emplyee_id=pk)
        old_cv_file=bio_info.cv_file
        contact_info=FormContact(request.POST or None,instance=contact_info_get)
        bank_info=BankForm(request.POST or None,instance=bank_info_get)
        joining_info=EmployeeJoiningForm(request.POST or None,instance=joining_info_get)
        name_of_exam=request.POST.getlist('name_of_exam[]')
        year_of_passing=request.POST.getlist('year_of_passing[]')
        board=request.POST.getlist('board[]')
        grade=request.POST.getlist('grade[]')
        company_name=request.POST.getlist('company_name[]')
        company_address=request.POST.getlist('company_address[]')
        designation=request.POST.getlist('designation[]')
        duration=request.POST.getlist('duration[]')
        file_of_cv= request.FILES.get('cv_file')
        if request.method == 'POST':
                basic_info=EmployeePersonalForm(request.POST,request.FILES,instance=basic_data_get)
                if basic_info.is_valid():
                        if request.FILES:
                                new_file=request.FILES.get('photo')
                                if not old_file == new_file:
                                        if os.path.isfile(old_file.path):
                                                os.remove(old_file.path)
                        get_pk = basic_info.save()
                        qualification_data.delete()
                        work_experience_data.delete() 
                        contact_save = contact_info.save(commit=False)
                        bank_save = bank_info.save(commit=False)
                        joining_save= joining_info.save(commit=False)
                        contact_save.emplyee_id=get_pk
                        bank_save.emplyee_id=get_pk
                        joining_save.emplyee_id=get_pk
                        if contact_info.is_valid():
                                contact_save.save()
                                if bank_info.is_valid():
                                        bank_save.save()
                                        if joining_info.is_valid():
                                                joining_save.save()
                                                
                                                if name_of_exam and year_of_passing and  board and grade:
                                                         if len(name_of_exam) !=0:
                                                                 for i in range(len(name_of_exam)):
                                                                         qualification=EmployeeQualificationModel()
                                                                         qualification.emplyee_id=get_pk
                                                                         qualification.name_of_exam=name_of_exam[i]
                                                                         qualification.year_of_passing=year_of_passing[i]
                                                                         qualification.board=board[i]
                                                                         qualification.grade=grade[i]
                                                                         qualification.save()
                                                                      
                                                if  company_name and  company_address and designation and duration:
                                                         if len(company_name) !=0:
                                                                 for j in range(len(company_name)):
                                                                         previouswork=EmployeePreviousworkModel()
                                                                         previouswork.emplyee_id=get_pk
                                                                         previouswork.company_name=company_name[j] 
                                                                         previouswork.company_address=company_address[j]
                                                                         previouswork.designation=designation[j]
                                                                         previouswork.duration=duration[j]
                                                                         previouswork.save()
                                                if file_of_cv:
                                                        new_file=request.FILES.get('cv_file')
                                                        if os.path.isfile(old_cv_file.path):
                                                                os.remove(old_cv_file.path)
                                                        bio_info.delete()
                                                        bio_info_update=EmployeePersonalbioModel()
                                                        bio_info_update.emplyee_id=get_pk
                                                        bio_info_update.cv_file=file_of_cv
                                                        bio_info_update.save()
                                                       
                                                messages.success(request,'Data Update Succsessfully')
                                                return redirect('employee_edit', pk=pk)

                                

        
               
        else:
                basic_info=EmployeePersonalForm(instance=basic_data_get)
                contact_info=FormContact(instance=contact_info_get)
                bank_info=BankForm(instance=bank_info_get)
                joining_info=EmployeeJoiningForm(instance=joining_info_get)
       
        context={
                'basic_info':basic_info,
                'contact_info':contact_info,
                'bank_info':bank_info,
                'joining_info':joining_info,
                'qualification':qualification_data,
                'work_experience':work_experience_data,
                'bio_info':bio_info,
                'basic_data_get':basic_data_get
        }
        return render(request,'backend/employee/employee_edit.html',context)
         

def DhashboardData(request):
        all_data=[]
        all_employee =EmployeePersonalModel.objects.all()
        count_employee=all_employee.count()
        count_department=DepartmentModel.objects.filter(department_status='Active').count()
        count_branch=BranchModel.objects.filter(branch_status='Active').count()
        count_designation=DesignationModel.objects.filter(designation_status='Active').count()
        all_data.append(count_employee)
        all_data.append(count_department)
        all_data.append(count_branch)
        all_data.append(count_designation)
        return HttpResponse(all_data)
        # serialize_data=serializers.serialize('json',all_data)
        # return HttpResponse(serialize_data,content_type='application/json')
        


   

