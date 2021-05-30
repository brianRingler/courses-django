from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Course, Description, Comment
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Avg


def index_view(request):
    return render(request, 'index.html')


def add_courses_view(request):

    if request.method == 'POST':

        # pass post data to ValidationManager method "validate"
        errors = Course.objects.validate(request.POST)

        if len(errors) > 0:
            for k, v in errors.items():
                # v is error msg can also pass k which is input name
                messages.error(request, v)

            return JsonResponse(errors, status=200)  
            # return redirect('/courses')


        Course.objects.create(
                course_name = request.POST.get('course-name-nm', None)
        )

        # create instance of last record from Course 
        course_added = Course.objects.all().last()

        # create relationship between Course and Description
        Description.objects.create(
                    course = course_added, 
                    course_desc = request.POST.get('course-desc-nm', None)
                )

        context =   {
                        'courses' : Course.objects.all()
                    }

        return render(request, 'add_courses.html', context)
    
    
    # GET request pass data    
    context =   {
                'courses' : Course.objects.all(),
                'avg_rating' : Course.objects.values('id').annotate(Avg('course_name_fk__rating'))
            }

    return render(request, 'add_courses.html', context)


def delete_courses_view(request, id_del):

    if request.method == 'POST':

        course_del = Course.objects.get(id=id_del)
        course_del.delete()

        return redirect('/courses')

    context = {
        'course' : Course.objects.get(id=id_del)
    }

    return render(request, 'delete_courses.html', context)


def comment_courses_view(request, id_rate):

    if request.method == 'POST':
                
        Comment.objects.create(
            rating = request.POST.get('course-rating-nm', None),
            comment = request.POST.get('course-comm-nm', None),
            course =  Course.objects.get(id=id_rate)
        ) 
        return redirect('/courses') 

    '''the id_rate is from Course table. First, get all comments then 
    filter using id_rate but based on Course table'''

    # filter based on id from the Course table 
    context = {
        'all_comm_rate' :  Comment.objects.filter(course__id=id_rate),
        'id_comm' : id_rate,
        'course_name' : Course.objects.get(id=id_rate)
    }    

    return render(request, 'comment_courses.html', context)