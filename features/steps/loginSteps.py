from time import sleep

from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from Configs.configurations import TestData
from Pages.LoginPage import LoginPage


@given(u'go to page')
def step_impl(context):

    context.driver = webdriver.Chrome(executable_path="chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    context.driver = webdriver.Chrome(chrome_options=options)
    url = TestData.BASE_URL
    context.driver.get(url)


@when(u'click giris yap')
def step_impl(context):
    LoginPage.do_click(context,LoginPage.GIRIS_YAP_BTTN)

@when(u'click facebook ile')
def fb_ile(context):
    sleep(2)
    parent_h = context.driver.current_window_handle
    print(context.driver.title)
    LoginPage.do_click(context, LoginPage.FB_ILE_GIRIS)
    sleep(3)
    handles = context.driver.window_handles[1]
    context.driver.switch_to_window(handles)
    context.driver.implicitly_wait(5)
    print(context.driver.title)
    LoginPage.do_send_keys(context, LoginPage.FB_EMAIL,"shenolbulut@gmail.com")
    LoginPage.do_send_keys(context, LoginPage.FB_PASSWORD, "kloiaN11")
    LoginPage.do_send_keys(context, LoginPage.FB_PASSWORD, Keys.ENTER)
    context.driver.switch_to_window(parent_h)

@then(u'verify the home page')
def verify(context):
    sleep(2)
    context.driver.find_element_by_id("acceptContract").click()
    context.driver.find_element_by_id("confirmBtn").click()
    sleep(2)
    assert context.driver.title == "n11.com - Hayat Sana Gelir"


