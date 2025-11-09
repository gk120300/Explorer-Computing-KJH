import streamlit as st
import os

st.set_page_config(
    page_title="Python 파일 뷰어",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Python 파일 뷰어")
st.markdown("---")

st.header("파일 선택")

# pages 폴더의 파일 목록 가져오기
pages_dir = "pages"
if os.path.exists(pages_dir):
    files = [f for f in os.listdir(pages_dir) if f.endswith('.py')]
else:
    st.error("❌ 'pages' 폴더를 찾을 수 없습니다!")
    st.stop()

if not files:
    st.warning("⚠️ pages 폴더에 Python 파일이 없습니다!")
    st.stop()

# 파일 선택 드롭다운
selected_file = st.selectbox(
    "보고 싶은 파일을 선택하세요:",
    files,
    index=0
)

st.markdown("---")

# 선택된 파일 읽기 및 표시
if selected_file:
    file_path = os.path.join(pages_dir, selected_file)
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.subheader(f"📄 {selected_file}")
    
    with col2:
        st.metric("파일 크기", f"{os.path.getsize(file_path)} bytes")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            file_content = f.read()
        
        # 탭으로 코드와 실행 결과 나누기
        tab1, tab2 = st.tabs(["📝 코드 보기", "▶️ 실행 결과"])
        
        with tab1:
            st.code(file_content, language='python', line_numbers=True)
            
            # 다운로드 버튼
            st.download_button(
                label="💾 파일 다운로드",
                data=file_content,
                file_name=selected_file,
                mime="text/plain"
            )
        
        with tab2:
            st.info("코드를 실행하려면 아래 버튼을 클릭하세요")
            if st.button("▶️ 코드 실행", type="primary"):
                st.markdown("### 실행 결과:")
                try:
                    # 코드 실행 (주의: 실제 환경에서는 보안상 위험할 수 있음)
                    exec_globals = {}
                    exec(file_content, exec_globals)
                    st.success("✅ 코드가 성공적으로 실행되었습니다!")
                except Exception as e:
                    st.error(f"❌ 실행 중 오류 발생: {e}")
    
    except Exception as e:
        st.error(f"❌ 파일을 읽는 중 오류가 발생했습니다: {e}")

st.markdown("---")
st.caption("Python 파일 뷰어 by Claude")

# 사이드바에 파일 목록 표시
with st.sidebar:
    st.header("📁 파일 목록")
    for i, file in enumerate(files, 1):
        if file == selected_file:
            st.success(f"✅ {i}. {file}")
        else:
            st.write(f"{i}. {file}")
