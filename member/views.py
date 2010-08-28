from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from happydjango.member.models import Member, MemberForm
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect

def get_login_info(req):
    if req.session.has_key('happydjango') and req.session['happydjango'] != '':
        return req.session['happydjango']
    else:
        return None
    
def index(request):
    return render_to_response('member/index.htm', {'login_info': get_login_info(request)})

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register/finish')
    else:
        form = MemberForm()
        
    return render_to_response('member/register.htm',{'form': form, 'login_info': get_login_info(request)}, context_instance=RequestContext(request))

def login(request):
    if request.POST:
        login_id = request.POST['login_id']
        login_pw = request.POST['login_pw']
        member = Member.objects.filter(login_id = login_id, login_pw = login_pw)
        if member:
            request.session['happydjango'] = login_id
            return HttpResponseRedirect('/')
        else:
            return render_to_response('member/login.htm', {'result': 'login fail'}, context_instance=RequestContext(request))

    return render_to_response('member/login.htm', context_instance=RequestContext(request))
    
def logout(request):
    try:
        del request.session['happydjango']
    except KeyError:
        pass
    return HttpResponseRedirect('/')