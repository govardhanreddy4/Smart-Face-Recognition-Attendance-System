import streamlit as st
import pandas as pd
import time 
import os
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# --- Configuration & Date Setup ---
st.set_page_config(page_title="Face Recognition Attendance System", layout="wide")

ts = time.time()
date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
timestamp = datetime.fromtimestamp(ts).strftime("%H:%M-%S")

# --- Auto-Refresh Logic ---
# This refreshes the app every 2000ms (2 seconds) to show live updates
count = st_autorefresh(interval=2000, limit=100, key="fizzbuzzcounter")

st.title("📅 Live Attendance Dashboard")

# --- Optional Status Display (FizzBuzz Logic) ---
with st.sidebar:
    st.header("Refresh Status")
    if count == 0:
        st.info("Started...")
    elif count % 3 == 0 and count % 5 == 0:
        st.success("✨ Live Update (Sync)")
    elif count % 3 == 0:
        st.warning("🔄 Refreshing Data")
    elif count % 5 == 0:
        st.info("📡 Connection Stable")
    else:
        st.write(f"Refresh Count: {count}")

# --- Data Loading & Display ---
file_path = f"Attendance/Attendance_{date}.csv"

# Check if the file exists before trying to read it
if os.path.exists(file_path):
    try:
        df = pd.read_csv(file_path)
        
        st.subheader(f"Attendance Log for {date}")
        
        # Displaying the dataframe with highlighting
        # highlight_max(axis=0) will highlight the maximum value in each column
        st.dataframe(df.style.highlight_max(axis=0), use_container_width=True)
        
        # Additional Metrics
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Entries", len(df))
        with col2:
            st.metric("Last Updated", timestamp)
            
    except Exception as e:
        st.error(f"Error reading data: {e}")
else:
    st.warning(f"No attendance records found for today ({date}). Start 'test.py' to begin logging.")