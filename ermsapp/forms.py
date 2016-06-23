from django import forms
from ermsapp.models import *
from django.contrib.auth.models import User
from bootstrap3_datetime.widgets import DateTimePicker



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('Post','NoOfInterviews','InterviewType')


class DepartmentForm(forms.ModelForm):
    class Meta:
        model=Department
        fields = ('DeptName',)

class DateInput(forms.DateInput):
    input_type = 'date'


#personal
class DEO_Entry_PersonalForm(forms.ModelForm):
    PImage = forms.ImageField(label='Personal Image',help_text="Upload Profile Image",required=False)
    CVPDF = forms.ImageField(label='CV Image',help_text="Upload CV Image",required=False)
    FName = forms.CharField(label = "First Name",widget=forms.TextInput(attrs={'size':50}),help_text="Enter First Name",required=True)
    LName = forms.CharField(label = "Last Name",widget=forms.TextInput(attrs={'size':50}),help_text="Enter Last Name")
    FullName = forms.CharField(label = "Full Name",widget=forms.TextInput(attrs={'size':50}),help_text="Enter Full Name e.g: John Fitzgerald Kennedy")
    ContactNum = forms.CharField(label="Contact Number",widget=forms.TextInput(attrs={'size':10}),help_text="e.g: 071xxxxxxx")
    DOB = forms.DateField(label="Date Of Birth",widget=DateInput())
    Email = forms.EmailField(help_text="e.g: someone@somemail.com")
    FacebookProf = forms.CharField(label="Facebook Name",widget=forms.TextInput(attrs={'size':50}))
    LinkedInProf = forms.CharField(label="LinkedIn Name",widget=forms.TextInput(attrs={'size':50}))
    AddressLine1 = forms.CharField(label="Address Line 1",widget=forms.TextInput(attrs={'size':50}))
    AddressLine2 = forms.CharField(label="Address Line 2",widget=forms.TextInput(attrs={'size':50}))
    AddressLine3 = forms.CharField(label="Address Line 3",widget=forms.TextInput(attrs={'size':50}))
    AddressLine4 = forms.CharField(label="Address Line 4",widget=forms.TextInput(attrs={'size':50}),required=False)
    Nationality = forms.CharField(label="Nationality",widget=forms.TextInput(attrs={'size':50}))


    class Meta:
        model = Person
        fields = ('FName','LName','FullName','NIC','Nationality','DOB','AddressLine1','AddressLine2','AddressLine3','AddressLine4','ContactNum','Email','FacebookProf','LinkedInProf','PImage','CVPDF','Objective','SpecialNotes')
        widgets = {
                  'SpecialNotes': forms.Textarea(attrs={'rows':6, 'cols':50}),
                  'Objective': forms.Textarea(attrs={'rows':6, 'cols':50}),
                 }

#personal


class DEO_Entry_OoAQualification(forms.ModelForm):
    Subject = forms.CharField(label='Subject',widget=forms.TextInput(attrs={'size':50}))
    SubResult = forms.CharField(label='Result',widget=forms.TextInput(attrs={'size':5}))

    class Meta:
        model = SubQualification
        fields = ("Subject","SubResult")

class DEO_Entry_OoAQualification1(forms.ModelForm):
    Subject = forms.CharField(label='',widget=forms.TextInput(attrs={'size':50}))
    SubResult = forms.CharField(label='',widget=forms.TextInput(attrs={'size':5}))
    class Meta:
        model = SubQualification
        fields = ("Subject","SubResult")

class DEO_Entry_OoAQualification2(forms.ModelForm):
    Subject = forms.CharField(label='',widget=forms.TextInput(attrs={'size':50}))
    SubResult = forms.CharField(label='',widget=forms.TextInput(attrs={'size':5}))
    class Meta:
        model = SubQualification
        fields = ("Subject","SubResult")

class DEO_Entry_OoAQualification3(forms.ModelForm):
    Subject = forms.CharField(label='',widget=forms.TextInput(attrs={'size':50}))
    SubResult = forms.CharField(label='',widget=forms.TextInput(attrs={'size':5}))
    class Meta:
        model = SubQualification
        fields = ("Subject","SubResult")

class DEO_Entry_OoAQualification4(forms.ModelForm):
    Subject = forms.CharField(label='',widget=forms.TextInput(attrs={'size':50}))
    SubResult = forms.CharField(label='',widget=forms.TextInput(attrs={'size':5}))
    class Meta:
        model = SubQualification
        fields = ("Subject","SubResult")

class DEO_Entry_OoAQualification5(forms.ModelForm):
    Subject = forms.CharField(label='',widget=forms.TextInput(attrs={'size':50}))
    SubResult = forms.CharField(label='',widget=forms.TextInput(attrs={'size':5}))
    class Meta:
        model = SubQualification
        fields = ("Subject","SubResult")

class DEO_Entry_OoAQualification6(forms.ModelForm):
    Subject = forms.CharField(label='',widget=forms.TextInput(attrs={'size':50}))
    SubResult = forms.CharField(label='',widget=forms.TextInput(attrs={'size':5}))
    class Meta:
        model = SubQualification
        fields = ("Subject","SubResult")

class DEO_Entry_OoAQualification7(forms.ModelForm):
    Subject = forms.CharField(label='',widget=forms.TextInput(attrs={'size':50}))
    SubResult = forms.CharField(label='',widget=forms.TextInput(attrs={'size':5}))
    class Meta:
        model = SubQualification
        fields = ("Subject","SubResult")

class DEO_Entry_OoAQualification8(forms.ModelForm):
    Subject = forms.CharField(label='',widget=forms.TextInput(attrs={'size':50}))
    SubResult = forms.CharField(label='',widget=forms.TextInput(attrs={'size':5}))
    class Meta:
        model = SubQualification
        fields = ("Subject","SubResult")

class DEO_Entry_OoAQualification9(forms.ModelForm):
    Subject = forms.CharField(label='',widget=forms.TextInput(attrs={'size':50}))
    SubResult = forms.CharField(label='',widget=forms.TextInput(attrs={'size':5}))
    class Meta:
        model = SubQualification
        fields = ("Subject","SubResult")

#Other Qualification
class DEO_Entry_QualificationForm(forms.ModelForm):

    CHOICES=[('select1','Educational'),
            ('select2','Proffesional')]

    QName = forms.CharField(label="Qualification",widget=forms.TextInput(attrs={'size':50}))
    QType = forms.ChoiceField(label="Qualification Type",widget=forms.RadioSelect(),choices=CHOICES)
    Result = forms.CharField(widget=forms.TextInput(attrs={'size':50}),help_text="Entire result for the qualification",required=False)

    class Meta:
        model = SubQualification
        fields =("QName","QType",'Result')


class DEO_Entry_SubQualificationForm(forms.ModelForm):
    Subject = forms.CharField(widget=forms.TextInput(attrs={'size':50}))
    SubResult = forms.CharField(label='Subject Result',widget=forms.TextInput(attrs={'size':5}))

    class Meta:
        model = SubQualification
        fields =('Subject','SubResult')

#Other Qualification


class DEO_DegreeChoiceForm(forms.ModelForm):

    class Meta:
        model = Degree
        fields =('University','DegreeType','DegreeField')


class DEO_Entry_DegreeForm(forms.ModelForm):

    class Meta:
        model = Person_Degree
        fields =('Degree','Year','Class','SpecialNotes')


class DEO_Entry_Skill1(forms.ModelForm):
    Skill = forms.Textarea()
    class Meta:
        model = Skill
        fields =('Skill',)
        widgets = {
                  'Skill': forms.Textarea(attrs={'rows':6, 'cols':100}),
                 }

class DEO_Entry_Skill2(forms.ModelForm):
    Skill = forms.Textarea()
    class Meta:
        model = Skill
        fields =('Skill',)
        widgets = {
                  'Skill': forms.Textarea(attrs={'rows':6, 'cols':100}),
                 }


class DEO_Entry_ExtraForm1(forms.ModelForm):

    class Meta:
        model = Extracurricular
        fields =('Extracurricular',)
        widgets = {
                  'Extracurricular': forms.Textarea(attrs={'rows':6, 'cols':100})
                }

class DEO_Entry_ExtraForm2(forms.ModelForm):

    class Meta:
        model = Extracurricular
        fields =('Extracurricular',)
        widgets = {
                  'Extracurricular': forms.Textarea(attrs={'rows':6, 'cols':100})
                }


class DEO_Entry_SportForm1(forms.ModelForm):
    Sports = forms.Textarea()
    class Meta:
        model = Sports
        fields =('Sports',)
        widgets = {
                  'Sports': forms.Textarea(attrs={'rows':6, 'cols':100}),
                }


class DEO_Entry_SportForm2(forms.ModelForm):
    Sports = forms.Textarea()
    class Meta:
        model = Sports
        fields =('Sports',)
        widgets = {
                  'Sports': forms.Textarea(attrs={'rows':6, 'cols':100}),
                }

class DEO_Entry_ExperienceForm(forms.ModelForm):
    Field = forms.CharField(widget=forms.TextInput(attrs={'size':50}))
    Duration = forms.CharField(widget=forms.TextInput(attrs={'size':50}))
    AltPost = forms.CharField(label = "Alternative Post",widget=forms.TextInput(attrs={'size':50}),help_text="If the Post is not defiened above enter your post")
    class Meta:
        model = Experience
        exclude = ('Person',)
        widgets = {
                  'Notes': forms.Textarea(attrs={'rows':6, 'cols':100}),
                }


class DEO_Enret_SpecialAchievements(forms.ModelForm):
    Heading_1 = forms.CharField(label="Main Heading")
    Heading_2 = forms.CharField(label="Sub Heading")
    class Meta:
        model = SpecialAchievements
        exclude = ("Person",)



class DEO_EntryForm(forms.Form):
    NIC = forms.CharField(widget=forms.TextInput(attrs={'size':50}),help_text="Enter Person's NIC number")




