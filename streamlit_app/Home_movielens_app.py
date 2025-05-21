import streamlit as st

# Navigation
page_0 = st.Page("page0.py", title="Home", icon="🏠")         # House
page_1 = st.Page("page1.py", title="Overview", icon="🎬")     # Film clapperboard
page_2 = st.Page("page2.py", title="Tags Insights", icon="📊")  # Bar chart
page_3 = st.Page("page3.py", title="Movie Explorer", icon="🔎") # Magnifying glass

pg = st.navigation([page_0, page_1, page_2, page_3])
pg.run()
# ---------- Bandeau de bas de page ----------
st.markdown("""
    <hr style="border-top: 1px solid #4CAF50; margin-top: 50px;"/>
    <div style="text-align: center; color: #888; font-size: 0.9em;">
        &copy; 2025 <strong>Josias Nteme</strong> - Tous droits réservés.
    </div>
""", unsafe_allow_html=True)

