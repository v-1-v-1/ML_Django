from django.http import HttpResponseRedirect
from django.shortcuts import render
from forms_app.models import Program, Student
from .forms import StudentForm          
from .models import Student

def index(request):
  program_values = Program.objects.all()
  student_values = Student.objects.all()
  my_dict = {'program_rows': program_values
             ,'student_rows': student_values}
  return render(request, 'index.html',context=my_dict)

def get_student(request):    
  if request.method == 'POST':          
    form = StudentForm(request.POST)  
    if form.is_valid():
      s_name = form.cleaned_data['name']
      s_roll = form.cleaned_data['roll']
      s_year = form.cleaned_data['year']
      s_dob = form.cleaned_data['dob']
      s_degree = form.cleaned_data['degree']        
      s_branch = form.cleaned_data['branch']
      s_program =Program(title=s_degree,branch=s_branch)
      s_program.save()
      models=Student(name=s_name,roll_number=s_roll,year=s_year,dob=s_dob,program=s_program)
      models.save()
    return HttpResponseRedirect('/student/')
  else: 
      form =StudentForm()
      return render(request, 'StudentForm.html', {'form': form})