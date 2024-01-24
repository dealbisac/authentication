from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required.")
        if not username:
            raise ValueError("Username is required.")
        if not password:
            raise ValueError("Password is required.")
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            **extra_fields
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        
        return self.create_user(
            email=self.normalize_email(email),
            password=password,
            **extra_fields
        )