from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class DataProcessingView(APIView):
    def post(self, request):
        # Przykład przetwarzania danych
        input_data = request.data.get('data')  # Przykład pobierania danych z requesta
        
        # Przetwarzanie danych (np. obliczenia, operacje na stringach itp.)
        processed_data = f"Przetworzone: {input_data.upper()}"
        
        return Response({"processed_data": processed_data}, status=status.HTTP_200_OK)