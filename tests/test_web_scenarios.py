from page_objects.MainPage import MainPage
from page_objects.PointsAdvancedSearch import PointsAdvancedSearch
from page_objects.PointsData import PointsData
from page_objects.ZonesAdvancedSearch import ZonesAdvancedSearch
from page_objects.ZonesData import ZonesData
from page_objects.Operators import Operators
from page_objects.CalendarView import CalendarView
from page_objects.PUInterruptions import PUInterruptions
import allure


def test_open_points_map(browser):
    """Проверка открытия карты с пунктами"""
    allure.dynamic.title(f'Opening points map and checking points elements on the map')
    MainPage(browser).open_main_page()
    MainPage(browser).open_points_category()
    MainPage(browser).open_points_map()


def test_open_points_advanced_search(browser):
    """Проверка открытия пункта Advanced search и наличия там таблицы с данными"""
    allure.dynamic.title(f'Opening points advanced search and checking data table presence')
    MainPage(browser).open_main_page()
    MainPage(browser).open_points_category()
    MainPage(browser).open_points_advanced_search()
    PointsAdvancedSearch(browser).data_table_check()


def test_open_points_data(browser):
    """Проверка открытия пункта Data и проверка наличия там основных элементов"""
    allure.dynamic.title(f'Opening points data and checking elements presence')
    MainPage(browser).open_main_page()
    MainPage(browser).open_points_category()
    MainPage(browser).open_points_data()
    PointsData(browser).data_graph_check()
    PointsData(browser).data_side_panel_check()
    PointsData(browser).data_side_panel_chart_range_check()
    PointsData(browser).data_side_panel_indicators_check()


def test_open_zones_map(browser):
    """Проверка открытия карты с пунктами"""
    allure.dynamic.title(f'Opening points map and checking points elements on the map')
    MainPage(browser).open_main_page()
    MainPage(browser).open_zones_category()
    MainPage(browser).open_zones_map()


def test_open_zones_advanced_search(browser):
    """Проверка открытия пункта Advanced search и наличия таблицы с данными"""
    allure.dynamic.title(f'Opening points advanced search and checking data table presence')
    MainPage(browser).open_main_page()
    MainPage(browser).open_zones_category()
    MainPage(browser).open_zones_advanced_search()
    ZonesAdvancedSearch(browser).data_table_check()


def test_open_zones_data(browser):
    """Проверка открытия пункта Data и проверка наличия основных элементов"""
    allure.dynamic.title(f'Opening points data and checking elements presence')
    MainPage(browser).open_main_page()
    MainPage(browser).open_zones_category()
    MainPage(browser).open_zones_data()
    ZonesData(browser).data_graph_check()
    ZonesData(browser).data_side_panel_check()
    ZonesData(browser).data_side_panel_chart_range_check()
    ZonesData(browser).data_side_panel_indicators_check()


def test_open_operators(browser):
    """Проверка открытия пункта Operators и наличия таблицы с данными по операторам"""
    allure.dynamic.title(f'Opening operators and checking data table presence')
    MainPage(browser).open_main_page()
    MainPage(browser).open_operators()
    Operators(browser).operators_table_check()


def test_open_calendar_view(browser):
    """Проверка открытия пункта Calendar>Calendar view и проверка наличия основных элементов"""
    allure.dynamic.title(f'Opening calendar data and checking elements presence')
    MainPage(browser).open_main_page()
    MainPage(browser).open_calendar_category()
    MainPage(browser).open_calendar_calendar_view()
    CalendarView(browser).calendar_check()
    CalendarView(browser).calendar_option_check()


def test_open_interruptions(browser):
    """Проверка открытия пункта Calendar>Planned/Unplanned Interruptions и проверка наличия основных элементов"""
    allure.dynamic.title(f'Opening Planned/Unplanned Interruptions and checking elements presence')
    MainPage(browser).open_main_page()
    MainPage(browser).open_calendar_category()
    MainPage(browser).open_calendar_actual_unplanned_interruptions()
    PUInterruptions(browser).table_check()
    PUInterruptions(browser).option_check()
