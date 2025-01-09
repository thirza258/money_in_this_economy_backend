from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.apps import apps


class FinanceView(APIView):
    app_config = apps.get_app_config("ai_handler")

    def get(self, request):
        # Get retriever instance from the app config
        retriever = self.app_config.retriever
        retrieved_docs = retriever.invoke("What is the current market sentiment?")
        
        # Return the retrieved data as JSON response
        return Response({"retrieved_docs": retrieved_docs}, status=status.HTTP_200_OK)

    def post(self, request):
        pass
