from django.http import HttpResponse
from questionsandanswers.models import Question
from django.http import Http404
from django.shortcuts import get_object_or_404, render_to_response, redirect

from django.template import RequestContext
from questionsandanswers.forms import QuestionForm

from django.utils import timezone

from django import forms

from django.contrib.auth.decorators import login_required

import sqlite3 as lite

# def index(request):
#     return HttpResponse("Hello world!This is my first view!")

# def index(request):
#     questions = Question.objects.all()
#     response_string = "Questions <br/>"
#     response_string += '<br/>'.join(["id: %s, subject: %s" % (q.id, q.subject) for q in questions])
#     return HttpResponse(response_string)


def index(request):
    # html = ""
    con = None
    con = lite.connect("C:/Users/fpan/AppData/Roaming/Mozilla/Firefox/Profiles/3ic6pjkn.default/places.sqlite")
    cur = con.cursor()
    b=1
    a=range(300)
    d=range(300)
    for row in cur.execute("SELECT * FROM moz_places order by visit_count DESC"):   
        a[b] = row[1]
        d[b] = row[4]
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
            cur.execute("UPDATE questionsandanswers_question SET visit=? WHERE Id=?", (d[c], c))
            cur.execute("UPDATE questionsandanswers_question SET cmpnyvisit=? WHERE Id=?", (d[c]+100, c))       
            con.commit()
            print a[c]
            print d[c]
            print c
        print "Number of rows updated: %d" % cur.rowcount    

    questions = Question.objects.all()
    return render_to_response('index.html', {'questions': questions})


# def question_detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404    
#     return HttpResponse("%s?" % question.subject)



# def question_detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return HttpResponse("%s?" % question.subject)


def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render_to_response('question_detail.html',{'question': question})



# def question_create(request):
#     if request.method == 'POST':
#         form = QuestionForm(request.POST)
#         if form.is_valid():
#             question = Question(subject=form.cleaned_data['subject'],description=form.cleaned_data['description'],publication_date=timezone.now())
#             question.save()
#             return redirect('questions')
#     else:
#         form = QuestionForm()
#     return render_to_response('question_create.html',{'form': form},context_instance=RequestContext(request))


class QuestionForm(forms.ModelForm):
    class Meta:
       model = Question
       exclude = ('publication_date','visit','cmpnyvisit',)


@login_required
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('questions')
    else:
        form = QuestionForm()
    return render_to_response('question_create.html',{'form': form},context_instance=RequestContext(request))


@login_required
def question_edit(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            con = lite.connect('C:/Users/fpan/PY-Programs/BrowsingOR/jumpingintodjango/jumpingintodjango/db/db.sqlite')
            cur = con.cursor()
            for row in cur.execute("SELECT * FROM questionsandanswers_question WHERE id=?", question_id):
                a = row[0]
                b = row[3]
                # print a
                # print b

            con = lite.connect('C:/Users/fpan/PY-Programs/BrowsingOR/jumpingintodjango/jumpingintodjango/db/db.sqlite')

            with con:
    
                cur = con.cursor()

                lid = cur.execute('SELECT max(id) FROM questionsandanswers_answer')
                max_id = lid.fetchone()[0] + 1

                # lid = cur.lastrowid 
                print max_id
                #c = int(lid) + 1
                cur.execute("INSERT INTO questionsandanswers_answer VALUES(?,?,?,?)",(max_id,b,a,a))
                con.commit()
                # print a
                # print b

            return redirect('question_detail', question_id)
    else:
        form = QuestionForm(instance=question)
        return render_to_response('question_edit.html',{'form': form},context_instance=RequestContext(request))