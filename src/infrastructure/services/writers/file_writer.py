# infrastructure/writers/file_writer.py

from pathlib import Path

class FileWriter:
    @staticmethod
    def write_text(path: Path, text: str) -> None:
        path.write_text(text, encoding="utf-8")
