from typing import Callable, Optional, List
import pytest
from utils import ProcessResult


@pytest.fixture(scope="class")
def class_fixture():
    print("\n[CLASS SETUP]")
    yield
    print("\n[CLASS TEARDOWN]")

@pytest.fixture(scope="function")
def function_fixture():
    print(f"\n[TEST SETUP]")
    yield
    print("\n[TEST TEARDOWN]")


TEST_IO_PAIRS = [
    ("01_input.txt", "01_output.txt"),
    ("02_input.txt", "02_output.txt"),
    ("03_input.txt", "03_output.txt"),
]


RunnerType = Callable[..., ProcessResult]

@pytest.mark.usefixtures("class_fixture", "function_fixture")
class TestExample:
    run_binary: RunnerType

    def test_1(self):
        result = self.run_binary("code1.wren", args=["--verbose"])
        assert result.return_code == 0

    @pytest.mark.parametrize("test_input, test_output", TEST_IO_PAIRS)
    def test_parametrized_2(self, test_input, test_output):
        print(f"Running test with input {test_input} and output {test_output}")
        assert True == True