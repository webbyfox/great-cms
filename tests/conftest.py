from unittest import mock

import pytest
from wagtail.core.models import Page
from wagtail_factories import SiteFactory, PageFactory

from tests.domestic import factories
from tests.helpers import create_response
from core.helpers import Airtable

from sso.models import BusinessSSOUser


@pytest.fixture
def root_page():
    """
    On start Wagtail provides one page with ID=1 and it's called "Root page"
    """
    Page.objects.all().delete()
    return PageFactory(title='root', slug='root')


@pytest.fixture
def domestic_homepage(root_page):
    return factories.DomesticHomePageFactory.create(title='homepage', parent=root_page, live=True)


@pytest.fixture
def domestic_site(domestic_homepage):
    return SiteFactory(root_page=domestic_homepage)


@pytest.fixture(autouse=True)
def auth_backend():
    patch = mock.patch(
        'directory_sso_api_client.sso_api_client.user.get_session_user',
        return_value=create_response(status_code=404)
    )
    yield patch.start()
    patch.stop()


@pytest.fixture
def user():
    return BusinessSSOUser(
        id=1,
        pk=1,
        mobile_phone_number='55512345',
        email='jim@example.com',
        first_name='Jim',
        last_name='Cross',
        session_id='123',
    )


@pytest.fixture
def client(client, auth_backend, settings):
    def force_login(user):
        client.cookies[settings.SSO_SESSION_COOKIE] = '123'
        auth_backend.return_value = create_response({
            'id': user.id,
            'email': user.email,
            'hashed_uuid': user.hashed_uuid,
            'user_profile': {
                'mobile_phone_number': user.mobile_phone_number,
                'first_name': user.first_name,
                'last_name': user.last_name
            }
        })
    client.force_login = force_login
    return client


@pytest.fixture(autouse=True)
def mock_airtable_rules_regs():
    airtable_data = [
        {
            'id': '1',
            'fields':
                {
                    'Country': 'India',
                    'Export Duty': 1.5,
                    'Commodity code': '2208.50.12',
                    'Commodity Name': 'Gin and Geneva 2l'
                },
         },
        {
            'id': '2',
            'fields':
                {
                    'Country': 'China',
                    'Export Duty': 1.5,
                    'Commodity code': '2208.50.13',
                    'Commodity Name': 'Gin and Geneva'
                },
        },
    ]
    patch = mock.patch.object(Airtable, 'get_all', return_value=airtable_data)
    yield patch.start()
    patch.stop()