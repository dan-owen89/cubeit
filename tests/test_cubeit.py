import pytest
from models.actions import CubeIt
from playwright.sync_api import Page, expect

# BASE_URL = "http://localhost:8000"  # Replace with the actual URL where your app is running
input_number = 33
expected_result = input_number ** 3
expected_string = str(expected_result)
error_string = "Please enter a number!"


def test_cube(page: Page):

    calculate = CubeIt(page)

    calculate.enter_number(str(input_number))

    calculate.calculate()

    calculate.verify_result(expected_string)


    # # Navigate to the application
    # page.goto(BASE_URL)
    
    # # Find the input field and fill it with the number
    # input_field = page.locator("id=numberInput")
    # input_field.fill(str(input_number))
    
    # # Find and click the calculate button
    # calculate_button = page.locator("id=calculateButton")
    # calculate_button.click()
    
    # # Check that the result is displayed
    # result = page.locator("div#result")
    # expect(result).to_be_visible()
    
    # # Verify the correct cube value is displayed
    # expect(result).to_have_text(f"The cube of {str(input_number)} is {expected_string}.")



def test_no_number_entered(page: Page):
    calculate = CubeIt(page)

    calculate.calculate()

    calculate.verify_result(error_string)






#     page.goto(BASE_URL)

#     # Find and click the calculate button
#     calculate_button = page.locator("id=calculateButton")
#     calculate_button.click()

#     # Check that the result is displayed
#     warning = page.locator("div#result")
#     expect(warning).to_be_visible()


#     # Confirm warning that number is required
#     # Verify the correct cube value is displayed
#     expect(warning).to_have_text("Please enter a number!")
