from django.shortcuts import render, redirect
from django.views import View
from .forms import StudentLoginForm, StudentRegistrationForm, FacultyRegistrationForm

class StudentLoginView(View):
    template_name = 'accounts/student_login.html'
    
    def get(self, request):
        form = StudentLoginForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            return redirect('dashboard')
        return render(request, self.template_name, {'form': form})

class RegisterView(View):
    template_name = 'accounts/register.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        account_type = request.POST.get('account_type')
        if account_type == 'student':
            return redirect('student_register')
        return redirect('faculty_register')

class StudentRegisterView(View):
    template_name = 'accounts/student_register.html'
    
    def get(self, request):
        form = StudentRegistrationForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            # Process registration data
            return redirect('student_login')
        return render(request, self.template_name, {'form': form})

class FacultyRegisterView(View):
    template_name = 'accounts/faculty_register.html'
    
    def get(self, request):
        form = FacultyRegistrationForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = FacultyRegistrationForm(request.POST)
        if form.is_valid():
            # Process registration data
            return redirect('faculty_login')
        return render(request, self.template_name, {'form': form})

class StudentDashboardView(View):
    template_name = 'accounts/dashboard/student_dashboard.html'
    
    def get(self, request):
        context = {
            'user_name': 'Student Name',  # We'll update this with actual user data later
            'notification_count': 2,
            'upcoming_exams': [
                {
                    'date': 'Dec 15',
                    'name': 'Math 181',
                    'room': '301',
                    'campus': 'Charleston Campus',
                    'time': '9:00 AM'
                },
                {
                    'date': 'Dec 18',
                    'name': 'English 101',
                    'room': '205',
                    'campus': 'Henderson Campus',
                    'time': '2:00 PM'
                }
            ]
        }
        return render(request, self.template_name, context)
    
class RegisterExamView(View):
    template_name = 'accounts/dashboard/register_exam.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        # Handle form submission
        course = request.POST.get('course')
        exam_type = request.POST.get('exam_type')
        campus = request.POST.get('campus')
        
        # Add logic for processing exam registration
        return render(request, self.template_name)


class ViewScheduleView(View):
    template_name = 'accounts/dashboard/view_schedule.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
class ProfileView(View):
    template_name = 'accounts/dashboard/profile.html'
    
    def get(self, request):
        return render(request, self.template_name)
        
    def post(self, request):
        # Handle profile updates here
        return render(request, self.template_name)
    
class NotificationsView(View):
    template_name = 'accounts/dashboard/notifications.html'
    
    def get(self, request):
        return render(request, self.template_name)

class SettingsView(View):
    template_name = 'accounts/dashboard/settings.html'
    
    def get(self, request):
        return render(request, self.template_name)

from django.contrib.auth import logout
from django.shortcuts import redirect

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('student_login')

class AdminDashboardView(View):
    template_name = 'accounts/dashboard/admin_dashboard.html'
    
    def get(self, request):
        return render(request, self.template_name)

class ManageStudentsView(View):
    template_name = 'accounts/dashboard/manage_students.html'
    
    def get(self, request):
        return render(request, self.template_name)

class AdminExamScheduleView(View):
    template_name = 'accounts/dashboard/admin_exam_schedule.html'
    
    def get(self, request):
        return render(request, self.template_name)

class CheckTimeSlotsView(View):
    def post(self, request):
        course = request.POST.get('course')
        exam_type = request.POST.get('exam_type')
        campus = request.POST.get('campus')
        
        # Sample time slots data
        time_slots = [
            {'time': '9:00 AM', 'room': '301', 'availability': '15/20'},
            {'time': '11:00 AM', 'room': '205', 'availability': '18/25'},
            {'time': '2:00 PM', 'room': '401', 'availability': '12/20'}
        ]
        
        return JsonResponse({'time_slots': time_slots})
