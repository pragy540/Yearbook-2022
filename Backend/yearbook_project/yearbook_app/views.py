from operator import getitem
from django.shortcuts import render
from werkzeug import Response
from django.db import models
from . import serializers 
from rest_framework import viewsets  
from rest_framework.decorators import api_view    
from rest_framework.response import Response
from . import models    
from .forms import *
from .options import *     
import urllib, base64, json, ssl
from django.views.decorators.csrf import ensure_csrf_cookie

# class ProfileView(viewsets.ModelViewSet):  
#     # serializer_class = ProfileSerializer 
#     # queryset = Profile.objects.all()     

# @api_view(['GET'])    
# def profile_disp(request):
#     data = models.Profile.objects.all()
#     data_serializer = serializers.ProfileSerializer(data, many=True)
#     return Response(data_serializer.data)

# @api_view(['POST'])
# def add_person(request):
#     req_data = request.data
#     person, created = models.Profile.objects.get_or_create(rollno = req_data['rollno'])
#     if created:
#         person.name = req_data['name']
#         person.save()
#         person_serializer = serializers.ProfileSerializer(person)
#         return Response(person_serializer.data)
#     else:
#         return Response({'status': 'Person already created'})
@ensure_csrf_cookie
@api_view (['POST'])
def register(request) :
    req_data = request.data
    iitborg = req_data['iitb_org']
    sso = req_data['email'].lower()
    email = sso+"@iitb.ac.in"
    # print(email)
    if iitborg is not None and iitborg != '':
        email_correct = True
        if Alum.objects.filter(sso_id = sso).exists():
            alum = Alum.objects.get(sso_id = sso)
            email_correct = False if ((alum.email).split('@')[0]).lower() != iitborg else email_correct
        email = str(iitborg).lower() + "@iitbombay.org" if email_correct else None
    if req_data['otp_field'] == '' or req_data['otp_field'] is None:
        name = req_data['first_name'] + req_data['last_name']
        import random
        otp = random.randint(100000,999999)
        print("The otp is ", otp)
        if Student.objects.filter(sso_id = sso).exists():
            print("User exists")
        else:
            print("User does not exist")
        request.session['sso_id'] = sso
        request.session['otp'] = otp
        request.session['otp_email'] = email
        request.session.save()
        print(request.session.get('otp'))
        return Response({"status": "OTP sent successfully to your LDAP Id. It is `${otp}`"})

        html_content = "<p> Otp for login is: <b>" + f"{otp}" + "</b></p>"
        # response = send_mail(email,name,"OTP: YearBook 2021", html_content=html_content,  
        #             sender_email="sarc@iitb.ac.in", sender_name="SARC", reply_name="SARC", reply_to="no-reply-sarc@iitb.ac.in")
        # if response.status_code != 202:
        #     response_iitb_mail = send_sso_mail(email,name,"OTP: YearBook 2021", html_content=html_content,  
        #             sender_email="sarc@iitb.ac.in", sender_name="SARC", reply_name="SARC", reply_to="no-reply-sarc@iitb.ac.in")
        #     if len(response_iitb_mail.keys())!=0:
        #         return({'status': 'OTP not sent, Contact SARC'})
        #             # return render(request, 'index.html',{'redirect':False, 'form': form, 'alert': 'OTP NOT SENT. Contact Dhairya Jain (9967876281)'})
        # EmailNotifs.objects.create(
        #     email = email,
        #     otp = otp,
        #     first_name = req_data['first_name'],
        #     last_name = req_data['last_name']
        #     )
    
    submitted_otp = req_data['otp_field']
    print(submitted_otp)
    # print(int(submitted_otp)==150000)
    print(request.session.get('otp_email'))
    # print(request.session.get('otp_email',-1)==email)
    if (f"{request.session.get('otp',-1)}" == submitted_otp) or request.session.get('otp_email',-1)==email or 1: 
        print("Correct")                   
        student, created = Student.objects.get_or_create(sso_id=sso)
        if created:
            student.first_name=req_data['first_name']
            student.last_name=req_data['last_name']
            student.save()
            request.session['user_id'] = student.sso_id
            request.session.save()
            print(student)
            return Response( { "status" : "registered"})
        return Response({'status': 'already exists'})
    return Response({'status': 'otp entered is incorrect'})

@api_view(['GET'])
def profile(request):
    # req_data = request.session\
    print(request.session['user_id'])
    student = Student.objects.get(sso_id = request.session['user_id'])
    data_serializer = serializers.StudentSerializer(student)
    return Response(data_serializer.data)