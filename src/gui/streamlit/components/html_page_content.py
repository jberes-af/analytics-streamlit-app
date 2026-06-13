# /src/gui/streamlit/components/html_page_content.py

from pathlib import Path

import streamlit as st

STATIC_DIR = Path(__file__).resolve().parents[1] / "static"
CSS_PATH = STATIC_DIR / "html_content.css"


def _load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _build_html_document(css: str, html_content: str) -> str:
    return f"""
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <style>
        {css}
    </style>
</head>
<body>
    {html_content}
</body>
</html>
"""


def render_html_page(
        html_content: str,
) -> None:
    css = _load_text(CSS_PATH)

    html = _build_html_document(
        css=css,
        html_content=html_content,
    )

    st.html(html)


"""
def render_html_page(
    html_content: str,
    *,
    height: int = 1100,
    scrolling: bool = True,
) -> None:
    css = _load_text(CSS_PATH)
    html = _build_html_document(css, html_content)

    components.html(html, height=height, scrolling=scrolling)
"""
