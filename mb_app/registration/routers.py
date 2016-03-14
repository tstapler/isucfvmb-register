from swampdragon import route_handler
from swampdragon.route_handler import ModelRouter
from registration.serializers import StudentSerializer
from registration.models import Student

class StudentModelRouter(ModelRouter):
    serializer_class = StudentSerializer
    model = Student
    route_name = 'student'

    def get_object(self, **kwargs):
        return self.model.objects.get(pk=kwargs['id'])

    def get_query_set(self, **kwargs):
        return self.model.objects.all()

route_handler.register(StudentModelRouter)
