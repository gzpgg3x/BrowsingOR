from django.http import HttpResponse
from questionsandanswers.models import Question
from django.http import Http404
from django.shortcuts import get_object_or_404, render_to_response, redirect

from django.template import RequestContext
from questionsandanswers.forms import QuestionForm

from django.utils import timezone

from django import forms

from django.contrib.auth.decorators import login_required

# def index(request):
#     return HttpResponse("Hello world!This is my first view!")

# def index(request):
#     questions = Question.objects.all()
#     response_string = "Questions <br/>"
#     response_string += '<br/>'.join(["id: %s, subject: %s" % (q.id, q.subject) for q in questions])
#     return HttpResponse(response_string)


def index(request):
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
       exclude = ('publication_date',)


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
            return redirect('question_detail', question_id)
    else:
        form = QuestionForm(instance=question)
        return render_to_response('question_edit.html',{'form': form},context_instance=RequestContext(request))
