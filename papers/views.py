from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from .models import Subjects, Papers, QuestionPaper, Semester

from django.core.files.storage import FileSystemStorage
# from textblob import TextBlob
from django.contrib import messages

from .forms import AddSubjectForm, AddPaperForm  # AddQtnPaperForm
# Create your views here.


def Blank(request):
    return redirect('index/')


def Index(request):
    return render(request, 'papers/commonView/index.html')


def Home(request):
    context = dict()

    subject = Subjects.objects.values('subjectName')
    semester = Semester.objects.all()

    context['subjectName'] = subject
    context['sem'] = semester
    # print(context)
    return render(request, 'papers/commonView/home.html', context)


def GetPaperName(request, selectedSubject='', sem=''):
    paperName = Papers.objects.filter(
        subjectName=selectedSubject, semesterName=sem).values('paperName')

    if(len(paperName) > 0):
        msg = {
            'result': list(paperName),
            'status': 'success',
        }
    else:
        msg = {
            'msg': 'No Papers Found',
            'status': 'failed',
        }

    return JsonResponse(msg)


def QtnPaper(request):

    if request.method == 'POST':
        subjectName = request.POST['subject_name']
        paper = request.POST['paper']

        print(subjectName, paper)

        # pap = paper.replace(" ", "")
        return redirect('/qtnPaperWithSubject/'+subjectName+'/'+paper)

    return redirect('/home')


def QtnPaperWithSubject(request, subject='', paper=''):
    context = dict()

    # print(subject, paper)

    qtns = QuestionPaper.objects.filter(
        subjectName=subject, paperName=paper)

    print(qtns)

    if len(qtns) > 0:

        context['qtnPapers'] = qtns

        return render(request, 'papers/commonView/questionPapersView.html', context)
    
    messages.success(request,"No Records Found")
    return redirect('/home')



############# admin section ################


def AdminLogin(request):
    return render(request, 'papers/adminView/adminLogin.html')


def AdminDashBoard(request):

    context = dict()

    totalSubjects = Subjects.objects.values('subjectName')
    lastThreeSubjects = Subjects.objects.values().order_by('-id')[:3]

    totalPapers = Papers.objects.values('paperName')
    lastThreePapers = Papers.objects.values().order_by('-id')[:3]

    totalQtnPapers = QuestionPaper.objects.values('questionPaperName')
    lastThreeQtnPapers = QuestionPaper.objects.values().order_by('-id')[:3]

    totalSem = Semester.objects.values('semesterName')
    lastThreeSem = Semester.objects.values().order_by('-id')[:3]

    context['totalSubjects'] = len(totalSubjects)
    context['totalPapers'] = len(totalPapers)
    context['totalQtnPapers'] = len(totalQtnPapers)
    context['totalsem'] = len(totalSem)

    context['lastThreeSubject'] = lastThreeSubjects
    context['lastThreePaper'] = lastThreePapers
    context['lastThreeQtnPaper'] = lastThreeQtnPapers
    context['lastThreeSem'] = lastThreeSem

    # print(lastThreeSubjects)

    return render(request, 'papers/adminView/adminDashBoard.html', context)


def AllSubject(request):
    context = dict()

    allSubjectDetails = Subjects.objects.all()

    form = AddSubjectForm()
    context = {'form': form}
    context['allSubjectDetails'] = allSubjectDetails

    return render(request, 'papers/adminView/subjectArea/allSubjects.html', context)


def AllPaper(request):
    context = dict()

    allPaperDetails = Papers.objects.all()

    form = AddPaperForm()
    context = {'form': form}

    context['allPaperDetails'] = allPaperDetails

    # print(context)

    return render(request, 'papers/adminView/paperArea/allPapers.html', context)


def AllQtnPaper(request):
    context = dict()

    allQtnPaperDetails = QuestionPaper.objects.all()

    # form = AddQtnPaperForm()
    # context = {'form': form}

    context['allQtnPaperDetails'] = allQtnPaperDetails

    # print(context)

    return render(request, 'papers/adminView/qtnPaperArea/allQtnPapers.html', context)


#    start subject section   #

def AddSubject(request):

    if request.method == 'POST':
        subjectName = request.POST['subjectName'].title()
        streamName = request.POST['streamName'].title()

        # spell correction

        # checkSubjectSpell = TextBlob(subjectName)
        # correctSubjectName = checkSubjectSpell.correct()

        # checkSteamSpell = TextBlob(streamName)
        # correctSteamName = checkSteamSpell.correct()

        # print(correctSubjectName, correctSteamName)

        # end

        print(subjectName, streamName)

        subject = Subjects.objects.create(
            subjectName=subjectName, streamName=streamName)

        msg = {
            'id': subject.id,
            'status': 'success'
        }

        return JsonResponse(msg)

    return JsonResponse({'status': 'faield'})


def EditSubject(request):

    if request.method == 'POST':

        id = request.POST['id']
        subject_name = request.POST['subjectName'].title()
        stream_name = request.POST['streamName'].title()

        # spell correction

        # checkSubjectSpell = TextBlob(subject_name)
        # correctSubjectName = checkSubjectSpell.correct()

        # checkSteamSpell = TextBlob(stream_name)
        # correctSteamName = checkSteamSpell.correct()

        # print(correctSubjectName, correctSteamName)

        # end

        print(id, subject_name, stream_name)

        updated_subject = Subjects.objects.filter(
            pk=id).update(subjectName=subject_name, streamName=stream_name)

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'faield'})


def DeleteSubject(request, id=0):

    pi = Subjects.objects.get(pk=id)
    print(pi)
    pi.delete()

    return JsonResponse({'status': 'success'})

#      end subject section         #

#      start paper section         #


def AddPaper(request):
    if request.method == 'POST':
        subjectName = request.POST['subjectName'].title()
        paperName = request.POST['paperName'].title()
        semName = request.POST['semName'].title()

        # spell correction

        # checkSubjectSpell = TextBlob(subjectName)
        # correctSubjectName = checkSubjectSpell.correct()

        # checkPaperSpell = TextBlob(paperName)
        # correctPaperName = checkPaperSpell.correct()

        # checkSemSpell = TextBlob(semName)
        # correctSemName = checkSemSpell.correct()

        # print(correctSubjectName, correctPaperName, correctSemName)

        # end

        print(subjectName, paperName, semName)

        paper = Papers.objects.create(
            paperName=paperName, subjectName=subjectName, semesterName=semName)

        msg = {
            'id': paper.id,
            'status': 'success'
        }

        return JsonResponse(msg)

    return JsonResponse({'status': 'faield'})


def EditPaper(request):

    if request.method == 'POST':

        id = request.POST['id']
        subject_name = request.POST['subjectName'].title()
        paperName = request.POST['paperName'].title()
        semName = request.POST['semester'].title()

        # spell correction

        # checkSubjectSpell = TextBlob(subject_name)
        # correctSubjectName = checkSubjectSpell.correct()

        # checkPaperSpell = TextBlob(paperName)
        # correctPaperName = checkPaperSpell.correct()

        # checkSemSpell = TextBlob(semName)
        # correctSemName = checkSemSpell.correct()

        # print(correctSubjectName, correctPaperName, correctSemName)

        # end

        print(id, subject_name, paperName, semName)

        updated_paper = Papers.objects.filter(
            pk=id).update(subjectName=subject_name, paperName=paperName, semesterName=semName)

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'faield'})


def DeletePaper(request, id=0):
    print(id)

    pi = Papers.objects.get(pk=id)
    pi.delete()

    return JsonResponse({'status': 'success'})

#     end paper section     #

#     start Qtnpaper section     #


def QtnPaperDetails(request):
    context = dict()

    if request.method == 'POST':
        qtnFile = request.FILES['qtnPaper']
        subject = request.POST['subject'].title()
        paper = request.POST['paper'].title()
        course = request.POST['courseName'].title()
        year = request.POST['year']

        print(qtnFile, subject, paper, course, year)

        id = QuestionPaper.objects.create(questionPaperName=qtnFile, subjectName=subject, paperName=paper,
                                          courseName=course, yearOfQuestions=year)

        print(id)
    #     return JsonResponse ({'status':'success'})

        context['qtn'] = id

    return redirect('/allQtnPaper', context)

    # return JsonResponse ({'status':'falied'})


def editQtnPaperDetails(request):

    if request.method == 'POST':

        id = request.POST['qtn_id']
        subject = request.POST['edit_subject'].title()
        paper = request.POST['edit_paper'].title()
        course = request.POST['edit_courseName'].title()
        year = request.POST['edit_year']

        print(id, subject, paper, course, year)

        id = QuestionPaper.objects.filter(pk=id).update(subjectName=subject, paperName=paper,
                                                        courseName=course, yearOfQuestions=year)

    return redirect('/allQtnPaper')


def DeleteQtnPaper(request, id=0):
    print(id)

    if request.method == 'POST':
        qtn = QuestionPaper.objects.get(pk=id)
        print(qtn)
        qtn.delete()
    return redirect('/allQtnPaper')

#     end Qtnpaper section     #


def AdminRegistration(request):
    return render(request, 'papers/adminView/adminRegistration.html')
