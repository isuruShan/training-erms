from django.conf.urls import url,include
from .views import *
from projectERMS.views import *

urlpatterns = [
    url(r'^DEO/logedin', logedindeo_view),
    url(r'^Post',getPostDetail),
    url(r'^Department',getDepartment),
    url(r'^DEO/entry',DEO_Entry),
    url(r'^DEO/personal_info',DEO_Entry_Personal),
    url(r'^DEO/degreechoice',DEO_DegreeChoice),
    url(r'^DEO/degree_info',DEO_Entry_Degree),
    url(r'^DEO/OLoAL',DEO_Entry_OoA),
    url(r'^DEO/degreetype',degreeType),
    url(r'^DEO/qualification',DEO_Entry_Qualification),
    url(r'^DEO/sub_qualification',DEO_Entry_SubQualification),
    url(r'^DEO/skills',DEO_Entry_Skills),
    url(r'^DEO/extra_info',DEO_Entry_Extra),
    url(r'^DEO/sport_info',DEO_Entry_Sport),
    url(r'^DEO/experience_info',DEO_Entry_Experience),
    url(r'^DEO/spcl_achvmnt_info',DEO_Entry_SpecialAchievements)

]