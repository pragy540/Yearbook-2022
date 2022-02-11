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

@api_view (['POST'])
def register(request) :
    req_data = request.data
    iitborg = req_data['iitb_org']
    sso = req_data['email'].lower()
    email = sso+"@iitb.ac.in"
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
        request.session['otp'] = otp
        request.session['otp_email'] = email
        request.session.save()
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
        return Response({"status": "OTP sent successfully to your LDAP Id. It is `${otp}`"})
    
    submitted_otp = req_data['otp_field']
    if f"{request.session.get('otp',-1)}" == submitted_otp and request.session.get('otp_email',-1)==email:                    
        student, created = Student.objects.get_or_create(sso_id=sso)
        if created:
            student.first_name=req_data['first_name']
            student.last_name=req_data['last_name']
            student.save()
            request.session['user_id'] = student.sso_id
            request.session.save()
            print(student)
        return Response( { "status" : "registered"})


@api_view (['POST'])
def register1(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        sso = str(form.cleaned_data.get('email')).lower()
        email = sso + "@iitb.ac.in"
        iitborg = form.cleaned_data.get('iitborg',None)
        if iitborg is not None and iitborg != '':
            email_correct = True
            if Alum.objects.filter(sso_id = sso).exists():
                alum = Alum.objects.get(sso_id = sso)
                email_correct = False if ((alum.email).split('@')[0]).lower() != iitborg else email_correct
            email = str(iitborg).lower() + "@iitbombay.org" if email_correct else None
            if email is None:
                return("Need email")
                # return render(request, 'index.html',{'redirect':False, 'form': form, 'alert': f'Alum with this sso and iitbombay.org username does not exist'})
            
        if form.cleaned_data.get('otp_field','') == '' or form.cleaned_data.get('otp_field',None) is None:
            name = form.cleaned_data.get('first_name') + " " + form.cleaned_data.get('last_name')
            import random
            otp = random.randint(100000,1000000)
            request.session['otp'] = otp
            request.session['otp_email'] = email
            request.session.save()
            html_content = "<p> Otp for login is: <b>" + f"{otp}" + "</b></p>"
            response = send_mail(email,name,"OTP: YearBook 2021", html_content=html_content,  
                        sender_email="sarc@iitb.ac.in", sender_name="SARC", reply_name="SARC", reply_to="no-reply-sarc@iitb.ac.in")
            if response.status_code != 202:
                response_iitb_mail = send_sso_mail(email,name,"OTP: YearBook 2021", html_content=html_content,  
                        sender_email="sarc@iitb.ac.in", sender_name="SARC", reply_name="SARC", reply_to="no-reply-sarc@iitb.ac.in")
                # if len(response_iitb_mail.keys())!=0:
                    # return render(request, 'index.html',{'redirect':False, 'form': form, 'alert': 'OTP NOT SENT. Contact Dhairya Jain (9967876281)'})
            EmailNotifs.objects.create(
                email = email,
                otp = otp,
                first_name = form.cleaned_data.get('first_name'), 
                last_name = form.cleaned_data.get('last_name')
            )
            return Response({"status": "OTP sent successfully to your LDAP Id"})
                # return render(request, 'index.html',{'redirect':False, 'form': form, 'alert': f'OTP Sent Successfully to {email}'})
        else:
            submitted_otp = form.cleaned_data.get('otp_field')
            if f"{request.session.get('otp',-1)}" == submitted_otp and request.session.get('otp_email',-1)==email:                    
                req_data = request.data
                student, created = Student.objects.get_or_create(sso_id=req_data['sso_id'])
                    
                profile, profile_created = Student_Profile.objects.get_or_create(student = student, email=email)
                if created:
                    student.first_name=form.cleaned_data.get('first_name')
                    student.last_name=form.cleaned_data.get('last_name')
                    student.save()
                request.session['user_id'] = student.sso_id
                request.session.save()
    return Response( { "status" : "registered"})
                


def index(request):
    """
    The person always lands on this page after logging in,
    the view is divided into three panes,
    in the first pane, we have the person's photo, some details and various options to navigat through the site
    it is essentially our nav bar, similar to what we see on facebook
    the second pane is where a list of recommended friends will be displayed
    the third pane is where we will have the recent feed, encapsulating who most recently wrote what for someone else

    """
    # request.session['user_id'] = '193310023'
    # request.session.save()
    if request.method == 'GET':
        try:
            if request.session.get('user_id',"abc")!="abc":
                if request.GET.get('r'):
                    a=request.GET.get('r')
            else:
                raise Exception
        except:
        
            if request.GET.get('access_token'):
            
                access_token = request.GET.get('access_token')
                path = "https://gymkhana.iitb.ac.in/sso/user/api/user/?fields=first_name,last_name,type,insti_address,mobile,program,roll_number"
                http_request = urllib.Request(path)
                #gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
                http_request.add_header("Authorization", "Bearer "+access_token)
                result = urllib.urlopen(http_request)
                data = json.load(result)
                try:
                
                    logged_in_student = Student.objects.get(sso_id = data['roll_number'])
                    request.session['user_id'] = logged_in_student.sso_id
                except:
                
                    logged_in_student = Student(sso_id = data['roll_number'], first_name = data.get('first_name', '').title(), last_name = data.get('last_name', '').title())
                    logged_in_student.save()
                try:
                
                    profile = Student_Profile.objects.get(student = logged_in_student)
                    if profile.details_done:
                    
                        if request.GET.get('r'):
                            
                            a=request.GET.get('r')

                except:
                    
                    profile = Student_Profile(student = logged_in_student)
                    if data.get('program', None):
                        program = data['program']
                        if program.get('department_name', None):
                            profile.department = program['department_name']
                        if program.get('join_year', None):
                            profile.join_year = program['join_year']
                        if program.get('graduation_year', None):
                            profile.graduation_year = program['graduation_year']
                        if program.get('degree', None):
                            profile.degree = program['degree']
                    if data.get('insti_address', None):
                        address = data['insti_address']
                        if address.get('hostel', None):
                            profile.hostel = address['hostel']
                        if address.get('room', None):
                            profile.room_no = address['room']
                    if data.get('type', None):
                        profile.program = data['type']
                    profile.save()
                    request.session['user_id'] = logged_in_student.sso_id
                    print("E13")
                    if request.GET.get('r'):
                        print("E14")
                        a=request.GET.get('r')
        form = LoginForm(None)
        if request.GET.get('r'):
            
            redirect_uri = request.GET.get('r')
            return Response({'status': 'Person already created'})

            # return render(request,'index.html',{'redirect_uri':redirect_uri,'redirect':True,'form':form, 'alert': 'Welcome to YearBook21'})
        # else:
            
            # return render(request, 'index.html',{'redirect':False, 'form': form, 'alert': 'Welcome to YearBook21'})
    else:
        form = LoginForm(request.POST or None)
        if form.is_valid():
            sso = str(form.cleaned_data.get('email')).lower()
            email = sso + "@iitb.ac.in"
            iitborg = form.cleaned_data.get('iitborg',None)
            if iitborg is not None and iitborg != '':
                email_correct = True
                if Alum.objects.filter(sso_id = sso).exists():
                    alum = Alum.objects.get(sso_id = sso)
                    email_correct = False if ((alum.email).split('@')[0]).lower() != iitborg else email_correct
                email = str(iitborg).lower() + "@iitbombay.org" if email_correct else None
            # if email is None:
                # return render(request, 'index.html',{'redirect':False, 'form': form, 'alert': f'Alum with this sso and iitbombay.org username does not exist'})
            
            if form.cleaned_data.get('otp_field','') == '' or form.cleaned_data.get('otp_field',None) is None:
                name = form.cleaned_data.get('first_name') + " " + form.cleaned_data.get('last_name')
                import random
                otp = random.randint(100000,1000000)
                request.session['otp'] = otp
                request.session['otp_email'] = email
                request.session.save()
                html_content = "<p> Otp for login is: <b>" + f"{otp}" + "</b></p>"
                response = send_mail(email,name,"OTP: YearBook 2021", html_content=html_content,  
                            sender_email="sarc@iitb.ac.in", sender_name="SARC", reply_name="SARC", reply_to="no-reply-sarc@iitb.ac.in")
                if response.status_code != 202:
                    response_iitb_mail = send_sso_mail(email,name,"OTP: YearBook 2021", html_content=html_content,  
                            sender_email="sarc@iitb.ac.in", sender_name="SARC", reply_name="SARC", reply_to="no-reply-sarc@iitb.ac.in")
                    # if len(response_iitb_mail.keys())!=0:
                        # return render(request, 'index.html',{'redirect':False, 'form': form, 'alert': 'OTP NOT SENT. Contact Dhairya Jain (9967876281)'})
                EmailNotifs.objects.create(
                    email = email,
                    otp = otp,
                    first_name = form.cleaned_data.get('first_name'), 
                    last_name = form.cleaned_data.get('last_name')
                )
                
                # return render(request, 'index.html',{'redirect':False, 'form': form, 'alert': f'OTP Sent Successfully to {email}'})
            else:
                submitted_otp = form.cleaned_data.get('otp_field')
                if f"{request.session.get('otp',-1)}" == submitted_otp and request.session.get('otp_email',-1)==email:                    
                    student, created = Student.objects.get_or_create(sso_id=sso)
                    
                    profile, profile_created = Student_Profile.objects.get_or_create(student = student, email=email)
                    if created:
                        student.first_name=form.cleaned_data.get('first_name')
                        student.last_name=form.cleaned_data.get('last_name')
                        student.save()
                    request.session['user_id'] = student.sso_id
                    request.session.save()

                    # return redirect('home')
                # else:
                    # return render(request, 'index.html',{'redirect':False, 'form': form, 'alert': 'Wrong OTP for this roll no'})
