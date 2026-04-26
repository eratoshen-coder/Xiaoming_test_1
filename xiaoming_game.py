import streamlit as st

# 1. 頁面設定
st.set_page_config(page_title="小明的五味冒險", page_icon="🍱", layout="centered")

# 2. 注入華麗卡通風格 CSS
st.markdown("""
<style>
    .stApp { background-color: #FDFCF0; }
    /* 華麗卡通場景卡片 */
    .scene-card {
        background: white; border: 4px solid #333; border-radius: 25px;
        padding: 25px; box-shadow: 10px 10px 0px #FFAA00; margin-bottom: 25px;
    }
    /* 角色名稱標籤 */
    .char-name {
        background: #333; color: #FFD700; padding: 5px 20px;
        border-radius: 50px; font-weight: 900; display: inline-block;
        margin-bottom: 15px; border: 2px solid #333;
    }
    /* 對話文字氣泡感 */
    .dialogue { font-size: 22px; font-weight: 700; color: #333; line-height: 1.6; }
    
    /* 華麗動漫風按鈕 */
    .stButton>button {
        width: 100%; background-color: #FFFFFF; color: #FF8800 !important;
        border: 3px solid #FF8800 !important; border-radius: 15px !important;
        padding: 15px !important; font-size: 18px !important; font-weight: 800 !important;
        box-shadow: 0 6px 0 #FF8800 !important; transition: 0.1s;
    }
    .stButton>button:hover {
        transform: translateY(2px); box-shadow: 0 3px 0 #FF8800 !important;
        background-color: #FF8800 !important; color: white !important;
    }
    /* 結果大卡片 */
    .result-box {
        background: white; border: 6px solid #FF8800; border-radius: 40px;
        padding: 40px; text-align: center; box-shadow: 0 15px 35px rgba(255,136,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# 3. 初始化數據 (使用簡單加分制，避免 list 報錯)
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'scores' not in st.session_state:
    st.session_state.scores = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}

# 4. 華麗場景資料
questions = [
    {
        "icon": "🎒", "place": "校園門口", 
        "story": "期中考終於結束了！小明帥氣地走出校門，感覺大腦已經乾枯...",
        "say": "呼...腦袋徹底當機！現在我需要超重口味的食物來重啟靈魂，走吧！",
        "opts": [("A. 泰式酸辣粉 (酸爽帶勁)", "A"), ("B. 苦甜黑巧舒芙蕾 (大人苦味)", "B"), ("C. 蜂蜜奶油厚鬆餅 (甜蜜爆發)", "C"), ("D. 地獄麻辣大火鍋 (辛辣發散)", "D"), ("E. 雙倍濃鹽濃湯拉麵 (鹹鮮入味)", "E")]
    },
    {
        "icon": "🏮", "place": "東京・巷弄食堂", 
        "story": "小明牽著女朋友的手，在新宿發現一家掛著黃色燈籠的神祕老店。",
        "say": "「親愛的，這家店的味道聞起來好專業！我們點這個招牌試試看？」",
        "opts": [("A. 極致醃漬青梅", "A"), ("B. 炭火焦香銀杏", "B"), ("C. 甜醬嫩燉和牛", "C"), ("D. 哇沙米激辣串燒", "D"), ("E. 熟成醬油醃魚卵", "E")]
    },
    {
        "icon": "🏠", "place": "溫馨老家廚房", 
        "story": "推開門，鍋鏟與鐵鍋的敲擊聲傳來，是媽媽正在準備大餐。",
        "say": "「好香啊！媽，今天該不會是準備了我最愛的那一道吧？」",
        "opts": [("A. 秘製祖傳糖醋肉", "A"), ("B. 降火微苦排骨湯", "B"), ("C. 補氣山藥地瓜甜湯", "C"), ("D. 辛香爆蔥快炒肉", "D"), ("E. 鹹鮮入味紅燒肉", "E")]
    },
    {
        "icon": "🎂", "place": "KTV 派對現場", 
        "story": "霓虹燈閃爍，朋友們都在起鬨，輪到小明決定慶生蛋糕的口味。",
        "say": "「既然是慶祝，口味絕對要挑最令人難忘的那種才行！」",
        "opts": [("A. 爆漿檸檬塔", "A"), ("B. 炭焙苦咖啡蛋糕", "B"), ("C. 傳統古法大布丁", "C"), ("D. 肉桂生薑香料糕", "D"), ("E. 海鹽焦糖起司糕", "E")]
    },
    {
        "icon": "🎬", "place": "深夜沙發", 
        "story": "半夜兩點，劇集正播到高潮，小明的肚子卻大聲抗議。",
        "say": "「可惡...不來點靈魂零食，我真的會餓到沒法專心看大結局！」",
        "opts": [("A. 瞇眼超級酸蜜餞", "A"), ("B. 濃郁厚抹茶苦飲", "B"), ("C. 軟Q牛奶大糖球", "C"), ("D. 嗆鼻哇沙米脆餅", "D"), ("E. 厚切煙燻牛肉乾", "E")]
    }
]

# 5. 介面渲染
if st.session_state.step < len(questions):
    q = questions[st.session_state.step]
    st.markdown(f"<h1 style='text-align: center; color: #FF8800;'>{q['icon']} 小明的冒險</h1>", unsafe_allow_html=True)
    st.progress((st.session_state.step) / len(questions))
    
    st.markdown(f"""
    <div class="scene-card">
        <div class="char-name">📍 {q['place']}</div>
        <p style='color: #888; font-style: italic; font-size: 16px;'>{q['story']}</p>
        <hr style="border: 1px dashed #DDD;">
        <div class="dialogue">小明：「{q['say']}」</div>
    </div>
    """, unsafe_allow_html=True)
    
    for btn_text, code in q['opts']:
        if st.button(btn_text, key=f"btn_{st.session_state.step}_{code}"):
            st.session_state.scores[code] += 1
            st.session_state.step += 1
            st.rerun()

else:
    # 6. 結果計算 (使用加分制，絕對不會有 list 報錯)
    st.balloons()
    st.markdown("<h1 style='text-align: center; color: #FF8800;'>🔮 探險終點</h1>", unsafe_allow_html=True)
    
    # 找出最高分的字母
    final_type = max(st.session_state.scores, key=st.session_state.scores.get)

    results_map = {
        "A": {"title": "🍋 偏好「酸」味 —— 肝氣偏盛型", "desc": "在生活中，你是個精明且追求效率的人，做事乾脆俐落，但也可能代表你目前的狀態比較緊繃。"},
        "B": {"title": "☕ 偏好「苦」味 —— 心氣偏盛型", "desc": "這代表你擁有超越同齡人的成熟感，在朋友圈中是個可靠的守護者，默默承擔著責任。"},
        "C": {"title": "🍯 偏好「甘」味 —— 脾氣偏盛型", "desc": "你追求甜蜜與穩定。性格溫和、熱愛和平，是大家眼中的開心果，但有時會因為太愛安逸而忘了前進。"},
        "D": {"title": "🌶️ 偏好「辛」味 —— 肺氣偏盛型", "desc": "你喜歡熱情奔放的挑戰！直來直往、非常有正義感，是行動派代表，但也容易耗損元氣。"},
        "E": {"title": "🧂 偏好「鹹」味 —— 腎氣偏盛型", "desc": "你行事踏實、注重細節，是腳踏實地的實踐家，但要注意適時放鬆壓力。"}
    }
    
    res = results_map[final_type]
    
    st.markdown(f"""
    <div class="result-box">
        <h2 style='color: #FF8800;'>{res['title']}</h2>
        <hr style="border: 2px solid #FF8800;">
        <p style='font-size: 20px; line-height: 1.8; color: #333;'>
            <b>【生活樣貌】</b><br>{res['desc']}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("再陪小明冒險一次"):
        st.session_state.step = 0
        st.session_state.scores = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
        st.rerun()
