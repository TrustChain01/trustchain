from django.db import models

class Login(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    type = models.CharField(max_length=20)

class University(models.Model):
    LOGIN = models.ForeignKey(Login,on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    phone = models.BigIntegerField()
    photo = models.FileField()
    email = models.CharField(max_length=40)
    place = models.CharField(max_length=40)
    post = models.CharField(max_length=40)
    pin = models.IntegerField()

class Student(models.Model):
    LOGIN = models.ForeignKey(Login,on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    phone = models.BigIntegerField()
    photo = models.FileField()
    email = models.CharField(max_length=40)
    place = models.CharField(max_length=40)
    post = models.CharField(max_length=40)
    pin = models.IntegerField()

class Employer(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=40)
    place = models.CharField(max_length=40)
    post = models.CharField(max_length=40)
    pin = models.IntegerField()
    photo = models.FileField()

class Feedback(models.Model):
    feedback = models.TextField()
    rating = models.IntegerField()
    date = models.DateField()
    user_id = models.ForeignKey(Login, on_delete=models.CASCADE)

class Requirements(models.Model):
    job = models.CharField(max_length=50)
    job_details = models.TextField()
    qualification =  models.TextField()
    date = models.DateField()


class student_Request(models.Model):
    Requirement_id = models.ForeignKey(Requirements, on_delete= models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    request = models.CharField(max_length=50)
    date = models.DateField()
    Status = models.CharField(max_length=20)



class Score(models.Model):
    request_id = models.ForeignKey(student_Request, on_delete=models.CASCADE)

#
class totsl_score(models.Model):
    grade = models.CharField(max_length=20)
    year = models.BigIntegerField()
    month = models.CharField(max_length=40)
    image = models.FileField()


class Complaint(models.Model):
    complaint = models.TextField()
    reply = models.TextField()
    date = models.DateField()
    user = models.ForeignKey(Login ,on_delete=models.CASCADE)



