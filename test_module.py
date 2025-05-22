import pytest
from time import sleep
from selene import browser, have
import os
import allure
from utils.attach import *

@allure.title("Successfull fill form")
def test_fill_form():
    browser.open('/automation-practice-form')

    with allure.step("Open registrations form"):
        browser.open("https://demoqa.com/automation-practice-form")
        browser.element(".practice-form-wrapper").should(have.text("Student Registration Form"))
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")
    with allure.step("Fill form"):
#паспортные данные
        browser.element('#firstName').type('Diana')
        browser.element('#lastName').type('Ermilova')
        browser.all('[for^=gender-radio]').element_by(have.text('Other')).click()
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker').element('[class$="month-select"]').click()
        browser.element('.react-datepicker').element('[class$="month-select"]').all('option').element_by(have.text('September')).click()
        browser.element('.react-datepicker').element('[class$="year-select"]').click()
        browser.element('.react-datepicker').element('[class$="year-select"]').all('option').element_by(have.text('1996')).click()
        browser.element('.react-datepicker').element('[class*="day--018"]').click()
    #контактные данные
        browser.element('#userEmail').type('testmail@gmail.com')
        browser.element('#userNumber').type('8800123121')
        #sleep(200)
    #интересы
        browser.element('#subjectsInput').type('Physics').press_enter()
        browser.element('[for=hobbies-checkbox-1]').click()
        #browser.element('[for=hobbies-checkbox-2]').click()
        #browser.element('[for=hobbies-checkbox-3]').click()
    #аватар
        browser.element('#uploadPicture').send_keys(os.path.abspath('pigeon.jpg'))

    #адрес
        browser.element('#currentAddress').type('London, county of Surrey, Privet Drive 4')
        browser.element('#state').click()
        browser.all('[id^="react-select-3-option"]').element_by(have.exact_text('Haryana')).click()
        browser.element('#city').click()
        browser.all('[id^="react-select-4-option"]').element_by(have.exact_text('Panipat')).click()

    #отправка
    with allure.step("Submit"):
        browser.element('#submit').click()



    with allure.step("Check results"):
        browser.element('.modal-content').should(have.text('Thanks for submitting the form'))
    #проверка заполнения формы
        browser.element('.modal-content table').all('td:nth-child(2)').should(
            have.exact_texts(
                'Diana Ermilova',
                'testmail@gmail.com',
                'Other',
                '8800123121',
                '18 September,1996',
                '_Physics',
                'Sports',
                'pigeon.jpg',
                'London, county of Surrey, Privet Drive 4',
                'Haryana Panipat',
            )
        )


    add_screenshot(browser)
    add_logs(browser)
    add_html(browser)
    add_video(browser)