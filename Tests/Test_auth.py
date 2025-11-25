import  pytest
import time
from selenium.common.exceptions import TimeoutException
from pages.auth_page import AuthPage

def test_auth_chrome(driver_chrome):
    driver_chrome.get("https://my.proweb.uz/log-in?q=/home")
    auth_page = AuthPage(driver_chrome)
    auth_page.input_number("998998548681")
    auth_page.click_btn_next()
    auth_page.input_password("FamaTester")
    auth_page.click_btn_submit()
    auth_page.click_btn_sessions()
    auth_page.click_btn_finish()


def test_auth_Edge(driver_Edge):
    driver_Edge.get("https://my.proweb.uz/log-in?q=/home")
    auth_page = AuthPage(driver_Edge)
    auth_page.input_number("998998548681")
    auth_page.click_btn_next()
    auth_page.input_password("FamaTester")
    auth_page.click_btn_submit()
    auth_page.click_btn_sessions()
    auth_page.click_btn_finish()


def test_auth_firefox(driver_firefox):
    driver_firefox.get("https://my.proweb.uz/log-in?q=/home")
    auth_page = AuthPage(driver_firefox)
    auth_page.input_number("998998548681")
    auth_page.click_btn_next()
    auth_page.input_password("FamaTester")
    auth_page.click_btn_submit()
    auth_page.click_btn_sessions()
    auth_page.click_btn_finish()
