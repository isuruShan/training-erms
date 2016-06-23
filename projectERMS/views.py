from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from projectERMS.forms import user_form,profile_form,DegreeType_Form
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ermsapp.models import Users,UserRole

#login views start#


def login_view(request):
    c={}
    c.update(csrf(request))
    return render_to_response('login.html', c)


def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username.strip(),password=password)
    u=User.objects.get(username=username)
    u1 = Users.objects.get(User=u)
    ur1 = UserRole.objects.get(Role__exact="DEO")
    ur2 = UserRole.objects.get(Role__exact="Admin")
    ur3 = UserRole.objects.get(Role__exact="HOD")
    ur4 = UserRole.objects.get(Role__exact="HR")
    ur5 = UserRole.objects.get(Role__exact="Interviewer")
    if user is not None:
        if user.is_active:
            if  u1.UserRole== ur1:
                auth.login(request,user)
                return HttpResponseRedirect("../../ermsapp/DEO/logedindeo")
            elif u1.UserRole== ur2:
                return HttpResponse("fuck you")
            elif u1.UserRole== ur3:
                auth.login(request,user)
                return HttpResponseRedirect("../../ermsapp/DEO/logedindeo")
            if  u1.UserRole== ur4:
                auth.login(request,user)
                return HttpResponseRedirect("../../ermsapp/DEO/logedindeo")
            if  u1.UserRole== ur5:
                auth.login(request,user)
                return HttpResponseRedirect("../../ermsapp/DEO/logedindeo")

        else:
            context={
                "login_error":"your account is no longer active"
    }
            return render(request, "login.html", context)
    else:
        return HttpResponseRedirect('invalid')


def invalid_view(request):
    context={

        "login_error":"Username or password is incorrect"
    }

    return render(request, "login.html", context)


def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect('../../accounts/login')


@login_required(login_url='/accounts/login/')
def logedindeo_view(request):
    context ={"topic":"Dashboard","user":request.user}

    return  render_to_response('deo/logedin.html',context)


#login views end#

#user registratoin views Stert#
@login_required(login_url='/accounts/login/')
def registration_view(request):
    if request.method=='POST':
        reg_form1= user_form(request.POST)
        reg_form2= profile_form(request.POST,request.FILES)

        if reg_form1.is_valid() and reg_form2.is_valid():
            u1 = reg_form1.save()
            u2= reg_form2.save(commit=False)
            u2.User = u1
            u2.save()
            registration = True
            return render_to_response('UserRegForm.html',{'registered':registration})

        else:
            context={
                'reg_form1': user_form(),
                'reg_form2': profile_form(),
                'completion': 'complete the registration fields before registering',
                'content': "Register Users"
            }
            return render_to_response('UserRegForm.html',context)

    args = {}
    args.update(csrf(request))

    args['reg_form1'] = user_form()
    args['reg_form2'] = profile_form()
    args['content'] = "Register User"
    return render_to_response('UserRegForm.html',args)

@login_required(login_url='/accounts/login/')
def registration_success():
    registration = True
    return render_to_response('UserRegForm.html',{'registered':registration})

#user registratoin views end#

@login_required(login_url='/accounts/login/')
def degreeType(request):
    if request.POST:
        form1=DegreeType_Form(request.POST)

        if form1.is_valid():
            form1.save()
            return HttpResponse('done')
        else:
            return HttpResponse('fuck')
    else:
        form1 = DegreeType_Form()
    args = {}
    args.update(csrf(request))
    args['form1'] = form1
    return render_to_response('deo/degreeType.html', args)