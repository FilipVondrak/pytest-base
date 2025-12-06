import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

@dataclass
class ProcessResult:
    return_code: int
    stdout:      str
    stderr:      str

def run_binary(binary_path: Path, input_file: str, args: Optional[List[str]] = None) -> ProcessResult:
    """Run a binary with specified arguments and capture its output."""

    # if no arguments are provided, use an empty list
    if args is None:
        args = []

    # assemble the command
    command = [str(binary_path)] + args

    # runs the binary like this: ./binary_path <args> < input_file
    try:
        with open(input_file, 'r') as f:
            result = subprocess.run(
                command,
                stdin=f,
                capture_output=True,
                text=True,
                check=False
            )
        return ProcessResult(
            return_code=result.returncode,
            stdout=result.stdout,
            stderr=result.stderr
        )
    except Exception as e:
        return ProcessResult(
            return_code=-1,
            stdout="",
            stderr=f"Execution failed: {str(e)}"
        )