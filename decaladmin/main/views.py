from django.shortcuts import render
from django.http import HttpResponse

from .models import Semester, Student, Facilitator, Assignment, Checkoff
from decaladmin.settings import CURRENT_SEMESTER

try:
    current_semester = Semester.objects.get(name=CURRENT_SEMESTER)
except:
    # The semester hasn't been created or migrations haven't been run.
    # Just ignore, so that the rest of the app can at least load.
    print("Can't load the current semester!")
    pass


def semfilter(obj, **kwargs):
    return obj.objects.filter(semester=current_semester, **kwargs)


def index(request):

    labs = {
        'advanced': current_semester.assignments.filter(track='advanced'),
        'beginner': current_semester.assignments.filter(track='beginner'),
    }

    ctx = {
        'semester': current_semester,
        'advanced_labs': labs['advanced'],
        'advanced_labs_required': labs['advanced'].filter(required=True),
        'advanced_students': semfilter(Student, track='advanced'),
        'beginner_labs': labs['beginner'],
        'beginner_labs_required': labs['beginner'].filter(required=True),
        'beginner_students': semfilter(Student, track='beginner'),
    }

    return render(request, 'main/index.txt', ctx)


def lab(request, lab):
    req_lab = semfilter(Assignment, slug=lab)[0]
    ctx = {
        'lab': req_lab,
        'checkoffs': req_lab.checkoffs.all(),
    }
    
    return render(request, 'main/lab.txt', ctx)


def student(request, student):
    req_student = semfilter(Student, username=student)[0]
    track = req_student.track
    all_assignments = current_semester.assignments.filter(track=track)
    checkoffs = req_student.checkoffs.all()
        
    ctx = {
        'student': req_student,
        'checkoffs': checkoffs,
        'passing': checkoffs.count() >= all_assignments.count() - 2
    }

    return render(request, 'main/student.txt', ctx)
