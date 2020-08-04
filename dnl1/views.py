from django.shortcuts import render
from photogallery.models import Topic
from teachers.models import Teacher
import datetime

def page_is_in_work(request):
    return render(request, 'dnl1/page-is-in-work.html')

def index(request):
    return render(request, 'dnl1/homePage.html')

def about_us(request):
    try:
        old_photos_alb = Topic.objects.get(name = 'Старі фотографії')
    except: 
        old_photos_alb = False
    return render(request, 'dnl1/about-us.html', {'old_photos_alb': old_photos_alb})

def contacts(request):
    return render(request, 'dnl1/contacts.html')
    
def entry_rules(request):
    return render(request, 'dnl1/entry-rules.html')

def vacancies(request):
    return render(request, 'dnl1/vacancies.html')

def inclination(request):
    return render(request, 'dnl1/inclination.html')

def material_base(request):
    try:
        material_alb = Topic.objects.get(name = 'Матеріальна база')  
        images = Topic.objects.get(name = 'Матеріальна база').photo_set.all()
    except: 
        material_alb = False
    return render(request, 'dnl1/material-base.html', {'material_alb': material_alb, 'images': images})

def educational_activities(request):
    return render(request, 'dnl1/educational-activities.html')

def zno(request):
    return render(request, 'dnl1/zno.html')

def social_service(request):
    return render(request, 'dnl1/social-service.html')

def psychological_service(request):
    return render(request, 'dnl1/psychological-service.html')

def medical_service(request):
    return render(request, 'dnl1/medical-service.html')
    

def collective(request):
    teachers = Teacher.objects.all()
    return render(request, 'dnl1/collective.html', {'teachers':teachers})

def year_structure(request):
    return render(request, 'dnl1/year-structure.html')

def dining(request):
    return render(request, 'dnl1/dining.html')

def library(request):
    return render(request, 'dnl1/library.html')

def circle_schedule(request):
    return render(request, 'dnl1/circle-schedule.html')
    
def rings_schedule(request):
    return render(request, 'dnl1/rings-schedule.html')

def questionnaire_parents(request):
    return render(request, 'dnl1/questionnaire_parents.html')
    
def questionnaire_pupils(request):
    return render(request, 'dnl1/questionnaire_pupils.html')

def events(request):
    return render(request, 'dnl1/events.html')

def educational_system(request):
    return render(request, 'dnl1/educational-system.html')

def teachers_recs(request):
    return render(request, 'dnl1/teachers-recommendations.html')

# pages in work
def license(request):
    return page_is_in_work(request)


#pages with google documents
def statut(request):
    page_name = 'Статут ліцею'
    links = (
        ['', 'https://drive.google.com/file/d/1chSGn1oFPE2DPbz62Pkpp8FmLkKXC1lj/preview'],
        ['', 'https://drive.google.com/file/d/1TI5VSDabTLNVGB6ThjvO3haXNGAbfCrJ/preview']
    )
    return render(request, 'dnl1/google-documents-page.html', {'page_name': page_name, 'links': links})

def financial_statements(request):
    page_name = 'Фінансова звітність'
    links = (
        ['', 'https://drive.google.com/file/d/1ryHn4ulftKhH_BQRqOW-RZAGCrbhUtBK/preview'],
    )
    return render(request, 'dnl1/google-documents-page.html', {'page_name': page_name, 'links': links})

def educational_programs(request):
    page_name = 'Освітні програми'
    links = (
        ['', 'https://drive.google.com/file/d/1QCKGXM-ZN4_GsPVnga00ptNfmrPF7hfd/preview'],
        ['5-6 класи', 'https://drive.google.com/file/d/1iqt9g_RCMCROZ4r0JlOZZb-JHFytzxQz/preview'],
        ['7-8 класи', 'https://drive.google.com/file/d/1FeY9sxJ5x3hKSeFfeXMM5JQeZ1sRqRZB/preview'],
        ['9аб класи', 'https://drive.google.com/file/d/1Jw4hzDhQO-jOa4RCns5fxTFurlPs3C_L/preview'],
        ['10 класи', 'https://drive.google.com/file/d/1xyRtKpBvrw9MZ0Wb3t8H1R2kzBHPv2wF/preview'],
        ['11 класи', 'https://drive.google.com/file/d/1TXHqJoIk7qd3Hxfm7xoB3dJRSocwBBvu/preview'],
    )
    return render(request, 'dnl1/google-documents-page.html', {'page_name': page_name, 'links': links})

def books_selection(request):
    page_name = 'Вибір підручників'
    links = (
        ['', 'https://drive.google.com/file/d/1yDaF2VdVRvIRq5GGn7mkxGkMiVWdArh6/preview'],
    )
    return render(request, 'dnl1/google-documents-page.html', {'page_name': page_name, 'links': links})

def work_plan(request):
    page_name = 'Річний план ліцею'
    links = (
        ['', 'https://drive.google.com/file/d/1KOafxF8szmtQgFBJqex7dJbegfRwQyvs/preview'],
    )
    return render(request, 'dnl1/google-documents-page.html', {'page_name': page_name, 'links': links})

def pedagogical_meetings(request):
    page_name = 'Педагогічні ради'
    links = (
        ['', 'https://drive.google.com/file/d/1zVyC1N7o_Sx2m_viaBtwitddDBRhhioK/preview'],
    )
    return render(request, 'dnl1/google-documents-page.html', {'page_name': page_name, 'links': links})
    
def orders(request):
    page_name = 'Накази'
    links = (
        ['', 'https://drive.google.com/file/d/11Wjxj_cZJyIMoTxayvYeGZwfRmIB05JP/preview'],
        ['', 'https://drive.google.com/file/d/1tA3sUfts9Xi9YW-wrIfUoeYRtBgOqB3i/preview'],
    )
    return render(request, 'dnl1/google-documents-page.html', {'page_name': page_name, 'links': links})

def activity_report(request):
    page_name = 'Звіт про діяльність закладу'
    links = (
        ['', 'https://drive.google.com/file/d/1PPFtfePEoZUm7LspkgnLQcZvKKq2hXTb/preview'],
        ['', 'https://drive.google.com/file/d/1bG7M3IbQBCVpGrWEqeKpUbLDadp7layf/preview'],
    )
    return render(request, 'dnl1/google-documents-page.html', {'page_name': page_name, 'links': links})