from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Subject, Enrollment, Student
import json
# Create your views here.

def homep(request):
    return render(request,'homep.html')

def showprofile(request):
    return render(request,'showprofile.html')

def addprofile(request):
    subjectData = Subject.objects.all()
    enrollmentData = Enrollment.objects.all()
    grade = ['A', 'B', 'B+','C', 'C+', 'D', 'D+', 'F', 'W', 'S', 'S#','U','U#']
    return render(request,'addprofile.html',{'subjectData':subjectData, 'enrollmentData':enrollmentData, 'grade':grade})

    if request.method == 'GET':
        return render(request,'addprofile.html')
    if request.method == 'POST':
        ObjEnrolled = json.loads(request.body)  #jsEnrolled is python Object or python dictionary
        
        for key,value in ObjEnrolled.iteritems():
            std_id = str(Student.objects.get(username__username=request.session['username']).std_id)

            #update
            if Enrollment.objects.filter(std_id__std_id = std_id ,sub_id__sub_id=key ).exists():
                record = Enrollment.objects.get(std_id__std_id=std_id, sub_id__sub_id=key ) 
                record.grade = value['grade']
                record.term = value['term']
                record.year = value['year']
                record.save()
                #print >> sys.stderr, type(value['year'])
        return HttpResponse("OK")

def editprofile(request):
    return render(request,'editprofile.html')

def predict(request):
    return render(request, 'predict.html')

def jsonSubject(request):
    subjectID = Subject.objects.all()

    subjectIDdata = { i.sub_id : {'sub_name' : i.sub_name} for i in subjectID } 
    return JsonResponse(subjectIDdata)

"""def jsonEnrollment(request):
    subjectIDdata = Enrollment.objects.all()
    #subjectIDdata = { 'subjectID': [i for i in subjectID ]} 
    return JsonResponse({'subjectIDdata':subjectIDdata})"""

def jsonEnrollment(request):
    std_id = str(Student.objects.get(username__username=request.session['username']).std_id)
    enrollmentID = Enrollment.objects.filter(std_id=std_id)
    #enrollmentID = Enrollment.objects.filter(std_id__username__username=request.session['username'])
    enrollmentData = { i.sub_id.sub_id : { 'sub_id': i.sub_id.sub_id,'term': str(i.term), 'year': str(i.year) , 'grade': i.grade} for i in enrollmentID  }
    #enrollmentData['std_id'] = std_id
    return JsonResponse(enrollmentData)

def test(request):
    return render(request,'test.html')


def coordinate(request):
    myfile = {
    "link": [
        {
            "source": 19,
            "target": 22,
            "type": "licensing"
        },
        {
            "source": 20,
            "target": 22,
            "type": "licensing"
        },
        {
            "source": 22,
            "target": 25,
            "type": "licensing"
        },
        {
            "source": 22,
            "target": 28,
            "type": "licensing"
        },
        {
            "source": 22,
            "target": 29,
            "type": "licensing"
        },
        {
            "source": 22,
            "target": 35,
            "type": "licensing"
        },
        {
            "source": 25,
            "target": 31,
            "type": "licensing"
        },
        {
            "source": 25,
            "target": 36,
            "type": "licensing"
        },
        {
            "source": 25,
            "target": 46,
            "type": "licensing"
        },
        {
            "source": 25,
            "target": 50,
            "type": "licensing"
        },
        {
            "source": 25,
            "target": 55,
            "type": "licensing"
        },
        {
            "source": 25,
            "target": 59,
            "type": "licensing"
        },
        {
            "source": 25,
            "target": 64,
            "type": "licensing"
        },
        {
            "source": 28,
            "target": 47,
            "type": "licensing"
        },
        {
            "source": 29,
            "target": 48,
            "type": "licensing"
        },
        {
            "source": 29,
            "target": 50,
            "type": "licensing"
        },
        {
            "source": 29,
            "target": 74,
            "type": "licensing"
        },
        {
            "source": 29,
            "target": 76,
            "type": "licensing"
        },
        {
            "source": 31,
            "target": 34,
            "type": "licensing"
        },
        {
            "source": 31,
            "target": 53,
            "type": "licensing"
        },
        {
            "source": 31,
            "target": 54,
            "type": "licensing"
        },
        {
            "source": 31,
            "target": 80,
            "type": "licensing"
        },
        {
            "source": 31,
            "target": 81,
            "type": "licensing"
        },
        {
            "source": 31,
            "target": 82,
            "type": "licensing"
        },
        {
            "source": 32,
            "target": 58,
            "type": "licensing"
        },
        {
            "source": 35,
            "target": 37,
            "type": "licensing"
        },
        {
            "source": 35,
            "target": 39,
            "type": "licensing"
        },
        {
            "source": 35,
            "target": 58,
            "type": "licensing"
        },
        {
            "source": 35,
            "target": 60,
            "type": "licensing"
        },
        {
            "source": 35,
            "target": 71,
            "type": "licensing"
        },
        {
            "source": 35,
            "target": 72,
            "type": "licensing"
        },
        {
            "source": 35,
            "target": 86,
            "type": "licensing"
        },
        {
            "source": 35,
            "target": 89,
            "type": "licensing"
        },
        {
            "source": 34,
            "target": 38,
            "type": "licensing"
        },
        {
            "source": 34,
            "target": 63,
            "type": "licensing"
        },
        {
            "source": 39,
            "target": 61,
            "type": "licensing"
        },
        {
            "source": 39,
            "target": 87,
            "type": "licensing"
        },
        {
            "source": 40,
            "target": 64,
            "type": "licensing"
        },
        {
            "source": 40,
            "target": 65,
            "type": "licensing"
        },
        {
            "source": 40,
            "target": 42,
            "type": "licensing"
        },
        {
            "source": 41,
            "target": 65,
            "type": "licensing"
        },
        {
            "source": 44,
            "target": 69,
            "type": "licensing"
        },
        {
            "source": 47,
            "target": 49,
            "type": "licensing"
        },
        {
            "source": 130,
            "target": 64,
            "type": "licensing"
        },
        {
            "source": 50,
            "target": 51,
            "type": "licensing"
        },
        {
            "source": 50,
            "target": 52,
            "type": "licensing"
        },
        {
            "source": 50,
            "target": 74,
            "type": "licensing"
        },
        {
            "source": 50,
            "target": 75,
            "type": "licensing"
        },
        {
            "source": 50,
            "target": 78,
            "type": "licensing"
        },
        {
            "source": 51,
            "target": 62,
            "type": "licensing"
        },
        {
            "source": 51,
            "target": 77,
            "type": "licensing"
        },
        {
            "source": 51,
            "target": 79,
            "type": "licensing"
        },
        {
            "source": 55,
            "target": 83,
            "type": "licensing"
        },
        {
            "source": 55,
            "target": 84,
            "type": "licensing"
        },
        {
            "source": 58,
            "target": 85,
            "type": "licensing"
        },
        {
            "source": 59,
            "target": 85,
            "type": "licensing"
        },
        {
            "source": 60,
            "target": 87,
            "type": "licensing"
        },
        {
            "source": 60,
            "target": 88,
            "type": "licensing"
        },
        {
            "source": 64,
            "target": 42,
            "type": "licensing"
        },
        {
            "source": 64,
            "target": 66,
            "type": "licensing"
        },
        {
            "source": 64,
            "target": 67,
            "type": "licensing"
        },
        {
            "source": 65,
            "target": 67,
            "type": "licensing"
        },
        {
            "source": 66,
            "target": 90,
            "type": "licensing"
        },
        {
            "source": 67,
            "target": 68,
            "type": "licensing"
        },
        {
            "source": 67,
            "target": 91,
            "type": "licensing"
        },
        {
            "source": 55,
            "target": 56,
            "type": "licensing"
        },
        {
            "source": 55,
            "target": 57,
            "type": "licensing"
        },
        {
            "source": 69,
            "target": 70,
            "type": "licensing"
        },
        {
            "source": 80,
            "target": 82,
            "type": "licensing"
        },
        {
            "source": 111,
            "target": 80,
            "type": "licensing"
        },
        {
            "source": 28,
            "target": 203,
            "type": "licensing"
        },
        {
            "source": 29,
            "target": 204,
            "type": "licensing"
        },
        {
            "source": 35,
            "target": 205,
            "type": "licensing"
        },
        {
            "source": 38,
            "target": 206,
            "type": "licensing"
        },
        {
            "source": 50,
            "target": 207,
            "type": "licensing"
        },
        {
            "source": 52,
            "target": 208,
            "type": "licensing"
        },
        {
            "source": 53,
            "target": 209,
            "type": "licensing"
        },
        {
            "source": 11,
            "target": 209,
            "type": "licensing"
        },
        {
            "source": 67,
            "target": 210,
            "type": "licensing"
        },
        {
            "source": 90,
            "target": 210,
            "type": "licensing"
        },
        {
            "source": 53,
            "target": 211,
            "type": "licensing"
        },
        {
            "source": 53,
            "target": 212,
            "type": "licensing"
        },
    ],
    "node": [
        {
            "name": "AN201",
            "type": "freedom"
        },
        {
            "name": "AS171",
            "type": "freedom"
        },
        {
            "name": "AS177",
            "type": "freedom"
        },
        {
            "name": "AS178",
            "type": "freedom"
        },
        {
            "name": "AT207",
            "type": "freedom"
        },
        {
            "name": "AT307",
            "type": "freedom"
        },
        {
            "name": "AT316",
            "type": "freedom"
        },
        {
            "name": "AT326",
            "type": "freedom"
        },
        {
            "name": "AT336",
            "type": "freedom"
        },
        {
            "name": "AT346",
            "type": "freedom"
        },
        {
            "name": "AT366",
            "type": "freedom"
        },
        {
            "name": "BA291",
            "type": "general"
        },
        {
            "name": "CF366",
            "type": "freedom"
        },
        {
            "name": "CF367",
            "type": "freedom"
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
            "name": "CN342",
            "type": "freedom"
        },
        {
            "name": "CS101",
            "type": "comsci"
        },
        {
            "name": "CS102",
            "type": "comsci"
        },
        {
            "name": "CS105",
            "type": "comsci"
        },
        {
            "name": "CS111",
            "type": "comsci"
        },
        {
            "name": "CS115",
            "type": "comsci"
        },
        {
            "name": "CS211",
            "type": "comsci"
        },
        {
            "name": "CS213",
            "type": "comsci"
        },
        {
            "name": "CS214",
            "type": "comsci"
        },
        {
            "name": "CS215",
            "type": "comsci"
        },
        {
            "name": "CS222",
            "type": "comsci"
        },
        {
            "name": "CS223",
            "type": "comsci"
        },
        {
            "name": "CS231",
            "type": "comsci"
        },
        {
            "name": "CS251",
            "type": "comsci"
        },
        {
            "name": "CS261",
            "type": "comsci"
        },
        {
            "name": "CS275",
            "type": "comsci"
        },
        {
            "name": "CS281",
            "type": "comsci"
        },
        {
            "name": "CS284",
            "type": "comsci"
        },
        {
            "name": "CS285",
            "type": "comsci"
        },
        {
            "name": "CS286",
            "type": "comsci"
        },
        {
            "name": "CS288",
            "type": "comsci"
        },
        {
            "name": "CS289",
            "type": "comsci"
        },
        {
            "name": "CS295",
            "type": "comsci"
        },
        {
            "name": "CS296",
            "type": "comsci"
        },
        {
            "name": "CS297",
            "type": "comsci"
        },
        {
            "name": "CS300",
            "type": "comsci"
        },
        {
            "name": "CS301",
            "type": "comsci"
        },
        {
            "name": "CS302",
            "type": "comsci"
        },
        {
            "name": "CS311",
            "type": "comsci"
        },
        {
            "name": "CS314",
            "type": "comsci"
        },
        {
            "name": "CS326",
            "type": "comsci"
        },
        {
            "name": "CS328",
            "type": "comsci"
        },
        {
            "name": "CS341",
            "type": "comsci"
        },
        {
            "name": "CS342",
            "type": "comsci"
        },
        {
            "name": "CS348",
            "type": "comsci"
        },
        {
            "name": "CS356",
            "type": "comsci"
        },
        {
            "name": "CS359",
            "type": "comsci"
        },
        {
            "name": "CS365",
            "type": "comsci"
        },
        {
            "name": "CS366",
            "type": "comsci"
        },
        {
            "name": "CS367",
            "type": "comsci"
        },
        {
            "name": "CS374",
            "type": "comsci"
        },
        {
            "name": "CS377",
            "type": "comsci"
        },
        {
            "name": "CS385",
            "type": "comsci"
        },
        {
            "name": "CS386",
            "type": "comsci"
        },
        {
            "name": "CS387",
            "type": "comsci"
        },
        {
            "name": "CS388",
            "type": "comsci"
        },
        {
            "name": "CS395",
            "type": "comsci"
        },
        {
            "name": "CS396",
            "type": "comsci"
        },
        {
            "name": "CS397",
            "type": "comsci"
        },
        {
            "name": "CS398",
            "type": "comsci"
        },
        {
            "name": "CS399",
            "type": "comsci"
        },
        {
            "name": "CS401",
            "type": "comsci"
        },
        {
            "name": "CS402",
            "type": "comsci"
        },
        {
            "name": "CS407",
            "type": "comsci"
        },
        {
            "name": "CS408",
            "type": "comsci"
        },
        {
            "name": "CS409",
            "type": "comsci"
        },
        {
            "name": "CS426",
            "type": "comsci"
        },
        {
            "name": "CS427",
            "type": "comsci"
        },
        {
            "name": "CS429",
            "type": "comsci"
        },
        {
            "name": "CS446",
            "type": "comsci"
        },
        {
            "name": "CS447",
            "type": "comsci"
        },
        {
            "name": "CS449",
            "type": "comsci"
        },
        {
            "name": "CS456",
            "type": "comsci"
        },
        {
            "name": "CS457",
            "type": "comsci"
        },
        {
            "name": "CS459",
            "type": "comsci"
        },
        {
            "name": "CS467",
            "type": "comsci"
        },
        {
            "name": "CS469",
            "type": "comsci"
        },
        {
            "name": "CS479",
            "type": "comsci"
        },
        {
            "name": "CS486",
            "type": "comsci"
        },
        {
            "name": "CS487",
            "type": "comsci"
        },
        {
            "name": "CS488",
            "type": "comsci"
        },
        {
            "name": "CS489",
            "type": "comsci"
        },
        {
            "name": "CS496",
            "type": "comsci"
        },
        {
            "name": "CS499",
            "type": "comsci"
        },
        {
            "name": "DM201",
            "type": "freedom"
        },
        {
            "name": "DM207",
            "type": "freedom"
        },
        {
            "name": "DM215",
            "type": "freedom"
        },
        {
            "name": "EC210",
            "type": "general"
        },
        {
            "name": "EG241",
            "type": "freedom"
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
            "name": "EL202",
            "type": "freedom"
        },
        {
            "name": "EL231",
            "type": "freedom"
        },
        {
            "name": "EL295",
            "type": "general"
        },
        {
            "name": "EL395",
            "type": "general"
        },
        {
            "name": "ES256",
            "type": "freedom"
        },
        {
            "name": "ES356",
            "type": "freedom"
        },
        {
            "name": "ES456",
            "type": "freedom"
        },
        {
            "name": "FD211",
            "type": "freedom"
        },
        {
            "name": "FN211",
            "type": "freedom"
        },
        {
            "name": "GE225",
            "type": "freedom"
        },
        {
            "name": "GE311",
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
            "name": "HS266",
            "type": "freedom"
        },
        {
            "name": "HS269",
            "type": "freedom"
        },
        {
            "name": "HS356",
            "type": "freedom"
        },
        {
            "name": "HS360",
            "type": "freedom"
        },
        {
            "name": "IS201",
            "type": "freedom"
        },
        {
            "name": "JC200",
            "type": "freedom"
        },
        {
            "name": "JC201",
            "type": "freedom"
        },
        {
            "name": "JC260",
            "type": "freedom"
        },
        {
            "name": "JC281",
            "type": "freedom"
        },
        {
            "name": "JP171",
            "type": "freedom"
        },
        {
            "name": "JP172",
            "type": "freedom"
        },
        {
            "name": "LA209",
            "type": "freedom"
        },
        {
            "name": "MA211",
            "type": "general"
        },
        {
            "name": "MA212",
            "type": "general"
        },
        {
            "name": "MA216",
            "type": "freedom"
        },
        {
            "name": "MA217",
            "type": "freedom"
        },
        {
            "name": "MA221",
            "type": "freedom"
        },
        {
            "name": "MA332",
            "type": "freedom"
        },
        {
            "name": "MU100",
            "type": "freedom"
        },
        {
            "name": "MU130",
            "type": "freedom"
        },
        {
            "name": "MU135",
            "type": "freedom"
        },
        {
            "name": "MU165",
            "type": "freedom"
        },
        {
            "name": "MU202",
            "type": "freedom"
        },
        {
            "name": "MU275",
            "type": "freedom"
        },
        {
            "name": "MU277",
            "type": "freedom"
        },
        {
            "name": "MU278",
            "type": "freedom"
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
            "name": "MW318",
            "type": "freedom"
        },
        {
            "name": "NS112",
            "type": "freedom"
        },
        {
            "name": "NS132",
            "type": "freedom"
        },
        {
            "name": "PC286",
            "type": "freedom"
        },
        {
            "name": "PE240",
            "type": "freedom"
        },
        {
            "name": "PE245",
            "type": "freedom"
        },
        {
            "name": "PM215",
            "type": "freedom"
        },
        {
            "name": "PM235",
            "type": "freedom"
        },
        {
            "name": "PM236",
            "type": "freedom"
        },
        {
            "name": "PY211",
            "type": "freedom"
        },
        {
            "name": "PY217",
            "type": "freedom"
        },
        {
            "name": "PY218",
            "type": "freedom"
        },
        {
            "name": "PY226",
            "type": "freedom"
        },
        {
            "name": "PY228",
            "type": "general"
        },
        {
            "name": "PY237",
            "type": "freedom"
        },
        {
            "name": "PY267",
            "type": "freedom"
        },
        {
            "name": "RE333",
            "type": "freedom"
        },
        {
            "name": "RT326",
            "type": "freedom"
        },
        {
            "name": "SC123",
            "type": "freedom"
        },
        {
            "name": "SC135",
            "type": "general"
        },
        {
            "name": "SC173",
            "type": "freedom"
        },
        {
            "name": "SC185",
            "type": "general"
        },
        {
            "name": "SN212",
            "type": "freedom"
        },
        {
            "name": "SO201",
            "type": "freedom"
        },
        {
            "name": "ST216",
            "type": "general"
        },
        {
            "name": "ST217",
            "type": "freedom"
        },
        {
            "name": "ST218",
            "type": "freedom"
        },
        {
            "name": "ST326",
            "type": "freedom"
        },
        {
            "name": "SW111",
            "type": "freedom"
        },
        {
            "name": "SW201",
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
            "name": "SW214",
            "type": "freedom"
        },
        {
            "name": "SW221",
            "type": "freedom"
        },
        {
            "name": "SW222",
            "type": "freedom"
        },
        {
            "name": "SW223",
            "type": "freedom"
        },
        {
            "name": "SW224",
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
            "name": "SW366",
            "type": "freedom"
        },
        {
            "name": "SW467",
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
            "name": "SW486",
            "type": "freedom"
        },
        {
            "name": "SW489",
            "type": "freedom"
        },
        {
            "name": "SW496",
            "type": "freedom"
        },
        {
            "name": "TA395",
            "type": "freedom"
        },
        {
            "name": "TD436",
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
            "name": "TU111",
            "type": "freedom"
        },
        {
            "name": "TU113",
            "type": "freedom"
        },
        {
            "name": "TU115",
            "type": "freedom"
        },
        {
            "name": "TU116",
            "type": "freedom"
        },
        {
            "name": "TU120",
            "type": "general"
        },
        {
            "name": "TU121",
            "type": "freedom"
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
            "name": "TU153",
            "type": "freedom"
        },
        {
            "name": "TU154",
            "type": "general"
        },
        {
            "name": "TU156",
            "type": "freedom"
        },
        {
            "name": "CS439",
            "type": "comsci"
        },
        {
            "name": "CS327",
            "type": "comsci"
        },
        {
            "name": "CS406",
            "type": "comsci"
        },
        {
            "name": "CS389",
            "type": "comsci"
        },
        {
            "name": "CS428",
            "type": "comsci"
        },
        {
            "name": "CS448",
            "type": "comsci"
        },
        {
            "name": "CS458",
            "type": "comsci"
        },
        {
            "name": "CS497",
            "type": "comsci"
        },
        {
            "name": "CS357",
            "type": "comsci"
        },
        {
            "name": "CS358",
            "type": "comsci"
        },
    ]
}
    

    return JsonResponse({'myfile':myfile})