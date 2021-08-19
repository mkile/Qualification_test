import pytest
from random import uniform
import allure

from page_objects.MainPage import MainPage
from page_objects.PointsAdvancedSearch import PointsAdvancedSearch
from page_objects.PointsData import PointsData
from page_objects.ZonesAdvancedSearch import ZonesAdvancedSearch
from page_objects.ZonesData import ZonesData
from page_objects.Operators import Operators
from page_objects.CalendarView import CalendarView
from page_objects.PUInterruptions import PUInterruptions
from page_objects.UMMUnavailabilities import UMMUnavailabilities
from page_objects.UMMOtherMarketInformation import UMMOtherMarketInformation

import time


def test_open_points_map(browser):
    """Проверка открытия карты с пунктами"""
    allure.dynamic.title(f'Открытие карты с пунктами и проверка наличия пунктов на карте')
    MainPage(browser).open_main_page()
    MainPage(browser).open_points_category()
    MainPage(browser).open_points_map()
    MainPage(browser).check_points_is_on_map()
    MainPage(browser).check_zones_not_on_map()


def test_open_points_advanced_search(browser):
    """Проверка открытия пункта Advanced search и наличия там таблицы с данными"""
    allure.dynamic.title(f'Открытие продвинутого поиска точек и проверка наличия элементов')
    MainPage(browser).open_main_page()
    MainPage(browser).open_points_category()
    MainPage(browser).open_points_advanced_search()
    PointsAdvancedSearch(browser).data_table_check()


def test_open_points_data(browser):
    """Проверка открытия пункта Data и проверка наличия там основных элементов"""
    allure.dynamic.title(f'Открытие страницы данных по пунктам и проверка наличия элементов')
    MainPage(browser).open_main_page()
    MainPage(browser).open_points_category()
    MainPage(browser).open_points_data()
    PointsData(browser).data_graph_check()
    PointsData(browser).data_side_panel_check()
    PointsData(browser).data_side_panel_chart_range_check()
    PointsData(browser).data_side_panel_indicators_check()


def test_open_zones_map(browser):
    """Проверка открытия карты с зонами"""
    allure.dynamic.title(f'Открытия карты с зонами и проверка наличия зон на карте')
    MainPage(browser).open_main_page()
    MainPage(browser).open_zones_category()
    MainPage(browser).open_zones_map()
    MainPage(browser).check_zones_is_on_map()
    MainPage(browser).check_points_not_on_map()


def test_open_zones_advanced_search(browser):
    """Проверка открытия пункта Advanced search и наличия таблицы с данными"""
    allure.dynamic.title(f'Открытие продвинутого поиска зон и проверка наличия элементов')
    MainPage(browser).open_main_page()
    MainPage(browser).open_zones_category()
    MainPage(browser).open_zones_advanced_search()
    ZonesAdvancedSearch(browser).data_table_check()


def test_open_zones_data(browser):
    """Проверка открытия пункта Data и проверка наличия основных элементов"""
    allure.dynamic.title(f'Открытие данных по зонам и проверка наличия элементов')
    MainPage(browser).open_main_page()
    MainPage(browser).open_zones_category()
    MainPage(browser).open_zones_data()
    ZonesData(browser).data_graph_check()
    ZonesData(browser).data_side_panel_check()
    ZonesData(browser).data_side_panel_chart_range_check()
    ZonesData(browser).data_side_panel_indicators_check()


def test_open_operators(browser):
    """Проверка открытия пункта Operators и наличия таблицы с данными по операторам"""
    allure.dynamic.title(f'Открытие пункта операторы и проверка наличия элементов')
    MainPage(browser).open_main_page()
    MainPage(browser).open_operators()
    Operators(browser).operators_filter_sort_check()
    Operators(browser).operators_table_check()


def test_open_calendar_calendar_view(browser):
    """Проверка открытия пункта Calendar>Calendar view и проверка наличия основных элементов"""
    allure.dynamic.title(f'Открытие календаря и проверка наличия элементов')
    MainPage(browser).open_main_page()
    MainPage(browser).open_calendar_category()
    MainPage(browser).open_calendar_calendar_view()
    CalendarView(browser).calendar_check()
    CalendarView(browser).calendar_option_check()


def test_open_calendar_interruptions(browser):
    """Проверка открытия пункта Calendar>Planned/Unplanned Interruptions и проверка наличия основных элементов"""
    allure.dynamic.title(f'Открытие пункта по прерываниям и проверка наличия элементов')
    MainPage(browser).open_main_page()
    MainPage(browser).open_calendar_category()
    MainPage(browser).open_calendar_actual_unplanned_interruptions()
    PUInterruptions(browser).table_check()
    PUInterruptions(browser).option_check()


def test_open_umm_unavailabilities(browser):
    """Проверка открытия пункта UMM>Unavailabilities of gas facilities и проверка наличия основных элементов"""
    allure.dynamic.title(f'Открытие пункта по недоступным мощностям и проверка наличия элементов')
    MainPage(browser).open_main_page()
    MainPage(browser).open_umm_category()
    MainPage(browser).open_umm_unavailabilities()
    UMMUnavailabilities(browser).navbar_check()
    UMMUnavailabilities(browser).calendar_check()
    UMMUnavailabilities(browser).sidebar_check()


def test_umm_other_market_information(browser):
    """Проверка открытия пункта UMM>Other Market Information и проверка наличия основных элементов"""
    allure.dynamic.title(f'Открытие пункта по прочей рыночной информации и проверка наличия элементов')
    MainPage(browser).open_main_page()
    MainPage(browser).open_umm_category()
    MainPage(browser).open_umm_other_market_info()
    UMMOtherMarketInformation(browser).navbar_check()
    UMMOtherMarketInformation(browser).table_check()
    UMMOtherMarketInformation(browser).sidebar_check()


@pytest.mark.parametrize("point", [int(uniform(0, 99)) for x in range(3)])
def test_point_search_from_main_page(browser, connection_points_sample_data, point):
    point_name = connection_points_sample_data[point]['pointLabel']
    allure.dynamic.title(f'Открытие таблицы данных по пункту: {point_name}')
    MainPage(browser).enter_object_name(point_name)
    MainPage(browser).open_found_points_dropdown()
    MainPage(browser).access_first_point_data_page()
    PointsData(browser).navbar_check()
    PointsData(browser).data_graph_check()
    PointsData(browser).data_side_panel_check()
    PointsData(browser).data_side_panel_chart_range_check()
    PointsData(browser).data_side_panel_indicators_check()

