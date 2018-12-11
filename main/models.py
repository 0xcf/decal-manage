from django.db import models


class Semester(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Facilitator(models.Model):
    username = models.CharField(max_length=16)
    semester = models.ForeignKey(Semester, on_delete=models.PROTECT)

    def __str__(self):
        return self.username

    
class Student(models.Model):
    username = models.CharField(max_length=16)
    sid = models.IntegerField()
    track = models.CharField(
        max_length=10,
        choices=(('advanced', 'Advanced'), ('beginner', 'Beginner'))
    )
    semester = models.ForeignKey(Semester, on_delete=models.PROTECT)

    def __str__(self):
        return self.username
    """
        return "<Student: {} ({}, {})>".format(
            self.username,
            self.track,
            self.semester,
        )
    """


class Assignment(models.Model):
    slug = models.SlugField(max_length=5)
    name = models.CharField(max_length=60)
    track = models.CharField(
        max_length=10,
        choices=(('advanced', 'Advanced'), ('beginner', 'Beginner'))
    )
    semester = models.ForeignKey(Semester, on_delete=models.PROTECT)

    def __str__(self):
        return "<Assignment: {} ({})>".format(self.slug, self.semester)

    
class Checkoff(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    assignment = models.ForeignKey(Assignment, on_delete=models.PROTECT)
    facilitator = models.ForeignKey(Facilitator, on_delete=models.PROTECT)
    semester = models.ForeignKey(Semester, on_delete=models.PROTECT)

    def __str__(self):
        return "<Checkoff: {} for {} on {} by {}>".format(
            self.assignment,
            self.student,
            self.timestamp,
            self.facilitator,
        )

