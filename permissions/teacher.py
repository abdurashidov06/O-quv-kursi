from django.http import HttpResponse


def teacher_requered(func):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            if request.user.role != 'teacher':
                return HttpResponse('SIzga mumkin emas')
        return func(request,*args,**kwargs)

    return wrapper