# Apache License
# Version 2.0, January 2004
# http://www.apache.org/licenses/

# Copyright 2025 emanoyhl and emanoyhl.net find me at github.com/emanoyhl 
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import requests

class APISecurityTester:
    def __init__(self, base_url):
        self.base_url = base_url

    def test_authentication(self):
        print("Testing Authentication Flaws:")
        # Check for missing authentication
        response = requests.get(self.base_url + "/protected-endpoint")
        if response.status_code == 200:
            print("Warning: Unauthenticated access to a protected endpoint.")
        else:
            print("Authentication is enforced on protected endpoints.")

    def test_data_exposure(self):
        print("\nTesting for Data Exposure:")
        response = requests.get(self.base_url + "/api/data")
        if 'sensitive_info' in response.text:
            print("Warning: Sensitive information exposed in API response.")
        else:
            print("No sensitive information found in API response.")

    def test_sql_injection(self):
        print("\nTesting for SQL Injection:")
        payload = {"username": "' OR '1'='1", "password": "dummy"}
        response = requests.post(self.base_url + "/login", data=payload)
        if "Welcome" in response.text:
            print("Warning: SQL Injection vulnerability detected.")
        else:
            print("No SQL Injection vulnerability detected.")

    def run_tests(self):
        self.test_authentication()
        self.test_data_exposure()
        self.test_sql_injection()

if __name__ == "__main__":
    base_url = input("Enter the API base URL: ") # Ensure you have permission to test the API as unauthorized testing can be illegal
    tester = APISecurityTester(base_url)
    tester.run_tests()
