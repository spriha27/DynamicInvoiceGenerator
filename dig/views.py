from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from dig.models import Document, File
from dig.forms import DocumentForm, FileForm

def home(request):
    documents = Document.objects.all()
    return render(request, 'home.html', { 'documents': documents })

def file_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'file_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'file_upload.html')

def uploaded_files():
	return render(request, 'uploaded_files.html')

