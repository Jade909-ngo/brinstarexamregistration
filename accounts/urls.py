from django.urls import path
from .views import (
    StudentLoginView, 
    RegisterView, 
    StudentRegisterView, 
    FacultyRegisterView,
    StudentDashboardView,
    RegisterExamView,
    ViewScheduleView,
    ProfileView,
    NotificationsView,
    SettingsView,
    LogoutView,
    AdminDashboardView,
    ManageStudentsView,
    AdminExamScheduleView,
    CheckTimeSlotsView,
)

urlpatterns = [
    path('', StudentLoginView.as_view(), name='student_login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register/student/', StudentRegisterView.as_view(), name='student_register'),
    path('register/faculty/', FacultyRegisterView.as_view(), name='faculty_register'),
    path('dashboard/', StudentDashboardView.as_view(), name='dashboard'),
    path('register-exam/', RegisterExamView.as_view(), name='register_exam'),
    path('view-schedule/', ViewScheduleView.as_view(), name='view_schedule'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('notifications/', NotificationsView.as_view(), name='notifications'),
    path('settings/', SettingsView.as_view(), name='settings'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('admin-dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('manage-students/', ManageStudentsView.as_view(), name='manage_students'),
    path('admin-exam-schedule/', AdminExamScheduleView.as_view(), name='admin_exam_schedule'),
    path('check-time-slots/', CheckTimeSlotsView.as_view(), name='check_time_slots'),

]

