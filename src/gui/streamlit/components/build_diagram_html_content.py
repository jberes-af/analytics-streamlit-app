# /src/gui/streamlit/components/build_diagram_html_content.py

def build_flow_html(
        *,
        config_json: str,
        css: str,
        js: str,
) -> str:
    return f"""
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8" />

    <script>
        window.patientFlowConfig = {config_json};
    </script>

    <script type="module">
        {js}
    </script>

    <style>
        {css}
    </style>
</head>

<body>
    <div class="chart-card">
        <div id="chart"></div>
    </div>
    
    <section id="node-details-frame" class="details-frame hidden">
        <h3 id="node-details-title"></h3>

        <details>
            <summary>Screen Specification</summary>

            <h4>Purpose</h4>
            <p id="node-screen-spec"></p>

            <h4>Displayed Data</h4>
            <ul id="node-screen-displayed-data"></ul>

            <h4>User Inputs</h4>
            <ul id="node-screen-user-inputs"></ul>

            <h4>Primary Action</h4>
            <p id="node-screen-primary-action"></p>

            <h4>Secondary Actions</h4>
            <ul id="node-screen-secondary-actions"></ul>

            <h4>Validation Rules</h4>
            <ul id="node-screen-validation-rules"></ul>

            <h4>Navigation In</h4>
            <ul id="node-screen-navigation-in"></ul>

            <h4>Navigation Out</h4>
            <ul id="node-screen-navigation-out"></ul>

            <h4>States</h4>
            <p><strong>Empty:</strong> <span id="node-screen-empty-state"></span></p>
            <p><strong>Loading:</strong> <span id="node-screen-loading-state"></span></p>
            <p><strong>Error:</strong> <span id="node-screen-error-state"></span></p>
        </details>

        <details open>
            <summary>Screen Sketches</summary>
            <div id="node-details-adl" class="details-adl"></div>
            <p id="node-details-image-empty" class="muted hidden">
                No screen sketches available.
            </p>
        </details>

        <details>
            <summary>Use Cases</summary>
            <div id="node-use-cases"></div>
        </details>

        <details>
            <summary>Workflows</summary>
            <div id="node-workflows"></div>
        </details>

        <details>
            <summary>Required Permissions</summary>
            <ul id="node-required-permissions"></ul>
        </details>

        <details>
            <summary>Client Contracts</summary>
            <div id="node-client-contracts"></div>
        </details>

        <details>
            <summary>Backend Data Model</summary>
            <div id="node-backend-data-model"></div>

            <h4>Domain Objects</h4>
            <div id="node-definition-dtos"></div>
            
            <h4>Persistence DTOs</h4>
            <div id="node-persistence-dtos"></div>

            <h4>Data Reads</h4>
            <ul id="node-data-reads"></ul>

            <h4>Data Writes</h4>
            <ul id="node-data-writes"></ul>
        </details>

        <details>
            <summary>Rules Engine</summary>

            <h4>Engines</h4>
            <ul id="node-rules-engines"></ul>

            <h4>Rules Purpose</h4>
            <ul id="node-rules-purpose"></ul>

            <div id="node-rules-output-dtos"></div>
        </details>

        <details open>
            <summary>Description</summary>
            <p id="node-details-description"></p>
        </details>
    </section>


    <div id="screen-drawer" class="screen-drawer">
    
        <div class="drawer-header">
            <h3 id="screen-drawer-title"></h3>

            <div class="drawer-button-group">
    
                <button id="download-image-button" class="drawer-button">
                    ⬇️ Download
                </button>
    
                <button id="show-data-model-button" class="drawer-button">
                    🧩 Data Model
                </button>
    
                <button id="close-screen-drawer-button" class="drawer-button drawer-button-close">
                    ✖ Close
                </button>
    
            </div>

        </div>
        <div id="screen-image-container"></div>
    
    </div>
    
    <div id="data-model-drawer" class="data-model-drawer">
    
        <div class="drawer-header">
    
            <h3>Related Data Model</h3>
    
            <div class="drawer-button-group">
    
                <button id="download-data-model-button" class="drawer-button">
                    ⬇️ Download
                </button>
    
                <button
                    id="close-data-model-button" class="drawer-button drawer-button-close">
                    ✖ Close
                </button>
    
            </div>
    
        </div>
    
        <div id="data-model-content"></div>
    
    </div>

</body>
</html>
"""
