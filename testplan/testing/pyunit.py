"""PyUnit test runner."""

from testplan.testing import base as testing
from testplan.report import testing as report_testing
from testplan.common import config
from testplan.testing.multitest.entries import assertions
from testplan.testing.multitest.entries import schemas

import unittest


class PyUnitConfig(testing.TestConfig):
    """
    Configuration object for :py:class`~testplan.testing.pyunit.PyUnit` test
    runner.
    """

    @classmethod
    def get_options(cls):
        return {
            config.ConfigOption('suite'): unittest.suite.TestSuite
        }


class PyUnit(testing.Test):
    """Test runner for PyUnit unit tests."""

    CONFIG = PyUnitConfig

    def __init__(self, **options):
        super(PyUnit, self).__init__(**options)
        self._suite_report = report_testing.TestGroupReport(
            name=self.cfg.name,
            category='suite')

    def main_batch_steps(self):
        """Specify the test steps: run the tests, then log the results."""
        self._add_step(self.run_tests)
        self._add_step(self.log_test_results)

    def run_tests(self):
        """Run PyUnit and wait for it to terminate."""
        suite_result = unittest.TestResult()
        self.cfg.suite.run(suite_result)

        for call, error in suite_result.errors:
            testcase_report = report_testing.TestCaseReport(name=str(call))
            assertion_obj = assertions.RawAssertion(
                description=str(call),
                content=str(error).strip(),
                passed=False)
            testcase_report.append(
                schemas.base.registry.serialize(assertion_obj))
            self.result.report.entries.append(testcase_report)

        for call, error in suite_result.failures:
            testcase_report = report_testing.TestCaseReport(name=str(call))
            assertion_obj = assertions.RawAssertion(
                description=str(call),
                content=str(error).strip(),
                passed=False)
            testcase_report.append(
                schemas.base.registry.serialize(assertion_obj))
            self.result.report.entries.append(testcase_report)

    def get_test_context(self):
        """TODO find out if we can inspect suites/testcases."""
        return []
