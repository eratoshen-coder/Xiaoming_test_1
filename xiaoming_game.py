import streamlit as st
from collections import Counter

# 頁面設定
st.set_page_config(page_title="小明的五味靈魂探險", page_icon="🎨", layout="centered")

# --- 華麗 CSS 樣式表 ---
st.markdown("""
    <style>
    /* 整體背景：溫暖的日系卡通色調 */
    .stApp {
        background: linear-gradient(135deg, #fdfcf0 0%, #fff9e6 100%);
    }

    /* 華麗場景卡片 */
    .scenario-container {
        background: white;
        padding: 30px;
        border-radius: 30px;
        border: 4px solid #ffcc00;
        box-shadow: 10px 10px 0px #ffaa00;
        margin-bottom: 25px;
        position: relative;
    }

    /* 角色對話框氣泡 */
    .character-bubble {
        background: #fff;
        border: 3px solid #333;
        padding: 15px;
        border-radius: 20px;
        position: relative;
        font-size: 18px;
        font-weight: bold;
        color: #333;
        margin-top: 10px;
    }

    .character-name {
        background: #333;
        color: #fff;
        padding: 5px 15px;
        border-radius: 10px;
        font-size: 14px;
        display: inline-block;
        margin-bottom: 5px;
    }

    /* 按鈕樣式：華麗 3D 感 */
    .stButton>button {
        background: white;
        color: #ff8800;
        border: 3px solid #ff8800;
        border-radius: 50px;
        padding: 10px 20px;
        font-size: 18px;
        font-weight: 800;
        transition: all 0.3s ease;
        box-shadow: 0 5px 0 #ff8800;
        margin-bottom: 10px;
    }

    .stButton>button:hover {
        transform: translateY(-3px);
        background: #ff8800;
        color: white;
        box-shadow: 0 8px 0 #cc6600;
    }

    .stButton>button:active {
        transform: translateY(2px);
        box-shadow: 0 2px 0 #cc6600;
    }

    /* 進度條美化 */
    .stProgress > div > div > div > div {
        background-color: #ffaa00;
    }

    /* 結果標題 */
    .result-card {
        background: linear-gradient(135deg, #ffffff 0%, #fff4e6 100%);
        border: 5px solid #ffaa00;
        padding: 40px;
        border-radius: 40px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 初始化遊戲狀態
if 'step' not in st.session_state:
    st.session_state.step = 0
    st.session_state.answers = []

# --- 題目情境資料庫 ---
questions = [
    {
        "icon": "🏫",
        "scene_name": "校園出口・慶祝時刻",
        "scene": "夕陽灑在校門口，小明把課本用力塞進背包，對著剛考完試的死黨揮手！",
        "dialogue": "「終於考完了！我現在大腦需要重油重口味的補給，誰都別攔我！」",
        "options": [
            ("A. 泰式檸檬魚配酸辣粉（就是要酸爽）", "A"),
            ("B. 特濃苦甜巧克力（大人的慶祝）", "B"),
            ("C. 蜂蜜奶油厚鬆餅（甜到心坎裡）", "C"),
            ("D. 川味地獄麻辣火鍋（辣到發汗）", "D"),
            ("E. 雙倍鹽度日式拉麵（重鹹萬歲）", "E")
        ]
    },
    {
        "icon": "🏮",
        "scene_name": "東京巷弄・居酒屋時光",
        "scene": "小明跟女朋友在熱鬧的歌舞伎町迷路了，誤打誤撞進了一間掛滿紅燈籠的店。",
        "dialogue": "「寶貝你看，這家店氛圍超讚！我們點這道主廚推薦的如何？」",
        "options": [
            ("A. 醋漬青梅涼菜", "A"),
            ("B. 鹽烤焦香銀杏", "B"),
            ("C. 甜醬燉黑毛和牛", "C"),
            ("D. 七味粉激辛雞串燒", "D"),
            ("E. 醬油醃漬生魚卵", "E")
        ]
    },
    {
        "icon": "🍲",
        "scene_name": "老家廚房・媽媽的味道",
        "scene": "一推開門，廚房傳來滋滋作響的聲音，那是記憶中最熟悉的味道。",
        "dialogue": "「媽，我回來了！好香喔...今天的主菜難道是那個？」",
        "options": [
            ("A. 秘製糖醋排骨", "A"),
            ("B. 降火苦瓜排骨湯", "B"),
            ("C. 山藥地瓜甜湯", "C"),
            ("D. 爆蔥乾煸牛肉", "D"),
            ("E. 紅燒鹹香獅子頭", "E")
        ]
    },
    {
        "icon": "🎉",
        "scene_name": "歡樂派對・壽星最大",
        "scene": "KTV包廂燈光閃爍，小明拿著蛋糕目錄，正陷入嚴重的選恐中。",
        "dialogue": "「今天這場派對，蛋糕的口味絕對要驚豔全場才行！」",
        "options": [
            ("A. 極致檸檬塔（酸勁十足）", "A"),
            ("B. 深焙咖啡慕斯（優雅微苦）", "B"),
            ("C. 經典大布丁蛋糕（甜蜜補給）", "C"),
            ("D. 薑汁肉桂香料蛋糕（獨特辛香）", "D"),
            ("E. 海鹽焦糖起司蛋糕（鹹甜濃郁）", "E")
        ]
    },
    {
        "icon": "🛋️",
        "scene_name": "深夜沙發・追劇靈魂",
        "scene": "半夜兩點，小明正看到劇情的關鍵時刻，肚子卻響得比音響還大聲。",
        "dialogue": "「可惡...這時候如果不來點重口味的，根本睡不著啊！」",
        "options": [
            ("A. 檸檬蜜餞", "A"),
            ("B. 厚抹抹茶飲", "B"),
            ("C. 牛奶糖/龍鬚糖", "C"),
            ("D. 哇沙米脆餅", "D"),
            ("E. 煙燻辣味牛肉乾", "E")
        ]
    }
]

# --- 遊戲邏輯顯示 ---
if st.session_state.step < len(questions):
    curr = questions[st.session_state.step]
    
    st.markdown(f"<h1 style='text-align: center; color: #ff8800;'>{curr['icon']} 小明的冒險</h1>", unsafe_allow_html=True)
    st.progress((st.session_state.step) / len(questions))
    
    # 場景顯示區
    st.markdown(f"""
    <div class="scenario-container">
        <span class="character-name">📍 {curr['scene_name']}</span>
        <p style='font-size: 18px; color: #666; font-style: italic;'>{curr['scene']}</p>
        <div class="character-bubble">
            小明：「{curr['dialogue']}」
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 選項顯示
    st.write("---")
    st.markdown("<p style='text-align: center; font-weight: bold;'>如果是你，會選哪一個呢？</p>", unsafe_allow_html=True)
    
    # 建立按鈕
    for text, code in curr['options']:
        if st.button(text, key=text):
            st.session_state.answers.append(code)
            st.session_state.step += 1
            st.rerun()

else:
    # --- 結果計算與華麗顯示 ---
    st.balloons()
    st.markdown("<h1 style='text-align: center; color: #ff8800;'>🔮 探險終點：你的靈魂味覺</h1>", unsafe_allow_html=True)
    
    final_answer = Counter(st.session_state.answers).most_common(1)
    
    results = {
        "A": {"title": "🍋 偏好「酸」味 —— 肝氣偏盛型", "desc": "在小明的冒險中，你總是選擇清爽收斂。在生活中，你是個精明且追求效率的人，做事乾脆，但也可能代表你目前的精神狀態比較緊繃。"},
        "B": {"title": "☕ 偏好「苦」味 —— 心氣偏盛型", "desc": "你選擇了沉穩的苦味。這代表你擁有超越年齡的成熟心智，生活中你是個可靠的避風港，默默承擔著責任。"},
        "C": {"title": "🍯 偏好「甘」味 —— 脾氣偏盛型", "desc": "你追求甜蜜與穩定。在生活中，你性格溫和、好相處，是一個熱愛和平的人，但有時會因為太愛安逸而忘了前進。"},
        "D": {"title": "🌶️ 偏好「辛」味 —— 肺氣偏盛型", "desc": "你喜歡熱情奔放的快感！生活中你直來直往、熱愛挑戰，是朋友圈中的點火器，但也容易因為衝動而耗損元氣。"},
        "E": {"title": "🧂 偏好「鹹」味 —— 腎氣偏盛型", "desc": "你偏好厚實且入味的層次感。生活中你行事踏實、注重細節，是腳踏實地的實踐家，但也要注意別給自己太大的壓力。"}
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
