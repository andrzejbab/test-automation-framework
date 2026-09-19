import pytest
import os
import shutil


@pytest.fixture(scope="session")
def setup_jmeter():
        jmeter_path = os.environ.get("JMETER_HOME")
        if jmeter_path:
            jmeter_path = os.path.join(jmeter_path, "bin", "jmeter")
        else:
            jmeter_path = shutil.which("jmeter")

        result_file = "./tests/performance/results.jtl"
        report_path = "./tests/performance/report"

        # Clean up the report directory before running the test
        if os.path.exists(report_path):
            shutil.rmtree(report_path)
        os.makedirs(report_path, exist_ok=True)
        # Remove jtl file if it exists
        if os.path.exists(result_file):
            os.remove(result_file)


        return {
             "jmeter_path": jmeter_path,
             "result_file": result_file,
             "report_path": report_path
        }