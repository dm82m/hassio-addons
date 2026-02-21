import streamlit as st
import subprocess
import os

st.set_page_config(page_title="NZB-Monkey-Go Web UI", page_icon="🐒", layout="wide")

# Tabs definieren
tab1, tab2 = st.tabs(["🚀 Process Links", "⚙️ Configuration"])

# --- TAB 1: LINKS VERARBEITEN ---
with tab1:
    st.title("🐒 NZB-Monkey-Go")

    mode = st.radio("Select Mode:", ("Standard", "Direct Search"), horizontal=True)
    script = "/n.sh" if mode == "Standard" else "/nd.sh"

    links = st.text_area(
        "Paste your NZB-Links here:", height=150, placeholder="nzblnk:..."
    )

    if st.button("Start Processing"):
        if links.strip():
            link_list = [link.strip() for link in links.splitlines() if link.strip()]

            for i, line in enumerate(link_list):
                st.markdown(f"### 📦 Processing {i + 1}/{len(link_list)}")

                # Container für die Live-Ausgabe
                console_header = st.empty()
                console_output = st.empty()
                full_log = ""

                # Subprocess mit Popen starten, um den Stream abzugreifen
                process = subprocess.Popen(
                    [script, line],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    bufsize=1,
                )

                # Live-Logging Loop
                with console_output.code("Initializing..."):
                    for output_line in iter(process.stdout.readline, ""):
                        full_log += output_line
                        # Update das Code-Feld live mit dem bisherigen Log
                        console_output.code(full_log)

                    process.stdout.close()
                    return_code = process.wait()

                if return_code == 0:
                    st.success(f"Finished: {line[:50]}...")
                else:
                    st.error(f"Failed with Exit Code {return_code}")

                st.divider()
        else:
            st.warning("Please enter at least one link.")

# --- TAB 2: CONFIGURATION EDITOR ---
with tab2:
    st.title("📝 Config Editor")

    configs = {
        "Standard Config": "/config/nzb-monkey-go.conf",
        "Direct Search Config": "/config/nzb-monkey-go_direct.conf",
    }

    selected_cfg = st.selectbox("Select file to edit:", list(configs.keys()))
    file_path = configs[selected_cfg]

    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            content = f.read()

        new_content = st.text_area(f"Editing {file_path}:", value=content, height=200)

        if st.button("Save Configuration"):
            try:
                with open(file_path, "w") as f:
                    f.write(new_content)
                st.success(f"Successfully saved to {file_path}!")
            except Exception as e:
                st.error(f"Error saving file: {e}")
    else:
        st.error(f"File not found: {file_path}")
