# 组员 D 负责修改此文件
# Issue #4：更新用户偏好配置数据

# 情绪偏好选项
MOOD_PREFERENCE_OPTIONS = ["治愈温柔", "欢快反差", "动感解压"]

# 人声偏好选项
VOCAL_PREFERENCE_OPTIONS = ["纯音乐", "人声歌曲", "无所谓"]

# 语种偏好选项
LANGUAGE_PREFERENCE_OPTIONS = ["华语", "日韩", "欧美", "全部"]

# 默认用户偏好示例
DEFAULT_USER_PREFERENCE = {
    "name": "示例用户",
    "weather_mood": "治愈温柔",      # 同一天气下的情绪偏好
    "vocal_pref": "无所谓",          # 人声偏好
    "language_pref": "华语",         # 语种偏好
}

# 行为权重说明
# - 点赞（like）：该类风格推荐权重 +0.2，后续同天气优先推送
# - 收藏（collect）：该曲/歌单权重 +0.3，进入个人精选库
# - 跳过（skip）：该类风格推荐权重 -0.15，同天气减少此类推送
# - 循环播放（loop）：该曲权重 +0.25，视为强烈喜好信号
# - 黑名单（block）：该歌手/曲风永久屏蔽，同天气不再推送
