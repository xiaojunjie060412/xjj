from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Problem, Answer
from django.views.generic import View
# Create your views here.


class ListViews(View):

    def get(self, req):
        problems = Problem.objects.all()
        return render(req, 'vote/list.html', locals())


class DetailViews(View):

    def get(self, req, id):
        problem = Problem.objects.get(pk=id)
        return render(req, 'vote/detail.html', locals())

    def post(self, req, id):
        a_id = req.POST.get('res')
        a = Answer.objects.get(pk=a_id)
        a.count += 1
        a.save()
        return redirect(reverse('vote:result', args=(id,)))


class ResultViews(View):

    def get(self, req, id):
        problem = Problem.objects.get(pk=id)
        return render(req, 'vote/result.html', locals())