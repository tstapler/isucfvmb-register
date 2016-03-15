from swampdragon.serializers.model_serializer import ModelSerializer
import time


class StudentSerializer(ModelSerializer):
    class Meta:
        model = 'registration.Student'
        publish_fields = ('first_name', 'last_name', 'instrument', "submission_time")

    def serialize_submission_time(self, obj):
        print(obj.submission_time.isoformat())
        return int(time.mktime(obj.submission_time.timetuple())) * 1000
