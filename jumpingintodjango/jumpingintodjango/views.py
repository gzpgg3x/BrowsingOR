from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from jumpingintodjango.forms import LoginForm
from django.contrib.auth import authenticate, login, logout

import sqlite3 as lite
from questionsandanswers.models import Question

def homepage(request):

    con = None
    con = lite.connect("C:/Users/fpan/AppData/Roaming/Mozilla/Firefox/Profiles/3ic6pjkn.default/places.sqlite")
    cur = con.cursor()
    b=1
    a=range(20)
    for row in cur.execute("SELECT * FROM moz_places order by visit_count DESC"):   
        a[b] = row[1]
        # html = html + "          "+ str(b) + a[b]
        b=b+1
    # print html

    # cur = lite.connect("C:/Users/fpan/PY-Programs/BrowsingOR/jumpingintodjango/jumpingintodjango/db/db.sqlite")
    # cur.execute("update questionsandanswers.question set subject = "" where id IN b", ('new', a))

    con = lite.connect('C:/Users/fpan/PY-Programs/BrowsingOR/jumpingintodjango/jumpingintodjango/db/db.sqlite')

    with con:
        for c in range(b):
            cur = con.cursor()

            cur.execute("UPDATE questionsandanswers_question SET subject=? WHERE Id=?", (a[c], c))        
            con.commit()
            print a[c]
            print c
        print "Number of rows updated: %d" % cur.rowcount    

    questions = Question.objects.all()
    # return render_to_response('homepage.html',context_instance=RequestContext(request))
    return render_to_response('homepage.html', {'questions': questions})

def login_page(request):
    message = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    message = "You logged in with success"
                else:
                    message = "Your user is inactive"
            else:
                    message = "Invalid username and/or password"
    else:
            form = LoginForm()
    return render_to_response('login.html', {'message': message,'form': form},context_instance=RequestContext(request))


def logout_view(request):
    logout(request)
    return redirect('homepage')

