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

        if not parent_id:
            return render(request, 'students/add-student.html', {
                'parents': parents,
                'error': 'Please select a parent.'
            })

        parent = Parent.objects.filter(id=parent_id).first()
        if not parent:
            return render(request, 'students/add-student.html', {
                'parents': parents,
                'error': 'Selected parent does not exist.'
            })

        Student.objects.create(
            nom=nom,
            prenom=prenom,
            age=age,
            adresse=adresse,
            parent=parent
        )

        return redirect('student_list')

    return render(request, 'students/add-student.html', {'parents': parents})


def edit_student(request, id):
    student = Student.objects.get(id=id)
    parents = Parent.objects.all()

    if request.method == 'POST':
        student.nom = request.POST.get('nom')
        student.prenom = request.POST.get('prenom')
        student.age = request.POST.get('age')
        student.adresse = request.POST.get('adresse')

        parent_id = request.POST.get('parent')
        if not parent_id:
            return render(request, 'students/edit-student.html', {
                'student': student,
                'parents': parents,
                'error': 'Please select a parent.'
            })

        parent = Parent.objects.filter(id=parent_id).first()
        if not parent:
            return render(request, 'students/edit-student.html', {
                'student': student,
                'parents': parents,
                'error': 'Selected parent does not exist.'
            })

        student.parent = parent
        student.save()
        return redirect('student_list')

    return render(request, 'students/edit-student.html', {
        'student': student,
        'parents': parents
    })


def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student_list')