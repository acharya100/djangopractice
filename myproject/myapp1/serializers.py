from rest_framework import serializers
from myapp1.models import Department,Individual

class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class IndividualSerializers(serializers.ModelSerializer):
    class Meta:
        model = Individual
        fields = '__all__'