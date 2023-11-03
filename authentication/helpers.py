from django.http import JsonResponse

import os
import uuid
import random
import string
import jwt
import datetime

secret_key = "7aa9fb03addfb2010ca7e558be6640a7715a17db55a3a2bd361e1e5d61f80be3b8f02eeb028d2aefcca834a669f4351106fe3d391c0fcce52690fb60b79cd240"

def create_jwt_token(email):
    payload = {
        'email': email,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1), 
    }
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token

def decode_jwt_token(token):
    payload = jwt.decode(token, secret_key, algorithms=['HS256'])
    return payload

def require_access_token(view_func):
    def _wrapped_view(request, *args, **kwargs):
        token = request.session.get('token')  # Change this to how you store your token
        if token:
            try:
                payload = jwt.decode(token, secret_key, algorithms=['HS256'])
                # You can perform additional checks on the payload if needed
                return view_func(request, *args, **kwargs)
            except jwt.ExpiredSignatureError:
                # Handle expired token
                return JsonResponse({'error': 'Token has expired'}, status=401)
            except jwt.DecodeError:
                # Handle invalid token
                return JsonResponse({'error': 'Invalid token'}, status=401)
        else:
            # Handle missing token (e.g., redirect to the login page)
            return JsonResponse({'error': 'Token required'}, status=401)
    return _wrapped_view