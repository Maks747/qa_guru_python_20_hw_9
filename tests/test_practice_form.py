from selene import browser, command, have
import os

def test_practice_form_filling():
    browser.open('/automation-practice-form')
    # Заполняем поля
    browser.element('#firstName').type('Андрей')
    browser.element('#lastName').type('Смирнов')
    browser.element('#userEmail').type('name123@example.com')
    browser.element(f"//label[contains(text(),'Male')]").click()
    browser.element('#userNumber').type('1234567891')
    browser.element('#dateOfBirthInput').click()
    browser.element(".react-datepicker__year-select").type('1990').click()
    browser.element(".react-datepicker__month-select").element('[value="3"]').click()
    browser.element(".react-datepicker__day--020").click()
    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.element(f"//label[contains(text(),'Sports')]").click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('beautiful_tropical_beach_sea_ocean.png'))
    browser.element('#currentAddress').perform(command.js.scroll_into_view).type('Street, 15 house')
    browser.element('#state').click().element('#react-select-3-option-2').click()
    browser.element('#city').click().element('#react-select-4-option-0').click()

    #Подтверждаем заполнение данных
    browser.element('#submit').perform(command.js.scroll_into_view).click()

    #Проверка после нажатия на кнопку submit
    browser.element('.table-responsive').all('td').even.should(have.exact_texts
    (f'Андрей Смирнов', 'name123@example.com', 'Male', '1234567891', '20 April,1990', 'Computer Science', 'Sports',
     'beautiful_tropical_beach_sea_ocean.png', 'Street, 15 house', 'Haryana Karnal'))