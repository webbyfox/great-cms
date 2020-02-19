from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from wagtail.core.models import Page, Site

from tests.domestic import factories

User = get_user_model()


class Command(BaseCommand):

    def handle(self, *args, **options):
        # On start Wagtail provides one page with ID=1 and it's called "Root page"
        root_page = Page.objects.get(pk=1)
        # On start Wagtail provides one site with ID=1
        site = Site.objects.get(pk=1)
        homepage = factories.DomesticHomePageFactory(title='homepage', parent=root_page, live=True)
        site.root_page = homepage
        site.save()
        # Delete welcome to wagtail page
        Page.objects.get(pk=2).delete()

        # creates a superuser for local environment
        user = User(username='test', is_staff=True, is_superuser=True, is_active=True)
        user.save()
        user.set_password('password')
        user.save()