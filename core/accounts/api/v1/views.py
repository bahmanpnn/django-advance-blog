from rest_framework import generics
from .serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework import status


class RegistrationAPIView(generics.GenericAPIView):
    serializer_class=RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer=RegistrationSerializer(data=request.data)
        # serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            data={
                'email':serializer.validated_data['email']
            }
            
            return Response(data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
        
    # def post(self,request):
    #     serializer=self.serializer_class(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     data={
    #             'email':serializer.validated_data['email']
    #         }
    #     return Response(data,status=201)
    


