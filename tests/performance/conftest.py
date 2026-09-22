import pytest
import os
import shutil
from pathlib import Path


@pytest.fixture(scope="session")
def setup_jmeter():
        # set envs
        project_root = Path(__file__).resolve().parents[2]
        jmeter_home = project_root / "apache-jmeter-5.6.3"

        os.environ["DISPLAY"] = ":99"
        os.environ["JMETER_HOME"] = str(jmeter_home)
        os.environ["PATH"] = f"{jmeter_home / 'bin'}{os.pathsep}{os.environ.get('PATH', '')}"

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