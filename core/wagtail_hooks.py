from great_components.helpers import add_next
from wagtail.core import hooks

from django.urls import reverse
from django.shortcuts import redirect

from core import mixins, views


@hooks.register('before_serve_page')
def anonymous_user_required(page, request, serve_args, serve_kwargs):
    if isinstance(page, mixins.AnonymousUserRequired):
        if request.user.is_authenticated:
            return redirect(page.anonymous_user_required_redirect_url)


@hooks.register('before_serve_page')
def login_required_signup_wizard(page, request, serve_args, serve_kwargs):
    if page.template == 'learn/lesson_page.html' and request.user.is_anonymous:
        signup_url = reverse('core:signup-wizard', kwargs={'step': views.SignupWizardView.STEP_START})
        url = add_next(destination_url=signup_url, current_url=request.get_full_path())
        return redirect(url)
