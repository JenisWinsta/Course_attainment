from django.db import models 

# Create your models here.

# db models which converts to db tables

# models.py

    
class Department(models.Model):
    name = models.CharField(max_length=150, unique=True)
    def __str__(self):
        return f'{self.name}'
    



 
class Programme(models.Model):
    name = models.CharField(max_length=50, unique=True)  
    def __str__(self):
        return f'{self.name}'

class Programme_Outcome(models.Model):
    code = models.CharField(max_length=5)
    description = models.TextField(unique=True)
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)    
    def __str__(self):
        return f'{self.code}'
    


class Programme_Specific(models.Model):    
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.department}'

class Programme_Specific_Outcome(models.Model):
    code = models.CharField(max_length=6)
    description = models.TextField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)    
    def __str__(self):
        return f'{self.code}, {self.department}'
    
 


 

class Year(models.Model):
    name = models.CharField(max_length=6)   
    def __str__(self):
        return f'{self.name}'
    
class Semester(models.Model):
    name = models.CharField(max_length=11) 
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name}'    
    
    

class Course(models.Model):
    name = models.CharField(max_length=250)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    
    course_code = models.CharField(max_length=20)    
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    programme_specific = models.ForeignKey(Programme_Specific, on_delete=models.CASCADE)    
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE, default=1)  

    assigned_to = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_courses'
    )

    programme_outcomes = models.ManyToManyField(Programme_Outcome, through='Course_Programme_Outcome')

    def __str__(self):
        return f'({self.course_code}) {self.name}'
        

class Course_Programme_Outcome(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    programme_outcome = models.ForeignKey(Programme_Outcome, on_delete=models.CASCADE)
    strength = models.PositiveSmallIntegerField(default=1)  # Range of connection strength (1, 2, 3)

    class Meta:
        unique_together = ('course', 'programme_outcome')  # Ensures one course can be connected to a PO only once

    def __str__(self):
        return f'Course: {self.course.course_code}, {self.course.name},PO: {self.programme_outcome.code}, Strength: {self.strength}'



class Course_Outcome(models.Model):
    code = models.CharField(max_length=5)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)   
    programme_specific_outcomes = models.ManyToManyField(Programme_Specific_Outcome) 
    programme_outcomes = models.ManyToManyField(Programme_Outcome) 
    def __str__(self):
        return f'{self.code}, {self.course.name}'    

