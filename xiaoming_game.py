import streamlit as st
from collections import Counter

# 1. 頁面設定
st.set_page_config(page_title="小明的五味冒險", page_icon="🍱", layout="centered")

# 2. 注入華麗卡通風格 CSS
st.markdown("""
<style>
    .stApp { background-color: #FDFCF0; }
    .chat-card {
        background: white; border: 4px solid #333; border-radius: 20px;
        padding: 25px; box-shadow: 8px 8px 0px #FFAA00; margin-bottom: 20px;
    }
    .char-label {
        background: #333; color: #FFD700; padding: 5px 15px;
        border-radius: 10px; font-weight: bold; display: inline-block; margin-bottom: 10px;
    }
    .bubble { font-size: 20px; font-weight: 800; color: #444; line-height: 1.5; }
    .stButton>button {
        width: 100%; background-color: white; color: #FF8800 !important;
        border: 3px solid #FF8800 !important; border-radius: 50px !important;
        padding: 12px !important; font-size: 18px !important; font-weight: bold !important;
        box-shadow: 0 6px 0 #FF8800 !important; transition: 0.2s;
    }
    .stButton>button:hover {
        transform: translateY(-3px); background-color: #FF8800 !important;
        color: white !important; box-shadow: 0 9px 0 #CC6600 !important;
    }
    .result-box {
        background: #FFF; border: 6px solid #FF8800; border-radius: 30px;
        padding: 40px; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# 3. 初始化數據
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'answers' not in st.session_state:
    st.session_state.answers = []

# 4. 場景與題目
questions = [
    {
        "icon": "🎒", "place": "校園門口", "story": "期中考結束了！夕陽下的小明感覺大腦電力剩 1%...",
        "say": "「呼...腦袋徹底當機！現在我需要超重口味的食物來重啟靈魂，走吧！」",
        "opts": [("A. 泰式酸辣魚粉 (酸爽帶勁)", "A"), ("B. 苦甜黑巧舒芙蕾 (大人滋味)", "B"), ("C. 蜂蜜奶油厚鬆餅 (甜蜜爆發)", "C"), ("D. 地獄麻辣大火鍋 (辛辣發散)", "D"), ("E. 雙倍濃鹽濃湯拉麵 (鹹鮮入味)", "E")]
    },
    {
        "icon": "🏮", "place": "東京・居酒屋", "story": "小明帶女朋友旅遊，走進掛滿紅燈籠的巷弄神祕小店。",
        "say": "「親愛的，聽說這家的『味覺覺醒』料理超有名，我們試試這道？」",
        "opts": [("A. 極致醃漬青梅", "A"), ("B. 炭火焦香銀杏", "B"), ("C. 甜醬嫩燉和牛", "C"), ("D. 哇沙米激辣雞串", "D"), ("E. 熟成醬油醃魚卵", "E")]
    },
    {
        "icon": "🏠", "place": "溫馨老家", "story": "推開門，廚房傳來熟悉的鍋鏟聲，媽媽正在準備晚餐。",
        "say": "「哇！這香味...媽！你是不是做了我夢寐以求的那道菜？」",
        "opts": [("A. 秘製祖傳糖醋肉", "A"), ("B. 降火微苦排骨湯", "B"), ("C. 補氣山藥地瓜甜湯", "C"), ("D. 辛香爆蔥快炒肉", "D"), ("E. 鹹鮮入味紅燒肉", "E")]
    },
    {
        "icon": "🎂", "place": "驚喜派對", "story": "派對現場氣氛嗨爆！小明拿著蛋糕目錄，準備點壓軸點心。",
        "say": "「今天的聚會，一定要選一個讓大家舌尖都跳舞的口味！」",
        "opts": [("A. 爆漿酸檸檬塔", "A"), ("B. 炭焙苦咖啡蛋糕", "B"), ("C. 傳統古法大布丁", "C"), ("D. 肉桂生薑香料糕", "D"), ("E. 海鹽焦糖起司糕", "E")]
    },
    {
        "icon": "🎬", "place": "深夜沙發", "story": "半夜兩點，小明正看到精彩結局...肚子卻咕嚕叫了！",
        "say": "「可惡，如果不來點靈魂零食，我真的沒法專心看劇情！」",
        "opts": [("A. 瞇眼超級酸蜜餞", "A"), ("B. 濃郁厚抹茶苦飲", "B"), ("C. 軟Q牛奶大糖球", "C"), ("D. 嗆鼻哇沙米脆餅", "D"), ("E. 厚切煙燻牛肉乾", "E")]
    }
]

# 5. 遊戲介面
if st.session_state.step < len(questions):
    q = questions[st.session_state.step]
    st.markdown(f"<h1 style='text-align: center; color: #FF8800;'>{q['icon']} 小明的日常探險</h1>", unsafe_allow_html=True)
    st.progress((st.session_state.step) / len(questions))
    
    st.markdown(f"""
    <div class="chat-card">
        <div class="char-label">📍 {q['place']}</div>
        <p style='color: #888; font-style: italic;'>{q['story']}</p>
        <hr>
        <div class="bubble">小明：「{q['say']}」</div>
    </div>
    """, unsafe_allow_html=True)
    
    # 建立選項按鈕
    for btn_text, code in q['opts']:
        if st.button(btn_text, key=f"btn_{st.session_state.step}_{code}"):
            st.session_state.answers.append(code)
            st.session_state.step += 1
            st.rerun()

else:
    # 6. 結果計算與顯示
    st.balloons()
    st.markdown("<h1 style='text-align: center; color: #FF8800;'>🔮 探險終點：你的靈魂味覺</h1>", unsafe_allow_html=True)
    
    # 使用 Counter 計算最高頻率的選項
    if st.session_state.answers:
        counts = Counter(st.session_state.answers)
        final_key = counts.most_common(1) # 取得 A, B, C, D 或 E 
    else:
        final_key = "C"

    # 結果資料庫 (Key 必須是字串 'A', 'B'...)
    results_map = {
        "A": {"title": "🍋 偏好「酸」味 —— 肝氣偏盛型", "desc": "在小明的冒險中，你總是選擇清爽收斂。生活中你是個精明且追求效率的人，做事乾脆，但也代表你目前的狀態比較緊繃。"},
        "B": {"title": "☕ 偏好「苦」味 —— 心氣偏盛型", "desc": "你選擇了沉穩的苦味。這代表你擁有超越年齡的成熟感，在朋友圈中是個可靠的守護者，默默承擔著責任。"},
        "C": {"title": "🍯 偏好「甘」味 —— 脾氣偏盛型", "desc": "你追求甜蜜與穩定。性格溫和、熱愛和平，是大家眼中的開心果，但有時會因為太愛安逸而忘了前進。"},
        "D": {"title": "🌶️ 偏好「辛」味 —— 肺氣偏盛型", "desc": "你喜歡熱情奔放的挑戰！直來直往、有正義感，是行動派的代表，但也容易因為衝動而耗損元氣。"},
        "E": {"title": "🧂 偏好「鹹」味 —— 腎氣偏盛型", "desc": "你偏好厚實且紮實的層次感。行事踏實、注重細節，是腳踏實地的實踐家，要注意適度放鬆。"}
    }
    
    # 這裡確保 final_key 是一個字串，就不會報 TypeError 了
    res = results_map.get(final_key, results_map["C"])
    
    st.markdown(f"""
    <div class="result-box">
        <h2 style='color: #FF8800;'>{res['title']}</h2>
        <hr>
        <p style='font-size: 22px; line-height: 1.8; color: #333;'>
            <b>【生活樣貌】</b><br>{res['desc']}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("再陪小明冒險一次"):
        st.session_state.step = 0
        st.session_state.answers = []
        st.rerun()
