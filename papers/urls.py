
from django.urls import path
from .import views

urlpatterns = [
    path('', views.Blank, name='Blank'),
    path('index/', views.Index, name='Index'),
    path('home/', views.Home, name='Home'),

    path('paperName/<selectedSubject>/<sem>', views.GetPaperName, name='GetPaperName'),

    path('qtnPaper', views.QtnPaper, name='QtnPaper'),
    path('qtnPaperWithSubject/<subject>/<paper>', views.QtnPaperWithSubject, name='QtnPaperWithSubject'),



    ######## admin section #########

    path('adminLogin', views.AdminLogin, name='AdminLogin'),
    path('adminDashBoard', views.AdminDashBoard, name='AdminDashBoard'),
    path('allSubject', views.AllSubject, name='AllSubject'),
    path('allPaper', views.AllPaper, name='AllPaper'),
    path('allQtnPaper', views.AllQtnPaper, name='AllQtnPaper'),
    path('adminRegistration', views.AdminRegistration, name='AdminRegistration'),

    path('addSubject', views.AddSubject, name='AddSubject'),
    path('editSubject', views.EditSubject, name='EditSubject'),
    path('deleteSubject/<int:id>', views.DeleteSubject, name='DeleteSubject'),

    path('addPaper', views.AddPaper, name='AddPaper'),
    path('editpaper', views.EditPaper, name='EditPaper'),
    path('deletePaper/<int:id>', views.DeletePaper, name='DeletePaper'),

    # path('addQtnPaper', views.AddQtnPaper, name='AddQtnPaper'),
    path('addQtnPaperDetails', views.QtnPaperDetails, name='QtnPaperDetails'),
    path('editQtnPaperDetails', views.editQtnPaperDetails, name='editQtnPaperDetails'),
    path('deleteQtnPaper/<int:id>', views.DeleteQtnPaper, name='DeleteQtnPaper'),
    
]