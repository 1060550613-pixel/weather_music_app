# 云听 - 天气推荐音乐 App

> 听见天气的声音

## 项目简介

根据当前天气（晴/雨/雪/雾等）自动推荐匹配情绪的音乐歌单，支持天气→情绪→曲风多维度精准匹配。

## 功能模块

- 🏠 **首页**：天气心情文案 + 专属推荐歌曲 + 匹配歌单
- 🎵 **歌单广场**：预制天气主题歌单合集
- ⚙️ **偏好设置**：个性化情绪/人声/语种偏好 + 隐私说明

## 小组分工（Fork + PR 协作）

| Issue | 组员 | 负责文件 |
|-------|------|---------|
| #1 | 组员A | data/weather_tags.py |
| #2 | 组员B | data/song_library.py |
| #3 | 组员C | data/playlists.py |
| #4 | 组员D | data/user_preference.py |
| #5 | 组员E | data/page_text.py |

## 本地运行

```bash
pip install flask
python app.py
```

访问 http://127.0.0.1:5000

## 技术栈

- 后端：Python Flask
- 前端：HTML + CSS（Jinja2 模板）
- 部署：Vercel
