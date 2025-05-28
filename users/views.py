# from django.conf import settings
# from django.contrib import messages
# from django.contrib.auth import get_user_model, login
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.tokens import default_token_generator
# from django.contrib.sites.shortcuts import get_current_site
# from django.core.mail import send_mail
# from django.shortcuts import redirect, render
# from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
# from django.views.generic import TemplateView
#
# from .forms import UserRegistrationForm
# from .models import Client
#
# User = get_user_model()
#
#
# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = User.objects.create_user(
#                 form.cleaned_data['email'],
#                 form.cleaned_data['password']
#             )
#             user.is_active = False
#             user.is_blocked = True
#             user.save()
#
#             client = Client(
#                 user=user,
#                 first_name=form.cleaned_data['first_name'],
#                 last_name=form.cleaned_data['last_name']
#             )
#             client.save()
#
#             token = default_token_generator.make_token(user)
#             uid = urlsafe_base64_encode(str(user.pk).encode())
#             current_site = get_current_site(request)
#
#             subject = 'User registration'
#             message = render_to_string(
#                 'emails/email_activation.html',
#                 {
#                     'user': user,
#                     'domain': current_site,
#                     'uid': uid,
#                     'token': token
#                 }
#             )
#             send_mail(
#                 subject,
#                 message,
#                 settings.DEFAULT_FROM_EMAIL,
#                 [form.cleaned_data['email']]
#             )
#
#             messages.add_message(
#                 request,
#                 messages.SUCCESS,
#                 'Wellcome to our site!'
#             )
#         else:
#             messages.add_message(
#                 request,
#                 messages.ERROR,
#                 'Passwords are not equal!'
#             )
#     else:
#         form = UserRegistrationForm()
#
#     return render(
#         request,
#         'registration.html',
#         {'form': form}
#     )
#
#
# def activate(request, uid, token):
#     try:
#         uid = urlsafe_base64_decode(uid).decode()
#         user = User.objects.get(pk=uid)
#     except (TypeError, ValueError, User.DoesNotExist):
#         user = None
#
#     if user is not None and default_token_generator.check_token(user, token):
#         user.is_active = True
#         user.is_blocked = False
#         user.save()
#         login(request, user)
#         return redirect('index')
#     else:
#         return redirect('login')
#
#
# class LoginView(TemplateView):
#     template_name = 'account.html'
#
#
# class AccountView(LoginRequiredMixin, TemplateView):
#     login_url = 'users/login/'
#     template_name = 'account.html'
#
#     def get(self, request):
#         return super().get(request)
