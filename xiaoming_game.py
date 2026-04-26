import streamlit as st

# 設定網頁標題與風格
st.set_page_config(page_title="小明的五味靈魂探險", page_icon="🍱", layout="centered")

# 自定義 CSS 讓畫面更活潑
st.markdown("""
    <style>
    .main {
        background-color: #fffdf0;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #ffaa00;
        color: white;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #ff8800;
        color: white;
    }
    .scenario-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        border-left: 10px solid #ffaa00;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 初始化遊戲狀態
if 'step' not in st.session_state:
    st.session_state.step = 0
    st.session_state.answers = []

# 定義題目與情境
questions = [
    {
        "scene": "🏃‍♂️ **場景一：校園門口**\n\n小明剛考完最後一科期中考，走出校門時覺得大腦燒焦了！他轉頭對同學說：『走！我們去大吃一頓狂歡一下！』",
        "question": "這時小明最想衝去吃什麼？",
        "options": [
            ("A. 特調酸爽的泰式檸檬魚配涼拌酸辣粉", "A"),
            ("B. 充滿成熟大人味的苦甜黑巧克力舒芙蕾", "B"),
            ("C. 一大盤沾滿蜂蜜、鮮奶油的現烤厚鬆餅", "C"),
            ("D. 挑戰地獄等級、滿滿辣油的川味麻辣火鍋", "D"),
            ("E. 日式濃郁豚骨拉麵，湯頭要加雙倍鹽度", "E")
        ]
    },
    {
        "scene": "✈️ **場景二：東京街頭**\n\n小明帶女朋友出國旅遊，兩人在歌舞伎町的小巷弄裡發現一家隱藏版食堂。老闆正熱情地招手。",
        "question": "你會建議小明幫女朋友點哪道招牌菜？",
        "options": [
            ("A. 爽口開胃、醋味十足的醃漬青梅", "A"),
            ("B. 烤得微焦、帶點苦甘焦香味的銀杏", "B"),
            ("C. 入口即化的軟糯燉肉，醬汁帶有甘甜焦糖香", "C"),
            ("D. 噴香刺鼻、撒滿胡椒與七味粉的烤雞串燒", "D"),
            ("E. 鹹香十足、味道厚實的醬油醃漬魚卵", "E")
        ]
    },
    {
        "scene": "🏠 **場景三：溫暖的家中**\n\n周末回老家，媽媽在廚房忙進忙出，對客廳的小明喊著：『兒子，快洗手，煮了你最愛的那道菜！』",
        "question": "小明聞到廚房飄出來的味道，直覺那盤菜是？",
        "options": [
            ("A. 糖醋排骨，那股酸勁最下飯", "A"),
            ("B. 清熱退火、微苦卻回甘的苦瓜排骨湯", "B"),
            ("C. 濃稠順口、補中益氣的山藥地瓜甜湯", "C"),
            ("D. 爆炒大量蔥薑蒜、辛香味十足的快炒牛肉", "D"),
            ("E. 滷了一整天、鹹鮮入味的紅燒獅子頭", "E")
        ]
    },
    {
        "scene": "🎂 **場景四：KTV 包廂**\n\n好兄弟過生日，小明負責訂蛋糕。當店員詢問口味時，小明腦中浮現的第一個念頭是...",
        "question": "小明最後決定訂哪種口味的蛋糕？",
        "options": [
            ("A. 極致酸香的檸檬塔或百香果慕斯", "A"),
            ("B. 特製深焙咖啡凍蛋糕，苦而不澀", "C"), # 這裡對應 C 是為了符合甘味，或者修正為 B
            ("C. 傳統鮮奶油大布丁蛋糕，純粹甘甜", "C"),
            ("D. 帶有肉桂與生薑風味的特色香料蛋糕", "D"),
            ("E. 焦糖海鹽起司蛋糕，鹹甜交織", "E")
        ]
    },
    {
        "scene": "🎬 **場景五：深夜的沙發**\n\n深夜一點，小明一個人在家追劇，劇情正精彩，但肚子卻不爭氣地咕嚕咕嚕叫了。",
        "question": "小明打開櫃子，最後拿出了哪款靈魂零食？",
        "options": [
            ("A. 酸得瞇起眼的蜜餞或檸檬乾", "A"),
            ("B. 一杯濃郁的無糖抹茶或苦味黑咖啡", "B"),
            ("C. 甜膩軟Q的牛奶糖或傳統龍鬚糖", "C"),
            ("D. 脆口嗆鼻的哇沙米脆餅", "D"),
            ("E. 鹹香夠味的煙燻牛肉乾", "E")
        ]
    }
]

# 遊戲邏輯
if st.session_state.step < len(questions):
    curr = questions[st.session_state.step]
    st.title("🍱 小明的五味靈魂探險")
    st.progress((st.session_state.step) / len(questions))
    
    st.markdown(f'<div class="scenario-box">{curr["scene"]}</div>', unsafe_allow_html=True)
    st.subheader(curr["question"])
    
    for text, code in curr["options"]:
        if st.button(text):
            st.session_state.answers.append(code)
            st.session_state.step += 1
            st.rerun()
else:
    # 計算結果
    from collections import Counter
    final_answer = Counter(st.session_state.answers).most_common(1)
    
    st.title("🔮 探險終點：你的靈魂味覺")
    
    results = {
        "A": {"title": "偏好「酸」味 —— 肝氣偏盛型", "desc": "你喜歡收斂、清爽的酸感，在生活中你是個追求效率、凡事想要迅速達到目標的人，但也可能代表你目前的狀態比較緊繃。"},
        "B": {"title": "偏好「苦」味 —— 心氣偏盛型", "desc": "你追求降火、沉穩的苦味，這代表你擁有比一般人更成熟的心智，在生活中可能正承擔著較大的責任感。"},
        "C": {"title": "偏好「甘」味 —— 脾氣偏盛型", "desc": "你是甜食與澱粉愛好者。在生活中，你追求安穩、幸福感，性格溫和，但也容易因為環境安逸而變得懶散。"},
        "D": {"title": "偏好「辛」味 —— 肺氣偏盛型", "desc": "你追求發散、出汗的快感。生活中你直來直往、熱情如火，喜歡冒險與感官上的強烈刺激。"},
        "E": {"title": "偏好「鹹」味 —— 腎氣偏盛型", "desc": "你偏好厚重、入味的鹹鮮感。在生活中你較為踏實、注重細節，但有時會給自己過多的壓力。"}
    }
    
    st.success(f"### 檢測結果：{results[final_answer]['title']}")
    st.info(f"**生活樣貌：**\n\n{results[final_answer]['desc']}")
    
    if st.button("再測一次"):
        st.session_state.step = 0
        st.session_state.answers = []
        st.rerun()