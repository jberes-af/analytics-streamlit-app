# /src/gui/streamlit/routing/routes.py

from src.gui.streamlit.routing.route_types import RouteHandler

from src.gui.streamlit.screens.main_page import render_main_page


NAVIGATION: dict[str, dict[str, RouteHandler]] = {
    "Overview": {
       "Mobile App Overview": render_main_page,
    },
}
