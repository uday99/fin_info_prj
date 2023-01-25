from django.http import Http404
from django.shortcuts import render
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from app1.serializers import EmployeeSerializer
from app1.models import Employee
from rest_framework.response import Response
from rest_framework import status

from django.db.utils import OperationalError,DatabaseError,ProgrammingError,IntegrityError
from django.http import HttpResponse,JsonResponse
from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException


# Create your views here.



class CreateEmp(APIView,APIException):
    def post(self,request):
        data=request.data
        #parser_classes = (FileUploadParser,)

        try:
            es = EmployeeSerializer(data=data)
            if es.is_valid():


                es.save()
                em=Employee.objects.latest('id')
                empid=em.id
                message = {"message": "Employee Saved","EMPID":empid,"success":True}
                return Response(message,status=status.HTTP_200_OK)

            else:
                message = {"error": es.errors}
                return  Response(message,status=status.HTTP_400_BAD_REQUEST)
        except :
            message={'message':"employe already exist","success":False}
            return Response(message,status=status.HTTP_200_OK)


class List_Allemp(APIView):
    def get(self,request):

        try:
            e=Employee.objects.all()
            es=EmployeeSerializer(e,many=True)
            return Response(es.data,status=status.HTTP_200_OK)
        except (Employee.DoesNotExist| es.errors) as error:
            content={'errors':error}
            return Response(content,status=status.HTTP_400_BAD_REQUEST)






class Read_One_Emp(APIView):
    def get(self,request,regid):
        if regid:
            try:
                e=Employee.objects.get(pk=regid)
                es=EmployeeSerializer(e)
                return Response(es.data,status=status.HTTP_200_OK)
            except (Employee.DoesNotExist  | es.errors) as e:
                content={'error':e}
                return Response(content)
        else:

            raise Http404


class Update_Emp(APIView):
    def put(self,request,regid):
        if regid:
            try:
                data=request.data
                e=Employee.objects.get(pk=regid)
                es=EmployeeSerializer(e,data)
                if es.is_valid():
                    es.save()

                    content={'message':"Employee update successfully","success":True}
                    return Response(content,status=status.HTTP_201_CREATED)
                else:
                    content={"error":es.errors}
                    return Response(content,status=status.HTTP_400_BAD_REQUEST)


            except Employee.DoesNotExist:
                content={"error":"no employee found with this regid","success":False}
                return Response(content,status=status.HTTP_400_BAD_REQUEST)

        else:
            raise Http404


class Delete_Emp(APIView):
    def delete(self,request):
        try:
            data=request.data
            id=data['regid']
            try:
                Employee.objects.get(pk=id).delete()
                content={'message': "Employee Deleted successfully","success":True}
                return Response(content,status=status.HTTP_200_OK)
            except :
                content={'message':"employe deletion failed","success":False}
                return Response(content, status=status.HTTP_200_OK)

        except Employee.DoesNotExist:
            content={"message":"no employee found with this regid","success":False}
            return Response(content,status=status.HTTP_404_NOT_FOUND)
