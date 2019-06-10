from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Problem, Answer
# Create your views here.


def list(req):
    problems = Problem.objects.all()
    return render(req, 'vote/list.html', {'problems': problems})


def detail(req, id):
    problem = Problem.objects.get(pk=id)
    if req.method == 'GET':
        return render(req, 'vote/detail.html', {'problem': problem})
    elif req.method == "POST":
        answer = Answer.objects.get(choice=req.POST.get('res'), relation=problem.id)
        # if req.POST.get('res') == problem.choice1:
        #     answer = Answer.objects.get(choice=problem.choice1)
        #     answer.count += 1
        #     answer.save()
        # elif req.POST.get('res') == problem.choice2:
        #     answer = Answer.objects.get(choice=problem.choice2)
        #     answer.count += 1
        #     answer.save()
        answer.count += 1
        answer.save()
        answer = problem.answer_set.all()
        return render(req, 'vote/result.html', {'problem': problem, "answer": answer})


def result(req, id):
    problem = Problem.objects.get(pk=id)
    answer = problem.answer_set.all()
    return render(req, 'vote/result.html', {'problem': problem, "answer": answer})