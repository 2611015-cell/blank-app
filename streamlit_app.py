import streamlit as st

# 1. 웹 페이지 제목 설정
st.title("🌡️ 스마트 홈 온·습도 제어 시스템")
st.subheader("실내외 온도에 따른 최적의 조치를 추천합니다.")
st.markdown("---")

# 2. 사이드바 또는 메인 화면에 입력 위젯 배치
st.sidebar.header("📥 온도 입력 설정")

# 실내 온도 입력 (기본값: 30, 범위: 15~40)
in_temp = st.sidebar.slider("현재 실내 온도 (°C)", min_value=15, max_value=40, value=30)

# 실외 온도 입력 (기본값: 29, 범위: 15~40)
out_temp = st.sidebar.number_input("현재 실외 온도 (°C)", min_value=15, max_value=40, value=29)

# 3. 기존 코드의 핵심 로직 (그대로 유지)
actions = ["창문 열기", "에어컨 켜기", "대기"]

if in_temp > 26:
    if in_temp > out_temp:
        target = actions[0]  # 창문 열기
    else:
        target = actions[1]  # 에어컨 켜기
else:
    target = actions[2]      # 대기

# 4. 결과 출력 및 대시보드 구성
st.subheader("📊 현재 상태 및 추천 조치")

# 데이터 시각화를 위한 컬럼 나누기
col1, col2 = st.columns(2)
with col1:
    st.metric(label="실내 온도", value=f"{in_temp} °C", delta=f"{in_temp - 26} °C" if in_temp > 26 else None)
with col2:
    st.metric(label="실외 온도", value=f"{out_temp} °C")

st.markdown("---")

# 결과 출력 로직 (print 대신 st.success 및 알림 위젯 사용)
for act in actions:
    if act == target:
        if act == "대기":
            st.info(f"💡 현재 상태: **{act}** (쾌적한 온도입니다.)")
        else:
            st.warning("⚠️ 조치를 취하십시오!")
            st.success(f"추천 행동: **【 {act} 】**")