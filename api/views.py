from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from .models import Department, District, Town
from rest_framework.response import Response
from .serializer import DepartmentSerializer, DistrictsSerializer, NeighborhoodsSerializer, TownSerializer
from rest_framework import status

class DepartmentView(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [AllowAny,]


class DepartmentTownView(RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        department = Department.objects.get(pk=self.kwargs.get('pk'))
        towns = department.towns.all()
        serializer = TownSerializer(towns, many=True)
        datas = {
                "department": department.name,
                "towns": serializer.data
            }
        return Response(datas, status.HTTP_200_OK)


class TownDistrictsView(RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        town = Town.objects.get(pk=self.kwargs.get('pk'))
        districs = town.districts.all()
        serializer = DistrictsSerializer(districs, many=True)
        datas = {
            'town': town.name,
            'districts': serializer.data
        }
        return Response(datas, status.HTTP_200_OK)

class NeighborhoodsView(RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        district = District.objects.get(pk=self.kwargs.get('pk'))
        neighborhoods = district.neighborhoods.all()
        serializer = NeighborhoodsSerializer(neighborhoods, many=True)
        datas = {
            'district': district.name,
            "neighborhoods": serializer.data
        }
        return Response(datas, status.HTTP_200_OK)