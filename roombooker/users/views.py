from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.views.generic import DetailView
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.http.response import HttpResponse

User = get_user_model()

class ProfileDetailView(DetailView):
        queryset = User.objects.filter(is_active=True)
        template_name = 'user/user.html'

        def get_object(self):
                user = self.request.user
                return get_object_or_404(User, username__iexact = user.username)
        
        def get(self, request, *args, **kwargs):
                try:
                        self.object = self.get_object()
                except Http404:
                        return HttpResponseRedirect(reverse('user:login'))

                context = self.get_context_data(object=self.object)
                return self.render_to_response(context)
