from pytest_bdd import scenarios, given, when, then, parsers
from page_objects.MainPage import MainPage

scenarios('../features/map_point_open_data.feature')


@given('ENTSOG map is displayed')
def entsog_map_displayed(browser):
    MainPage(browser).open_main_page()


@when('user clicks zoom in')
def click_map_point(browser):
    MainPage(browser).click_zoom_in()


@then('small point locator is available')
def click_map_point(browser):
    MainPage(browser).check_small_point_on_the_map(browser)
