
# ------------------------------------------------------------
# 1. 偏好维度选项
# ------------------------------------------------------------

# 情绪偏好选项（至少3种）
MOOD_PREFERENCE_OPTIONS = [
    {
        "key": "healing",
        "label": "治愈温柔",
        "desc": "轻柔舒缓，治愈心情，适合放松或入眠"
    },
    {
        "key": "cheerful",
        "label": "欢快反差",
        "desc": "活泼明朗，反差萌感，适合元气满满的早晨"
    },
    {
        "key": "energetic",
        "label": "动感解压",
        "desc": "节奏强劲，释放压力，适合运动或通勤"
    },
    {
        "key": "melancholy",
        "label": "慵懒伤感",
        "desc": "细腻低沉，适合阴雨天或独处时光"
    },
    {
        "key": "focus",
        "label": "专注沉浸",
        "desc": "氛围感强，适合学习、工作或深度思考"
    },
]

# 人声偏好选项
VOCAL_PREFERENCE_OPTIONS = [
    {"key": "instrumental", "label": "纯音乐",  "desc": "无人声，纯器乐演奏"},
    {"key": "vocal",        "label": "人声歌曲", "desc": "有演唱，注重歌词与嗓音"},
    {"key": "no_pref",      "label": "无所谓",   "desc": "不限制，随机推荐"},
]

# 语种偏好选项
LANGUAGE_PREFERENCE_OPTIONS = [
    {"key": "mandarin", "label": "华语",   "desc": "普通话 / 粤语"},
    {"key": "jpkr",     "label": "日韩",   "desc": "日语 / 韩语"},
    {"key": "western",  "label": "欧美",   "desc": "英语 / 其他西方语种"},
    {"key": "all",      "label": "全部",   "desc": "不限语种，全球音乐"},
]

# ------------------------------------------------------------
# 2. 默认用户偏好配置
#    字段说明：
#      name          — 用户昵称（展示用）
#      weather_mood  — 情绪偏好 key，对应 MOOD_PREFERENCE_OPTIONS
#      vocal_pref    — 人声偏好 key，对应 VOCAL_PREFERENCE_OPTIONS
#      language_pref — 语种偏好 key，对应 LANGUAGE_PREFERENCE_OPTIONS
# ------------------------------------------------------------

DEFAULT_USER_PREFERENCE = {
    "name": "音乐旅人",
    "weather_mood": "healing",       # 默认：治愈温柔
    "vocal_pref":   "vocal",         # 默认：人声歌曲
    "language_pref": "mandarin",     # 默认：华语
    # 附加可选字段（扩展用，不影响核心逻辑）
    "favorite_genres": ["流行", "民谣", "轻音乐"],
    "disliked_genres": [],
    "enable_personalized": True,     # 是否开启个性化推荐
}

# 示例：多个预设偏好档案，供新用户快速选择
PRESET_PROFILES = [
    {
        "profile_id": "preset_relax",
        "display_name": "放松模式",
        "weather_mood": "healing",
        "vocal_pref": "instrumental",
        "language_pref": "all",
    },
    {
        "profile_id": "preset_active",
        "display_name": "活力模式",
        "weather_mood": "energetic",
        "vocal_pref": "vocal",
        "language_pref": "western",
    },
    {
        "profile_id": "preset_focus",
        "display_name": "专注模式",
        "weather_mood": "focus",
        "vocal_pref": "instrumental",
        "language_pref": "all",
    },
]

# ------------------------------------------------------------
# 3. 行为权重说明
# ------------------------------------------------------------
#
#  用户的每次操作都会影响个性化推荐的权重，规则如下：
#
#  【点赞 👍】
#    - 权重增量：+0.3
#    - 影响范围：该首歌曲的所有标签（曲风、情绪、语种、BPM区间）
#    - 逻辑：下次遇到相同天气时，优先推荐同类标签的歌曲
#
#  【跳过 ⏭️】
#    - 权重增量：-0.2（轻度惩罚，不完全屏蔽）
#    - 影响范围：该首歌曲的主情绪标签
#    - 逻辑：在本次会话内降低同情绪歌曲出现频率；跨会话衰减（×0.5 每天）
#    - 注意：连续跳过3首同一曲风时，触发"曲风疲劳"机制，临时降低该曲风权重 -0.5
#
#  【收藏 ⭐】
#    - 权重增量：+0.5（最强正反馈）
#    - 影响范围：该首歌曲的全部标签 + 所属歌单的天气场景标签
#    - 逻辑：收藏的歌曲进入「我的收藏」，同时永久提升对应天气场景的推荐优先级
#
#  【权重衰减机制】
#    - 所有正向权重每7天自然衰减 ×0.8，防止推荐固化
#    - 用户主动「刷新推荐」时，当次会话权重重置为默认值，不影响长期权重
#
#  【冷启动策略】
#    - 新用户没有行为数据时，使用 DEFAULT_USER_PREFERENCE 作为初始权重基准
#    - 引导用户完成「口味测试」（快速选3首喜欢的歌）后，加速个性化进程
#
# ------------------------------------------------------------

# 行为权重配置字典（供推荐引擎读取）
BEHAVIOR_WEIGHTS = {
    "like":         +0.3,   # 点赞
    "skip":         -0.2,   # 跳过
    "collect":      +0.5,   # 收藏
    "fatigue_skip":  3,     # 连续跳过触发曲风疲劳的阈值
    "fatigue_penalty": -0.5, # 曲风疲劳惩罚值
    "decay_interval_days": 7,  # 权重衰减周期（天）
    "decay_factor":  0.8,   # 每个衰减周期的乘数
}
