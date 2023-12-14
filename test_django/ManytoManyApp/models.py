from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=40)
    expirience = models.IntegerField()
    students = models.ManyToManyField(
        Student, 
        related_name='teacher'
        )
    
student1 = Student.objects.create(name='student1', age=15)
student2 = Student.objects.create(name='student3', age=17)
student2 = Student.objects.create(name='student2', age=16)
student3 = Student.objects.create(name='student3', age=17)

teacher1 = Teacher.objects.create(name='teacher1', subject='math', expirience=2)
teacher1.students.set([student1, student2]) # обращаемся к связи и добавляем новых студентов
teacher1.students.all()
# <QuerySet [Student:]>




#!!!!!!!!!!!!!! related_name | related_query_name




