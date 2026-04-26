import streamlit as st
from collections import Counter

# 1. 網頁基本設定
st.set_page_config(page_title="小明的五味靈魂探險", page_icon="🎨", layout="centered")

# 2. 華麗視覺樣式 (CSS)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #fdfcf0 0%, #fff9e6 100%);
    }
    .scenario-container {
        background: white;
        padding: 30px;
        border-radius: 30px;
        border: 4px solid #ffcc00;
        box-shadow: 10px 10px 0px #ffaa00;
        margin-bottom: 25px;
    }
    .character-bubble {
        background: #f0f0f0;
        border: 2px solid #333;
        padding: 15px;
        border-radius: 15px;
        font-weight: bold;
        color: #333;
    }
    .stButton>button {
        background: white;
        color: #ff8800;
        border: 3px solid #ff8800;
        border-radius: 50px;
        font-size: 18px;
        font-weight: bold;
        box-shadow: 0 5px 0 #ff8800;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: translateY(-3px);
        background: #ff8800;
        color: white;
    }
    .result-card {
        background: white;
        border: 5px solid #ffaa00;
        padding: 30px;
        border-radius: 30px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 初始化狀態
if 'step' not in st.session_state:
    st.session_state.step = 0
    st.session_state.answers = []

# 4. 題目資料
questions = [
    {
        "icon": "🏫", "scene_name": "校園出口", 
        "scene": "期中考終於結束了，夕陽照在校門口，小明伸了一個大懶腰！",
        "dialogue": "「終於考完了！我現在大腦需要重口味的補充，走吧！」",
        "options": [("A. 泰式檸檬魚配酸辣粉", "A"), ("B. 特濃苦甜巧克力舒芙蕾", "B"), ("C. 蜂蜜奶油厚鬆餅", "C"), ("D. 地獄麻辣火鍋", "D"), ("E. 雙倍鹽度日式拉麵", "E")]
    },
    {
        "icon": "🏮", "scene_name": "東京巷弄", 
        "scene": "小明跟女朋友在旅行，走進一家掛滿紅燈籠的神祕居酒屋。",
        "dialogue": "「這裡氣氛真好！我們點這道招牌料理來試試看吧？」",
        "options": [("A. 醋漬青梅涼菜", "A"), ("B. 鹽烤焦香銀杏", "B"), ("C. 甜醬燉黑毛和牛", "C"), ("D. 七味粉辣雞串燒", "D"), ("E. 醬油醃漬生魚卵", "E")]
    },
    {
        "icon": "🍲", "scene_name": "老家廚房", 
        "scene": "一回到家，廚房就傳來陣陣香味，是媽媽正在準備晚餐。",
        "dialogue": "「媽！好香喔！今天的主菜是我最喜歡的那道嗎？」",
        "options": [("A. 秘製糖醋排骨", "A"), ("B. 降火苦瓜排骨湯", "B"), ("C. 山藥地瓜甜湯", "C"), ("D. 爆蔥乾煸牛肉", "D"), ("E. 紅燒鹹香獅子頭", "E")]
    },
    {
        "icon": "🎉", "scene_name": "慶生派對", 
        "scene": "KTV包廂裡燈光閃爍，輪到小明決定要訂哪種口味的蛋糕。",
        "dialogue": "「既然是慶祝，口味絕對要挑最令人難忘的那種！」",
        "options": [("A. 極致檸檬塔", "A"), ("B. 深焙咖啡慕斯", "B"), ("C. 經典布丁大蛋糕", "C"), ("D. 薑汁肉桂香料蛋糕", "D"), ("E. 海鹽焦糖起司蛋糕", "E")]
    },
    {
        "icon": "🎬", "scene_name": "深夜沙發", 
        "scene": "半夜追劇正精彩，小明的肚子卻不爭氣地大聲抗議了。",
        "dialogue": "「可惡...這時候如果不來點靈魂零食，根本看不下去！」",
        "options": [("A. 檸檬蜜餞", "A"), ("B. 厚抹抹茶飲", "B"), ("C. 牛奶糖/龍鬚糖", "C"), ("D. 哇沙米脆餅", "D"), ("E. 煙燻辣味牛肉乾", "E")]
    }
]

# 5. 遊戲邏輯與畫面顯示
if st.session_state.step < len(questions):
    curr = questions[st.session_state.step]
    st.markdown(f"<h1 style='text-align: center; color: #ff8800;'>{curr['icon']} 小明的日常探險</h1>", unsafe_allow_html=True)
    st.progress((st.session_state.step) / len(questions))
    
    st.markdown(f"""
    <div class="scenario-container">
        <b style='color: #ffaa00;'>📍 {curr['scene_name']}</b>
        <p style='color: #666; font-style: italic;'>{curr['scene']}</p>
        <div class="character-bubble">小明：「{curr['dialogue']}」</div>
    </div>
    """, unsafe_allow_html=True)
    
    for text, code in curr['options']:
        if st.button(text, key=f"btn_{st.session_state.step}_{code}"):
            st.session_state.answers.append(code)
            st.session_state.step += 1
            st.rerun()

else:
    # 6. 計算與結果顯示
    st.balloons()
    st.markdown("<h1 style='text-align: center; color: #ff8800;'>🔮 探險終點：你的靈魂味覺</h1>", unsafe_allow_html=True)
    
    # 防止空名單報錯
    if st.session_state.answers:
        final_answer = Counter(st.session_state.answers).most_common(1)
    else:
        final_answer = "C"

    results = {
        "A": {"title": "🍋 偏好「酸」味 —— 肝氣偏盛型", "desc": "在小明的冒險中，你總是選擇清爽收斂。在生活中，你是個精明且追求效率的人，做事乾脆，但也可能代表你目前的狀態比較緊繃。"},
        "B": {"title": "☕ 偏好「苦」味 —— 心氣偏盛型", "desc": "你選擇了沉穩的苦味。這代表你擁有超越年齡的成熟心智，生活中你是個可靠的避風港。"},
        "C": {"title": "🍯 偏好「甘」味 —— 脾氣偏盛型", "desc": "你追求甜蜜與穩定。在生活中，你性格溫和、熱愛和平，但有時會因為太愛安逸而忘了前進。"},
        "D": {"title": "🌶️ 偏好「辛」味 —— 肺氣偏盛型", "desc": "你喜歡熱情奔放的快感！生活中你直來直往、熱愛挑戰，是朋友圈中的點火器。"},
        "E": {"title": "🧂 偏好「鹹」味 —— 腎氣偏盛型", "desc": "你偏好厚實且入味的層次感。生活中你行事踏實，是腳踏實地的實踐家。"}
    }
    
    res = results[final_answer]
    st.markdown(f"""
    <div class="result-card">
        <h2 style='color: #ff8800;'>{res['title']}</h2>
        <hr>
        <p style='font-size: 20px; line-height: 1.6; color: #444;'><b>生活樣貌：</b><br>{res['desc']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("再陪小明冒險一次"):
        st.session_state.step = 0
        st.session_state.answers = []
        st.rerun()
