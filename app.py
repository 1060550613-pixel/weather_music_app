from flask import Flask, render_template, request
from data.weather_tags import WEATHER_CONDITIONS, WEATHER_EMOTION_MAP, TEMPERATURE_TAGS
from data.song_library import SONG_LIBRARY, MATCH_RULES
from data.playlists import PLAYLISTS
from data.user_preference import DEFAULT_USER_PREFERENCE, MOOD_PREFERENCE_OPTIONS, VOCAL_PREFERENCE_OPTIONS, LANGUAGE_PREFERENCE_OPTIONS
from data.page_text import APP_NAME, APP_SLOGAN, HOME_TEXT, PLAYLIST_SQUARE_TEXT, PRIVACY_TEXT

app = Flask(__name__)


def get_recommended_songs(weather, emotion_pref=None):
    """根据天气和情绪偏好推荐歌曲"""
    emotions = WEATHER_EMOTION_MAP.get(weather, ["治愈"])
    recommended = []
    for song in SONG_LIBRARY:
        if song["emotion"] in emotions:
            recommended.append(song)
    if not recommended:
        recommended = SONG_LIBRARY[:3]
    return recommended


def get_weather_playlists(weather):
    """根据天气获取匹配的预制歌单"""
    matched = []
    for pl in PLAYLISTS:
        if weather in pl["weather_tags"]:
            matched.append(pl)
    if not matched:
        matched = PLAYLISTS[:2]
    return matched


@app.route("/", methods=["GET", "POST"])
def index():
    # 默认天气（实际项目对接天气API）
    weather = request.form.get("weather", "晴天")
    mood_text = WEATHER_CONDITIONS.get(weather, "今天天气不错，来首好歌吧！")
    emotions = WEATHER_EMOTION_MAP.get(weather, ["治愈"])
    songs = get_recommended_songs(weather)
    playlists = get_weather_playlists(weather)
    weather_list = list(WEATHER_CONDITIONS.keys())

    return render_template(
        "index.html",
        app_name=APP_NAME,
        app_slogan=APP_SLOGAN,
        home_text=HOME_TEXT,
        weather=weather,
        mood_text=mood_text,
        emotions=emotions,
        songs=songs,
        playlists=playlists,
        weather_list=weather_list,
    )


@app.route("/square")
def square():
    return render_template(
        "square.html",
        app_name=APP_NAME,
        square_text=PLAYLIST_SQUARE_TEXT,
        playlists=PLAYLISTS,
    )


@app.route("/preference")
def preference():
    return render_template(
        "preference.html",
        app_name=APP_NAME,
        user_pref=DEFAULT_USER_PREFERENCE,
        mood_options=MOOD_PREFERENCE_OPTIONS,
        vocal_options=VOCAL_PREFERENCE_OPTIONS,
        language_options=LANGUAGE_PREFERENCE_OPTIONS,
        privacy_text=PRIVACY_TEXT,
    )


if __name__ == "__main__":
    app.run(debug=True)
