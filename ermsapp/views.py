
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from ermsapp.forms import *
from ermsapp.models import *
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from datetime import date
from dateutil.relativedelta import relativedelta
from django.utils.timezone import now



def getPostDetail(request):
    if request.method == 'POST':
        post = PostForm(request.POST)
        if post.is_valid() :
            post.save()
            return HttpResponse('saved to the db')
    else:
        post= PostForm()

    return render(request, 'post_form.html', {'PostForm': post})


def getDepartment(request):
    if request.POST :
        department = DepartmentForm(request.POST)
        if department.is_valid() :
            department.save()
            return HttpResponse('saved to the db')
    else:
        department= DepartmentForm()

    return render(request, 'dept_form.html', {'DepartmentForm': department})

#deo views start#

def DEO_Entry(request):
    if request.POST:
        deo_form = DEO_EntryForm(request.POST)
        if deo_form.is_valid():
            #data = deo_form.cleaned_data['NIC']

            #check = Person.objects.get(NIC__exact=data)
            limit = date.today()-relativedelta(month=3)
            valid = Person.objects.get(Date__gte=now())
            if valid.is_empty:
                return HttpResponseRedirect('personal_info')
            else:
                return HttpResponse("Person details are already enterd in the system")

        else:
            context={
                'deo_form': deo_form,
                'completion': 'complete all the fields before proceding',
                'topic': 'Personal Information',
            }
            return render_to_response('deo/deo_entry.html',context)
    else:
        deo_form = DEO_EntryForm()

    args = {}
    args.update(csrf(request))

    args['deo_form'] = deo_form
    args['topic']= 'DEO Entry'
    return render_to_response('deo/deo_entry.html',args)


@login_required(login_url='/accounts/login/')

def DEO_Entry_Personal(request):
    if request.POST:
        deo_form1 = DEO_Entry_PersonalForm(request.POST,request.FILES)
        if deo_form1.is_valid():
            data=deo_form1.save()
            data.date = date.today()
            data.save()


            return HttpResponseRedirect('degreechoice',data)
        else:
            u=Person.objects.filter(NIC__startswith="93")
            context={
                'deo_form': deo_form1,
                'completion': 'complete all the fields before proceding',
                'topic': 'Personal Information',
            }
            return render_to_response('deo/deo_personal.html',context)
    else:
        deo_form1 = DEO_Entry_PersonalForm()

    args = {}
    args.update(csrf(request))

    args['deo_form'] = deo_form1
    args['topic']= 'Personal Information'
    return render_to_response('deo/deo_personal.html',args)


@login_required(login_url='/accounts/login/')
def DEO_DegreeChoice(request):
    if request.POST:
        deo_form1 = DEO_DegreeChoiceForm(request.POST)
        if deo_form1.is_valid():
            uni = deo_form1.University
            type = deo_form1.DegreeType
            field = deo_form1.DegreeField
            deg= Degree.objects.filter(University__exact=uni,DegreeType__exact=type,DegreeField__exact=field),

            return HttpResponseRedirect('degree_info',deg)


        else:
            context={
                'deo_form': deo_form1,
                'completion': 'complete all the fields before proceding',
                'topic': 'Degree Information',
            }
            return render_to_response('deo/deo_degreechoice.html',context)
    else:
        deo_form1 = DEO_DegreeChoiceForm()

    args = {}
    args.update(csrf(request))

    args['deo_form'] = deo_form1
    args['topic']= 'Degree Specifications'
    return render_to_response('deo/deo_degreechoice.html',args)


@login_required(login_url='/accounts/login/')
def DEO_Entry_Degree(request):
    if request.POST:
        deo_form1 = DEO_Entry_DegreeForm(request.POST)
        if deo_form1.is_valid():

            data=deo_form1.save(commit=False)
            data.Person = Person.objects.latest("id")
            data.save()

            return HttpResponseRedirect('degreechoice')
        else:
            context={
                'deo_form': deo_form1,
                'completion': 'complete all the fields before proceding',
                'topic': 'Degree Information',
            }
            return render_to_response('deo/deo_degree.html',context)
    else:
        deo_form1 = DEO_Entry_DegreeForm()

    args = {}
    args.update(csrf(request))

    args['deo_form'] = deo_form1
    args['topic']= 'Degree Information'
    return render_to_response('deo/deo_degree.html',args)


@login_required(login_url='/accounts/login/')
def DEO_Entry_OoA(request):
    if request.POST:
        deo_form_ol1 = DEO_Entry_OoAQualification(request.POST)
        deo_form_ol2 = DEO_Entry_OoAQualification1(request.POST)
        deo_form_ol3 = DEO_Entry_OoAQualification2(request.POST)
        deo_form_ol4 = DEO_Entry_OoAQualification3(request.POST)
        deo_form_ol5 = DEO_Entry_OoAQualification4(request.POST)
        deo_form_ol6 = DEO_Entry_OoAQualification5(request.POST)
        deo_form_ol7 = DEO_Entry_OoAQualification6(request.POST)
        deo_form_ol8 = DEO_Entry_OoAQualification7(request.POST)
        deo_form_ol9 = DEO_Entry_OoAQualification8(request.POST)
        deo_form_ol10 = DEO_Entry_OoAQualification9(request.POST)


        if deo_form_ol1.is_valid() and deo_form_ol2.is_valid() and deo_form_ol3.is_valid() and deo_form_ol4.is_valid() and deo_form_ol5.is_valid() and deo_form_ol6.is_valid() and deo_form_ol7.is_valid() and deo_form_ol8.is_valid() and deo_form_ol9.is_valid() and deo_form_ol10.is_valid():

            ol1 = deo_form_ol1.save(commit=False)
            ol1.QName  = "Ordinary Level"
            ol1.person = Person.objects.latest('id')
            ol1.QType = True
            ol1.save()

            ol2 = deo_form_ol2.save(commit=False)
            ol2.QName  = "Ordinary Level"
            ol2.person = Person.objects.latest('id')
            ol2.QType = True
            ol2.save()

            ol3 = deo_form_ol3.save(commit=False)
            ol3.QName  = "Ordinary Level"
            ol3.person = Person.objects.latest('id')
            ol3.QType = True
            ol3.save()

            ol4 = deo_form_ol4.save(commit=False)
            ol4.QName  = "Ordinary Level"
            ol4.person = Person.objects.latest('id')
            ol4.QType = True
            ol4.save()

            ol5 = deo_form_ol5.save(commit=False)
            ol5.QName  = "Ordinary Level"
            ol5.person = Person.objects.latest('id')
            ol5.QType = True
            ol5.save()

            ol6 = deo_form_ol6.save(commit=False)
            ol6.QName  = "Ordinary Level"
            ol6.person = Person.objects.latest('id')
            ol6.QType = True
            ol6.save()

            ol7 = deo_form_ol7.save(commit=False)
            ol7.QName  = "Ordinary Level"
            ol7.person = Person.objects.latest('id')
            ol7.QType = True
            ol7.save()

            ol8 = deo_form_ol8.save(commit=False)
            ol8.QName  = "Ordinary Level"
            ol8.person = Person.objects.latest('id')
            ol8.QType = True
            ol8.save()

            ol9 = deo_form_ol9.save(commit=False)
            ol9.QName  = "Ordinary Level"
            ol9.person = Person.objects.latest('id')
            ol9.QType = True
            ol9.save()

            ol10 = deo_form_ol10.save(commit=False)
            ol10.QName  = "Ordinary Level"
            ol10.person = Person.objects.latest('id')
            ol10.QType = True
            ol10.save()


            return HttpResponse("good")#ResponseRedirect('ermsapp/DEO/qual_other')
        else:
            context={
                'deo_form_ol1': deo_form_ol1,
                'deo_form_ol2': deo_form_ol2,
                'completion': 'complete all the fields before proceding',
                'topic': 'O/L and A/L'
            }
            return render_to_response('deo/deo_OoA.html',context)
    else:
        deo_form_ol1 = DEO_Entry_OoAQualification()
        deo_form_ol2 = DEO_Entry_OoAQualification1()
        deo_form_ol3 = DEO_Entry_OoAQualification2()
        deo_form_ol4 = DEO_Entry_OoAQualification3()
        deo_form_ol5 = DEO_Entry_OoAQualification4()
        deo_form_ol6 = DEO_Entry_OoAQualification5()
        deo_form_ol7 = DEO_Entry_OoAQualification6()
        deo_form_ol8 = DEO_Entry_OoAQualification7()
        deo_form_ol9 = DEO_Entry_OoAQualification8()
        deo_form_ol10 = DEO_Entry_OoAQualification9()


    args = {}
    args.update(csrf(request))

    args['deo_form_ol1'] = deo_form_ol1
    args['deo_form_ol2'] = deo_form_ol2
    args['deo_form_ol3'] = deo_form_ol3
    args['deo_form_ol4'] = deo_form_ol4
    args['deo_form_ol5'] = deo_form_ol5
    args['deo_form_ol6'] = deo_form_ol6
    args['deo_form_ol7'] = deo_form_ol7
    args['deo_form_ol8'] = deo_form_ol8
    args['deo_form_ol9'] = deo_form_ol9
    args['deo_form_ol10'] = deo_form_ol10
    args['topic']= 'O/L and A/L'
    return render_to_response('deo/deo_OoA.html',args)


@login_required(login_url='/accounts/login/')
def DEO_Entry_Qualification(request):
    if request.POST:
        deo_form1 = DEO_Entry_QualificationForm(request.POST)
        if deo_form1.is_valid():


            completion= 'Successfully added previous Qualification data to the system'
            return HttpResponseRedirect('sub_qualification',completion)
        else:
            context={
                'deo_form': deo_form1,
                'completion': 'complete all the fields before proceding',
                'topic': 'Other Qualification',
            }
            return render_to_response('deo/deo_otherqual.html',context)
    else:
        deo_form1 = DEO_Entry_QualificationForm()

        args = {}
        args.update(csrf(request))

        args['deo_form'] = deo_form1
        args['topic']= 'Other Qualification'
        return render_to_response('deo/deo_otherqual.html',args)


@login_required(login_url='/accounts/login/')
def DEO_Entry_SubQualification(request):
    if request.POST:
        deo_form1 = DEO_Entry_SubQualificationForm(request.POST)
        if deo_form1.is_valid():


            completion= 'Successfully added previous Qualification data to the system'
            return HttpResponseRedirect('sub_qualification',completion)
        else:

            context={
                'deo_form': deo_form1,
                'completion': 'complete all the fields before proceding',
                'topic': 'Other Qualification',
                'relavance':"Enter Subjectwise result of ",
                'qname': SubQualification.objects.latest("QName"),
            }
            return render_to_response('deo/deo_otherqual_sub.html',context)
    else:
        deo_form1 = DEO_Entry_SubQualificationForm()

        args = {}
        args.update(csrf(request))

        args['deo_form'] = deo_form1
        args['topic']= 'Other Qualification'
        return render_to_response('deo/deo_otherqual_sub.html',args)

@login_required(login_url='/accounts/login/')
def DEO_Entry_Skills(request):
    if request.POST:
        deo_form1 = DEO_Entry_Skill1(request.POST)
        deo_form2 = DEO_Entry_Skill2(request.POST)
        if deo_form1.is_valid() and deo_form2.is_valid():
            s1 = deo_form1.save(commit=False)
            s1.Person = Person.objects.latest("ID")
            s1.save()
            s2 = deo_form2.save(commit=False)
            s2.Person = Person.objects.latest("ID")
            s2.save()
            completion= 'Successfully added previous Qualification data to the system'
            return HttpResponseRedirect('skills',completion)
        else:

            context={
                'deo_form1': deo_form1,
                'deo_form2': deo_form2,
                'completion': 'complete all the fields before proceding',
                'topic': 'Skills',

            }
            return render_to_response('deo/deo_skills.html',context)
    else:
        deo_form1 = DEO_Entry_Skill1()
        deo_form2 = DEO_Entry_Skill2()

        args = {}
        args.update(csrf(request))

        args['deo_form1'] = deo_form1
        args['deo_form2'] = deo_form2
        args['topic']= 'Skills'
        return render_to_response('deo/deo_skills.html',args)


@login_required(login_url='/accounts/login/')
def DEO_Entry_Extra(request):
    if request.POST:
        deo_form1 = DEO_Entry_ExtraForm1(request.POST)
        deo_form2 = DEO_Entry_ExtraForm2(request.POST)
        if deo_form1.is_valid() and deo_form2.is_valid():
            s1 = deo_form1.save(commit=False)
            s1.Person = Person.objects.latest("ID")
            s1.save()
            s2 = deo_form2.save(commit=False)
            s2.Person = Person.objects.latest("ID")
            s2.save()
            completion= 'Successfully added previous Extracurricular data to the system'
            return HttpResponseRedirect('extra_info',completion)
        else:

            context={
                'deo_form1': deo_form1,
                'deo_form2': deo_form2,
                'completion': 'complete all the fields before proceding',
                'topic': 'Extracurricular Activities',
            }
            return render_to_response('deo/deo_extra.html',context)
    else:
        deo_form1 = DEO_Entry_ExtraForm1()
        deo_form2 = DEO_Entry_ExtraForm2()

        args = {}
        args.update(csrf(request))

        args['deo_form1'] = deo_form1
        args['deo_form2'] = deo_form2
        args['topic']= 'Extracurricular Activities'
        return render_to_response('deo/deo_extra.html',args)


@login_required(login_url='/accounts/login/')
def DEO_Entry_Sport(request):
    if request.POST:
        deo_form1 = DEO_Entry_SportForm1(request.POST)
        deo_form2 = DEO_Entry_SportForm2(request.POST)
        if deo_form1.is_valid() and deo_form2.is_valid():
            s1 = deo_form1.save(commit=False)
            s1.Person = Person.objects.latest("ID")
            s1.save()
            s2 = deo_form2.save(commit=False)
            s2.Person = Person.objects.latest("ID")
            s2.save()
            completion= 'Successfully added previous Sport data to the system'
            return HttpResponseRedirect('sport_info',completion)
        else:

            context={
                'deo_form1': deo_form1,
                'deo_form2': deo_form2,
                'completion': 'complete all the fields before proceding',
                'topic': 'Sports',
            }
            return render_to_response('deo/deo_sport.html',context)
    else:
        deo_form1 = DEO_Entry_SportForm1()
        deo_form2 = DEO_Entry_SportForm2()

        args = {}
        args.update(csrf(request))

        args['deo_form1'] = deo_form1
        args['deo_form2'] = deo_form2
        args['topic']= 'Sports'
        return render_to_response('deo/deo_sport.html',args)



@login_required(login_url='/accounts/login/')
def DEO_Entry_Experience(request):
    if request.POST:
        deo_form = DEO_Entry_ExperienceForm(request.POST)
        if deo_form.is_valid():
            ex = deo_form.save(commit=False)
            ex.Person = Person.objects.latest("ID")
            ex.save()
            completion= 'Successfully added previous Experience data to the system'
            return HttpResponseRedirect('experience_info',completion)
        else:

            context={
                'deo_form': deo_form,
                'completion': 'complete all the fields before proceding',
                'topic': 'Experience',
            }
            return render_to_response('deo/deo_experience.html',context)
    else:
        deo_form = DEO_Entry_ExperienceForm()


        args = {}
        args.update(csrf(request))

        args['deo_form'] = deo_form
        args['topic']= 'Experience'
        return render_to_response('deo/deo_experience.html',args)


@login_required(login_url='/accounts/login/')
def DEO_Entry_SpecialAchievements(request):
    if request.POST:
        deo_form = DEO_Entry_SpecialAchievements(request.POST)
        if deo_form.is_valid():
            sp = deo_form.save(commit=False)
            sp.Person = Person.objects.latest("ID")
            sp.save()
            completion= 'Successfully added previous Achivement data to the system'
            return HttpResponseRedirect('spcl_achvmnt_info',completion)
        else:

            context={
                'deo_form': deo_form,
                'completion': 'complete all the fields before proceding',
                'topic': 'Special Achievements',
            }
            return render_to_response('deo/deo_special_achievement.html',context)
    else:
        deo_form = DEO_Entry_SpecialAchievements()

        args = {}
        args.update(csrf(request))
        args['deo_form'] = deo_form
        args['topic']= 'Special Achievements'
        return render_to_response('deo/deo_special_achievement.html',args)