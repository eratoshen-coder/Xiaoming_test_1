import streamlit as st

# 1. 頁面基底設定 (layout設為wide，給圖片更多空間)
st.set_page_config(page_title="小明的五味靈魂探險", page_icon="🍱", layout="wide")

# 2. 注入華麗卡通風格 CSS (優化排版與卡片)
st.markdown("""
<style>
    /* 全域背景：日系米色 */
    .stApp {
        background-color: #FDFCF0;
    }
    
    /* 卡通場景卡片 (圖片+文字) */
    .scene-card {
        background: white;
        border: 4px solid #333;
        border-radius: 25px;
        padding: 0; /* 圖片滿版 */
        box-shadow: 10px 10px 0px #FFAA00;
        margin-bottom: 25px;
        overflow: hidden; /* 確保圖片圓角 */
    }
    
    /* 場景圖片排版 */
    .scene-image {
        width: 100%;
        height: auto;
        display: block;
        border-bottom: 4px solid #333;
    }
    
    /* 文字內容區 */
    .scene-content {
        padding: 25px;
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
    }
    
    /* 對話文字 (動漫感) */
    .dialogue {
        font-size: 24px;
        font-weight: 700;
        color: #333;
        line-height: 1.6;
    }
    
    /* 按鈕樣式：華麗 3D */
    .stButton>button {
        width: 100%;
        background-color: #FFFFFF;
        color: #FF8800 !important;
        border: 3px solid #FF8800 !important;
        border-radius: 15px !important;
        padding: 18px !important;
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

# 3. 初始化數據 (使用簡單加分制，絕對穩定)
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'scores' not in st.session_state:
    st.session_state.scores = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}

# 4. 華麗場景資料庫 (整合圖片URL與故事)
# 圖片 URL 需使用原始檔案連結 (如 GitHub raw 或是其他圖床)
# 在此我直接使用剛剛生成的 image 變數名稱作為示範，你只需在部署時確認檔案路徑即可。

questions = [
    {
        "icon": "🎒", "place": "校園出口", 
        "image_url": "image_0.png", # 場景 1 圖
        "story": "期中考考完啦！小明甩上背包走出校門，夕陽餘暉灑在校門口。",
        "say": "「呼...大腦乾枯。現在必須吃點靈魂食物來重新啟動大腦，走吧！」",
        "opts": [("A. 泰式酸辣粉 (酸爽帶勁)", "A"), ("B. 苦甜黑巧舒芙蕾 (大人苦味)", "B"), ("C. 蜂蜜奶油厚鬆餅 (甜蜜爆發)", "C"), ("D. 地獄麻辣火鍋 (辛辣發散)", "D"), ("E. 雙倍濃鹽濃湯拉麵 (鹹鮮入味)", "E")]
    },
    {
        "icon": "🏮", "place": "東京・巷弄居酒屋", 
        "image_url": "image_1.png", # 場景 2 圖
        "story": "小明跟女朋友在熱鬧的歌舞伎町迷路，發現掛滿紅燈籠的神祕老店。",
        "say": "「親愛的，你看，這家店氛圍超讚！我們點主廚推薦的如何？」",
        "opts": [("A. 極致醃漬青梅", "A"), ("B. 炭火焦香銀杏", "B"), ("C. 甜醬嫩燉和牛", "C"), ("D. 哇沙米激辣串燒", "D"), ("E. 熟成醬油醃魚卵", "E")]
    },
    {
        "icon": "🍲", "place": "家鄉・溫馨廚房", 
        "image_url": "image_2.png", # 場景 3 圖
        "story": "推開家門，鍋鏟聲與香氣傳來，記憶中最熟悉的家庭晚餐正要上桌。",
        "say": "「媽，我回來了！好香喔...今天主菜難道是那個？」",
        "opts": [("A. 秘製祖傳糖醋肉", "A"), ("B. 降火微苦排骨湯", "B"), ("C. 補氣山藥地瓜甜湯", "C"), ("D. 辛香爆蔥快炒肉", "D"), ("E. 紅燒鹹香獅子頭", "E")]
    },
    {
        "icon": "🎉", "place": "KTV 包廂派對", 
        "image_url": "image_3.png", # 場景 4 圖
        "story": "霓虹燈閃爍，朋友們嗨翻天，輪到小明決定慶生蛋糕的口味。",
        "say": "「既然是慶祝，口味絕對要挑最令人難忘的那種才行！」",
        "opts": [("A. 爆漿檸檬塔", "A"), ("B. 炭焙苦咖啡蛋糕", "B"), ("C. 傳統古法大布丁", "C"), ("D. 肉桂生薑香料糕", "D"), ("E. 海鹽焦糖起司糕", "E")]
    },
    {
        "icon": "🎬", "place": "深夜公寓沙發", 
        "image_url": "image_4.png", # 場景 5 圖
        "story": "深夜兩點，電視螢幕閃爍，劇集正播到精彩大結局...肚子抗議了！",
        "say": "「可惡...不來點靈魂零食，饿到根本沒法專心看劇情啊！」",
        "opts": [("A. 瞇眼超級酸蜜餞", "A"), ("B. 濃郁厚抹茶苦飲", "B"), ("C. 軟Q牛奶大糖球", "C"), ("D. 嗆鼻哇沙米脆餅", "D"), ("E. 厚切煙燻牛肉乾", "E")]
    }
]

# 5. 遊戲介面渲染邏輯
if st.session_state.step < len(questions):
    q = questions[st.session_state.step]
    
    st.markdown(f"<h1 style='text-align: center; color: #FF8800;'>{q['icon']} 小明的日常探險</h1>", unsafe_allow_html=True)
    st.progress((st.session_state.step) / len(questions))
    
    # 建立左右排版：左圖右文
    col1, col2 = st.columns() # 圖占2/3, 文占1/3
    
    with col1:
        # 使用 markdown 顯示滿版圓角圖片
        st.markdown(f"""
        <div class="scene-card">
            <img src="{q['image_url']}" class="scene-image" alt="Scene Image">
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        # 文字與對話區 (對話區域放大)
        st.markdown(f"""
        <div class="scene-card">
            <div class="scene-content">
                <div class="char-name">📍 {q['place']}</div>
                <p style='color: #666; font-style: italic; font-size: 16px;'>{q['story']}</p>
                <hr style="border: 1px dashed #DDD;">
                <div class="dialogue">小明：「{q['say']}」</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # 按鈕選項 (放在col2，緊鄰對話區)
        st.write("---")
        for btn_text, code in q['opts']:
            # 按鈕 Key 加上 step 確保唯一性
            if st.button(btn_text, key=f"btn_{st.session_state.step}_{code}"):
                st.session_state.scores[code] += 1
                st.session_state.step += 1
                st.rerun()

else:
    # 6. 結果計算與顯示 (加分制，絕對穩定)
    st.balloons()
    st.markdown("<h1 style='text-align: center; color: #FF8800;'>🔮 探險終點：你的靈魂味覺</h1>", unsafe_allow_html=True)
    
    # 找出最高分的字母 (若平手，max會回傳最先找到的)
    final_type = max(st.session_state.scores, key=st.session_state.scores.get)

    results_map = {
        "A": {"title": "🍋 偏好「酸」味 —— 肝氣偏盛型", "desc": "在列表中，你是個精明且追求效率的人，做事乾脆俐落，但也可能代表你目前的精神狀態比較緊繃。"},
        "B": {"title": "☕ 偏好「苦」味 —— 心氣偏盛型", "desc": "這代表你擁有超越同齡人的成熟感，在朋友圈中是個可靠的守護者，默默承擔著責任。"},
        "C": {"title": "🍯 偏好「甘」味 —— 脾氣偏盛型", "desc": "你追求甜蜜與穩定。性格溫和、好相處，熱愛和平，但有時會因為太愛安逸而忘了前進。"},
        "D": {"title": "🌶️ 偏好「辛」味 —— 肺氣偏盛型", "desc": "你喜歡熱情奔放的挑戰！生活中直來直往、最有正義感，是行動派代表，但也容易耗損元氣。"},
        "E": {"title": "🧂 偏好「鹹」味 —— 腎氣偏盛型", "desc": "你行事踏實、注重細節，是腳踏實地的實踐家，但要注意適時放鬆壓力。"}
    }
    
    # 防止空數據報錯 (理論上不會發生)
    res = results_map.get(final_type, results_map["C"])
    
    # 結果畫面集中顯示 (wide layout)
    col_empty1, col_res, col_empty2 = st.columns()
    with col_res:
        st.markdown(f"""
        <div class="result-box">
            <h2 style='color: #FF8800;'>{res['title']}</h2>
            <hr style="border: 2px solid #FF8800;">
            <p style='font-size: 22px; line-height: 1.8; color: #333;'>
                <span style="background-color: #FFD700; padding: 2px 10px; border-radius: 5px; font-weight: bold;">生活樣貌</span><br><br>
                {res['desc']}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("---")
        if st.button("再陪小明冒險一次"):
            # 重置數據
            st.session_state.step = 0
            st.session_state.scores = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
            st.rerun()
