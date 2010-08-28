from django.shortcuts import render_to_response, get_object_or_404
from happydjango.book.models import Book

def get_login_info(req):
    if req.session.has_key('happydjango') and req.session['happydjango'] != '':
        return req.session['happydjango']
    else:
        return None

def welcome(request):
    return render_to_response('book/welcome.htm', {'login_info': get_login_info(request)})

def index(request):
    books = Book.objects.all()
    return render_to_response('book/index.htm', {'books' : books, 'login_info': get_login_info(request)})

def detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render_to_response('book/detail.htm', {'book': book, 'login_info': get_login_info(request)})