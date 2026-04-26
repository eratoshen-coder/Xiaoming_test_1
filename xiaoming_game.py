import streamlit as st
from collections import Counter

# 1. 網頁基本設定
st.set_page_config(page_title="小明的五味靈魂探險", page_icon="🍱", layout="centered")

# 2. 注入華麗卡通風格 CSS (模擬動漫對話框)
st.markdown("""
<style>
    /* 整體背景：溫暖的日系米色 */
    .stApp {
        background-color: #FDFCF0;
    }
    /* 卡通場景卡片 */
    .scene-card {
        background: white;
        border: 4px solid #333;
        border-radius: 25px;
        padding: 25px;
        box-shadow: 10px 10px 0px #FFAA00;
        margin-bottom: 25px;
    }
    /* 角色名稱標籤 */
    .char-name {
        background: #333;
        color: #FFD700;
        padding: 5px 20px;
        border-radius: 50px;
        font-weight: 900;
        display: inline-block;
        margin-bottom: 15px;
        border: 2px solid #333;
    }
    /* 對話文字 */
    .dialogue {
        font-size: 22px;
        font-weight: 700;
        color: #333;
        line-height: 1.6;
    }
    /* 華麗動漫風按鈕 */
    .stButton>button {
        width: 100%;
        background-color: #FFFFFF;
        color: #FF8800 !important;
        border: 3px solid #FF8800 !important;
        border-radius: 15px !important;
        padding: 15px !important;
        font-size: 18px !important;
        font-weight: 800 !important;
        box-shadow: 0 6px 0 #FF8800 !important;
        transition: 0.1s;
    }
    .stButton>button:hover {
        transform: translateY(2px);
        box-shadow: 0 3px 0 #FF8800 !important;
        background-color: #FF8800 !important;
        color: white !important;
    }
    /* 結果大卡片 */
    .result-box {
        background: white;
        border: 6px solid #FF8800;
        border-radius: 40px;
        padding: 40px;
        text-align: center;
        box-shadow: 0 15px 35px rgba(255,136,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# 3. 初始化遊戲數據
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'answers' not in st.session_state:
    st.session_state.answers = []

# 4. 華麗場景資料庫
questions = [
    {
        "icon": "🎒", "place": "校園門口", 
        "story": "期中考考完啦！小明帥氣地走出校門，陽光灑在他的背影上。",
        "say": "「呼...大腦已經乾枯了。走吧！現在必須吃點重口味的來重新啟動靈魂！」",
        "opts": [("A. 泰式酸辣粉 (酸爽帶勁)", "A"), ("B. 苦甜黑巧舒芙蕾 (大人苦味)", "B"), ("C. 蜂蜜奶油厚鬆餅 (甜蜜爆發)", "C"), ("D. 地獄麻辣大火鍋 (辛辣發散)", "D"), ("E. 雙倍濃鹽濃湯拉麵 (鹹鮮入味)", "E")]
    },
    {
        "icon": "🏮", "place": "東京・巷弄食堂", 
        "story": "小明牽著女朋友的手，在新宿的巷弄發現一家掛著黃色燈籠的神祕老店。",
        "say": "「親愛的，這家店的味道聞起來好專業！我們點這個招牌試試看？」",
        "opts": [("A. 極致醃漬青梅", "A"), ("B. 炭火焦香銀杏", "B"), ("C. 甜醬嫩燉和牛", "C"), ("D. 哇沙米激辣串燒", "D"), ("E. 熟成醬油醃魚卵", "E")]
    },
    {
        "icon": "🏠", "place": "溫馨老家廚房", 
        "story": "推開家門，鍋鏟與鐵鍋的敲擊聲傳來，是媽媽正在揮汗準備大餐。",
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
        "icon": "🎬", "place": "深夜追劇沙發", 
        "story": "半夜兩點，劇集正播到高潮，小明的肚子卻不爭氣地咕嚕咕嚕大聲抗議。",
        "say": "「可惡...不來點零魂零食，我真的會餓到沒法專心看大結局！」",
        "opts": [("A. 瞇眼超級酸蜜餞", "A"), ("B. 濃郁厚抹茶苦飲", "B"), ("C. 軟Q牛奶大糖球", "C"), ("D. 嗆鼻哇沙米脆餅", "D"), ("E. 厚切煙燻牛肉乾", "E")]
    }
]

# 5. 遊戲畫面渲染
if st.session_state.step < len(questions):
    q = questions[st.session_state.step]
    st.markdown(f"<h1 style='text-align: center; color: #FF8800;'>{q['icon']} 小明的冒險</h1>", unsafe_allow_html=True)
    st.progress((st.session_state.step) / len(questions))
    
    # 渲染卡通場景卡片
    st.markdown(f"""
    <div class="scene-card">
        <div class="char-name">📍 {q['place']}</div>
        <p style='color: #888; font-style: italic; font-size: 16px;'>{q['story']}</p>
        <hr style="border: 1px dashed #DDD;">
        <div class="dialogue">小明：「{q['say']}」</div>
    </div>
    """, unsafe_allow_html=True)
    
    # 渲染按鈕
    for btn_text, code in q['opts']:
        if st.button(btn_text, key=f"q{st.session_state.step}_{code}"):
            st.session_state.answers.append(code)
            st.session_state.step += 1
            st.rerun()

else:
    # 6. 結果計算與顯示 (修復 TypeError 關鍵點)
    st.balloons()
    st.markdown("<h1 style='text-align: center; color: #FF8800;'>🔮 探險終點：你的靈魂味覺</h1>", unsafe_allow_html=True)
    
    # 正確取出出現次數最多的「字母」字串
    if st.session_state.answers:
        counts = Counter(st.session_state.answers)
        final_letter = counts.most_common(1) # 這會得到 'A', 'B', 'C' 等字串
    else:
        final_letter = "C"

    # 生活樣貌結果字典
    results_map = {
        "A": {"title": "🍋 偏好「酸」味 —— 肝氣偏盛型", "desc": "在小明的冒險中，你總是選擇清爽收斂。在生活中，你是個精明且追求效率的人，做事乾脆俐落，但也可能代表你目前的狀態比較緊繃。"},
        "B": {"title": "☕ 偏好「苦」味 —— 心氣偏盛型", "desc": "你選擇了沉穩的苦味。這代表你擁有超越同齡人的成熟感，在朋友圈中是個可靠的守護者，默默承擔著責任。"},
        "C": {"title": "🍯 偏好「甘」味 —— 脾氣偏盛型", "desc": "你追求甜蜜與穩定。在生活中，你性格溫和、熱愛和平，是大家眼中的開心果，但有時會因為太愛安逸而忘了前進。"},
        "D": {"title": "🌶️ 偏好「辛」味 —— 肺氣偏盛型", "desc": "你喜歡熱情奔放的挑戰！生活中你直來直往、非常有正義感，是行動派的代表，但也容易因為衝動而耗損元氣。"},
        "E": {"title": "🧂 偏好「鹹」味 —— 腎氣偏盛型", "desc": "你偏好厚實且紮實的層次感。生活中你行事踏實、注重細節，是腳踏實地的實踐家，但要注意適時放鬆。"}
    }
    
    # 確保使用單個字串作為 Key
    res = results_map.get(final_letter, results_map["C"])
    
    st.markdown(f"""
    <div class="result-box">
        <h2 style='color: #FF8800;'>{res['title']}</h2>
        <hr style="border: 2px solid #FF8800;">
        <p style='font-size: 22px; line-height: 1.8; color: #333;'>
            <span style="background-color: #FFD700; padding: 2px 10px; border-radius: 5px;">生活樣貌</span><br><br>
            {res['desc']}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("再陪小明冒險一次"):
        st.session_state.step = 0
        st.session_state.answers = []
        st.rerun()
