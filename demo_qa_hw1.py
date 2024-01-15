from selene import browser, be, have
import time


# browser.open('https://google.com')
# browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
# browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_selene():
    browser.open('https://demoqa.com/text-box')
    browser.element('[type="text"]').should(be.blank).type("Danil Reznikov")
    browser.element('[type="email"]').should(be.blank).type("test1@mail.ru")
    browser.element('#currentAddress').should(be.blank).type("Hello world")
    browser.element('[id="permanentAddress"]').should(be.blank).type(":)")
    browser.element('[id="submit"]').click()
