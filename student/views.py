from django.shortcuts import render, redirect
from .models import Student, Parent

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/students.html', {'students': students})

def add_student(request):
    parents = Parent.objects.all()

    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        age = request.POST.get('age')
        adresse = request.POST.get('adresse')
        parent_id = request.POST.get('parent')

        parent = Parent.objects.get(id=parent_id)

        Student.objects.create(
            nom=nom,
            prenom=prenom,
            age=age,
            adresse=adresse,
            parent=parent
        )

        return redirect('student_list')

    return render(request, 'students/add-student.html', {'parents': parents})