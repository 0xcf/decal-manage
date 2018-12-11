from django.db import models


def fk(n, r):
    return models.ForeignKey(
        n,
        on_delete=models.PROTECT,
        related_name=r
    )


class Semester(models.Model):
    slug = models.SlugField(max_length=5)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.slug


class Facilitator(models.Model):
    username = models.CharField(max_length=16)
    semester = fk(Semester, 'facilitators')

    def __str__(self):
        return self.username

    
class Student(models.Model):
    username = models.CharField(max_length=16)
    sid = models.IntegerField()
    track = models.CharField(
        max_length=10,
        choices=(('advanced', 'Advanced'), ('beginner', 'Beginner'))
    )
    semester = fk(Semester, 'students')

    def __str__(self):
        return self.username

    class Meta:
        unique_together = ('sid', 'track', 'semester')

    
class Assignment(models.Model):
    slug = models.SlugField(max_length=5)
    name = models.CharField(max_length=60)
    track = models.CharField(
        max_length=10,
        choices=(('advanced', 'Advanced'), ('beginner', 'Beginner'))
    )
    semester = fk(Semester, 'assignments')
    required = models.BooleanField(default=True)
    
    def __str__(self):
        return "{}-{}".format(self.semester, self.slug)

    class Meta:
        ordering = ('slug',)
        unique_together = ('semester', 'slug')

    
class Checkoff(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    
    student = fk(Student, 'checkoffs')
    assignment = fk(Assignment, 'checkoffs')
    facilitator = fk(Facilitator, 'checkoffs')
    semester = fk(Semester, 'checkoffs')

    def __str__(self):
        return "{}-{}-{}".format(
            self.semester,
            self.assignment,
            self.student,
        )

    class Meta:
        unique_together = ('student', 'assignment', 'semester')

        
class Attendance(models.Model):
    date = models.DateField()
    student = fk(Student, 'attendance')
    semester = fk(Semester, 'attendances')
    excused = models.BooleanField(default=False)
    
    def __str__(self):
        return "{}-{}-attendance-{}".format(self.semester, self.student, self.date)

    class Meta:
        ordering = ('semester', 'date', 'student')
        unique_together = ('semester', 'student', 'date')
