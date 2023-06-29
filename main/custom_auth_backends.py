from django.contrib.auth.backends import ModelBackend
from .models import User, Worker

class MultiUserModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Try authenticating against the first user model (UserModel1)
        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            return user
        
        # Try authenticating against the second user model (UserModel2)
        user = Worker.objects.filter(username=username).first()
        if user and user.check_password(password):
            return user
        
        # If authentication fails for both models, return None
        return None
