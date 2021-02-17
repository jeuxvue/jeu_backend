from rest_framework import serializers


class GameSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    rawg_id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    release_date = serializers.DateField()
    age_rating_id = serializers.IntegerField()
    sys_req = serializers.CharField()
