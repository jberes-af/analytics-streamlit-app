# /utils/convert_png_to_text.py

"""
Convert PNG image to text file (base64)
"""

from functools import lru_cache
from pathlib import Path
import base64


@lru_cache(maxsize=128)
def image_to_data_uri(image_path: str | Path) -> str:
    path = Path(image_path)
    suffix = image_path.suffix.lower().replace(".", "")

    mime_type = {
        "png": "image/png",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "svg": "image/svg+xml",
    }.get(suffix)

    if mime_type is None:
        raise ValueError(f"Unsupported image type: {path}")

    # encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    encoded = base64.b64encode(path.read_bytes()).decode("utf-8")

    return f"data:{mime_type};base64,{encoded}"
