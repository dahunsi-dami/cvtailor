#!/usr/bin/env python3
"""Module to handle job application form submission."""
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import JobApplicationForm


def upload_view(request):
    """
    Handles file upload & job description submission using-
    -JobApplicationForm.

    If request method is POST, saves the uploaded file and-
    -job descriptioin to database. Then redirects to a-
    -success page/returns an error.

    Args:
        request: the HTTP request.

    Returns:
        HttpResponse: A response object with either a success message-
        -or an error.
    """
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("CV and description save success!")
    else:
        form = JobApplicationForm()

    return render(request, 'index.html', {'form': form})
