from rest_framework import serializers
from . models import mutual

class employeeSerializers(serializers.ModelSerializer):
    class Meta:
        model=mutual

        fields='__all__'