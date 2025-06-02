import streamlit as st
from streamlit_folium import folium_static
import folium
from folium.plugins import MarkerCluster
import pandas as pd

st.title("진주시 CCTV 현황")

# ✅ Raw GitHub URL (올바르게 설정)
csv_url = "https://raw.githubusercontent.com/junha0319/jjjjjha/main/jinju_cctv_20250513.csv"

# ✅ 파일 불러오기
df = pd.read_csv(csv_url, encoding='euc-kr')
st.dataframe(df, height=200)

# ✅ 지도 시각화
df[["lat", "lon"]] = df[["위도", "경도"]]
m = folium.Map(location=[35.1799817, 128.1076213], zoom_start=13)
marker_cluster = MarkerCluster().add_to(m)

for idx, row in df.iterrows():
    folium.Marker(
        location=[row["lat"], row["lon"]],
        popup=row["설치장소"],
    ).add_to(marker_cluster)

folium_static(m)
