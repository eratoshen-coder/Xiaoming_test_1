import streamlit as st

# 1. 頁面設定
st.set_page_config(page_title="小明的冒險", page_icon="🍱", layout="centered")

# 2. 注入動漫風格 CSS
st.markdown("""
<style>
    .stApp { background-color: #FDFCF0; }
    .img-box { border: 4px solid #333; border-radius: 20px; overflow: hidden; box-shadow: 10px 10px 0px #FFAA00; margin-bottom: 20px; }
    .dialogue-card { background: white; border: 4px solid #333; border-radius: 20px; padding: 25px; box-shadow: 5px 5px 0px #333; }
    .char-label { background: #333; color: #FFD700; padding: 5px 20px; border-radius: 50px; font-weight: bold; display: inline-block; margin-bottom: 10px; }
    .dialogue-text { font-size: 22px; font-weight: bold; color: #333; line-height: 1.6; }
    .stButton>button { width: 100%; background-color: white !important; color: #FF8800 !important; border: 3px solid #FF8800 !important; border-radius: 15px !important; padding: 15px !important; font-size: 20px !important; font-weight: bold !important; box-shadow: 0 4px 0 #FF8800 !important; margin-bottom: 10px; }
    .stButton>button:hover { background-color: #FF8800 !important; color: white !important; transform: translateY(2px); box-shadow: 0 1px 0 #FF8800 !important; }
</style>
""", unsafe_allow_html=True)

# 3. 初始化數據
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'scores' not in st.session_state:
    st.session_state.scores = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}

# 4. 題目資料
questions = [
    {"icon": "🎒", "place": "校園出口", "img": "image_0.png", "story": "期中考完啦！小明走出校門。", "say": "「大腦電力 0%...現在必須吃點重口味的！」", "opts": [("A. 泰式酸辣粉 (酸爽)", "A"), ("B. 苦甜黑巧舒芙蕾 (大人苦)", "B"), ("C. 蜂蜜奶油厚鬆餅 (甜蜜)", "C"), ("D. 地獄麻辣大火鍋 (辛辣)", "D"), ("E. 雙倍濃鹽拉麵 (鹹鮮)", "E")]},
    {"icon": "🏮", "place": "東京巷弄", "img": "image_1.png", "story": "夜晚的東京居酒屋街。", "say": "「這家店的味道聞起來好專業！點這道？」", "opts": [("A. 極致醃漬青梅", "A"), ("B. 炭火焦香銀杏", "B"), ("C. 甜醬嫩燉和牛", "C"), ("D. 哇沙米激辣串燒", "D"), ("E. 醬油醃漬魚卵", "E")]},
    {"icon": "🏠", "place": "溫馨老家", "img": "image_2.png", "story": "推開家門，飯菜香味撲鼻。", "say": "「媽！今天的主菜是我最喜歡的那道嗎？」", "opts": [("A. 秘製糖醋排骨", "A"), ("B. 降火微苦排骨湯", "B"), ("C. 山藥地瓜甜湯", "C"), ("D. 辛香爆蔥快炒肉", "D"), ("E. 紅燒鹹香獅子頭", "E")]},
    {"icon": "🎉", "place": "KTV 派對", "img": "image_3.png", "story": "霓虹燈閃爍，朋友們都在起鬨。", "say": "「口味絕對要挑最令人難忘的那種！」", "opts": [("A. 爆漿檸檬塔", "A"), ("B. 炭焙苦咖啡蛋糕", "B"), ("C. 傳統古法大布丁", "C"), ("D. 肉桂生薑香料糕", "D"), ("E. 海鹽焦糖起司蛋糕", "E")]},
    {"icon": "🎬", "place": "深夜沙發", "img": "image_4.png", "story": "半夜兩點，劇集正播到高潮。", "say": "「不來點零食，沒法專心看大結局啊！」", "opts": [("A. 瞇眼超級酸蜜餞", "A"), ("B. 濃郁厚抹茶苦飲", "B"), ("C. 軟Q牛奶大糖球", "C"), ("D. 嗆鼻哇沙米脆餅", "D"), ("E. 厚切煙燻牛肉乾", "E")]}
]

# 5. 遊戲主畫面
if st.session_state.step < len(questions):
    q = questions[st.session_state.step]
    st.markdown(f"<h1 style='text-align: center; color: #FF8800;'>{q['icon']} 小明的探險</h1>", unsafe_allow_html=True)
    
    # 改為上下排列，完全不使用 st.columns 以確保穩定性
    st.markdown('<div class="img-box">', unsafe_allow_html=True)
    try:
        st.image(q["img"], use_container_width=True)
    except:
        st.warning(f"請確認 GitHub 已上傳圖片: {q['img']}")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class='dialogue-card'>
        <div class='char-label'>📍 {q['place']}</div>
        <p style='color: #666;'>{q['story']}</p>
        <hr>
        <div class='dialogue-text'>小明：「{q['say']}」</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    for btn_text, code in q['opts']:
        if st.button(btn_text, key=f"q_{st.session_state.step}_{code}"):
            st.session_state.scores[code] += 1
            st.session_state.step += 1
            st.rerun()
else:
    # 6. 結果顯示
    st.balloons()
    final_type = max(st.session_state.scores, key=st.session_state.scores.get)
    res_map = {
        "A": "肝氣偏盛型：追求效率、做事乾脆，但也可能代表你目前比較緊繃。",
        "B": "心氣偏盛型：擁有成熟感，是朋友圈中可靠的守護者。",
        "C": "脾氣偏盛型：追求穩定與甜蜜。性格溫和熱愛和平。",
        "D": "肺氣偏盛型：熱愛挑戰！直來直往有正義感，是行動派代表。",
        "E": "腎氣偏盛型：行事踏實注重細節，是腳踏實地的實踐家。"
    }
    st.markdown(f"""
    <div style='background: white; border: 6px solid #FF8800; border-radius: 30px; padding: 40px; text-align: center;'>
        <h2 style='color: #FF8800;'>測驗結果</h2>
        <hr>
        <p style='font-size: 22px; font-weight: bold;'>{res_map[final_type]}</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("再陪小明冒險一次"):
        st.session_state.step = 0
        st.session_state.scores = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
        st.rerun()
