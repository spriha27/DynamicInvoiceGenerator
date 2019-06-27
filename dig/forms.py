from django import forms

from dig.models import Document, File

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ( 'document', )

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ( 'file', )