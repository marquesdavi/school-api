from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from escola.models import Student, Course, Registration
from .serializer import (
    StudentSerializer,
    CourseSerializer,
    RegistrationSerializer,
    ListStudentRegistrationsSerializer,
    ListCourseRegistrationsSerializer,
    StudentSerializerV2
)
    
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class StudentsViewSet(viewsets.ModelViewSet):
    """Show all the Students"""

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [ BasicAuthentication ]
    permission_classes = [ IsAuthenticated ]

    def get_serializer_class(self):
        if 'application/json;version=v2' in self.request.headers.get('Accept', ''):
            return StudentSerializerV2
        else:
            return StudentSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    """Show all the Courses"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [ BasicAuthentication ]
    permission_classes = [ IsAuthenticated ]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        response = Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        id = str(serializer.data['id'])
        response['Location'] = request.build_absolute_uri() + id
        return response


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