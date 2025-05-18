import streamlit as st
import numpy as np
import time
import matplotlib.pyplot as plt

# ✅ 페이지 설정은 반드시 최상단에
st.set_page_config(page_title="정렬 알고리즘 시각화", page_icon="📊", layout="centered")

# 눈 효과 (기본 내장)
st.snow()

# 타이틀
st.title("📊 정렬 알고리즘 시각화")
st.markdown("다양한 정렬 알고리즘의 동작 과정을 시각적으로 확인해보세요!")

# 사이드바 설정
st.sidebar.header("설정")
array_size = st.sidebar.slider("배열 크기", 5, 50, 20)
speed = st.sidebar.slider("정렬 속도", 0.1, 2.0, 0.5)

# 정렬 알고리즘 선택
algorithm = st.sidebar.selectbox(
    "정렬 알고리즘 선택",
    ["버블 정렬", "선택 정렬", "삽입 정렬"]
)

# 랜덤 배열 생성
if 'array' not in st.session_state:
    st.session_state.array = np.random.randint(1, 100, array_size)

# 정렬 함수들
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # 시각화 업데이트
                fig, ax = plt.subplots(figsize=(10, 4))
                ax.bar(range(len(arr)), arr)
                ax.set_title("버블 정렬 진행 중")
                st.pyplot(fig)
                plt.close()
                time.sleep(speed)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        # 시각화 업데이트
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.bar(range(len(arr)), arr)
        ax.set_title("선택 정렬 진행 중")
        st.pyplot(fig)
        plt.close()
        time.sleep(speed)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
            # 시각화 업데이트
            fig, ax = plt.subplots(figsize=(10, 4))
            ax.bar(range(len(arr)), arr)
            ax.set_title("삽입 정렬 진행 중")
            st.pyplot(fig)
            plt.close()
            time.sleep(speed)
        arr[j+1] = key

# 초기 배열 표시
st.subheader("초기 배열")
fig, ax = plt.subplots(figsize=(10, 4))
ax.bar(range(len(st.session_state.array)), st.session_state.array)
ax.set_title("정렬 전 배열")
st.pyplot(fig)
plt.close()

# 정렬 실행 버튼
if st.button("정렬 시작"):
    arr = st.session_state.array.copy()
    
    if algorithm == "버블 정렬":
        bubble_sort(arr)
    elif algorithm == "선택 정렬":
        selection_sort(arr)
    else:
        insertion_sort(arr)
    
    # 정렬 완료 후 결과 표시
    st.subheader("정렬 완료!")
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.bar(range(len(arr)), arr)
    ax.set_title("정렬 후 배열")
    st.pyplot(fig)
    plt.close()

# 새 배열 생성 버튼
if st.button("새 배열 생성"):
    st.session_state.array = np.random.randint(1, 100, array_size)
    st.experimental_rerun()
