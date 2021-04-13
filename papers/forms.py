from django import forms
from .models import Subjects, Papers, QuestionPaper


class AddSubjectForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = ['subjectName', 'streamName']
        labels = {
            'subjectName': 'Subject',
            'streamName': 'Stream',
        }
        widgets = {
            'subjectName': forms.TextInput(attrs={'id': 'subjectName',  'class':'shadow-none'}),
            'streamName': forms.TextInput(attrs={'id': 'stream',  'class':'shadow-none'}),
        }



class AddPaperForm(forms.ModelForm):
    class Meta:
        model = Papers
        fields = ['paperName', 'subjectName', 'semesterName']
        labels = {
            'paperName': 'Paper',
            'subjectName': 'Subject',
            'semesterName': 'Semester'
        }
        widgets = {
            'paperName': forms.TextInput(attrs={'id': 'paperName', 'class':'shadow-none'}),
            'subjectName': forms.TextInput(attrs={'id': 'subjectName', 'class':'shadow-none'}),
            'semesterName': forms.TextInput(attrs={'id': 'semesterName', 'class':'shadow-none'}),
        }



# class AddQtnPaperForm(forms.ModelForm):
#     class Meta:
#         model = QuestionPaper
#         fields = ['qtnFile', 'subjectName', 'paperName', 'courseName', 'yearOfQuestions']
#         labels = {
#             'qtnFile': 'Upload File',
#             'subjectName': 'Subject',
#             'paperName': 'Paper',
#             'courseName': 'Course',
#             'yearOfQuestions': 'Year',
#         }
#         widgets = {
#             'qtnFile': forms.FileInput(attrs={'id':'file', 'name': 'file', 'class': 'fileUpload'}),
#             'subjectName': forms.TextInput(attrs={'id': 'subjectName', 'class': 'subjectName'}),
#             'paperName': forms.TextInput(attrs={'id': 'paperName'}),
#             'courseName': forms.TextInput(attrs={'id': 'courseName'}),
#             'yearOfQuestions': forms.TextInput(attrs={'id': 'yearOfQuestions'}),            
#         }