from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import csv

# from django.core import mail
# from django.template.loader import render_to_string
# from django.utils.html import strip_tags

from dig.models import Document, File
from dig.forms import DocumentForm, FileForm

def home(request):
    documents = Document.objects.all()
    return render(request, 'dig/templates/home.html', { 'documents': documents })

def file_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        if myfile.name.endswith('.html'):
            fileObj = Document(document = myfile)
            fileObj.save()
        elif myfile.name.endswith('.csv'):
            fileObj = File(file=myfile)
            fileObj.save()
    allDocObj = Document.objects.all()
    allCsvObj = File.objects.all()
    return render(request, 'dig/templates/file_upload.html', {
        'documents': allDocObj,'csvs': allCsvObj
    })

def continue_to_data(request):
	return render(request, 'dig/templates/uploaded_files.html')

def renderTemp(request):
    if request.method == "POST":
        html = request.POST["html"]
        csvId = request.POST["csv"]
        htmlObj = Document.objects.get(id=html)
        csvDataSource = File.objects.get(id=csvId)
        f = csvDataSource.file
        with f.open(mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            data = {}
            for row in csv_reader:
                data = row
            print(htmlObj.document.name)
    return render(request,"media/"+htmlObj.document.name,data)
# def send_mail(request):
# 	subject = 'Subject'
# 	html_message = render_to_string('mail_template.html', {'context': 'values'})
# 	plain_message = strip_tags(html_message)
# 	from_email = 'From <from@example.com>'
# 	to = 'to@example.com'

# 	mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)