from rest_framework import viewsets, generics
from escola.models import Student, Course, Registration
from .serializer import \
    StudentSerializer,\
    CourseSerializer,\
    RegistrationSerializer,\
    ListStudentRegistrationsSerializer,\
    ListCourseRegistrationsSerializer\
    
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class StudentsViewSet(viewsets.ModelViewSet):
    """Show all the Students"""

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [ BasicAuthentication ]
    permission_classes = [ IsAuthenticated ]


class CoursesViewSet(viewsets.ModelViewSet):
    """Show all the Courses"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [ BasicAuthentication ]
    permission_classes = [ IsAuthenticated ]


class RegistrationsViewSet(viewsets.ModelViewSet):
    """Show the registrations"""

    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    authentication_classes = [ BasicAuthentication ]
    permission_classes = [ IsAuthenticated ]


class ListStudentRegistrations(generics.ListAPIView):
    """List of the students registrations"""

    def get_queryset(self):
        queryset = Registration.objects.filter(
            student_id = self.kwargs['pk']
        )
        return queryset
    serializer_class = ListStudentRegistrationsSerializer
    authentication_classes = [ BasicAuthentication ]
    permission_classes = [ IsAuthenticated ]


class ListCourseRegistrations(generics.ListAPIView):
    """List all the students registered on a course"""

    def get_queryset(self):
        queryset = Registration.objects.filter(
            course_id = self.kwargs['pk']
        )
        return queryset
    serializer_class = ListCourseRegistrationsSerializer
    authentication_classes = [ BasicAuthentication ]
    permission_classes = [ IsAuthenticated ]