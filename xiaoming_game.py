import streamlit as st

# 1. 頁面設定 (使用 wide 模式讓圖片有空間)
st.set_page_config(page_title="小明的五味靈魂探險", page_icon="🍱", layout="wide")

# 2. 注入華麗動漫風格 CSS
st.markdown("""
<style>
    .stApp { background-color: #FDFCF0; }
    
    /* 圖片外框 */
    .img-container {
        border: 4px solid #333;
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 10px 10px 0px #FFAA00;
        margin-bottom: 20px;
    }
    
    /* 對話框卡片 */
    .dialogue-card {
        background: white;
        border: 4px solid #333;
        border-radius: 20px;
        padding: 20px;
        box-shadow: 5px 5px 0px #333;
    }
    
    .char-label {
        background: #333;
        color: #FFD700;
        padding: 5px 15px;
        border-radius: 10px;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 10px;
    }
    
    .dialogue-text {
        font-size: 22px;
        font-weight: bold;
        color: #333;
        line-height: 1.5;
    }
    
    /* 按鈕樣式 */
    .stButton>button {
        width: 100%;
        background-color: white;
        color: #FF8800 !important;
        border: 3px solid #FF8800 !important;
        border-radius: 15px !important;
        padding: 15px !important;
        font-size: 18px !important;
        font-weight: bold !important;
        box-shadow: 0 4px 0 #FF8800 !important;
    }
    .stButton>button:hover {
        background-color: #FF8800 !important;
        color: white !important;
        transform: translateY(2px);
        box-shadow: 0 1px 0 #FF8800 !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. 初始化數據 (加分制最穩定)
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'scores' not in st.session_state:
    st.session_state.scores = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}

# 4. 場景資料庫
questions = [
    {
        "icon": "🎒", "place": "校園出口", "img": "image_0.png",
        "story": "期中考完啦！小明走出校門，夕陽灑在紅磚牆上。",
        "say": "「大腦電力 0%...現在必須吃點重口味的來重啟靈魂！」",
        "opts": [("A. 泰式酸辣粉 (酸爽)", "A"), ("B. 苦甜黑巧舒芙蕾 (大人苦)", "B"), ("C. 蜂蜜奶油厚鬆餅 (甜蜜)", "C"), ("D. 地獄麻辣大火鍋 (辛辣)", "D"), ("E. 雙倍濃鹽拉麵 (鹹鮮)", "E")]
    },
    {
        "icon": "🏮", "place": "東京・巷弄", "img": "image_1.png",
        "story": "夜晚的東京居酒屋街，掛滿了紅燈籠，氣氛非常神祕。",
        "say": "「這家店的味道聞起來好專業！點這道招牌試試看？」",
        "opts": [("A. 極致醃漬青梅", "A"), ("B. 炭火焦香銀杏", "B"), ("C. 甜醬嫩燉和牛", "C"), ("D. 哇沙米激辣串燒", "D"), ("E. 醬油醃漬魚卵", "E")]
    },
    {
        "icon": "🏠", "place": "溫馨老家", "img": "image_2.png",
        "story": "推開家門，熟悉的飯菜香味撲鼻而來。",
        "say": "「媽！好香喔！今天的主菜是我最喜歡的那道嗎？」",
        "opts": [("A. 秘製糖醋排骨", "A"), ("B. 降火微苦排骨湯", "B"), ("C. 山藥地瓜甜湯", "C"), ("D. 辛香爆蔥快炒肉", "D"), ("E. 紅燒鹹香獅子頭", "E")]
    },
    {
        "icon": "🎉", "place": "KTV 派對", "img": "image_3.png",
        "story": "霓虹燈閃爍，朋友們都在起鬨，輪到小明決定慶生蛋糕。",
        "say": "「既然是慶祝，口味絕對要挑最令人難忘的那種！」",
        "opts": [("A. 爆漿檸檬塔", "A"), ("B. 炭焙苦咖啡蛋糕", "B"), ("C. 傳統古法大布丁", "C"), ("D. 肉桂生薑香料糕", "D"), ("E. 海鹽焦糖起司糕", "E")]
    },
    {
        "icon": "🎬", "place": "深夜沙發", "img": "image_4.png",
        "story": "半夜兩點，劇集正播到高潮，小明的肚子卻大聲抗議。",
        "say": "「可惡...不來點零食，我沒法專心看大結局啊！」",
        "opts": [("A. 瞇眼超級酸蜜餞", "A"), ("B. 濃郁厚抹茶苦飲", "B"), ("C. 軟Q牛奶大糖球", "C"), ("D. 嗆鼻哇沙米脆餅", "D"), ("E. 厚切煙燻牛肉乾", "E")]
    }
]

# 5. 遊戲畫面
if st.session_state.step < len(questions):
    q = questions[st.session_state.step]
    st.markdown(f"<h1 style='text-align: center; color: #FF8800;'>{q['icon']} 小明的日常探險</h1>", unsafe_allow_html=True)
    
    # 修正：傳入正確比例參數
    col1, col2 = st.columns()
    
    with col1:
        st.markdown('<div class="img-container">', unsafe_allow_html=True)
        st.image(q["img"], use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown(f"""
        <div class="dialogue-card">
            <div class="char-label">📍 {q['
