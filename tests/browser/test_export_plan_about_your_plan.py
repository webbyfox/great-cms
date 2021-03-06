# -*- coding: utf-8 -*-
import pytest

from tests.browser.common_selectors import (
    ExportPlanTargetMarkets,
    HeaderCommon,
    HeaderSignedIn,
    StickyHeader,
)
from tests.browser.steps import should_see_all_expected_page_sections, visit_page

pytestmark = [
    pytest.mark.browser,
    pytest.mark.export_plan,
    pytest.mark.export_plan_about_your_plan,
]


@pytest.mark.django_db
def test_export_plan_brand_and_product_page(
    server_user_browser_dashboard, mock_all_dashboard_and_export_plan_requests_and_responses
):
    live_server, _, browser = server_user_browser_dashboard

    visit_page(live_server, browser, 'exportplan:target-markets', 'Target markets')

    should_see_all_expected_page_sections(
        browser, [HeaderCommon, HeaderSignedIn, StickyHeader, ExportPlanTargetMarkets]
    )
