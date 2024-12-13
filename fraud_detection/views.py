from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os

from django.contrib.auth.models import User
from fraud_detection.models import Transaction
from fraud_detection.serializer import TransactionSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .preprocess import preprocess_data, split_and_encode
from .analyze import analyze_csv

# Create your views here.
def index(request):
    return HttpResponse("Fraud Detection Home Page")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_transactions(request):
    user = request.user
    transactions = Transaction.objects.filter(owner=user)
    serializer = TransactionSerializer(transactions, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])  # Adjust permission based on your requirement
def preprocess_file(request):
    try:
        # Fetch file from request
        file = request.FILES['file']
        file_path = os.path.join(settings.MEDIA_ROOT, file.name)

        # Save the file temporarily
        with open(file_path, 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)

        # Process the file
        df = preprocess_data(file_path)
        X_train, X_val, X_test, y_train, y_val, y_test, label_encoded = split_and_encode(df)

        # Save preprocessed files for verification
        X_train.to_csv(os.path.join(settings.MEDIA_ROOT, 'X_train.csv'), index=False)
        y_train.to_csv(os.path.join(settings.MEDIA_ROOT, 'y_train.csv'), index=False)

        # Make predictions using the analyze_csv function
        predictions = analyze_csv(file_path)

        # Return predictions
        return Response({
            "message": "File preprocessed and analyzed successfully!",
            "predictions": predictions.tolist()
        }, status=200)

    except Exception as e:
        return Response({"error": str(e)}, status=500)
