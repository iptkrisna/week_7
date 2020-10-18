from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.
def add_student_view(request):
    print(request.user)
    datafile = models.FileData.objects.all()

    if request.method == 'POST':
        search = request.POST['search']
        datafile = models.FileData.objects.filter(
            Q(filename__contains=search)
        )

    context = {
        'file': datafile
    }
    # return render(request, '', context)

    if request.user.is_authenticated:
        return redirect('add-student-data')

    if request.user.status == 'Admin' or request.user.status == 'FM':
        if request.method == 'POST':
            post = request.POST
            email = post['email']
            name = post['name']

            # CREATE NEW DATA MODELS
            new_student = models.StudentData(
                email=email,
                name=name
            )
            new_student.save()

        # READ DATA MODELS
        student = models.StudentData.objects.get(email="a@s.com")
        course = models.Course.objects.filter(student=student)

        # print(course)

        form = forms.StudentForm
        context = {
            "form": form
        }
        return render(request, 'add-student.html', context)
    else:
        return redirect('add-student-data')