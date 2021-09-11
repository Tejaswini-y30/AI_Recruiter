from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import Info,markslist
from .resumematch import match
from .sentiement import analysis
import json
import random
from .chatbot import rate
import sqlite3
from sqlite3 import Error

# Create your views here.

name='none'
email='none'
commentrate='none'
ans0='none'
ans1='none'
ans2='none'
total=0
resumerate=0.0
commentrate=0.0
avgtotal=0.0
def index(request):
    return render(request,'index.html')

def studentform(request):
    return render(request,'form.html') 

def adminlogin(request):
    return render(request,'adminlogin.html') 

def form_submitted(request):
    global name
    global email
    global resumerate
    global commentrate
    fname= request.POST.get("fname")
    lname= request.POST.get("lname")
    name = fname+ ' ' +lname
    email= request.POST.get("email")
    number= request.POST.get("number")
    position=request.POST.get("position")
    status=request.POST.get("status")
    gender=request.POST.get("gender")
    jobtype=request.POST.get("jobtype")
    comment=request.POST.get("comment")
    sdate=request.POST.get("sdate")
    matchper=match()
    resumerate=matchper
    commentrate=analysis(comment)
    print(fname)
    print(lname)
    print(email)
    print(number)
    print(position)
    print(status)
    print(gender)
    print(jobtype)
    print(comment)
    print(sdate)
    print(matchper)
    print(commentrate)

    info= Info(fname=fname,lname=lname,email=email,number=number,position=position,gender=gender,jobtype=jobtype,sdate=sdate)
    info.save()
    return render(request,'bot.html',{'name':name})

def msg(request):
    global ans0
    global total
    a= request.POST.get("ans0")
    ans0=a
    print(a)
    marks=rate(ans0)
    total=total+marks
    print(marks)
    return render(request,'b1.html',{'name':name,'ans0':ans0})


def msg1(request):
    global ans0
    global ans1
    global total
    a1= request.POST.get("ans1")
    ans1=a1
    print(a1)
    marks=rate(ans1)
    total=total+marks
    print(marks)
    return render(request,'b2.html',{'name':name,'ans0':ans0, 'ans1':ans1})

def msg2(request):
    global ans0
    global ans1
    global ans2
    global total
    global resumerate
    global commentrate
    global avgtotal
    ans2= request.POST.get("ans2")
    print(ans2)
    marks=rate(ans2)
    total=(total+marks)/3
    print(total)
    avgtotal=(commentrate+resumerate+total)/3
    print(avgtotal)
    m=markslist(name=name,commentrate=commentrate,resumematchper=resumerate,botscore=total,avg=avgtotal)
    m.save()
    return render(request, 'b3.html', {'name':name ,'ans0':ans0, 'ans1':ans1, 'ans2':ans2})


def admin(request):
    conn=create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM myapp_markslist")

    mark = cur.fetchall()
    print(mark)
    return render(request,'admin.html', {"mark":mark})


def create_connection():
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    
    database = r"D:/xp/Xperimentsproject/airecruiter/db.sqlite3"

    # create a database connection
    conn = sqlite3.connect(database)

    return conn
def success(request):
    return render(request,'success.html')

