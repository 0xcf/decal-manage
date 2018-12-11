from django.shortcuts import render
from django.http import HttpResponse

from .models import Semester, Student, Facilitator, Assignment, Checkoff
from decaladmin.settings import CURRENT_SEMESTER

current_semester = Semester.objects.get(name=CURRENT_SEMESTER)


def npad(m):
    return "\n{}\n".format(m)


def semfilter(obj, **kwargs):
    return obj.objects.filter(semester=current_semester, **kwargs)


def index(request):
    advanced_labs = semfilter(Assignment, track='advanced')
    advanced_students = semfilter(Student, track='advanced')
    
    beginner_labs = semfilter(Assignment, track='beginner')
    beginner_students = semfilter(Student, track='advanced')
    
    msg = ""
    msg += npad(current_semester.name)
    msg += npad("Beginner Students: " +
                ", ".join(s.username for s in beginner_students))
    msg += npad("Advanced Students: " +
                ", ".join(s.username for s in advanced_students))
    msg += npad("Beginner Labs: " +
                ", ".join(s.name for s in beginner_labs))
    msg += npad("Advanced Labs: " +
                ", ".join(s.name for s in advanced_labs))
    return HttpResponse(msg)


def lab(request, lab):
    req_lab = semfilter(Assignment, slug=lab)[0]
    ctx = {
        'lab': req_lab,
        'checkoffs': req_lab.checkoff_set.all(),
    }
    
    return render(request, 'main/lab.txt', ctx)


def student(request, student):
    req_student = semfilter(Student, username=student)[0]
    ctx = {
        'student': req_student,
        'checkoffs': req_student.checkoff_set.all(),
    }

    return render(request, 'main/student.txt', ctx)
