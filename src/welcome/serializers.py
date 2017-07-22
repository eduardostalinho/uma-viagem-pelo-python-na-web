from rest_framework import serializers

class DiceSerializer(serializers.Serializer):
    n_faces = serializers.IntegerField()
    result = serializers.IntegerField()
