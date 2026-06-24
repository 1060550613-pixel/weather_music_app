# -*- coding: utf-8 -*-
# 组员 C 负责修改此文件
# Issue #3：更新预制天气歌单合集
# 负责人：ANGELOhsz
#
# 任务要求：
# 1. 至少 6 个预制歌单，覆盖不同天气场景（必选：夏日暴晒歌单、雨夜emo合集、下雪氛围感歌单）
# 2. 每个歌单包含：名称、适用天气标签、情绪标签、简介描述
# 3. 新增至少 1 个自定义天气歌单

# ============================================================
#  预制天气歌单合集
#  每个歌单字段说明：
#    - id:             歌单编号
#    - name:           歌单名称
#    - weather_tags:   适用天气标签（对应 weather_tags.py 中的天气状况）
#    - emotion_tags:   情绪标签（对应 weather_tags.py 中的情绪映射）
#    - description:    一句话简介
#    - songs:          示例歌曲列表（歌名 - 歌手）
# ============================================================

PLAYLISTS = [
    # ---------- 必选歌单 1 ----------
    {
        "id": 1,
        "name": "☀️ 夏日暴晒歌单",
        "weather_tags": ["晴天", "炎热", "酷暑"],
        "emotion_tags": ["清爽", "解压", "欢快", "活力"],
        "description": "高温暴晒就对了——用高 BPM 电音和夏日流行帮你物理降温。",
        "songs": [
            "夏天的风 - 温岚",
            "宁夏 - 梁静茹",
            "好的夏天 - 告五人",
            "Good Time - Owl City & Carly Rae Jepsen",
            "Summer - Calvin Harris",
        ],
    },

    # ---------- 必选歌单 2 ----------
    {
        "id": 2,
        "name": "🌧️ 雨夜emo合集",
        "weather_tags": ["小雨", "大雨", "暴雨"],
        "emotion_tags": ["治愈", "慵懒", "伤感", "舒缓"],
        "description": "雨滴落在窗台，情绪慢慢蔓延，今晚允许自己脆弱一下。",
        "songs": [
            "雨天 - 孙燕姿",
            "说散就散 - 袁娅维",
            "慢慢喜欢你 - 莫文蔚",
            "Fix You - Coldplay",
            "Someone Like You - Adele",
        ],
    },

    # ---------- 必选歌单 3 ----------
    {
        "id": 3,
        "name": "❄️ 下雪氛围感歌单",
        "weather_tags": ["雪", "寒冷", "严寒"],
        "emotion_tags": ["温暖", "治愈", "安静", "浪漫"],
        "description": "窗外飘雪，屋内热可可，这些歌就是冬天最好的伴奏。",
        "songs": [
            "雪落下的声音 - 陆虎",
            "白色恋人 - 张学友",
            "飘雪 - 陈慧娴",
            "Let It Go - Idina Menzel",
            "Winter Song - Sara Bareilles & Ingrid Michaelson",
        ],
    },

    # ---------- 补充歌单 4 ----------
    {
        "id": 4,
        "name": "⛅ 多云微风散步歌单",
        "weather_tags": ["多云", "凉爽", "舒适"],
        "emotion_tags": ["轻松", "自在", "慵懒", "治愈"],
        "description": "云层挡住了刺眼的阳光，戴上耳机去散步吧，节奏刚刚好。",
        "songs": [
            "平凡之路 - 朴树",
            "旅行的意义 - 陈绮贞",
            "Walking on Sunshine - Katrina and the Waves",
            "Better Together - Jack Johnson",
            "小情歌 - 苏打绿",
        ],
    },

    # ---------- 补充歌单 5 ----------
    {
        "id": 5,
        "name": "🌫️ 雾天沉浸歌单",
        "weather_tags": ["雾", "阴天"],
        "emotion_tags": ["沉浸", "神秘", "安静", "舒缓"],
        "description": "能见度很低，但内心很清晰——雾天专属的氛围感歌单。",
        "songs": [
            "迷雾 - 刘德华",
            "Foggy Day - Michael Bublé",
            "夜空中最亮的星 - 逃跑计划",
            "Fade Into You - Mazzy Star",
            "一直很安静 - 阿桑",
        ],
    },

    # ---------- 补充歌单 6 ----------
    {
        "id": 6,
        "name": "⛈️ 雷暴能量歌单",
        "weather_tags": ["雷暴", "大雨"],
        "emotion_tags": ["热血", "解压", "力量", "动感"],
        "description": "打雷了？那就听点更猛的——用摇滚和电子乐和雷电共振。",
        "songs": [
            "Thunder - Imagine Dragons",
            "怒放的生命 - 汪峰",
            "Believer - Imagine Dragons",
            "We Will Rock You - Queen",
            "追梦赤子心 - GALA",
        ],
    },

    # ---------- 自定义歌单 7（组员C自行设计） ----------
    {
        "id": 7,
        "name": "🏜️ 沙尘暴硬核歌单",
        "weather_tags": ["沙尘", "炎热"],
        "emotion_tags": ["硬核", "解压", "力量", "叛逆"],
        "description": "沙尘漫天挡不住你的节奏，用最硬核的说唱和摇滚对抗糟糕天气。",
        "songs": [
            "蜗牛 - 周杰伦",
            "命运 - 命运",
            "Lose Yourself - Eminem",
            "Numb - Linkin Park",
            "像风一样自由 - 许巍",
        ],
    },
]
