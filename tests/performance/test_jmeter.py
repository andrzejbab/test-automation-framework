import os
import shutil
import subprocess
import xml.etree.ElementTree as ET
import pytest
import allure

@pytest.mark.load
@allure.epic(("API Authentication & Onboarding"))
@allure.feature("User management")
@allure.story("The application should be able to handle a high volume of concurrent users in a short period of time.")
class TestLoad:

    def test_jmeter_run_and_parse(self, setup_jmeter):

        test_jmx_path = "./tests/performance/user_management.jmx" 

        # Run JMeter
        cmd = [setup_jmeter.get("jmeter_path"), "-n", "-t", test_jmx_path, "-l", 
               setup_jmeter.get("result_file"), "-e", "-o",setup_jmeter.get("report_path"),
            "-Jserver_name=localhost", "-Jport_nr=8000"]
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding="utf-8",  # Explicitly set encoding
            errors="replace"   # Replace undecodable characters
        )
        assert result.returncode == 0, f"JMeter failed: {result.stderr}"

