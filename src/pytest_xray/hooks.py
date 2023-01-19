from typing import Any, Dict

import pytest


@pytest.hookspec
def pytest_xray_results(results: Dict[str, Any], session: pytest.Session) -> None:
    """
    Called before uploading XRAY result to Jira server.

    :param results: xray results dictionary
    :param session: pytest session
    """
    
@pytest.hookspec   
def pytest_logfest_log_file_name_basic(filename_components):
    """Called after filling the array of filename components for the basic log file"""
