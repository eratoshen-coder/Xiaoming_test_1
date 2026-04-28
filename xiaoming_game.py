import streamlit as st

# 1. 頁面設定
st.set_page_config(page_title="小明的五味冒險", page_icon="🍱", layout="centered")

# 2. 注入動漫風格 CSS
st.markdown("""
<style>
    .stApp { background-color: #FDFCF0; }
    .img-box { border: 4px solid #333; border-radius: 20px; overflow: hidden; box-shadow: 10px 10px 0px #FFAA00; margin-bottom: 20px; text-align: center; }
    .dialogue-card { background: white; border: 4px solid #333; border-radius: 20px; padding: 25px; box-shadow: 5px 5px 0px #333; }
    .char-label { background: #333; color: #FFD700; padding: 5px 20px; border-radius: 50px; font-weight: bold; display: inline-block; margin-bottom: 10px; }
    .dialogue-text { font-size: 22px; font-weight: bold; color: #333; line-height: 1.6; }
    .stButton>button { width: 100%; background-color: white !important; color: #FF8800 !important; border: 3px solid #FF8800 !important; border-radius: 15px !important; padding: 15px !important; font-size: 20px !important; font-weight: bold !important; box-shadow: 0 4px 0 #FF8800 !important; }
</style>
""", unsafe_allow_html=True)

# 3. 初始化狀態
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'scores' not in st.session_state:
    st.session_state.scores = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}

# 4. 題目資料
questions = [
    {"p": "校園出口", "i": "image_0.png", "s": "期中考完啦！小明走出校門。", "d": "大腦電力 0%...現在必須吃點重口味的！", "o": [("A. 泰式酸辣粉", "A"), ("B. 苦甜黑巧", "B"), ("C. 蜂蜜鬆餅", "C"), ("D. 麻辣火鍋", "D"), ("E. 濃鹽拉麵", "E")]},
    {"p": "東京巷弄", "i": "image1.png", "s": "夜晚的東京居酒屋街。", "d": "這家店的味道聞起來好專業！點這道？", "o": [("A. 醃漬青梅", "A"), ("B. 焦香銀杏", "B"), ("C. 甜醬燉肉", "C"), ("D. 激辣串燒", "D"), ("E. 醬油魚卵", "E")]},
    {"p": "溫馨老家", "i": "image2.png", "s": "推開家門，飯菜香味撲鼻。", "d": "媽！今天的主菜是我最喜歡的那道嗎？", "o": [("A. 糖醋排骨", "A"), ("B. 苦瓜排骨湯", "B"), ("C. 山藥甜湯", "C"), ("D. 爆蔥快炒", "D"), ("E. 紅燒肉", "E")]},
    {"p": "KTV派對", "i": "image3.png", "s": "霓虹燈閃爍，朋友們都在起鬨。", "d": "口味絕對要挑最令人難忘的那種！", "o": [("A. 檸檬塔", "A"), ("B. 咖啡蛋糕", "B"), ("C. 大布丁", "C"), ("D. 香料蛋糕", "D"), ("E. 起司蛋糕", "E")]},
    {"p": "深夜沙發", "i": "image4.png", "s": "半夜兩點，劇集正播到高潮。", "d": "不來點零食，沒法專心看大結局啊！", "o": [("A. 酸蜜餞", "A"), ("B. 抹茶飲", "B"), ("C. 牛奶糖", "C"), ("D. 哇沙米", "D"), ("E. 牛肉乾", "E")]}
]

# 5. 畫面顯示
if st.session_state.step < len(questions):
    q = questions[st.session_state.step]
    st.markdown(f"<h1 style='text-align: center; color: #FF8800;'>小明的探險 ({st.session_state.step + 1}/5)</h1>", unsafe_allow_html=True)
    
    st.markdown('<div class="img-box">', unsafe_allow_html=True)
    st.image(q["i"], use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(f"<div class='dialogue-card'><div class='char-label'>📍 {q['p']}</div><p>{q['s']}</p><hr><div class='dialogue-text'>小明：{q['d']}</div></div>", unsafe_allow_html=True)
    
    st.write("---")
    for btn_text, code in q['o']:
        if st.button(btn_text, key=f"btn_{st.session_state.step}_{code}"):
            st.session_state.scores[code] += 1
            st.session_state.step += 1
            st.rerun()
else:
    st.balloons()
    win = max(st.session_state.scores, key=st.session_state.scores.get)
    res = {"A": "肝氣偏盛型：效率高、做事乾脆。", "B": "心氣偏盛型：成熟、可靠守護者。", "C": "脾氣偏盛型：穩重、性格溫和。", "D": "肺氣偏盛型：冒險、直爽正義。", "E": "腎氣偏盛型：踏實、注重細節。"}[win]
    st.markdown(f"<div style='background: white; border: 6px solid #FF8800; border-radius: 30px; padding: 40px; text-align: center;'><h2>測驗結果</h2><hr><h3>{res}</h3></div>", unsafe_allow_html=True)
    if st.button("再次測驗"):
        st.session_state.step = 0
        st.session_state.scores = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
        st.rerun()
