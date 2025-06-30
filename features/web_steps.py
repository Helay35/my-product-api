from behave import then

@then('I should see "{message}" on the page')
def step_impl(context, message):
    page_source = context.browser.page_source
    assert message in page_source, f'Error: Did not find "{message}" on the page but it should be present.'
