from django.db import models
from django.db.models.deletion import CASCADE

class ValidationManager(models.Manager):
    def validate(self, post_data):
        '''Custom validation to check that course name is more than 5 characters and
        description is more than 15.'''

        errors = {}

        if len(post_data['course-name-nm']) < 5:
            errors['course-name-nm'] = 'Required length course name is 5 characters.'

        if len(post_data['course-desc-nm']) < 15:
            errors['course-desc-nm'] = 'Course description required length 15 characters.'

        return errors



'''creating an instance of "Course". Use "related_name" to access the properties of "Description" '''
class Course(models.Model):
    course_name = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ValidationManager()

    def __str__(self):
        return f'{self.course_name}'

class Comment(models.Model):
    USER_RATING = [
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐⭐'),
    ]
    comment = models.CharField(max_length=255, null=True)
    rating = models.CharField(max_length=5, choices=USER_RATING, default=1, null=True)
    course = models.ForeignKey(Course, related_name='course_name_fk', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ValidationManager()
    
    def __str__(self):
        return f'{self.comment}, {self.rating}'

'''creating and instance of "Description" we would use "course" to access
the properties of "Course" '''
class Description(models.Model):
    course_desc = models.CharField(max_length=255, null=False)
    course = models.OneToOneField(Course, on_delete=models.CASCADE,related_name='description', primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ValidationManager()

    def __str__(self):
        return f'{self.course_desc}'