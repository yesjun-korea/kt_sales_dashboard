# -*- coding: utf-8 -*-
"""
토탈영업 B2B 영업 가이드
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import re
import os
import openpyxl
from io import BytesIO
import base64

# ============================================
# 페이지 설정
# ============================================
st.set_page_config(
    page_title="토탈영업 B2B 영업 가이드",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# 커스텀 CSS - 반응형 디자인 (PC 크게, 모바일 작게)
# ============================================
st.markdown("""
<style>
    /* ========== 공통 기본 스타일 ========== */
    .stApp {
        background-color: #f0f2f5;
        color: #333333;
        font-family: 'Inter', 'Segoe UI', sans-serif;
    }
    
    .custom-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 16px;
        box-shadow: 0 8px 30px rgba(0,0,0,0.12);
        border: 1px solid #e0e0e0;
        height: 100%;
        position: relative;
    }
    
    .keypoint-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 16px;
        box-shadow: 0 8px 30px rgba(0,0,0,0.15);
        border: 3px solid #f9d849;
        height: 100%;
    }
    
    /* ========== PC 버전 (기본값, 768px 이상) ========== */
    .header-box {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 16px;
        padding: 15px 25px;
        margin-bottom: 15px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        display: flex;
        align-items: center;
        gap: 12px;
        font-weight: 700;
        color: #006666;
        font-size: 1.8rem;
        width: 100%;
    }
    .header-box::before {
        content: '';
        display: inline-block;
        width: 6px;
        height: 28px;
        background-color: #f9d849;
        border-radius: 3px;
    }
    
    .h1-title {
        font-size: 2rem !important;
        font-weight: 800;
        color: #004d4d !important;
        margin-bottom: 25px;
        display: flex; align-items: center; gap: 15px;
        flex-wrap: wrap;
    }
    
    .opportunity-badge {
        display: inline-block;
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        color: #fff;
        padding: 8px 16px;
        border-radius: 25px;
        font-size: 1rem;
        font-weight: 700;
        margin: 5px 5px 5px 0;
        box-shadow: 0 3px 10px rgba(238,90,36,0.4);
        text-shadow: 0 1px 2px rgba(0,0,0,0.2);
    }
    
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #eef0f2;
        font-size: 1.4rem;
    }
    [data-testid="stSidebar"] .stMarkdown h2 { color: #006666 !important; font-size: 1.6rem !important; }
    [data-testid="stSidebar"] .stMarkdown h3 { font-size: 1.4rem !important; }
    [data-testid="stSidebar"] label { font-size: 1.2rem !important; }
    
    .info-row {
        display: flex; justify-content: space-between; align-items: center;
        padding: 12px 0;
        border-bottom: 1px dashed #e0e0e0;
    }
    .info-label { color: #64748b; font-weight: 600; font-size: 1.4rem; }
    .info-value { color: #1e293b; font-weight: 600; font-size: 1.5rem; }
    .info-value.highlight { color: #008080 !important; font-weight: 800; font-size: 1.7rem; }
    
    .keypoint-box {
        background-color: #fff9c4;
        border-radius: 12px; padding: 15px; 
    }
    .keypoint-text { color: #333; font-size: 1.5rem; line-height: 1.6; font-weight: 500; }
    
    .no-photo {
        width: 120px; height: 120px; border-radius: 50%;
        background-color: #e2e8f0; color: #94a3b8;
        display: flex; align-items: center; justify-content: center;
        font-size: 3rem; border: 3px solid #cbd5e1;
    }
    
    .product-item {
        display: flex; justify-content: space-between; align-items: center;
        padding: 12px 0; border-bottom: 1px solid #f0f0f0;
    }
    .product-name { font-weight: 600; color: #333; display: flex; align-items: center; gap: 10px; font-size: 1.4rem; }
    .product-count { font-weight: 700; color: #008080; background: #e0f2f1; padding: 4px 12px; border-radius: 12px; font-size: 1.3rem; }
    
    .chart-subtitle {
        text-align: center;
        font-size: 1.5rem;
        font-weight: 700;
        color: #006666;
        margin-bottom: 15px;
        padding: 10px 0;
    }
    
    /* ========== 모바일 버전 (768px 미만) ========== */
    @media (max-width: 768px) {
        .header-box {
            padding: 10px 15px;
            margin-bottom: 10px;
            font-size: 1rem;
            gap: 8px;
            border-radius: 12px;
        }
        .header-box::before {
            width: 4px;
            height: 16px;
        }
        
        .h1-title {
            font-size: 1.2rem !important;
            margin-bottom: 15px;
            gap: 8px;
        }
        
        .opportunity-badge {
            padding: 4px 10px;
            font-size: 0.7rem;
            margin: 2px;
            border-radius: 15px;
        }
        
        [data-testid="stSidebar"] { font-size: 0.9rem; }
        [data-testid="stSidebar"] .stMarkdown h2 { font-size: 1rem !important; }
        [data-testid="stSidebar"] .stMarkdown h3 { font-size: 0.9rem !important; }
        [data-testid="stSidebar"] label { font-size: 0.8rem !important; }
        
        .info-row { padding: 8px 0; }
        .info-label { font-size: 0.85rem; }
        .info-value { font-size: 0.9rem; }
        .info-value.highlight { font-size: 1rem; }
        
        .keypoint-box { padding: 10px; border-radius: 8px; }
        .keypoint-text { font-size: 0.9rem; line-height: 1.5; }
        
        .no-photo {
            width: 70px; height: 70px;
            font-size: 1.8rem;
        }
        
        .product-item { padding: 8px 0; }
        .product-name { font-size: 0.9rem; gap: 6px; }
        .product-count { font-size: 0.8rem; padding: 3px 8px; }
        
        .chart-subtitle { font-size: 0.95rem; margin-bottom: 8px; }
        
        .custom-card, .keypoint-card {
            padding: 12px;
            border-radius: 12px;
        }
    }
    
</style>
""", unsafe_allow_html=True)

# ============================================
# 데이터 로드
# ============================================
@st.cache_data
def load_data():
    try:
        df = pd.read_excel("Dash.xlsx", sheet_name=1, header=3)
        df.columns = df.columns.astype(str)
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
        df[numeric_cols] = df[numeric_cols].fillna(0)
        
        col_addr1, col_addr2 = df.columns[20], df.columns[21]
        df['전체주소'] = df.apply(lambda r: f"{str(r[col_addr1]).strip()} {str(r[col_addr2]).strip()}".strip(), axis=1)
        
        def extract_region(address):
            raw_addr = str(address).lower().strip()
            if not address or raw_addr == 'nan' or raw_addr == 'nan nan' or raw_addr == '': 
                return ('기타', '기타')
            parts = address.split()
            if len(parts) >= 2:
                sido, sigungu = parts[0], parts[1]
                if len(parts) > 2 and ('시' in parts[1] or '군' in parts[1]):
                    if '구' in parts[2] or '군' in parts[2]: sigungu = parts[1] + ' ' + parts[2]
                return (sido, sigungu)
            return ('기타', '기타')
        
        df['시도'], df['시군구'] = zip(*df['전체주소'].apply(extract_region))
        return df
    except:
        return pd.DataFrame()

@st.cache_data
def load_staff_photos():
    """폴더 내 jpg 파일에서 직원 사진 로드 (파일명 = 직원이름.jpg)"""
    mapping = {}
    try:
        # 현재 디렉토리에서 jpg 파일 검색
        photo_dir = os.path.dirname(os.path.abspath(__file__))
        for filename in os.listdir(photo_dir):
            if filename.lower().endswith('.jpg'):
                # 파일명에서 확장자 제거하여 직원 이름 추출
                name = os.path.splitext(filename)[0].strip().replace(' ', '')
                photo_path = os.path.join(photo_dir, filename)
                mapping[name] = photo_path
        return mapping
    except:
        return {}

df_main = load_data()
staff_photos = load_staff_photos()

COL_CUST = df_main.columns[5]
COL_REP = df_main.columns[3]
COL_SIZE = df_main.columns[16]
COL_SECTOR = df_main.columns[14]
COL_REV_ANNUAL = df_main.columns[95]
COL_NEW_ANNUAL = df_main.columns[83]
REV_COLS = [df_main.columns[i] for i in range(40, 52)]
NEW_REV_COLS = [df_main.columns[i] for i in range(54, 66)]
TOTAL_PROD_REVENUE = [(df_main.columns[85+i*2], df_main.columns[86+i*2]) for i in range(5)]
NEW_PROD_REVENUE = [(df_main.columns[68+i*3], df_main.columns[69+i*3]) for i in range(5)]
PRODUCT_COLS = [(df_main.columns[30+i*2], df_main.columns[31+i*2]) for i in range(5)]

def format_kr(val):
    if pd.isna(val) or val == 0: return "0원"
    v = abs(float(val))
    sign = "" if val >= 0 else "-"
    if v >= 100000000: return f"{sign}{int(v//100000000)}억 {int((v%100000000)//10000):,}만원"
    elif v >= 10000: return f"{sign}{int(v/10000):,}만원"
    return f"{sign}{int(v):,}원"

def get_product_icon(name):
    n = str(name).upper()
    if '전화' in n: return "📞"
    if '인터넷' in n: return "🌐"
    if 'TV' in n: return "📺"
    if '모바일' in n: return "📱"
    return "📦"

# [수정] 영업기회 인사이트 및 키워드 추출 함수 - KT 영업 관점 키워드
def generate_insights_and_keywords(row, products):
    insights = []
    keywords = []
    try: new_rev = float(row[COL_NEW_ANNUAL])
    except: new_rev = 0
    try: 
        workers = str(row[COL_SIZE])
        workers = int(re.sub(r'[^0-9]', '', workers)) if workers and workers != 'nan' else 0
    except: workers = 0
    sector = str(row[COL_SECTOR])
    prod_names = [p_name for p_name, count in products]
    
    triggered = False
    if new_rev > 0:
        insights.append("✨ 전년도 신규 매출이 발생하여 투자가 활발한 성장 기업입니다. 추가 제안 성공률이 높습니다.")
        keywords.append("🔥 추가제안 기회")
        triggered = True
    target_sectors_mobile = ['건설', '유통', '도매', '서비스', '영업']
    if workers >= 10 and any(s in sector for s in target_sectors_mobile) and not any(x in str(prod_names) for x in ['Mobile', '5G', 'LTE', '모바일']):
        insights.append(f"🏃‍♂️ 직원수({workers}명) 대비 법인폰 가입이 확인되지 않습니다. 외근직을 위한 패드/법인폰 결합 제안이 시급합니다.")
        keywords.append("📱 모바일 기회")
        triggered = True
    target_sectors_ai = ['병원', '의원', '음식', '식당', '관공서']
    if any(s in sector for s in target_sectors_ai) and not any(x in str(prod_names) for x in ['AI', '로봇', '하이오더']):
        insights.append("📞 고객 응대와 예약 관리가 핵심인 업종입니다. AI통화비서(링고) 또는 하이오더/로봇 도입 시 업무 효율이 급증합니다.")
        keywords.append("🤖 AI서비스 기회")
        triggered = True
    target_sectors_infra = ['소프트웨어', '시스템', '정보', '공공']
    if (any(s in sector for s in target_sectors_infra) or workers >= 30) and not any(x in str(prod_names) for x in ['전용회선', 'IDC', '코넷']):
        insights.append("☁️ 데이터 안정성이 중요한 업종/규모입니다. 일반 인터넷보다 안정적인 전용회선(Kornet) 및 보안 서비스 제안이 필요합니다.")
        keywords.append("🌐 인터넷 기회")
        triggered = True
    target_sectors_safety = ['제조', '공장', '물류', '창고']
    if any(s in sector for s in target_sectors_safety) and not any(x in str(prod_names) for x in ['CCTV', '텔레캅', '기가아이즈']):
        insights.append("👁️ 자재 도난 방지 및 산업 안전 관리가 필수입니다. 지능형 CCTV(기가아이즈) 제안으로 안전 이슈를 공략하세요.")
        keywords.append("🔒 보안서비스 기회")
        triggered = True
    if not any('전화' in p for p in prod_names):
        insights.append("☎️ 사업 필수재인 유선전화가 당사에 없습니다. 타사 사용 중으로 추정되니 번호이동(윈백)을 최우선으로 제안하세요.")
        keywords.append("☎️ 통화서비스 기회")
        triggered = True
    if not triggered and len(prod_names) <= 2:
        insights.append("🎁 현재 소수 상품만 이용 중입니다. 이탈 방지를 위해 인터넷+전화+TV 결합 할인을 통한 혜택을 강조하세요.")
        keywords.append("📦 결합상품 기회")
    return insights, keywords

def reset_filters():
    if 'sel_sido' in st.session_state: del st.session_state.sel_sido
    if 'sel_sigungu' in st.session_state: del st.session_state.sel_sigungu
    if 'sel_cust' in st.session_state: del st.session_state.sel_cust

# ============================================
# 사이드바
# ============================================
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=50)
    st.markdown("### 🔍 경북담당 성장고객 검색")
    
    unique_sidos = sorted([s for s in df_main['시도'].unique() if s not in ['경북', '대구', '기타'] and str(s).lower().strip() != 'nan'])
    
    priority_sidos = []
    if '경북' in df_main['시도'].unique(): priority_sidos.append('경북')
    if '대구' in df_main['시도'].unique(): priority_sidos.append('대구')
    
    final_sidos = ['전체'] + priority_sidos + unique_sidos
    if '기타' in df_main['시도'].unique(): final_sidos.append('기타')

    sel_sido = st.selectbox("📍 시/도", final_sidos, key='sel_sido')
    
    df_s1 = df_main if sel_sido == '전체' else df_main[df_main['시도'] == sel_sido]
    
    unique_sigungus = sorted([x for x in df_s1['시군구'].unique().tolist() if str(x).lower().strip() != 'nan'])
    sel_sigungu = st.selectbox("📍 시/군/구", ['전체'] + unique_sigungus, key='sel_sigungu')
    
    df_f = df_s1 if sel_sigungu == '전체' else df_s1[df_s1['시군구'] == sel_sigungu]
    
    cust_list = [x for x in df_f[COL_CUST].dropna().unique().tolist() if str(x).lower().strip() != 'nan']
    sel_cust = st.selectbox("👤 고객 선택", ['-- 선택하세요 --'] + sorted(cust_list), key='sel_cust')
    
    st.markdown("---")
    st.button("🔄 초기화", on_click=reset_filters, use_container_width=True)

# ============================================
# 메인 화면
# ============================================
if sel_cust == "-- 선택하세요 --":
    st.markdown("""
        <div style="text-align:center; padding-top:100px;">
            <h1 style="color:#008080;">📊 토탈영업 B2B 영업 가이드</h1>
            <p style="color:#777; font-size:1.5rem;">좌측 사이드바에서 고객을 선택하여 분석 리포트를 확인하세요.</p>
        </div>
    """, unsafe_allow_html=True)
else:
    c_data = df_f[df_f[COL_CUST] == sel_cust].iloc[0]
    prod_data = [(p, int(c_data[lc])) for pc, lc in PRODUCT_COLS if pd.notna(p := c_data[pc])]
    
    # 인사이트 및 키워드 생성
    insights, keywords = generate_insights_and_keywords(c_data, prod_data)
    
    # [수정] 타이틀 + 영업기회 뱃지 (눈에 띄는 빨간 계열)
    badges_html = ''.join([f'<span class="opportunity-badge">{kw}</span>' for kw in keywords])
    st.markdown(f'''
    <div class="h1-title">
        📊 {sel_cust} 분석 리포트
        <div style="margin-left: 20px;">{badges_html}</div>
    </div>
    ''', unsafe_allow_html=True)
    
    # Row 1
    r1c1, r1c2 = st.columns(2)
    
    with r1c1:
        with st.container():
            st.markdown('<div class="header-box" style="display:block; padding:15px;">🏢 고객 핵심 정보', unsafe_allow_html=True)
            info_items = [
                ("기업 규모", c_data[COL_SIZE]),
                ("업종", c_data[COL_SECTOR]),
                ("제품명", c_data[df_main.columns[23]]),
                ("전화번호", c_data[df_main.columns[22]]),
                ("주소", c_data['전체주소']),
                ("연간 매출", format_kr(c_data[COL_REV_ANNUAL]))
            ]
            for l, v in info_items:
                hl = " highlight" if l == "연간 매출" else ""
                st.markdown(f'<div class="info-row"><span class="info-label">{l}</span><span class="info-value{hl}">{v}</span></div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
    with r1c2:
        with st.container():
            st.markdown('<div class="custom-card" style="padding:0; overflow:hidden;">', unsafe_allow_html=True)
            addr_enc = str(c_data['전체주소']).replace(' ', '+')
            st.components.v1.iframe(f"https://maps.google.com/maps?q={addr_enc}&t=&z=16&ie=UTF8&iwloc=&output=embed", height=420)
            st.markdown('</div>', unsafe_allow_html=True)
            
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Row 2
    r2c1, r2c2 = st.columns(2)
    
    with r2c1:
        with st.container():
            st.markdown('<div class="header-box" style="display:block; padding:15px; border:3px solid #f9d849;">🎯 영업 키포인트', unsafe_allow_html=True)
            if insights:
                for idx, insight in enumerate(insights):
                    st.markdown(f'''
                    <div style="background-color:#e0f7fa; border-left:4px solid #006064; padding:12px; border-radius:4px; margin-bottom:10px;">
                        <span style="font-size:1.8rem;">{'💡' if idx==0 else '✅'}</span>
                        <span style="color:#004d4d; font-weight:500; font-size:1.7rem;">{insight}</span>
                    </div>
                    ''', unsafe_allow_html=True)
            else:
                 st.markdown(f'''
                    <div style="background-color:#e0f7fa; border-left:4px solid #006064; padding:12px; border-radius:4px;">
                        <span style="font-size:1.8rem;">💡</span>
                        <span style="font-size:1.7rem;">특이사항이 없습니다. 정기적인 안부 콜을 통해 관계를 유지하세요.</span>
                    </div>
                    ''', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
    with r2c2:
        with st.container():
            st.markdown('<div class="header-box" style="display:block; padding:15px;">👤 매핑직원', unsafe_allow_html=True)
            rep_name = str(c_data[COL_REP]).strip().replace(' ', '')
            c_img, c_txt = st.columns([0.3, 0.7])
            with c_img:
                if rep_name in staff_photos and staff_photos[rep_name]:
                    st.image(staff_photos[rep_name], width=130)
                else:
                    st.markdown('<div class="no-photo">👤</div>', unsafe_allow_html=True)
            with c_txt:
                st.markdown(f"""
                <div style="font-size:1.8rem; color:#333; line-height:1.6; margin-left:10px;">
                    <b style="font-size:2rem;">{c_data[COL_REP]}</b><br>
                    <span style="color:#666; font-size:1.6rem;">{c_data[df_main.columns[0]]} / {c_data[df_main.columns[1]]} / {c_data[df_main.columns[2]]}</span>
                </div>
                """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<HR style="border-top: 1px dashed #ccc; margin: 40px 0;">', unsafe_allow_html=True)
    col_prod, col_chart = st.columns([0.3, 0.7])
    
    with col_prod:
        with st.container():
             st.markdown('<div class="header-box" style="display:block; padding:15px;">📦 주요 상품 현황', unsafe_allow_html=True)
             if prod_data:
                 for p_name, p_count in prod_data:
                     icon = get_product_icon(p_name)
                     st.markdown(f'''
                     <div class="product-item">
                        <span class="product-name">{icon} {p_name}</span>
                        <span class="product-count">{p_count}회선</span>
                     </div>
                     ''', unsafe_allow_html=True)
             else:
                 st.info("가입 상품 정보 없음")
             st.markdown('</div>', unsafe_allow_html=True)
    with col_chart:
        with st.container():
            st.markdown('<div class="header-box" style="display:block; padding:15px;">📈 매출 추이 분석', unsafe_allow_html=True)
            months = [f"{i}월" for i in range(1, 13)]
            t_vals = [c_data[c] for c in REV_COLS]
            n_vals = [c_data[c] for c in NEW_REV_COLS]
            fig_line = go.Figure()
            fig_line.add_trace(go.Scatter(
                x=months, y=t_vals, name="전체 매출", mode='lines+markers+text',
                text=[format_kr(v) for v in t_vals], textposition='top center',
                line=dict(color='#008080', width=3), marker=dict(size=8, color='#004d4d'),
                textfont=dict(size=14)
            ))
            fig_line.add_trace(go.Scatter(
                x=months, y=n_vals, name="신규 매출", mode='lines+markers+text',
                text=[format_kr(v) for v in n_vals], textposition='top center',
                line=dict(color='#f9d849', width=3), marker=dict(size=8, color='#fbc02d'),
                textfont=dict(size=14)
            ))
            max_v = max(max(t_vals), max(n_vals) if n_vals else [0])
            ticks = [0, max_v*0.5, max_v]
            fig_line.update_layout(
                plot_bgcolor='white', paper_bgcolor='white',
                yaxis=dict(tickmode='array', tickvals=ticks, ticktext=[format_kr(v) for v in ticks], gridcolor='#f0f0f0', tickfont=dict(size=14)),
                xaxis=dict(showgrid=False, tickfont=dict(size=10)),
                legend=dict(orientation="h", y=1.1, x=1, xanchor='right', font=dict(size=11)),
                margin=dict(t=25, b=15, l=15, r=15), height=280
            )
            st.plotly_chart(fig_line, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<br>', unsafe_allow_html=True)
    
    st.markdown('''
    <div class="header-box" style="margin-bottom:15px; background-color:white;">🍩 매출 포트폴리오 (상품별 비중)</div>
    ''', unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    COLORS_TEAL = ['#008080', '#26a69a', '#80cbc4', '#b2dfdb', '#e0f2f1']
    COLORS_GOLD = ['#f9d849', '#fbc02d', '#fff176', '#fff9c4', '#fffde7']
    
    CHART_MARGIN = dict(t=50, b=50, l=50, r=50) 
    
    with c1:
        st.markdown('<div class="header-box" style="justify-content:center; font-size:1rem; margin-bottom:8px;">전체 상품 비중</div>', unsafe_allow_html=True)
        
        p_labels = [str(c_data[pc]) for pc, rc in TOTAL_PROD_REVENUE if pd.notna(c_data[pc]) and c_data[rc] > 0]
        p_values = [c_data[rc] for pc, rc in TOTAL_PROD_REVENUE if pd.notna(c_data[pc]) and c_data[rc] > 0]
        if sum(p_values) < c_data[COL_REV_ANNUAL]:
            p_labels.append("기타")
            p_values.append(c_data[COL_REV_ANNUAL] - sum(p_values))
        fig1 = go.Figure(data=[go.Pie(labels=p_labels, values=p_values, hole=0.5, marker=dict(colors=COLORS_TEAL), textinfo='label+percent', textposition='outside', texttemplate='%{label}<br>%{percent:.1%}')])
        fig1.update_layout(showlegend=False, margin=CHART_MARGIN, height=350, font=dict(size=11))
        st.plotly_chart(fig1, use_container_width=True)
        
    with c2:
        st.markdown('<div class="header-box" style="justify-content:center; font-size:1rem; margin-bottom:8px;">신규 매출 기여도</div>', unsafe_allow_html=True)
        new_rev = c_data[COL_NEW_ANNUAL]
        if new_rev > 0:
            pct = (new_rev/c_data[COL_REV_ANNUAL])*100
            # [수정] 신규를 12시→3시 방향으로 표시 (sort=False, direction='clockwise', rotation=90)
            # Plotly에서 rotation=90은 12시 방향에서 시작, 첫 번째 항목이 신규가 되도록 순서 조정
            fig2 = go.Figure(data=[go.Pie(
                labels=["신규", "기존"], 
                values=[new_rev, c_data[COL_REV_ANNUAL]-new_rev], 
                hole=0.6, 
                marker=dict(colors=['#f9d849', '#eee']), 
                textinfo='label+percent', 
                textposition='outside', 
                texttemplate='%{label}<br>%{percent:.1%}',
                sort=False,  # 순서 유지
                direction='clockwise',  # 시계 방향
                rotation=90  # 12시 방향에서 시작
            )])
            fig2.add_annotation(text=f"{pct:.1f}%", x=0.5, y=0.5, font=dict(size=24, color='#f9d849', family="Arial Black"), showarrow=False)
            fig2.update_layout(showlegend=False, margin=CHART_MARGIN, height=350, font=dict(size=11))
            st.plotly_chart(fig2, use_container_width=True)
        else: st.info("신규 매출 없음")
            
    with c3:
        st.markdown('<div class="header-box" style="justify-content:center; font-size:1rem; margin-bottom:8px;">신규 상품 비중</div>', unsafe_allow_html=True)
        if new_rev > 0:
            n_labels = [str(c_data[pc]) for pc, rc in NEW_PROD_REVENUE if pd.notna(c_data[pc]) and c_data[rc] > 0]
            n_values = [c_data[rc] for pc, rc in NEW_PROD_REVENUE if pd.notna(c_data[pc]) and c_data[rc] > 0]
            fig3 = go.Figure(data=[go.Pie(labels=n_labels, values=n_values, hole=0.5, marker=dict(colors=COLORS_GOLD), textinfo='label+percent', textposition='outside', texttemplate='%{label}<br>%{percent:.1%}')])
            fig3.update_layout(showlegend=False, margin=CHART_MARGIN, height=350, font=dict(size=11))
            st.plotly_chart(fig3, use_container_width=True)
        else: st.info("신규 상품 없음")

st.markdown('<div style="text-align:center; color:#aaa; margin-top:30px; font-size:0.8rem;">Copyright 2025 KT Enterprise Sales Guide</div>', unsafe_allow_html=True)
