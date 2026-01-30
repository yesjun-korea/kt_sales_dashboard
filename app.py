# -*- coding: utf-8 -*-
"""
서비스 임시 점검 안내 페이지
"""
import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="서비스 점검 안내",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 사이드바 숨기기 및 스타일
st.markdown("""
<style>
    /* 사이드바 완전히 숨기기 */
    [data-testid="stSidebar"] {
        display: none;
    }
    [data-testid="stSidebarCollapsedControl"] {
        display: none;
    }
    
    /* 전체 배경 */
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        min-height: 100vh;
    }
    
    /* 메인 컨테이너 */
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 80vh;
        padding: 40px 20px;
    }
    
    /* 아이콘 애니메이션 */
    .security-icon {
        font-size: 120px;
        margin-bottom: 40px;
        animation: pulse 2s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.1); opacity: 0.8; }
    }
    
    /* 메인 타이틀 */
    .main-title {
        font-size: 4.5rem;
        font-weight: 900;
        color: #ffffff;
        text-align: center;
        margin-bottom: 20px;
        text-shadow: 0 4px 20px rgba(0,0,0,0.3);
        letter-spacing: 8px;
    }
    
    /* 서브 타이틀 */
    .sub-title {
        font-size: 2rem;
        font-weight: 600;
        color: #f9d849;
        text-align: center;
        margin-bottom: 60px;
        letter-spacing: 2px;
    }
    
    /* 안내 박스 */
    .info-box {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 40px 60px;
        max-width: 700px;
        margin: 0 auto;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    }
    
    .info-text {
        font-size: 1.4rem;
        color: #e0e0e0;
        text-align: center;
        line-height: 2;
    }
    
    /* 로딩 바 애니메이션 */
    .loading-container {
        width: 300px;
        height: 6px;
        background: rgba(255, 255, 255, 0.2);
        border-radius: 3px;
        margin: 40px auto;
        overflow: hidden;
    }
    
    .loading-bar {
        width: 40%;
        height: 100%;
        background: linear-gradient(90deg, #f9d849, #ff6b6b, #f9d849);
        border-radius: 3px;
        animation: loading 2s ease-in-out infinite;
    }
    
    @keyframes loading {
        0% { transform: translateX(-100%); }
        100% { transform: translateX(350%); }
    }
    
    /* 푸터 */
    .footer {
        position: fixed;
        bottom: 20px;
        left: 0;
        right: 0;
        text-align: center;
        color: rgba(255,255,255,0.5);
        font-size: 0.9rem;
    }
    
    /* 모바일 대응 */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2.5rem;
            letter-spacing: 4px;
        }
        .sub-title {
            font-size: 1.3rem;
        }
        .security-icon {
            font-size: 80px;
        }
        .info-box {
            padding: 25px 30px;
            margin: 0 15px;
        }
        .info-text {
            font-size: 1.1rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# 메인 콘텐츠
st.markdown("""
<div class="main-container">
    <div class="security-icon">🔒</div>
    <h1 class="main-title">보안성 검토 중</h1>
    <p class="sub-title">Security Review in Progress</p>
    
    <div class="loading-container">
        <div class="loading-bar"></div>
    </div>
    
    <div class="info-box">
        <p class="info-text">
            현재 서비스 보안성 검토가 진행 중입니다.<br>
            더 안전한 서비스 제공을 위해 잠시 서비스를 중단하오니<br>
            이용에 불편을 드려 죄송합니다.<br><br>
            <strong style="color: #f9d849;">빠른 시일 내에 다시 찾아뵙겠습니다.</strong>
        </p>
    </div>
</div>

<div class="footer">
    Copyright 2025 KT Enterprise Sales Guide
</div>
""", unsafe_allow_html=True)
