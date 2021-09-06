from pytest_bdd import scenarios, given, when, then, parsers
from page_objects.MainPage import MainPage

CONVERTERS = dict(filter=str, point_type=str)
scenarios('../features/map_point_data.feature', example_converters=CONVERTERS)


@then('big point locators are on zoomed in map')
def click_map_point(browser):
    MainPage(browser).big_small_point_on_the_map()


@given('ENTSOG map is displayed')
def entsog_map_displayed(browser):
    MainPage(browser).open_main_page()


@when('user clicks zoom in')
def click_zoom_in(browser):
    MainPage(browser).click_zoom_in()


@when('user opens filters panel')
def open_filters_panel(browser):
    MainPage(browser).click_filter_panel()


@when('user sets infrastructure filter to <filter>')
@when(parsers.parse("user sets infrastructure filter to {filter:d}"))
def select_filter(browser, filter):
    MainPage(browser).filter_map_points(filter)


@then('<point_type> points are on the map')
@then(parsers.parse("{point_type:d} points are on the map"))
def check_point_type_on_map(browser, point_type):
    MainPage(browser).check_point_type_on_the_map(point_type)
