# 组员 B 负责修改此文件
# Issue #2：更新歌曲标签库与匹配数据

# 示例歌曲库（每首包含6维度标签）
SONG_LIBRARY = [
    {
        "title": "晴天",
        "artist": "周杰伦",
        "genre": "流行",
        "emotion": "欢快",
        "bpm": "快",       # 慢/<80  中/80~110  快/>110
        "scene": "通勤",
        "season": "春日清新",
        "language": "华语",
    },
    {
        "title": "七里香",
        "artist": "周杰伦",
        "genre": "流行",
        "emotion": "温柔",
        "bpm": "中",
        "scene": "散步",
        "season": "夏日专属",
        "language": "华语",
    },
    {
        "title": "雨爱",
        "artist": "杨丞琳",
        "genre": "流行",
        "emotion": "治愈",
        "bpm": "慢",
        "scene": "居家",
        "season": "秋日emo",
        "language": "华语",
    },
    {
        "title": "River Flows in You",
        "artist": "Yiruma",
        "genre": "纯音乐",
        "emotion": "静谧",
        "bpm": "慢",
        "scene": "睡前",
        "season": "冬日暖歌",
        "language": "纯器乐",
    },
    {
        "title": "夏天的风",
        "artist": "棉子",
        "genre": "民谣",
        "emotion": "清爽",
        "bpm": "中",
        "scene": "下午茶",
        "season": "夏日专属",
        "language": "华语",
    },
]

# 天气匹配规则示例
MATCH_RULES = [
    {
        "scene": "35℃大晴天+午后",
        "conditions": {"temp": "酷暑", "weather": "晴天", "time": "午间"},
        "recommend": {"bpm": "快", "genre": ["流行", "电子"], "emotion": ["清爽", "活力"]},
    },
    {
        "scene": "深夜小雨+低温",
        "conditions": {"temp": "寒冷", "weather": "小雨", "time": "深夜"},
        "recommend": {"bpm": "慢", "genre": ["民谣", "纯音乐"], "emotion": ["治愈", "温柔"]},
    },
    {
        "scene": "冬日下雪傍晚",
        "conditions": {"temp": "严寒", "weather": "雪", "time": "傍晚"},
        "recommend": {"bpm": "慢", "genre": ["纯音乐", "轻音乐"], "emotion": ["静谧", "温柔"]},
    },
]
