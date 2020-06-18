from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request,format=None):
        """Returns a lost of APIView features"""
        an_apiview =[
        'uses hhtp methods as function(get,post,patch,put,delete)',
        'is similar to a traditional django vieew',
        'gives you the most control over you application logic',
        'is mapped manually to urls',
        ]

        return Response({'message':'hello!', 'an_apiview':an_apiview})
