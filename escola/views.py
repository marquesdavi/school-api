from rest_framework import viewsets
from escola.models import Student, Course
from .serializer import StudentSerializer, CourseSerializer


class StudentsViewSet(viewsets.ModelViewSet):
    """Show all the Students"""

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CoursesViewSet(viewsets.ModelViewSet):
    """Show all the Courses"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

