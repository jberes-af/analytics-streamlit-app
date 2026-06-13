# /src/gui/streamlit/components/diagram_config.py

from typing import Any

from pathlib import Path
from src.domain.mobile_app_types import ScreenSpec


STATIC_DIR = Path(__file__).resolve().parents[1] / "static"
IMAGES_DIR = STATIC_DIR / "assets" / "images"
CSS_PATH = STATIC_DIR / "flow_diagram.css"
# JS_PATH = STATIC_DIR / "flow_diagram.js"
JS_PATH = STATIC_DIR / "flow_diagram.bundle.js"


PatientFlowNode = dict[str, Any]
PatientFlowNodes = dict[str, PatientFlowNode | ScreenSpec]
