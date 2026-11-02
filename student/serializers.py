from rest_framework import serializers
from student.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","password"]
        read_only_fields=["id"]


class StudentSerializer(serializers.ModelSerializer):
    fee_status = serializers.SerializerMethodField()
    class Meta:
        model=Students
        fields="__all__"
        read_only_fields=["id","joining_date"]

    def get_fee_status(self, obj):
        if obj.is_fee_paid:
            return "paid"
        else:
            return "pending"

