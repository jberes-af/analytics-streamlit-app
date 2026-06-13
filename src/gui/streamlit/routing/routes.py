# /src/gui/streamlit/routing/routes.py

from src.gui.streamlit.routing.route_types import RouteHandler

from src.gui.streamlit.screens.main_page import render_main_page

from src.gui.streamlit.screens.shared.home_flow import render_home_flow_screen

from src.gui.streamlit.screens.sensing.sensing_root_flow import render_sensing_root_flow_screen
from src.gui.streamlit.screens.sensing.sensing_dashboard_flow import render_sensing_dashboard_flow_screen
from src.gui.streamlit.screens.sensing.sensor_record_flow import render_sensing_record_flow_screen


from src.gui.streamlit.screens.care.care_flow import render_care_flow_screen
from src.gui.streamlit.screens.shared.more_flow import render_more_flow_screen

from src.gui.streamlit.screens.shared.account_flow import render_account_flow_screen
from src.gui.streamlit.screens.shared.setup_flow import render_setup_flow_screen

from src.gui.streamlit.screens.care.adl_resident_flow import render_adl_resident_flow_screen
from src.gui.streamlit.screens.care.therapeutic_plan_flow import render_therapeutic_plan_flow_screen
from src.gui.streamlit.screens.care.priority_item_flow import render_priority_item_flow_screen


NAVIGATION: dict[str, dict[str, RouteHandler]] = {
    "Overview": {
       "Mobile App Overview": render_main_page,
    },

}
