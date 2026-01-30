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
    /* 궁서체 사용 */
    
    /* 사이드바 완전히 숨기기 */
    [data-testid="stSidebar"] {
        display: none;
    }
    [data-testid="stSidebarCollapsedControl"] {
        display: none;
    }
    
    /* Streamlit 기본 컨테이너 배경 투명하게 */
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        min-height: 100vh;
    }
    
    /* 모든 Streamlit 컨테이너 투명하게 */
    .stMarkdown, .element-container, .stMarkdownContainer,
    [data-testid="stMarkdownContainer"],
    [data-testid="stVerticalBlock"],
    [data-testid="stHorizontalBlock"],
    .block-container, .main .block-container,
    div[data-testid="stAppViewBlockContainer"] {
        background: transparent !important;
        background-color: transparent !important;
    }
    
    /* main block-container 패딩 조정 */
    .main .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }
    
    /* 코드 블록이나 pre 태그 숨기기 */
    pre, code {
        display: none !important;
    }
    
    /* 메인 컨테이너 */
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 85vh;
        padding: 40px 20px;
        background: transparent !important;
    }
    
    /* 아이콘 애니메이션 */
    .security-icon {
        font-size: 150px;
        margin-bottom: 50px;
        animation: pulse 2s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.1); opacity: 0.8; }
    }
    
    /* 메인 타이틀 - 조선로동당 스타일 */
    .main-title {
        font-family: 'Gungsuh', '궁서', '궁서체', serif !important;
        font-size: 8rem !important;
        font-weight: 900 !important;
        color: #ffffff !important;
        text-align: center;
        margin-bottom: 30px;
        text-shadow: 0 6px 30px rgba(0,0,0,0.5);
        letter-spacing: 15px;
        line-height: 1.2;
        background: transparent !important;
    }
    
    /* 서브 타이틀 */
    .sub-title {
        font-size: 1.8rem !important;
        font-weight: 600 !important;
        color: #f9d849 !important;
        text-align: center;
        margin-bottom: 40px;
        letter-spacing: 3px;
        background: transparent !important;
    }
    
    /* 로딩 바 애니메이션 */
    .loading-container {
        width: 400px;
        height: 6px;
        background: rgba(255, 255, 255, 0.2) !important;
        border-radius: 3px;
        margin: 50px auto;
        overflow: hidden;
    }
    
    .loading-bar {
        width: 40%;
        height: 100%;
        background: linear-gradient(90deg, #f9d849, #ff6b6b, #f9d849) !important;
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
        color: rgba(255,255,255,0.5) !important;
        font-size: 0.9rem;
        background: transparent !important;
    }
    
    /* 모바일 대응 */
    @media (max-width: 768px) {
        .main-title {
            font-size: 3.5rem !important;
            letter-spacing: 8px;
        }
        .sub-title {
            font-size: 1.2rem !important;
        }
        .security-icon {
            font-size: 100px;
        }
        .loading-container {
            width: 250px;
        }
    }
</style>
""", unsafe_allow_html=True)

# 메인 콘텐츠
st.markdown("""
<div class="main-container">
    <div class="security-icon">🔒</div>
    <div class="main-title">보안성 검토 중</div>
    <div class="sub-title">Security Review in Progress</div>
    
    <div class="loading-container">
        <div class="loading-bar"></div>
    </div>
</div>

<div class="footer">
    Copyright 2025 KT Enterprise Sales Guide
</div>
""", unsafe_allow_html=True)
