import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import datetime

st.set_page_config(page_title="HeritageROI Optimization Platform", layout="wide", page_icon="🛕")

# 1. SEEDING THE DATA ENGINE WITH 75 HISTORICAL VISITOR SCANS
@st.cache_data
def generate_historical_tourism_data():
    np.random.seed(101)
    rows = []
    monuments = ["Grand Landmark Tower A", "Ancient Fortification Gate", "Royal Heritage Palace Sector"]
    languages = ["English", "Hindi", "Español", "Français"]
    channels = ["Free Audio Guide", "Premium Immersive Narrative Walk", "Interactive 3D AR Grid"]
    
    for i in range(1, 76):
        mon = np.random.choice(monuments)
        lang = np.random.choice(languages, p=[0.5, 0.3, 0.1, 0.1])
        chan = np.random.choice(channels, p=[0.4, 0.4, 0.2])
        
        # Strategic Business Logic Metrics Formulation
        dwell_time = int(np.random.normal(loc=95, scale=25)) if chan != "Free Audio Guide" else int(np.random.normal(loc=40, scale=10))
        dwell_time = max(15, dwell_time) # Clamping logic bounding
        
        micro_rev = 0.0
        if chan == "Premium Immersive Narrative Walk":
            micro_rev = 2.50 # Hardcoded conversion model fee ($ or equivalent units value)
        elif chan == "Interactive 3D AR Grid":
            micro_rev = 5.00
            
        indirect_spent = round(float(dwell_time * np.random.uniform(0.4, 0.8)), 2)
        
        rows.append({
            "Scan ID": f"SCN-{i:03d}",
            "Asset Target": mon,
            "Language Selector": lang,
            "Monetization Funnel Channel": chan,
            "Monitored Dwell-Time (Mins)": dwell_time,
            "Direct Yield Revenue ($)": micro_rev,
            "Projected Indirect Commerce Spends ($)": indirect_spent
        })
    return pd.DataFrame(rows)

if "tourism_db" not in st.session_state:
    st.session_state.tourism_db = generate_historical_tourism_data()

# 2. INTERACTIVE PRESENTATION INTERFACE
tab_biz, tab_mobile = st.tabs(["📊 HeritageROI Economic Performance Analytics", "📱 On-Site Front-End Scanning Screen Mockup"])

with tab_biz:
    st.title("📊 HeritageROI Platform Analytics")
    st.caption("Economic Optimization Platform assessing the conversion mechanics of physical monument traffic into direct and indirect digital GDP yield assets.")
    
    tdf = st.session_state.tourism_db
    
    # Financial Analytics Aggregation Calculations
    total_scans = len(tdf)
    total_direct_rev = tdf["Direct Yield Revenue ($)"].sum()
    total_indirect_leakage_saved = tdf["Projected Indirect Commerce Spends ($)"].sum()
    avg_dwell_index = tdf["Monitored Dwell-Time (Mins)"].mean()
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Aggregated Traffic Asset Scans", total_scans)
    m2.metric("Direct Micro-Transaction Value Ingested", f"${total_direct_rev:,.2f}")
    m3.metric("Indirect Local Marketplace Value Lift", f"${total_indirect_leakage_saved:,.2f}")
    m4.metric("Mean Visitor Engagement Window", f"{avg_dwell_index:.1f} Minutes Index")
    
    st.divider()
    col_l, col_r = st.columns(2)
    
    with col_l:
        st.subheader("📈 Direct Conversion Distribution Logic")
        fig_pie = px.pie(tdf, names="Monetization Funnel Channel", values="Direct Yield Revenue ($)",
                         title="Funnel Yield Distribution by Tier Packages",
                         color_discrete_sequence=px.colors.sequential.RdBu)
        st.plotly_chart(fig_pie, use_container_width=True)
        
    with col_r:
        st.subheader("📈 Engagement Velocity: Dwell-Time vs Marketplace Expenditure Correlation")
        fig_scatter = px.scatter(tdf, x="Monitored Dwell-Time (Mins)", y="Projected Indirect Commerce Spends ($)",
                                 color="Asset Target", size="Direct Yield Revenue ($)",
                                 title="Economic Value Elasticity Matrix Analysis Map",
                                 trendline="ols", color_discrete_sequence=px.colors.qualitative.Dark24)
        st.plotly_chart(fig_scatter, use_container_width=True)

with tab_mobile:
    # Simulating a narrow viewport matrix configuration layout
    st.subheader("📱 On-Site Consumer Interface Mockup")
    st.caption("Frictionless UX rendered instantly inside the visitor's mobile browser upon scanning a physical property asset plaque matrix.")
    
    c_left, c_mid, c_right = st.columns([1, 2, 1])
    with c_mid:
        st.info("📍 Physical QR Plaque Confirmed: Asset Node Matrix 009")
        target_monument = st.selectbox("Simulated Scan Target Location:", ["Grand Landmark Tower A", "Ancient Fortification Gate", "Royal Heritage Palace Sector"])
        user_lang = st.radio("Localization Language Structure:", ["English", "Hindi", "Español", "Français"], horizontal=True)
        
        st.divider()
        if user_lang == "English":
            st.markdown(f"### Welcome to {target_monument}")
            st.write("This site stands as an architectural masterclass of ancient craftsmanship, built in the middle medieval century eras to mark significant triumphs.")
        elif user_lang == "Hindi":
            st.markdown(f"### {target_monument} में आपका स्वागत है")
            st.write("यह ऐतिहासिक स्थल प्राचीन वास्तुकला और शिल्प कौशल का एक उत्कृष्ट उदाहरण है, जिसका निर्माण मध्यकालीन युग के दौरान ऐतिहासिक विजयों के उपलक्ष्य में किया गया था।")
        else:
            st.markdown(f"### {target_monument} Guide ({user_lang})")
            st.write("[Localization Translation Micro-Service API Activated] Enjoy your self-guided architectural multimedia walk experience node.")
            
        st.caption("🎬 Free Streaming Introductory Overview Video Node")
        st.video("https://youtube.com")
        
        st.divider()
        st.markdown("⭐ **Unlock Premium Experience Add-Ons**")
        chosen_funnel = st.selectbox("Select Access Tier Model:", ["Free Content Tier", "Premium Immersive Narrative Walk ($2.50)", "Interactive 3D AR Grid ($5.00)"])
        
        if st.button("Authorize Fast Checkout Payment Protocol"):
            st.success("Transaction Complete! Token verified. Premium audio/visual streaming data stream layer active.")