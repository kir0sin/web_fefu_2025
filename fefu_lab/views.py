from django.http import Http404, HttpResponseServerError
from django.shortcuts import render, get_object_or_404
import logging

logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'fefu_lab/index.html')


def about(request):
    return render(request, 'fefu_lab/about.html')


def student_detail(request):
    return render(request, 'fefu_lab/student_detail.html')


def course_detail(request):
    return render(request, 'fefu_lab/course_detail.html')


def page_not_found_view(request, exception):
    return render(request, 'fefu_lab/404.html', status=404)
