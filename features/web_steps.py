from behave import when

@when('I press "{button_text}"')
def step_press_button(context, button_text):
    # Your code here, for example simulate button click in tests
    print(f"Button pressed: {button_text}")
