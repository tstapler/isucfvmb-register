from swampdragon import route_handler
from swampdragon.route_handler import ModelPublisherRouter
from registration.serializers import StudentSerializer
from registration.models import Student

class StudentModelRouter(ModelRouter):
    serializer_class = StudentSerializer
    model = Student
    route_name = 'student'
