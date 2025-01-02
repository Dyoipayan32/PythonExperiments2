import datetime
import time

import pytest
import sqlite3

import pytest_html


def pytest_addoption(parser):
    parser.addoption(
        "--stringinput",
        action="append",
        default=[],
        help="list of stringinputs to pass to test functions",
    )


def pytest_generate_tests(metafunc):
    if "stringinput" in metafunc.fixturenames:
        metafunc.parametrize("stringinput", metafunc.config.getoption("stringinput"))


# Define a custom marker
def pytest_configure(config):
    config.addinivalue_line("markers", "custom_marker: marker for specific tests.")


# Hook to modify test collection results
def pytest_collection_finish(session):
    # Searching for tests with 'custom_marker'
    # marked_items = [
    #     item for item in session.items if item.get_closest_marker("custom_marker")
    # ]

    marked_items = [
        item for item in session.items
    ]

    # Print the names of the tests that have 'custom_marker'
    print("Tests ran:")
    for item in marked_items:
        print(f"- {item.name}")


def pytest_sessionstart(session):
    """Records the start time of the session."""
    session._starttime = time.time()
    session._endtime = None


# @pytest.hookimpl
def pytest_sessionfinish(session, exitstatus):
    """Generate a report at the end of the test session."""
    if hasattr(session, '_starttime'):
        session._endtime = time.time()
        duration = round(session._endtime - session._starttime, 3)
    else:
        duration = 'unknown'
    """Generate a report at the end of the test session."""
    summary = session.config.pluginmanager.get_plugin('terminalreporter').stats
    passed = len(summary.get('passed', []))
    failed = len(summary.get('failed', []))
    skipped = len(summary.get('skipped', []))
    total_tests = passed + failed + skipped

    report_content = (
        f"Test Run Summary:\n"
        f"Total tests executed: {total_tests}\n"
        f"Total tests passed: {passed}\n"
        f"Total tests failed: {failed}\n"
        f"Total tests skipped: {skipped}\n"
        f"Test run started at: {datetime.datetime.fromtimestamp(session._starttime)}\n"
        f"Test run finished at: {datetime.datetime.fromtimestamp(session._endtime)}\n"
        f"Total duration: {duration} seconds\n"
        f"Exit status: {exitstatus}\n"
    )

    with open('test_run_report.txt', 'w') as report_file:
        report_file.write(report_content)

    print("Test run report generated and saved to 'test_run_report.txt'.")


def pytest_html_report_title(report):
    report.title = "My very own title!"


def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend(["<p>\tBrief Prefix\t</p>"])
    summary.extend(["<p>\nRegression summary\n</p>"])
    postfix.extend(["<p>\tBrief Postfix\t</p>"])


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    report.extra = getattr(report, 'extra', [])
    if report.when == 'call' :
        if call.excinfo is not None and call.excinfo.type is pytest.TimeOutError:
            report.outcome = 'failed'
            report.longrepr = 'Test failed due to timeout'
            report.extra = getattr(report, 'extra', [])
            report.extra.append(pytest_html.extras.text('Test failed due to timeout'))
    # elif report.when == "call":
    #     # always add url to report
    #     extras.append(pytest_html.extras.url("http://www.example.com/", name='Added by Default'))
    #     xfail = hasattr(report, "wasxfail")
    #     if (report.skipped and xfail) or (report.failed and not xfail):
    #         # only add additional html on failure
    #         extras.append(pytest_html.extras.html("<div>Additional HTML"
    #                                               "<p> failed due to xyz reason !</p>"
    #                                               "</div>", name='Added by Default'))
    #         report.extras = extras


table_data = [(1, "books")]


@pytest.fixture(scope='session')
def connection():
    connection_str = sqlite3.connect('example.db')
    yield connection_str
    connection_str.close()


@pytest.fixture(scope='session')
def cursor(connection):
    yield connection.cursor()


@pytest.fixture(scope='function', params=table_data)
def table_cursor(request, cursor):
    print('table cursor fixture is executed')
    cursor.execute('drop table if exists items')
    cursor.execute('create table items (id int, name text)')
    cursor.execute(f'insert into items values {request.param}')
    cursor.connection.commit()
    yield cursor
    cursor.execute('drop table if exists items')
