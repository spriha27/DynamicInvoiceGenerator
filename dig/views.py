from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# from django.core import mail
# from django.template.loader import render_to_string
# from django.utils.html import strip_tags

from dig.models import Document, File
from dig.forms import DocumentForm, FileForm

def home(request):
    documents = Document.objects.all()
    return render(request, 'home.html', { 'documents': documents })

def file_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        if myfile.name.endswith('.html'):
            fileObj = Document(document = myfile);
            fileObj.save()
        elif myfile.name.endswith('.csv'):
            fileObj = File(file=myfile)
            fileObj.save()
        
    allObj = Document.objects.all()
    print(allObj)
    # fs = FileSystemStorage()
    # filename = fs.save(myfile.name, myfile)
    # uploaded_file_url = fs.url(filename)
    return render(request, 'file_upload.html', {
        'documents': allObj
    })

def continue_to_data(request):
	return render(request, 'uploaded_files.html')

# def send_mail(request):
# 	subject = 'Subject'
# 	html_message = render_to_string('mail_template.html', {'context': 'values'})
# 	plain_message = strip_tags(html_message)
# 	from_email = 'From <from@example.com>'
# 	to = 'to@example.com'

# 	mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)