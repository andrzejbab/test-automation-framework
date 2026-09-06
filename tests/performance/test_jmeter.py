import os
import shutil
import subprocess
import xml.etree.ElementTree as ET
import pytest

@pytest.mark.smoke
def test_jmeter_run_and_parse():
    jmeter_path = "C:\\D\\apache-jmeter-5.6.3\\apache-jmeter-5.6.3\\bin\\jmeter.bat"  # Update this path
    jmx_path = "./tests/performance/user_management.jmx"             # Update this path
    result_file = "./tests/performance/results.jtl"            # Update this path
    report_path = "./tests/performance/report"               # Update this path

    # Clean up the report directory before running the test
    if os.path.exists(report_path):
        shutil.rmtree(report_path)
    os.makedirs(report_path, exist_ok=True)
    # Remove jtl file if it exists
    if os.path.exists(result_file):
        os.remove(result_file)

    # Run JMeter
    cmd = [jmeter_path, "-n", "-t", jmx_path, "-l", result_file, "-e", "-o", report_path,
           "-Jserver_name=localhost", "-Jport_nr=8000"]
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        encoding="utf-8",  # Explicitly set encoding
        errors="replace"   # Replace undecodable characters
    )
    assert result.returncode == 0, f"JMeter failed: {result.stderr}"

