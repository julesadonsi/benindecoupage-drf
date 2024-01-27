from rest_framework.serializers import ModelSerializer

from .models import Department, District, Neighborhoods, Town

class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = ["id", "name",]


class TownSerializer(ModelSerializer):
    class Meta:
        model = Town
        fields = ["id", "name",]


class DistrictsSerializer(ModelSerializer):
    class Meta:
        model = District
        fields = ["id", "name",]

class NeighborhoodsSerializer(ModelSerializer):
    class Meta:
        model = Neighborhoods
        fields = ["id", "name",]