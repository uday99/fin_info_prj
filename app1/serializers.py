
from rest_framework import serializers
from app1.models import Employee
import base64
from drf_extra_fields.fields import Base64ImageField






class AdressData(object):
    def __int__(self,addressDetails):
        self.address_fields=addressDetails

class ExpSerializer(serializers.Serializer):
    companyName=serializers.CharField(max_length=100)
    fromDate=serializers.CharField(max_length=60)
    toDate=serializers.CharField(max_length=60)
    address=serializers.CharField(max_length=120)

class QualificationSerializer(serializers.Serializer):
    qualificationName=serializers.CharField(max_length=120)
    percentage=serializers.FloatField()

class ProjectSerializer(serializers.Serializer):
    title=serializers.CharField(max_length=50)
    description=serializers.CharField(max_length=120)




class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=80)
    email = serializers.EmailField(max_length=120)
    age = serializers.IntegerField()
    gender = serializers.CharField(max_length=20)
    phoneNo = serializers.CharField(max_length=20)
    addressDetails = serializers.DictField(child = serializers.CharField())
    workExperience=serializers.ListField(child = ExpSerializer())
    qualifications=serializers.ListField(child=QualificationSerializer())
    projects=serializers.ListField(child=ProjectSerializer())
    photo=Base64ImageField(required=False)

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.get("name",instance.name)
        instance.email=validated_data.get("email",instance.email)
        instance.age = validated_data.get("age", instance.age)
        instance.gender = validated_data.get("gender", instance.gender)
        instance.phoneNo = validated_data.get("phoneNo", instance.phoneNo)
        instance.addressDetails = validated_data.get("addressDetails", instance.addressDetails)
        instance.workExperience = validated_data.get("workExperience", instance.workExperience)
        instance.qualifications=validated_data.get("qualifications",instance.qualifications)
        instance.projects = validated_data.get("projects", instance.projects)

        instance.save()
        return instance



    # class Meta:
    #     model=Employee
    #     fields='__all__'






