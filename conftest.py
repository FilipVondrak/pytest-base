import pytest
import sys
from pathlib import Path
from utils import run_binary as raw_run_binary
from typing import Callable, List, Optional

TEST_ROOT = Path(__file__).parent.resolve()


@pytest.fixture(scope="session")
def binary_path():
    """
    Finds a path to the binary and verifies that it exists
    """

    # binary path relative to this file
    bin_rel_path = "../../src/binary"

    bin_path = (TEST_ROOT / bin_rel_path).resolve()

    # Windows fallback - add .exe suffix
    if sys.platform == "win32" and not bin_path.suffix:
        bin_path = bin_path.with_suffix(".exe")

    if not bin_path.exists():
        pytest.fail(f"CRITICAL: Executable not found at: {bin_path}")

    return bin_path


BinaryRunner = Callable[[str, Optional[List[str]]], 'ProcessResult']


@pytest.fixture(scope="session")
def run_binary(binary_path) -> BinaryRunner:
    """
    Returns a function (callable) which runs the compiler binary directly
    """

    def _wrapper(input_file: str, args: Optional[List[str]] = None):
        # convert relative paths to absolute paths
        input_path = Path(input_file)
        if not input_path.is_absolute():
            input_file = str((TEST_ROOT / input_file).resolve())
        # return the raw run_binary function
        return raw_run_binary(binary_path, input_file, args)

    return _wrapper


@pytest.fixture(scope="class", autouse=True)
def _inject_runner_globally(request, run_binary):
    if request.cls:
        # adds the run_binary function to every class as a static method
        request.cls.run_binary = staticmethod(run_binary)


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