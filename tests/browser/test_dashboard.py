# -*- coding: utf-8 -*-
import logging
import random
from typing import List

import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver

import allure
from directory_constants import choices
from tests.browser.common_selectors import (
    DashboardContents,
    DashboardContentsOnSuccess,
    DashboardContentsWithoutSuccess,
    DashboardModalLetsGetToKnowYou,
    HeaderSignedIn,
)
from tests.browser.steps import (
    should_not_see_any_element,
    should_not_see_errors,
    should_see_all_elements,
    should_see_all_expected_page_sections,
    visit_page,
)
from tests.browser.util import (
    attach_jpg_screenshot,
    find_element,
    selenium_action,
    try_alternative_click_on_exception,
)

pytestmark = [
    pytest.mark.browser,
    pytest.mark.dashboard,
]

logger = logging.getLogger(__name__)


@allure.step('Select random sample of sectors')
def select_random_sample_sectors() -> List[str]:
    sector_labels = [label for _, label in choices.SECTORS]
    sectors = random.sample(sector_labels, random.randint(1, 5))
    logger.info(f'Selected random sample of sectors: {sectors}')
    return sectors


@allure.step('Enter sector names: {industries}')
def enter_and_submit_industries(browser, industries):
    industries_input = find_element(browser, DashboardModalLetsGetToKnowYou.INDUSTRIES_INPUT)
    for industry in industries:
        industries_input.send_keys(industry)
        industries_input.send_keys(Keys.ENTER)

    attach_jpg_screenshot(browser, 'After entering industries', selector=DashboardModalLetsGetToKnowYou.MODAL)

    with selenium_action(browser, 'Failed to submit industries'):
        continue_button = find_element(browser, DashboardModalLetsGetToKnowYou.SUBMIT)
        with try_alternative_click_on_exception(browser, continue_button):
            continue_button.click()

    should_not_see_errors(browser)
    attach_jpg_screenshot(browser, 'Dashboard with success query parameter')


@allure.step('Should see "Lets get to know you modal"')
def should_see_lets_get_to_know_you_modal(browser: WebDriver):
    should_see_all_elements(browser, DashboardModalLetsGetToKnowYou)


@allure.step('Should NOT see "Lets get to know you modal"')
def should_not_see_lets_get_to_know_you_modal(browser: WebDriver):
    should_not_see_any_element(browser, DashboardModalLetsGetToKnowYou)


@pytest.mark.django_db
def test_dashboard_with_success_query_parameter(
    server_user_browser_dashboard, mock_update_company_profile, mock_dashboard_profile_events_opportunities,
):
    live_server, user, browser = server_user_browser_dashboard

    should_see_lets_get_to_know_you_modal(browser)
    industries = select_random_sample_sectors()

    enter_and_submit_industries(browser, industries)

    should_not_see_lets_get_to_know_you_modal(browser)
    should_see_all_expected_page_sections(browser, [HeaderSignedIn, DashboardContents, DashboardContentsOnSuccess])


@pytest.mark.django_db
def test_dashboard_without_success_query_parameter(
    server_user_browser_dashboard, mock_update_company_profile, mock_dashboard_profile_events_opportunities,
):
    live_server, user, browser = server_user_browser_dashboard

    should_see_lets_get_to_know_you_modal(browser)
    industries = select_random_sample_sectors()

    enter_and_submit_industries(browser, industries)
    should_not_see_lets_get_to_know_you_modal(browser)
    should_see_all_expected_page_sections(browser, [HeaderSignedIn, DashboardContents, DashboardContentsOnSuccess])

    visit_page(live_server, browser, 'core:dashboard', 'Dashboard without success query parameter')
    should_not_see_lets_get_to_know_you_modal(browser)
    should_see_all_expected_page_sections(browser, [HeaderSignedIn, DashboardContents, DashboardContentsWithoutSuccess])
