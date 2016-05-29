from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.urlresolvers import reverse
from .models import Subject, Enrollment, Student
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
import sys
import json
# Create your views here.

def home(request):
    username = User.objects.get(username=request.session['username'])
    student = Student.objects.filter(username__username=username)
    if not student:
        return render(request,'userprofile.html')
    else:
        return render(request,'home.html')

def homeD3(request):
    username = User.objects.get(username=request.session['username'])
    student = Student.objects.filter(username__username=username)
    if not student:
        return render(request,'userprofile.html')
    else:
        return render(request,'homeD3.html')

def showprofile(request):
    return render(request,'showprofile.html')

def addprofile(request):

    if request.method == 'GET':
        return render(request,'addprofile.html')
    if request.method == 'POST':
        enroll = json.loads(request.body)  #jsEnrolled is python Object or python dictionary  #101
        #body={"CS101": {"sub_id": "CS101", "grade": "A", "term": "2", "year": "2555"}}
        enrolled_old = Enrollment.objects.all() #2 cs101 cs102
        enrolled_oldData = { str(i.sub_id) : { 'sub_id': str(i.sub_id),'term': str(i.term), 'year': str(i.year) , 'grade': i.grade} for i in enrolled_old }

        for k in enrolled_oldData: #cs101, cs102
            if k in enroll:
                pass
            else:
                #delete
                delete_enroll = Enrollment.objects.filter(sub_id=k)
                delete_enroll.delete()


        for key,value in enroll.iteritems():
            std_id = str(Student.objects.get(username__username=request.session['username']).std_id)

            #update
            if Enrollment.objects.filter(std_id__std_id = std_id ,sub_id__sub_id=key ).exists():
                record = Enrollment.objects.get(std_id__std_id=std_id, sub_id__sub_id=key ) 
                record.grade = value['grade']
                record.term = value['term']
                record.year = value['year']
                record.save()

            #add
            elif Enrollment.objects.filter(std_id__std_id = std_id ,sub_id__sub_id=key ).exists() is False:
                fk_std_id = Student.objects.get(std_id=std_id)
                fk_sub_id = Subject.objects.get(sub_id=key)
                #print >> sys.stderr, fk_sub_id
                new_enroll = Enrollment.objects.create(std_id=fk_std_id, sub_id=fk_sub_id, grade=value['grade'], term=value['term'], year=value['year'])
                new_enroll.save()

        return HttpResponse("OK")

def editprofile(request):
    return render(request,'editprofile.html')

def predict(request):
    std_id = str(Student.objects.get(username__username=request.session['username']).std_id)
    enroll = Enrollment.objects.filter(std_id__std_id = std_id)
    
    return render(request, 'predict.html')

def userprofile(request):
    if request.method == 'GET':
        return render(request, 'userprofile.html')

    if request.method == 'POST':
        userprofile = json.loads(request.body)

        for key,value in userprofile.iteritems():
            username = str(User.objects.get(username=request.session['username']))


            #update
            if Student.objects.filter(username__username=username).exists():
                record = Student.objects.get(username__username=username)
                #str except int
                record.firstname = value['firstname']
                record.lastname = value['lastname']
                #integer 10
                record.std_id = value['std_id']
                # @
                record.email = value['email']
                #float .00
                record.sch_gpa = value['sch_gpa']
                record.admit_year = value['admit_year']
                record.province_id = value['province_id']
                #print >> sys.stderr, value['firstname']
                record.save()

                #check field none

            #add
            elif Student.objects.filter(username__username=username).exists() is False:
                fk_username = User.objects.get(username=username)

                #else:
                new_student = Student.objects.create(username=fk_username,firstname=value['firstname'],lastname=value['lastname'],std_id=value['std_id'],email=value['email'],sch_gpa=value['sch_gpa'],admit_year= value['admit_year'], province_id=value['province_id'])
                new_student.save()

        return render(request, 'userprofile.html')

def jsonProvience(request):
    province = {'10':{'name':'10-bangkok'},'11':{'name':'11-nonthaburi'}}
    return JsonResponse(province)

def jsonSubject(request):
    subjectID = Subject.objects.all()

    subjectIDdata = { i.sub_id : {'sub_name' : i.sub_name} for i in subjectID } 
    return JsonResponse(subjectIDdata)

def jsonEnrollment(request):
    std_id = str(Student.objects.get(username__username=request.session['username']).std_id)
    enrollmentID = Enrollment.objects.filter(std_id=std_id)
    #enrollmentID = Enrollment.objects.filter(std_id__username__username=request.session['username'])
    enrollmentData = { i.sub_id.sub_id : { 'sub_id': i.sub_id.sub_id,'term': str(i.term), 'year': str(i.year) , 'grade': i.grade} for i in enrollmentID  }
    return JsonResponse(enrollmentData)

def jsonStudent(request):
    username = User.objects.get(username=request.session['username'])
    student = Student.objects.filter(username__username=username)
    #studentData = {i.username.username :{'std_id': i.std_id, 'firstname'i.firstname, 'lastname': i.lastname, 'email': i.email, 'province':i.province, 'gpa':i.gpa, 'admityear':i.admityear} for i in student}
    studentData = { 'user' :{'std_id': str(i.std_id), 'firstname': i.firstname, 'lastname': i.lastname,'email': i.email, 'sch_gpa': str(i.sch_gpa),'admit_year': str(i.admit_year), 'province_id':i.province_id } for i in student}
    return JsonResponse(studentData)

def test(request):
    return render(request,'test.html')


def coordinate_home(request):
    myfile1 = {
    "link": [
        {
            "source": 87,
            "target": 44,
            "type": "licensing"
        },
        {
            "source": 1,
            "target": 3,
            "type": "licensing"
        },
        {
            "source": 2,
            "target": 3,
            "type": "licensing"
        },
        {
            "source": 3,
            "target": 5,
            "type": "licensing"
        },
        {
            "source": 3,
            "target": 7,
            "type": "licensing"
        },
        {
            "source": 3,
            "target": 8,
            "type": "licensing"
        },
        {
            "source": 3,
            "target": 12,
            "type": "licensing"
        },
        {
            "source": 5,
            "target": 9,
            "type": "licensing"
        },
        {
            "source": 5,
            "target": 13,
            "type": "licensing"
        },
        {
            "source": 5,
            "target": 22,
            "type": "licensing"
        },
        {
            "source": 5,
            "target": 27,
            "type": "licensing"
        },
        {
            "source": 5,
            "target": 34,
            "type": "licensing"
        },
        {
            "source": 5,
            "target": 38,
            "type": "licensing"
        },
        {
            "source": 5,
            "target": 44,
            "type": "licensing"
        },
        {
            "source": 7,
            "target": 23,
            "type": "licensing"
        },
        {
            "source": 7,
            "target": 59,
            "type": "licensing"
        },
        {
            "source": 8,
            "target": 24,
            "type": "licensing"
        },
        {
            "source": 8,
            "target": 25,
            "type": "licensing"
        },
        {
            "source": 8,
            "target": 27,
            "type": "licensing"
        },
        {
            "source": 8,
            "target": 55,
            "type": "licensing"
        },
        {
            "source": 8,
            "target": 58,
            "type": "licensing"
        },
        {
            "source": 9,
            "target": 11,
            "type": "licensing"
        },
        {
            "source": 9,
            "target": 30,
            "type": "licensing"
        },
        {
            "source": 9,
            "target": 33,
            "type": "licensing"
        },
        {
            "source": 9,
            "target": 64,
            "type": "licensing"
        },
        {
            "source": 9,
            "target": 65,
            "type": "licensing"
        },
        {
            "source": 9,
            "target": 67,
            "type": "licensing"
        },
        {
            "source": 10,
            "target": 37,
            "type": "licensing"
        },
        {
            "source": 12,
            "target": 14,
            "type": "licensing"
        },
        {
            "source": 12,
            "target": 16,
            "type": "licensing"
        },
        {
            "source": 12,
            "target": 37,
            "type": "licensing"
        },
        {
            "source": 12,
            "target": 39,
            "type": "licensing"
        },
        {
            "source": 12,
            "target": 51,
            "type": "licensing"
        },
        {
            "source": 12,
            "target": 52,
            "type": "licensing"
        },
        {
            "source": 12,
            "target": 53,
            "type": "licensing"
        },
        {
            "source": 12,
            "target": 71,
            "type": "licensing"
        },
        {
            "source": 12,
            "target": 74,
            "type": "licensing"
        },
        {
            "source": 11,
            "target": 15,
            "type": "licensing"
        },
        {
            "source": 11,
            "target": 42,
            "type": "licensing"
        },
        {
            "source": 15,
            "target": 43,
            "type": "licensing"
        },
        {
            "source": 16,
            "target": 40,
            "type": "licensing"
        },
        {
            "source": 16,
            "target": 72,
            "type": "licensing"
        },
        {
            "source": 0,
            "target": 66,
            "type": "licensing"
        },
        {
            "source": 17,
            "target": 44,
            "type": "licensing"
        },
        {
            "source": 17,
            "target": 45,
            "type": "licensing"
        },
        {
            "source": 17,
            "target": 19,
            "type": "licensing"
        },
        {
            "source": 18,
            "target": 45,
            "type": "licensing"
        },
        {
            "source": 20,
            "target": 49,
            "type": "licensing"
        },
        {
            "source": 23,
            "target": 26,
            "type": "licensing"
        },
        {
            "source": 27,
            "target": 28,
            "type": "licensing"
        },
        {
            "source": 27,
            "target": 29,
            "type": "licensing"
        },
        {
            "source": 27,
            "target": 55,
            "type": "licensing"
        },
        {
            "source": 27,
            "target": 56,
            "type": "licensing"
        },
        {
            "source": 27,
            "target": 57,
            "type": "licensing"
        },
        {
            "source": 27,
            "target": 61,
            "type": "licensing"
        },
        {
            "source": 28,
            "target": 41,
            "type": "licensing"
        },
        {
            "source": 28,
            "target": 60,
            "type": "licensing"
        },
        {
            "source": 28,
            "target": 63,
            "type": "licensing"
        },
        {
            "source": 29,
            "target": 62,
            "type": "licensing"
        },
        {
            "source": 30,
            "target": 31,
            "type": "licensing"
        },
        {
            "source": 30,
            "target": 32,
            "type": "licensing"
        },
        {
            "source": 30,
            "target": 66,
            "type": "licensing"
        },
        {
            "source": 34,
            "target": 35,
            "type": "licensing"
        },
        {
            "source": 34,
            "target": 36,
            "type": "licensing"
        },
        {
            "source": 34,
            "target": 69,
            "type": "licensing"
        },
        {
            "source": 37,
            "target": 70,
            "type": "licensing"
        },
        {
            "source": 38,
            "target": 70,
            "type": "licensing"
        },
        {
            "source": 39,
            "target": 72,
            "type": "licensing"
        },
        {
            "source": 39,
            "target": 73,
            "type": "licensing"
        },
        {
            "source": 44,
            "target": 19,
            "type": "licensing"
        },
        {
            "source": 44,
            "target": 46,
            "type": "licensing"
        },
        {
            "source": 44,
            "target": 47,
            "type": "licensing"
        },
        {
            "source": 45,
            "target": 47,
            "type": "licensing"
        },
        {
            "source": 46,
            "target": 75,
            "type": "licensing"
        },
        {
            "source": 47,
            "target": 48,
            "type": "licensing"
        },
        {
            "source": 47,
            "target": 76,
            "type": "licensing"
        },
        {
            "source": 47,
            "target": 77,
            "type": "licensing"
        },
        {
            "source": 49,
            "target": 50,
            "type": "licensing"
        },
        {
            "source": 64,
            "target": 67,
            "type": "licensing"
        },
        {
            "source": 75,
            "target": 76,
            "type": "licensing"
        },
        {
            "source": 84,
            "target": 64,
            "type": "licensing"
        },
        {
            "source": 0,
            "target": 66,
            "type": "licensing"
        }
    ],
    "node": [
        {
            "name": "BA291",
            "type": "general"
        },
        {
            "name": "CS101",
            "type": "force"
        },
        {
            "name": "CS102",
            "type": "force"
        },
        {
            "name": "CS111",
            "type": "force"
        },
        {
            "name": "CS112",
            "type": "force"
        },
        {
            "name": "CS213",
            "type": "force"
        },
        {
            "name": "CS214",
            "type": "force"
        },
        {
            "name": "CS222",
            "type": "force"
        },
        {
            "name": "CS223",
            "type": "force"
        },
        {
            "name": "CS251",
            "type": "force"
        },
        {
            "name": "CS261",
            "type": "force"
        },
        {
            "name": "CS281",
            "type": "force"
        },
        {
            "name": "CS284",
            "type": "force"
        },
        {
            "name": "CS285",
            "type": "force"
        },
        {
            "name": "CS286",
            "type": "force"
        },
        {
            "name": "CS288",
            "type": "force"
        },
        {
            "name": "CS289",
            "type": "force"
        },
        {
            "name": "CS295",
            "type": "force"
        },
        {
            "name": "CS296",
            "type": "force"
        },
        {
            "name": "CS297",
            "type": "force"
        },
        {
            "name": "CS301",
            "type": "force"
        },
        {
            "name": "CS302",
            "type": "force"
        },
        {
            "name": "CS311",
            "type": "force"
        },
        {
            "name": "CS314",
            "type": "force"
        },
        {
            "name": "CS326",
            "type": "force"
        },
        {
            "name": "CS327",
            "type": "force"
        },
        {
            "name": "CS328",
            "type": "force"
        },
        {
            "name": "CS341",
            "type": "force"
        },
        {
            "name": "CS342",
            "type": "force"
        },
        {
            "name": "CS348",
            "type": "force"
        },
        {
            "name": "CS356",
            "type": "force"
        },
        {
            "name": "CS357",
            "type": "force"
        },
        {
            "name": "CS358",
            "type": "force"
        },
        {
            "name": "CS359",
            "type": "force"
        },
        {
            "name": "CS365",
            "type": "force"
        },
        {
            "name": "CS366",
            "type": "force"
        },
        {
            "name": "CS367",
            "type": "force"
        },
        {
            "name": "CS374",
            "type": "force"
        },
        {
            "name": "CS377",
            "type": "force"
        },
        {
            "name": "CS385",
            "type": "force"
        },
        {
            "name": "CS386",
            "type": "force"
        },
        {
            "name": "CS387",
            "type": "force"
        },
        {
            "name": "CS388",
            "type": "force"
        },
        {
            "name": "CS389",
            "type": "force"
        },
        {
            "name": "CS395",
            "type": "force"
        },
        {
            "name": "CS396",
            "type": "force"
        },
        {
            "name": "CS397",
            "type": "force"
        },
        {
            "name": "CS398",
            "type": "force"
        },
        {
            "name": "CS399",
            "type": "force"
        },
        {
            "name": "CS401",
            "type": "force"
        },
        {
            "name": "CS402",
            "type": "force"
        },
        {
            "name": "CS406",
            "type": "force"
        },
        {
            "name": "CS407",
            "type": "force"
        },
        {
            "name": "CS408",
            "type": "force"
        },
        {
            "name": "CS409",
            "type": "force"
        },
        {
            "name": "CS426",
            "type": "force"
        },
        {
            "name": "CS427",
            "type": "force"
        },
        {
            "name": "CS428",
            "type": "force"
        },
        {
            "name": "CS429",
            "type": "force"
        },
        {
            "name": "CS439",
            "type": "force"
        },
        {
            "name": "CS446",
            "type": "force"
        },
        {
            "name": "CS447",
            "type": "force"
        },
        {
            "name": "CS448",
            "type": "force"
        },
        {
            "name": "CS449",
            "type": "force"
        },
        {
            "name": "CS456",
            "type": "force"
        },
        {
            "name": "CS457",
            "type": "force"
        },
        {
            "name": "CS458",
            "type": "force"
        },
        {
            "name": "CS459",
            "type": "force"
        },
        {
            "name": "CS467",
            "type": "force"
        },
        {
            "name": "CS469",
            "type": "force"
        },
        {
            "name": "CS479",
            "type": "force"
        },
        {
            "name": "CS486",
            "type": "force"
        },
        {
            "name": "CS487",
            "type": "force"
        },
        {
            "name": "CS488",
            "type": "force"
        },
        {
            "name": "CS489",
            "type": "force"
        },
        {
            "name": "CS496",
            "type": "force"
        },
        {
            "name": "CS497",
            "type": "force"
        },
        {
            "name": "CS499",
            "type": "force"
        },
        {
            "name": "EC210",
            "type": "general"
        },
        {
            "name": "EL070",
            "type": "general"
        },
        {
            "name": "EL171",
            "type": "general"
        },
        {
            "name": "EL172",
            "type": "general"
        },
        {
            "name": "EL295",
            "type": "general"
        },
        {
            "name": "EL395",
            "type": "force"
        },
        {
            "name": "HO201",
            "type": "general"
        },
        {
            "name": "MA211",
            "type": "force"
        },
        {
            "name": "MA212",
            "type": "force"
        },
        {
            "name": "MA332",
            "type": "force"
        },
        {
            "name": "PY228",
            "type": "general"
        },
        {
            "name": "SC123",
            "type": "force"
        },
        {
            "name": "SC135",
            "type": "force"
        },
        {
            "name": "SC173",
            "type": "force"
        },
        {
            "name": "SC185",
            "type": "force"
        },
        {
            "name": "ST216",
            "type": "force"
        },
        {
            "name": "TH161",
            "type": "general"
        },
        {
            "name": "TU100",
            "type": "general"
        },
        {
            "name": "TU110",
            "type": "general"
        },
        {
            "name": "TU120",
            "type": "general"
        },
        {
            "name": "TU122",
            "type": "general"
        },
        {
            "name": "TU130",
            "type": "general"
        },
        {
            "name": "TU154",
            "type": "general"
        }
    ]
}
    

    return JsonResponse({'myfile1':myfile1})









def coordinate_predict(request):
    myfile = {
    "link": [
        {
            "source": 7,
            "target": 10,
            "type": "licensing"
        },
        {
            "source": 8,
            "target": 10,
            "type": "licensing"
        },
        {
            "source": 10,
            "target": 13,
            "type": "licensing"
        },
        {
            "source": 10,
            "target": 16,
            "type": "licensing"
        },
        {
            "source": 10,
            "target": 17,
            "type": "licensing"
        },
        {
            "source": 10,
            "target": 22,
            "type": "licensing"
        },
        {
            "source": 13,
            "target": 19,
            "type": "licensing"
        },
        {
            "source": 13,
            "target": 23,
            "type": "licensing"
        },
        {
            "source": 13,
            "target": 33,
            "type": "licensing"
        },
        {
            "source": 13,
            "target": 36,
            "type": "licensing"
        },
        {
            "source": 13,
            "target": 40,
            "type": "licensing"
        },
        {
            "source": 13,
            "target": 44,
            "type": "licensing"
        },
        {
            "source": 13,
            "target": 49,
            "type": "licensing"
        },
        {
            "source": 16,
            "target": 34,
            "type": "licensing"
        },
        {
            "source": 17,
            "target": 35,
            "type": "licensing"
        },
        {
            "source": 17,
            "target": 36,
            "type": "licensing"
        },
        {
            "source": 17,
            "target": 59,
            "type": "licensing"
        },
        {
            "source": 17,
            "target": 61,
            "type": "licensing"
        },
        {
            "source": 19,
            "target": 21,
            "type": "licensing"
        },
        {
            "source": 19,
            "target": 39,
            "type": "licensing"
        },
        {
            "source": 19,
            "target": 64,
            "type": "licensing"
        },
        {
            "source": 19,
            "target": 65,
            "type": "licensing"
        },
        {
            "source": 19,
            "target": 66,
            "type": "licensing"
        },
        {
            "source": 20,
            "target": 43,
            "type": "licensing"
        },
        {
            "source": 22,
            "target": 24,
            "type": "licensing"
        },
        {
            "source": 22,
            "target": 26,
            "type": "licensing"
        },
        {
            "source": 22,
            "target": 43,
            "type": "licensing"
        },
        {
            "source": 22,
            "target": 45,
            "type": "licensing"
        },
        {
            "source": 22,
            "target": 56,
            "type": "licensing"
        },
        {
            "source": 22,
            "target": 57,
            "type": "licensing"
        },
        {
            "source": 22,
            "target": 68,
            "type": "licensing"
        },
        {
            "source": 22,
            "target": 71,
            "type": "licensing"
        },
        {
            "source": 21,
            "target": 25,
            "type": "licensing"
        },
        {
            "source": 21,
            "target": 48,
            "type": "licensing"
        },
        {
            "source": 26,
            "target": 46,
            "type": "licensing"
        },
        {
            "source": 26,
            "target": 69,
            "type": "licensing"
        },
        {
            "source": 27,
            "target": 49,
            "type": "licensing"
        },
        {
            "source": 27,
            "target": 50,
            "type": "licensing"
        },
        {
            "source": 27,
            "target": 29,
            "type": "licensing"
        },
        {
            "source": 28,
            "target": 50,
            "type": "licensing"
        },
        {
            "source": 31,
            "target": 54,
            "type": "licensing"
        },
        {
            "source": 84,
            "target": 49,
            "type": "licensing"
        },
        {
            "source": 36,
            "target": 37,
            "type": "licensing"
        },
        {
            "source": 36,
            "target": 38,
            "type": "licensing"
        },
        {
            "source": 36,
            "target": 59,
            "type": "licensing"
        },
        {
            "source": 36,
            "target": 60,
            "type": "licensing"
        },
        {
            "source": 37,
            "target": 47,
            "type": "licensing"
        },
        {
            "source": 37,
            "target": 62,
            "type": "licensing"
        },
        {
            "source": 37,
            "target": 63,
            "type": "licensing"
        },
        {
            "source": 40,
            "target": 67,
            "type": "licensing"
        },
        {
            "source": 45,
            "target": 69,
            "type": "licensing"
        },
        {
            "source": 45,
            "target": 70,
            "type": "licensing"
        },
        {
            "source": 49,
            "target": 29,
            "type": "licensing"
        },
        {
            "source": 49,
            "target": 51,
            "type": "licensing"
        },
        {
            "source": 49,
            "target": 52,
            "type": "licensing"
        },
        {
            "source": 50,
            "target": 52,
            "type": "licensing"
        },
        {
            "source": 52,
            "target": 53,
            "type": "licensing"
        },
        {
            "source": 40,
            "target": 41,
            "type": "licensing"
        },
        {
            "source": 40,
            "target": 42,
            "type": "licensing"
        },
        {
            "source": 54,
            "target": 55,
            "type": "licensing"
        },
        {
            "source": 64,
            "target": 66,
            "type": "licensing"
        },
        {
            "source": 78,
            "target": 64,
            "type": "licensing"
        }
    ],
    "node": [
        {
            "name": "AT316",
            "type": "freedom"
        },
        {
            "name": "AT326",
            "type": "freedom"
        },
        {
            "name": "BA291",
            "type": "general"
        },
        {
            "name": "CJ315",
            "type": "freedom"
        },
        {
            "name": "CJ316",
            "type": "freedom"
        },
        {
            "name": "CJ317",
            "type": "freedom"
        },
        {
            "name": "CJ321",
            "type": "freedom"
        },
        {
            "name": "CS101",
            "type": "force"
        },
        {
            "name": "CS102",
            "type": "force"
        },
        {
            "name": "CS105",
            "type": "force"
        },
        {
            "name": "CS111",
            "type": "force"
        },
        {
            "name": "CS115",
            "type": "force"
        },
        {
            "name": "CS211",
            "type": "force"
        },
        {
            "name": "CS213",
            "type": "force"
        },
        {
            "name": "CS214",
            "type": "force"
        },
        {
            "name": "CS215",
            "type": "force"
        },
        {
            "name": "CS222",
            "type": "force"
        },
        {
            "name": "CS223",
            "type": "force"
        },
        {
            "name": "CS231",
            "type": "force"
        },
        {
            "name": "CS251",
            "type": "force"
        },
        {
            "name": "CS261",
            "type": "force"
        },
        {
            "name": "CS281",
            "type": "force"
        },
        {
            "name": "CS284",
            "type": "force"
        },
        {
            "name": "CS285",
            "type": "force"
        },
        {
            "name": "CS286",
            "type": "force"
        },
        {
            "name": "CS288",
            "type": "force"
        },
        {
            "name": "CS289",
            "type": "force"
        },
        {
            "name": "CS295",
            "type": "force"
        },
        {
            "name": "CS296",
            "type": "force"
        },
        {
            "name": "CS297",
            "type": "force"
        },
        {
            "name": "CS300",
            "type": "force"
        },
        {
            "name": "CS301",
            "type": "force"
        },
        {
            "name": "CS302",
            "type": "force"
        },
        {
            "name": "CS311",
            "type": "force"
        },
        {
            "name": "CS314",
            "type": "force"
        },
        {
            "name": "CS326",
            "type": "force"
        },
        {
            "name": "CS341",
            "type": "force"
        },
        {
            "name": "CS342",
            "type": "force"
        },
        {
            "name": "CS348",
            "type": "force"
        },
        {
            "name": "CS356",
            "type": "force"
        },
        {
            "name": "CS365",
            "type": "force"
        },
        {
            "name": "CS366",
            "type": "force"
        },
        {
            "name": "CS367",
            "type": "force"
        },
        {
            "name": "CS374",
            "type": "force"
        },
        {
            "name": "CS377",
            "type": "force"
        },
        {
            "name": "CS385",
            "type": "force"
        },
        {
            "name": "CS386",
            "type": "force"
        },
        {
            "name": "CS387",
            "type": "force"
        },
        {
            "name": "CS388",
            "type": "force"
        },
        {
            "name": "CS395",
            "type": "force"
        },
        {
            "name": "CS396",
            "type": "force"
        },
        {
            "name": "CS397",
            "type": "force"
        },
        {
            "name": "CS398",
            "type": "force"
        },
        {
            "name": "CS399",
            "type": "force"
        },
        {
            "name": "CS401",
            "type": "force"
        },
        {
            "name": "CS402",
            "type": "force"
        },
        {
            "name": "CS407",
            "type": "force"
        },
        {
            "name": "CS408",
            "type": "force"
        },
        {
            "name": "CS409",
            "type": "force"
        },
        {
            "name": "CS426",
            "type": "force"
        },
        {
            "name": "CS427",
            "type": "force"
        },
        {
            "name": "CS429",
            "type": "force"
        },
        {
            "name": "CS446",
            "type": "force"
        },
        {
            "name": "CS449",
            "type": "force"
        },
        {
            "name": "CS456",
            "type": "force"
        },
        {
            "name": "CS457",
            "type": "force"
        },
        {
            "name": "CS459",
            "type": "force"
        },
        {
            "name": "CS467",
            "type": "force"
        },
        {
            "name": "CS486",
            "type": "force"
        },
        {
            "name": "CS487",
            "type": "force"
        },
        {
            "name": "CS488",
            "type": "force"
        },
        {
            "name": "CS489",
            "type": "force"
        },
        {
            "name": "EL070",
            "type": "general"
        },
        {
            "name": "EL171",
            "type": "general"
        },
        {
            "name": "EL172",
            "type": "general"
        },
        {
            "name": "EL295",
            "type": "general"
        },
        {
            "name": "EL395",
            "type": "force"
        },
        {
            "name": "ES356",
            "type": "freedom"
        },
        {
            "name": "HO201",
            "type": "general"
        },
        {
            "name": "HR201",
            "type": "freedom"
        },
        {
            "name": "LA209",
            "type": "freedom"
        },
        {
            "name": "MA211",
            "type": "force"
        },
        {
            "name": "MA212",
            "type": "force"
        },
        {
            "name": "MA216",
            "type": "freedom"
        },
        {
            "name": "MA332",
            "type": "force"
        },
        {
            "name": "MW313",
            "type": "freedom"
        },
        {
            "name": "MW314",
            "type": "freedom"
        },
        {
            "name": "NS132",
            "type": "freedom"
        },
        {
            "name": "PY228",
            "type": "general"
        },
        {
            "name": "SC123",
            "type": "force"
        },
        {
            "name": "SC135",
            "type": "force"
        },
        {
            "name": "SC173",
            "type": "force"
        },
        {
            "name": "SC185",
            "type": "force"
        },
        {
            "name": "SO201",
            "type": "freedom"
        },
        {
            "name": "ST216",
            "type": "force"
        },
        {
            "name": "SW111",
            "type": "freedom"
        },
        {
            "name": "SW212",
            "type": "freedom"
        },
        {
            "name": "SW213",
            "type": "freedom"
        },
        {
            "name": "SW221",
            "type": "freedom"
        },
        {
            "name": "SW335",
            "type": "freedom"
        },
        {
            "name": "SW365",
            "type": "freedom"
        },
        {
            "name": "SW475",
            "type": "freedom"
        },
        {
            "name": "SW478",
            "type": "freedom"
        },
        {
            "name": "TA395",
            "type": "freedom"
        },
        {
            "name": "TH161",
            "type": "general"
        },
        {
            "name": "TU100",
            "type": "general"
        },
        {
            "name": "TU110",
            "type": "general"
        },
        {
            "name": "TU120",
            "type": "general"
        },
        {
            "name": "TU122",
            "type": "general"
        },
        {
            "name": "TU130",
            "type": "general"
        },
        {
            "name": "TU154",
            "type": "general"
        }
    ]
}

    return JsonResponse({'myfile':myfile})