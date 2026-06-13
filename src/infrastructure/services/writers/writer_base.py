# infrastructure/writers/writer_base.py

from pathlib import Path
from typing import Any, Callable

WriteFn = Callable[[Any], None]

def write_stdout(output: Any) -> None:
    if output is None:
        return
    print(output)


def write_noop(_output: Any) -> None:
    return


def make_text_file_writer(path: Path) -> WriteFn:
    def _write(output: Any) -> None:
        if output is None:
            return
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(str(output), encoding="utf-8")
    return _write