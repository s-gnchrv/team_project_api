from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from myapp import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    path('organizations/', views.OrganizationList.as_view()),
    path('organizations/<int:pk>/', views.OrganizationDetail.as_view()),
    path('violation-types/', views.ViolationTypeList.as_view()),
    path("violations/", views.ViolationList.as_view()),
    path("violations/<int:pk>/", views.ViolationDetail.as_view()),
    path('tasks/', views.TaskList.as_view()),
    path('tasks/<int:pk>/', views.TaskDetail.as_view()),
    path('tasks/<int:task>/comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
    path('attachments/', views.AttachmentList.as_view()),
    path('attachments/<int:pk>/', views.AttachmentDetail.as_view()),
    path("users/", views.UserList.as_view()),
    path("users/<int:pk>/", views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
