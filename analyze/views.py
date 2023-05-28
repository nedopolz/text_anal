from rest_framework.decorators import api_view
from rest_framework.response import Response
from analyze.serializers import TextInputSerializer




@api_view(["POST"])
def analyze_text(request):
    serializer = TextInputSerializer(data=request.data)
    # serializer.is_valid(raise_exception=True)
    # result = serializer.save()
    return Response(data=request.data)