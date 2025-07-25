class LoginTestData:

    url = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"


#example for usage

import random, json, os
from datetime import datetime

class TestData:
    currentDateTime = datetime.now().strftime("%d_%m_%Y_%H%M%S")
    randomNo = str(random.randint(1, 9999))

    product_name = ""
    environment = ""
    browser = ""
    update_devops = False
    modules = []

    #  changed as discussed with divyesh sir
    def get_run_details_from_testinfo():
        """Parse the JSON file to get the run details."""
        ROOT_LOCATION = os.getenv('TEST_INFO_LOCATION')
        if ROOT_LOCATION is None:
            ROOT_LOCATION = os.getcwd()
            
        jsonFilePath = ROOT_LOCATION + "\\TestInfo.json"
        with open(jsonFilePath, 'r') as file:
            data = json.load(file)
        TestData.product_name = data['ProductName']
        TestData.environment = data['Environment']
        TestData.browser = data['Browser']
        TestData.update_devops = data['UpdateDevOps']
        
        for module in data['Modules']:
            module_name = module['ModuleName']
            test_cases = module['TestCases']
            TestData.modules.append({
                'ModuleName': module_name,
                'TestCases': test_cases
            })
 
    



