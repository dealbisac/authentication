from base64 import urlsafe_b64decode
from smtplib import SMTP
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from auth import settings
from django.core.mail import EmailMessage, send_mail, send_mass_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from accounts.tokens import app_token_generator
from redmail import outlook, EmailSender
from . models import *

User = get_user_model()

# Create your views here.

@login_required(login_url='/login/')
# Home page view
def home(request):
    context = {'page' : 'Home'}
    return render(request, 'index.html', context)


# Sign up page view
def signup_page(request, uidb64, token):
    context = {'page' : 'Sign Up', }

    # data from url
    try:
        invitedemail = force_str(urlsafe_base64_decode(uidb64))
        invitedUser = Invite.objects.get(email=invitedemail)

        # send email as context to sign up page
        context['invitedemail'] = invitedUser.email

        # check if token is valid
        # if not app_token_generator.check_token(invitedUser.token, token):
        #     messages.error(request, "Invalid token.")
        #     return redirect('/signup/'+uidb64+'/'+token)
        
       # get data from form to save to database
        if request.method == 'POST':
            email = request.POST.get('email')
            anonymousname = request.POST.get('anonymousname')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm-password')

            # check if passwords match
            if password != confirm_password:
                messages.error(request, "Password and Confirm Password do not match.")
                return redirect('/signup/'+uidb64+'/'+token)
            
            # username already exists in database
            if User.objects.filter(username=anonymousname).exists():
                messages.error(request, "Username already exists.")
                return redirect('/signup/'+uidb64+'/'+token)
            
            # email already exists in database
            if User.objects.filter(email=email).exists():
                messages.error(request, "You already have account. In case you forgot your password, you can reset it.")
                return redirect('/signup/'+uidb64+'/'+token)
            
            # save data to database
            user = User.objects.create(
                email=email, 
                username=anonymousname
            )
            user.set_password(password)
            user.save()
            
            messages.success(request, "Account created successfully. You can now login.")

            # Email Message to user
            subject = "Welcome to Course 101"
            message = "Hi " + anonymousname + ",\n\nWelcome to Course 101. We are glad to have you here. \n\nRegards,\nCourse 101 Team"
            from_email = "Course 101 <" + settings.EMAIL_HOST_USER +">"
            to_email = [email]
            send_mail(subject, message, from_email, to_email, fail_silently=False)

            # redirect to sign in page.
            return redirect('/login/')

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    # # data from form
    # if request.method == 'POST':
    #     email = request.POST.get('email')
    #     anonymousname = request.POST.get('anonymousname')
    #     password = request.POST.get('password')

    #     # check if email or username already exists
    #     if User.objects.filter(email=email).exists():
    #         messages.error(request, "Email already exists.")
    #         return redirect('/signup/')
    #     if User.objects.filter(username=anonymousname).exists():
    #         messages.error(request, "Username already exists.")
    #         return redirect('/signup/')
        

        
    #     # save data to database
    #     user = User.objects.create(
    #         email=email, 
    #         username=anonymousname
    #     )
    #     user.set_password(password)
    #     user.save()

    #     messages.success(request, "Account created successfully. You can now login.")

    #     # Email Message to user
    #     subject = "Welcome to Course 101"
    #     message = "Hi " + anonymousname + ",\n\nWelcome to Course 101. We are glad to have you here. \n\nRegards,\nCourse 101 Team"
    #     #from_email = "Course 101 <" + settings.EMAIL_HOST_USER +">"
    #     from_email = "Course 101 < no-reply@chattutor.dk >"
    #     to_email = [email]
    #     send_mail(subject, message, from_email, to_email, fail_silently=False)


    #     # redirect to sign in page.
    #     return redirect('/signup/')

    return render(request, 'signup.html', context)


# Sign in (Login) page view
def login_page(request):
    context = {'page' : 'Sign'}

    # data from form
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # check if email exists in database
        if not User.objects.filter(email=email).exists():
            messages.error(request, "Invalid email. Use your own student email.")
            return redirect('/login/')
        
        # authenticate user
        user = authenticate(email=email, password=password)

        if user is None:
            messages.error(request, "Invalid credentials.")
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/dashboard/')
        
    return render(request, 'signin.html', context)


# Logout page view
def logout_page(request):
    logout(request)
    return redirect('/login/')


@login_required(login_url='/login/')
# Profile page view
def profile_page(request):
    context = {'page' : 'Profile'}

    # data from database (Use this to display data on profile page) filter only current user
    users = User.objects.filter(id=request.user.id)
    context['users'] = users

    # data from form (Use this to save data to database)
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')

        # check if email or username already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('/profile/')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('/profile/')
        
        # save data to database
        user = User.objects.create(
            username=username, 
            email=email
        )
        user.save()

        messages.success(request, "Profile updated successfully.")

        # redirect to profile page.
        return redirect('/profile/')

    return render(request, 'profile.html', context)


def forgot_password_page(request):
    context = {'page' : 'Forgot Password'}
    email_template_name = 'reset-password-email.html'

    # data from form
    if request.method == 'POST':
        email = request.POST.get('email')

        # check if email exists in database
        if not User.objects.filter(email=email).exists():
            messages.error(request, "Invalid email. Provide your student email registered with us.")
            return redirect('/forgot-password/')
        
        # send email to user with reset password link
        current_site = get_current_site(request)
        subject = "Reset Your Password."
        from_email = "Course 101 < no-reply@chattutor.dk >"
        message = render_to_string('reset-password-email.html', {
            'user': email,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(email)),
            'token': app_token_generator.make_token(email),
        })

        email = EmailMessage(
            subject, 
            message,
            from_email,
            to=[email]
        )
        email.fail_silently = False
        email.send()

        """

        # Email for Outlook
        current_site = get_current_site(request)
        outlook_subject = "Reset Your Password."
        outlook_from_email = "Course 101 <" + settings.OUTLOOK_HOST_USER +">"
        outlook_message = render_to_string('reset-password-email.html', {
            'user': email,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(email)),
            'token': app_token_generator.make_token(email),
        })

        outlook_host = settings.OUTLOOK_HOST
        outlook_username = settings.OUTLOOK_HOST_USER
        outlook_password = settings.OUTLOOK_HOST_PASSWORD
        outlook_port = settings.OUTLOOK_PORT

        outlookemail = EmailSender(
            host=outlook_host,
            port=outlook_port,
            username=outlook_username,
            password=outlook_password,
            cls_smtp=SMTP,
            use_starttls=True
        )

        outlookemail.send(
            subject=outlook_subject,
            sender=outlook_from_email,
            receivers=[email],
            text=outlook_message
        )

        """

        messages.success(request, "Email sent successfully. Check your inbox.")

        # redirect to sign in page.
        return redirect('/forgot-password/')

    return render(request, 'forgot-password.html', context)


def reset_password_page(request, uidb64, token):
    context = {'page' : 'Reset Password'}

    try:
        # data from url (fix: TypeError: a bytes-like object is required, not 'str')
        email = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(email=email)

        # send email as context to reset password page
        context['email'] = user.email

        # check if token is valid
        if not app_token_generator.check_token(user, token):
            messages.error(request, "Invalid token.")
            return redirect('/reset-password/'+uidb64+'/'+token)
        
        # get data from form to save to database
        if request.method == 'POST':
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm-password')

            # check if passwords match
            if password != confirm_password:
                messages.error(request, "Password and Confirm Password do not match.")
                return redirect('/reset-password/'+uidb64+'/'+token)
            
            # save data to database
            user.set_password(password)
            user.save()
            
            messages.success(request, "Password reset successfully. You can now login.")

            # redirect to sign in page.
            return redirect('/login/')
        
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    return render(request, 'reset-password.html', context)


@login_required(login_url='/login/')
def change_password_page(request):
    return HttpResponse("Hello from change password view")


@login_required(login_url='/login/')
def admin_page(request):
    context = {'page' : 'Dashboard'}
    return render(request, 'admin.html', context)


@login_required(login_url='/login/')
def users_page(request):
    context = {'page' : 'Users'}
    email_template_name = 'invite-users-email.html'

    # data from database (Users)
    users = User.objects.all()
    context['users'] = users

    # data from form (Invite Users)
    if request.method == 'POST':
        recipientsemail= request.POST.get('recipientsEmail')
        messageoptional = request.POST.get('messageText')

        # separate if multiple emails from the form
        recipients = recipientsemail.split(',')
        recipients = [recipient.strip() for recipient in recipients]

        # send email to user for sign up to join course.
        current_site = get_current_site(request)
        subject = "Welcome to Course 101"
        from_email = "Course 101 <" + settings.EMAIL_HOST_USER +">"
        messagetemplate = "Hi,\n\nYou have been invited to join Course 101. Please sign up to join the course. \n\nRegards,\nCourse 101 Team"

        #if messageoptional is null then use default message
        message = messagetemplate if messageoptional is None else messageoptional

        for recipient in recipients:
            message = render_to_string('invite-users-email.html', {
                'user': recipient,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(recipient)),
                'token': app_token_generator.make_token(recipient)
            })
            email = EmailMessage(
                subject, 
                message,
                from_email,
                to=[recipient]
            )
            email.fail_silently = False
            email.send()

            # save data to database
            invite = Invite.objects.create(
                email=recipient, 
                token=app_token_generator.make_token(recipient)
            )
            invite.save()

        messages.success(request, "All users have been invited.")

        # redirect to sign in page.
        return redirect('/users/')

    return render(request, 'users.html', context)