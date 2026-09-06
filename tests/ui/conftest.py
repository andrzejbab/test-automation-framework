import pytest
import allure
from allure_commons.types import AttachmentType

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()

    # Check if the test failed during the execution ("call") phase
    if report.when == "call" and report.failed:
        
        # Access the 'driver' fixture from the test's arguments
        # Note: This assumes your WebDriver fixture is named 'driver'
        if "driver" in item.funcargs:
            driver = item.funcargs["driver"]
            
            try:
                # 1. Attach the Visual Screenshot
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name=f"Screenshot on Failure: {item.name}",
                    attachment_type=AttachmentType.PNG
                )
                
                # 2. Attach the HTML DOM Source (Industry standard pro-tip!)
                allure.attach(
                    driver.page_source,
                    name="HTML DOM state at failure",
                    attachment_type=AttachmentType.HTML
                )
            except Exception as e:
                print(f"Failed to capture evidence for Allure: {e}")