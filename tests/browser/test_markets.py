from unittest import mock

import pytest

from core import helpers
from tests.browser.common_selectors import Header, MarketsContainer
from tests.browser.util import attach_jpg_screenshot, should_see_all_elements
from tests.helpers import create_response

pytestmark = pytest.mark.browser


@pytest.mark.django_db
@mock.patch.object(helpers, 'create_company_profile')
def test_markets(
    mock_create_company_profile, mock_get_company_profile, server_user_browser_dashboard
):

    def side_effect(_):
        mock_get_company_profile.return_value = {'foo': 'bar'}

    mock_create_company_profile.return_value = create_response()
    mock_create_company_profile.side_effect = side_effect
    live_server, user, browser = server_user_browser_dashboard

    browser.get(live_server.url + "/markets/")

    attach_jpg_screenshot(browser, 'Markets')
    should_see_all_elements(browser, Header)
    should_see_all_elements(browser, MarketsContainer)
