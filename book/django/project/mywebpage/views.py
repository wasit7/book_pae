from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.urlresolvers import reverse
from .models import Subject, Enrollment, Student
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.staticfiles.templatetags.staticfiles import static
import sys
import json
import pickle
# Create your views here.
#y = []
def home(request):
    if request.method == 'GET':
        if 'username' not in request.session:
            return render(request, 'pleaselogin.html')
        else:
            username = User.objects.get(username=request.session['username'])
            student = Student.objects.filter(username__username=username)
            if not student:
                return render(request,'userprofile.html')
            else:
                return render(request,'home.html')

def homegraph(request):
    if request.method == 'GET':
        if 'username' not in request.session:
            return render(request, 'pleaselogin.html')
        else:
            return render(request, 'homegraph.html')


def showprofile(request):
    if request.method == 'GET':
        if 'username' not in request.session:
            return render(request, 'pleaselogin.html')
        else:
            return render(request, 'showprofile.html')

def addprofile(request):
    if request.method == 'GET':
        if 'username' not in request.session:
            return render(request, 'pleaselogin.html')
        else:
            return render(request, 'addprofile.html')
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
                new_enroll = Enrollment.objects.create(std_id=fk_std_id, sub_id=fk_sub_id, grade=value['grade'], term=value['term'], year=value['year'])
                new_enroll.save()

        return HttpResponse("OK")

#[0,0,2,3,8,5,0,8,....]
def sortLabel(request):
    subject = Subject.objects.values('sub_id').order_by('sub_id')  #sort by subid
    sList = [ i for i in subject ]
    subjectList =[]
    for i in range(len(sList)):
        v = sList[i]
        obj = v['sub_id']
        subjectList.append(obj)
    #print subjectList #[u'AT316, u'AT326, .... , u'TU154'] 110

    std_id = str(Student.objects.get(username__username=request.session['username']).std_id)
    enroll = Enrollment.objects.filter(std_id__std_id = std_id).order_by('sub_id').values('sub_id','grade')
    #print >> sys.stderr, enroll      #type(enroll) 

    enList = [i for i in enroll]    #[{'sub_id':u'AT316', 'grade': u'B'}] 3
    enrollList = []
    for i in range(len(enList)):
        v = enList[i]
        obj = v['sub_id']
        enrollList.append(obj)
    #print >> sys.stderr,enrollList      #type(enList)   

    label = []
    for i,n in enumerate(subjectList):
        if n in enrollList:
            label.append(n)
        else:
            label.append(0)

    for i in enList:
        #print type(i)  #print i['sub_id']
        if i['sub_id'] in label:
            sub = i['sub_id']
            rep = i['grade']

        if rep == 'A':
            label[label.index(sub)] = 8
        elif rep == 'B+':
            label[label.index(sub)] = 7
        elif rep == 'B':
            label[label.index(sub)] = 7
        elif rep == 'C+':
            label[label.index(sub)] = 6
        elif rep == 'C':
            label[label.index(sub)] = 6
        elif rep == 'D+':
            label[label.index(sub)] = 5
        elif rep == 'D':
            label[label.index(sub)] = 5
        elif rep == 'F':
            label[label.index(sub)] = 4
        elif rep == 'W':
            label[label.index(sub)] = 3
        elif rep == 'S':
            label[label.index(sub)] = 2
        elif rep == 'S#':
            label[label.index(sub)] = 2
        elif rep == 'U':
            label[label.index(sub)] = 1
        elif rep == 'U#':
            label[label.index(sub)] = 1 

    classify(label)
    return HttpResponse("yyyyyyyyyyyyyyyyyyy")

def predict(request):
    if request.method == 'GET':
        if 'username' not in request.session:
            return render(request, 'pleaselogin.html')
        else:
            sortLabel(request)
            return render(request, 'predict.html')

def classify(X):
    #print X
    subject = Subject.objects.values('sub_id').order_by('sub_id')  #sort by subid
    sList = [ i for i in subject ]
    subjectList =[]
    for i in range(len(sList)):
        v = sList[i]
        obj = v['sub_id']
        subjectList.append(obj)

    y = []
    for i in range(0,110):
            if X[i] == 0:
                subject = subjectList[i]
                f = "tree/tree%s.pic"%subject
                with open(f, 'rb') as pickleFile:
                        clf2 = pickle.load(pickleFile)
                clf2.predict(X)
                Grade=['A', 'B', 'C' , 'D' , 'F' , 'W' , 'S' , 'U' ,'na']
                grade_predicted = Grade[::-1][clf2.predict(X)]
                #print "prediction of %s: "%subject,grade_predicted

                y.append(grade_predicted)
            elif X[i] != 0: 
                subject = subjectList[i]
                Grade=['A', 'B', 'C' , 'D' , 'F' , 'W' , 'S' , 'U' ,'na']
                grade_truth=Grade[::-1][X[i]]
                #print "grade %s has already is "%subject,grade_truth
                y.append(grade_truth)
        #print "list of all grade predicted is %s"%y 
    print y

    with open('coordinate_predict.json') as f:
        myfile = json.load(f)
        #jj type is dict
        all_subject = myfile['node']
        for i,k in enumerate(all_subject):
            subject = all_subject[i]
            subject['grade'] = y[i]
        #print myfile

    with open('j.json','w+') as f:
        json.dump(myfile, f)
        f.close()

    return HttpResponse("OK")

def userprofile(request):
    if request.method == 'GET':
        if 'username' not in request.session:
            return render(request, 'pleaselogin.html')
        else:
            return render(request, 'userprofile.html')

    if request.method == 'POST':
        userprofile = json.loads(request.body)

        for key,value in userprofile.iteritems():
            #print key
            username = str(User.objects.get(username=request.session['username']))
            #print username
            #update
            if Student.objects.filter(username__username=username).exists() :
                record = Student.objects.get(username__username=username)
                #print "record"
                record.firstname = value['firstname']
                record.lastname = value['lastname']
                record.std_id = record.std_id
                #record.std_id = value['std_id']
                record.email = value['email']
                #float .00
                record.sch_gpa = value['sch_gpa']
                record.admit_year = value['admit_year']
                record.province_id = value['province_id']
                record.save()

            #add
            elif Student.objects.filter(username__username=username).exists() is False:
                fk_username = User.objects.get(username=username)
                new_student = Student.objects.create(username=fk_username,firstname=value['firstname'],lastname=value['lastname'],std_id=value['std_id'],email=value['email'],sch_gpa=value['sch_gpa'],admit_year= value['admit_year'], province_id=value['province_id'])
                new_student.save()

        return render(request, 'userprofile.html')

def jsonProvience(request):
    subject = Subject.objects.all().order_by('sub_id')
    return HttpResponse(subject)

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

def coordinate_home(request):
    with open('coordinate_home.json') as f:
        myfile1 = json.load(f)
        #print myfile1

    return JsonResponse({'myfile1':myfile1})

def coordinate_predict(request):
    #y = ['B', 'B', 'W', 'B', 'B', 'B', 'A', 'C', 'C', 'D', 'D', 'W', 'D', 'D', 'B', 'C', 'C', 'D', 'C', 'C', 'W', 'D', 'C', 'B', 'D', 'D', 'F', 'W', 'C', 'S', 'B', 'D', 'D', 'F', 'B', 'C', 'C', 'B', 'A', 'C', 'W', 'C', 'D', 'C', 'C', 'C', 'C', 'C', 'F', 'C', 'B', 'C', 'B', 'B', 'C', 'B', 'B', 'B', 'B', 'C', 'A', 'C', 'B', 'W', 'B', 'B', 'B', 'C', 'D', 'B', 'C', 'S', 'D', 'D', 'C', 'C', 'B', 'B', 'B', 'B', 'F', 'W', 'W', 'D', 'B', 'B', 'A', 'C', 'W', 'B', 'B', 'C', 'C', 'D', 'B', 'C', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'C', 'B', 'D', 'B', 'D', 'C', 'C']
    # with open('coordinate_predict.json') as f:
    #     myfile = json.load(f)
    #     #jj type is dict
    #     all_subject = myfile['node']
    #     for i,k in enumerate(all_subject):
    #         subject = all_subject[i]
    #         subject['grade'] = y[i]
    #     #print myfile

    # with open('j.json','w+') as f:
    #     json.dump(myfile, f)
    #     f.close()

    with open('j.json') as f:
        myfile = json.load(f)
    #print myfile
    return JsonResponse({'myfile':myfile})
    # return HttpResponse("OKKKK")


def test(request):

    return render(request, 'test.html')

def testcoor(request):
    with open('test2.json') as f:
        myfile = json.load(f)
        print myfile
    return JsonResponse({'myfile':myfile})