First, you need a WebDriver for your browser of choice:

Chrome: https://chromedriver.chromium.org/

Firefox: https://github.com/mozilla/geckodriver

Edge: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

Opera: https://github.com/operasoftware/operachromiumdriver

Safari: https://developer.apple.com/documentation/webkit/testing_with_webdriver_in_safari

(Make sure that the selected WebDriver version matches your current browser version)

The path to the webdriver must be in your PATH.


Then, install all dependencies with pip:

pip install -r requirements.txt

A test for a specific web page can then be executed with the following command:

python accessibility_tester.py [OPTIONS] WEBPAGE
For help, run:

python accessibility_tester.py --help
The required accessibility level is a value between 0 and 1. It is compared with the actual accessibility level that is achieved in the test, which is calculated by dividing the successful checks through the total number of executed checks. If the achieved accessibility level is equal to or higher than the required accessibility level, the program will return an exit code of 0, otherwise an exit code of 1 will be returned.
