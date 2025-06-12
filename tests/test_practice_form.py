from demoqa_tests.model.pages.registration_page import RegistrationPage
from selene import have

def test_practice_form_filling():
    registration_page = RegistrationPage()
    registration_page.open()
    # Заполняем поля
    registration_page.fill_first_name('Андрей')
    registration_page.fill_last_name('Смирнов')
    registration_page.fill_email('name123@example.com')
    registration_page.choose_gender('Male')
    registration_page.fill_phone_number('1234567891')
    registration_page.fill_birthday('1990','April','20')
    registration_page.fill_subjects('Computer Science')
    registration_page.fill_hobbies('Sports')
    registration_page.fill_picture('beautiful_tropical_beach_sea_ocean.png')
    registration_page.fill_address('Street, 15 house')
    registration_page.fill_state('Haryana')
    registration_page.fill_city('Karnal')

    #Подтверждаем заполнение данных
    registration_page.submit()

    #Проверка после нажатия на кнопку submit
    registration_page.should_open_form_with_text('Thanks for submitting the form')
    registration_page.registered_user_with.should(
        have.texts(
        'Андрей Смирнов',
        'name123@example.com',
        'Male',
        '1234567891',
        '20 April,1990',
        'Computer Science',
        'Sports',
        'beautiful_tropical_beach_sea_ocean.png',
        'Street, 15 house',
        'Haryana Karnal'
    )
    )
