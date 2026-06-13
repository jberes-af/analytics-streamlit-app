# /src/gui/streamlit/screens/overview.py

from src.gui.streamlit.components.html_page_content import render_html_page

import streamlit as st


def render_overview_html_screen() -> None:
    html_content: str = _get_overview_html()

    st.title("Mobile App Navigation Overview")

    render_html_page(
        html_content=html_content,
    )


def _get_overview_html() -> str:
    return f"""

    <div class="app-map">

        <h3>Summary</h3>
        
            <ul>
                <li>Four primary footer navigation tabs: `Home`, `Sensing`, `Care`, and `More`.</li>
        
                <li>
                    <strong>Home</strong>:
                    operational awareness and quick info scan;
                    includes resident summaries, device / sensing summaries,
                    and latest notifications.
                </li>
        
                <li>
                    <strong>Sensing</strong>:
                    device or 'sensing environment' focus;
                    includes latest sensor status, timelines, trends,
                    movement patterns, 
                    routines, and notification history.
                </li>
        
                <li>
                    <strong>Care</strong>:
                    resident-focused care workflows;
                    includes resident dashboards, ADLs,
                    notes, 
                    and device-to-ADL interpretation.
                </li>
        
                <li>
                    <strong>More</strong>:
                    administration (account management) and configuration 
                    (sensors, residents,
                    groups, user) .
                </li>
            </ul>

        <h3>Data Model Summary</h3>

            <a
                href="https://hackmd.io/@AlertaFamily/ByuSMgRyzl"
                target="_blank"
                rel="noopener noreferrer">
                Data Model Domain Objects
            </a>

        <h3>UI Information Hierarchy</h3>

            <a
                href="https://hackmd.io/@AlertaFamily/SJeYcAZgMx"
                target="_blank"
                rel="noopener noreferrer">
                Presentation of Analysis
            </a>

        <h3>Mobile App Screen Flow Overview</h3>
            
        <details>
            <summary>Content Details</summary>
    
            <h3>Version Legend</h3>
            <ul class="legend">
                <li><span class="badge v2">v2</span> Current released / Production DB</li>
                <li><span class="badge v3">v3</span> In development / Staging DB</li>
                <li><span class="badge v4">v4</span> Concept design / Draft</li>
                <li><span class="badge v5">v5</span> Future concept / Draft</li>
            </ul>
    
            <h3>Home</h3>
            <ul>
                <li>Resident Summary <span class="tag v4">v4 concept</span></li>
                <li>Sensing Summary <span class="tag v2">v2/v3 existing</span></li>
                <li>TBD: Notification Summary <span class="tag v2">v2/v3 existing</span></li>
            </ul>
    
            <h3>Sensing</h3>
            <ul>
                <li>Live Status <span class="tag v2">v2/v3 existing</span></li>
                <li>Sensing Dashboard <span class="tag v4">v4 concept</span></li>
                <li>Sensor Trends <span class="tag v2">v2/v3 existing</span></li>
                <li>Movement Patterns <span class="tag v2">v2/v3 existing</span></li>
                <li>Alerta Routines <span class="tag v2">v2/v3 existing</span></li>
                <li>Predictive Analytics <span class="tag v4">v4 concept</span></li>
                <li>Notification Timeline <span class="tag v2">v2/v3 existing</span></li>
            </ul>
    
            <h3>Care</h3>
            <ul>
                <li>Resident Dashboard <span class="tag v4">v4 concept</span></li>
                <li>ADLs <span class="tag v2">v2/v3 existing or planned</span></li>
                <li>Device-ADL Links <span class="tag v2">v2/v3 existing or planned</span></li>
                <li>Notes <span class="tag v2">v2/v3 existing</span></li>
                <li>Priority Items <span class="tag v4">v4 concept</span></li>
                <li>Therapeutic Plans <span class="tag v4">v4 concept</span></li>
            </ul>
    
            <h3>More</h3>
            <ul>
                <li>Account <span class="tag v2">v2/v3 existing</span></li>
                <li>Settings <span class="tag v2">v2/v3 existing</span></li>
                <li>Setup <span class="tag v2">v2/v3 existing</span></li>
                <li>Integrations <span class="tag v5">v5 concept</span></li>
            </ul>
        </details>

    </div>

"""

