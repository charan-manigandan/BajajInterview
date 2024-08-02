from rest_framework import serializers

class InputSerializer(serializers.Serializer):
    data = serializers.ListField(
        child=serializers.CharField()
    )

class OutputSerializer(serializers.Serializer):
    is_success = serializers.BooleanField()
    user_id = serializers.CharField()
    email = serializers.EmailField()
    roll_number = serializers.CharField()
    numbers = serializers.ListField(
        child=serializers.CharField()
    )
    alphabets = serializers.ListField(
        child=serializers.CharField()
    )
    highest_alphabet = serializers.ListField(
        child=serializers.CharField()
    )
