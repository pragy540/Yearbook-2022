from .models import *

def login_allowed(backend, user, response, *args, **kwargs):
    if not response['hd']=='iitb.ac.in':
        raise

def login_complete(backend, uid, user=None, *args, **kwargs):
    """
    3rd party: python-social-auth.

    Social auth pipeline to cleanup the user's data.  Must be placed
    after 'social_core.pipeline.user.create_user'.
    """
    # Check if the user object exists and a new account was just created.
    # if user and kwargs.get('is_new', False):
    details = kwargs['details']
    student, created = Student.objects.get_or_create(sso_id=details['email'].split("@")[0])
    if created:
        student.first_name = details['first_name']
        student.last_name = details['last_name']
        student.save()
    profile, created = Student_Profile.objects.get_or_create(student=student)
    if created:
        profile.email = details['email']
        profile.save()
    kwargs['request'].session['user_id'] = student.sso_id
    _session = kwargs['request'].session
    _session['user_id'] = student.sso_id
    _session.save()
    return {'user': user}

def index(request):
    """
    The person always lands on this page after logging in,
    the view is divided into three panes,
    in the first pane, we have the person's photo, some details and various options to navigat through the site
    it is essentially our nav bar, similar to what we see on facebook
    the second pane is where a list of recommended friends will be displayed
    the third pane is where we will have the recent feed, encapsulating who most recently wrote what for someone else

    """
    if request.method == 'GET':
        try:
            if request.session.get('user_id',"abc")!="abc":
                if request.GET.get('r'):
                    a=request.GET.get('r')
                    return redirect('/'+a+'/')
                return redirect('home')
            else:
                raise Exception
        except:
        
            if request.GET.get('access_token'):
            
                access_token = request.GET.get('access_token')
                path = "https://gymkhana.iitb.ac.in/sso/user/api/user/?fields=first_name,last_name,type,insti_address,mobile,program,roll_number"
                http_request = urllib2.Request(path)
                #gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
                http_request.add_header("Authorization", "Bearer "+access_token)
                result = urllib2.urlopen(http_request)
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
                            return redirect('/'+a+'/')
                        return redirect('home')
                    else:
                        
                        return redirect('edit-profile')
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
                        return redirect('/edit/?r='+a)
                    return redirect('edit-profile')
        if request.GET.get('r'):
            
            redirect_uri = request.GET.get('r')
            return render(request,'index.html',{'redirect_uri':redirect_uri,'redirect':True})
        else:
            
            return render(request, 'index.html',{'redirect':False})
