from swampdragon.serializers.model_serializer import ModelSerializer


class StudentSerializer(ModelSerializer):
    class Metta:
        model = 'registration.Student'
        publish_fields = ('first_name', 'last_name', 'instrument')
