from django.http import JsonResponse
from myapp1.serializers import DepartmentSerializers,IndividualSerializers
from myapp1.models import Department,Individual
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

@api_view(['GET'])
def list_dept(request):
    dept=Department.objects.all()
    serializer = DepartmentSerializers(dept,many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def post_dept(request):
    serializer = DepartmentSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

class personpagination(LimitOffsetPagination):
    'PAGE_SIZE'== 2

class Individual1(APIView):
    pagination_classes = [IsAuthenticated]
    # pagination_class=PageNumberPagination
    pagination_class=personpagination
    def get(self,request):
        i=Individual.objects.all()

        paginator=self.pagination_class()
        page=paginator.paginate_queryset(i,request)
        s=IndividualSerializers(page,many=True)
        return paginator.get_paginated_response(s.data)
    def post(self,request):
        s=IndividualSerializers(data=request.data)
        if s.is_valid():
            s.save()
            return Response("success")
        else:
            return Response("success")
           



class login1(APIView):

    def post(self,request):
        username=request.data.get('username')
        password=request.data.get("password")
        user=authenticate(username=username,password=password)
        
        if user is not None:
            refresh=RefreshToken.for_user(user)
            
            return Response({
                'message':"logged in",
                "access":str(refresh.access_token),
                "refresh":str(refresh)
            })
        return Response("error")   


class logout1(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        refresh_token=request.data.get('refresh')
        refresh=RefreshToken(refresh_token)
        refresh.blacklist()
        return Response({
            'message':'logged_out'
        })
        