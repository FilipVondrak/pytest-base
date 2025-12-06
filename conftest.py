import pytest

def perform_setup():
    print("\n[Setup] Preparing test environment...")
    return

def perform_teardown():
    print("\n[Teardown] Cleaning up...")
    return

# global setup and teardown for all tests
@pytest.fixture(scope="session", autouse=True)
def global_setup_teardown():
    perform_setup()
    yield  # waits for all tests to finish
    perform_teardown()