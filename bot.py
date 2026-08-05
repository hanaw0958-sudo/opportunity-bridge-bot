# -*- coding: utf-8 -*-
"""
Opportunity Bridge — Telegram-бот.
Все тексты и списки кнопок лежат в data.py — их можно менять, не трогая этот файл.
"""

import csv
import io
import os
import time

import requests
import telebot
from flask import Flask, request
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

import data

# ---------- Настройки из переменных окружения ----------

BOT_TOKEN = os.environ["BOT_TOKEN"]
SHEET_ID = os.environ["SHEET_ID"]
WEBHOOK_URL = os.environ.get("WEBHOOK_URL", "")  # заполняется на хостинге, см. README

SHEET_CSV_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv"

# Двоеточие внутри токена ломает разбор пути в некоторых версиях Flask/Werkzeug,
# поэтому в пути вебхука используем токен с заменённым двоеточием.
WEBHOOK_PATH = "/webhook/" + BOT_TOKEN.replace(":", "_")

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

# chat_id -> {"cat": int, "level_idx": int, "ctry_idx": int}
user_state = {}

# простой кэш строк таблицы, чтобы не дёргать Google каждый раз
_sheet_cache = {"rows": [], "ts": 0}
CACHE_SECONDS = 120


# ---------- Работа с Google Sheets ----------

def fetch_rows():
    now = time.time()
    if now - _sheet_cache["ts"] < CACHE_SECONDS and _sheet_cache["rows"]:
        return _sheet_cache["rows"]
    try:
        resp = requests.get(SHEET_CSV_URL, timeout=10)
        resp.raise_for_status()
        reader = csv.DictReader(io.StringIO(resp.text))
        rows = list(reader)
        _sheet_cache["rows"] = rows
        _sheet_cache["ts"] = now
        return rows
    except Exception as e:
        print("Ошибка чтения Google Sheet:", e)
        return _sheet_cache["rows"]  # вернём старый кэш, если запрос упал


def filter_opportunities(category, level, country, field):
    rows = fetch_rows()
    results = []
    for row in rows:
        row_type = (row.get("Type") or "").strip().lower()
        if row_type != category["sheet_type"].lower():
            continue

        row_level = (row.get("Level") or "").strip().lower()
        if row_level != level.lower():
            continue

        if country.lower() != "worldwide":
            row_country = (row.get("Country") or "").strip().lower()
            if row_country != country.lower():
                continue

        if field.lower() not in ("all fields",):
            row_field = (row.get("Field of Study") or "").strip().lower()
            if row_field != field.lower():
                continue

        results.append(row)
    return results


def format_result(row):
    parts = [f"🎓 {row.get('Opportunity', '').strip()}"]
    if row.get("Country"):
        parts.append(f"🌍 {row['Country'].strip()}")
    if row.get("Field of Study"):
        parts.append(f"📚 {row['Field of Study'].strip()}")
    if row.get("Funding"):
        parts.append(f"💰 {row['Funding'].strip()}")
    if row.get("Deadline"):
        parts.append(f"⏳ Deadline: {row['Deadline'].strip()}")
    if row.get("Requirements"):
        parts.append(f"📋 {row['Requirements'].strip()}")
    if row.get("Official Link"):
        parts.append(f"🔗 {row['Official Link'].strip()}")
    return "\n".join(parts)


# ---------- Клавиатуры ----------

def markup_from_pairs(pairs, row_width=2, back_data="menu:main", back_text="⬅ Back to Main Menu"):
    markup = InlineKeyboardMarkup(row_width=row_width)
    buttons = [InlineKeyboardButton(text, callback_data=cb) for text, cb in pairs]
    markup.add(*buttons)
    if back_data:
        markup.add(InlineKeyboardButton(back_text, callback_data=back_data))
    return markup


def main_menu_markup():
    markup = InlineKeyboardMarkup(row_width=1)
    for text, cb in data.MAIN_MENU_BUTTONS:
        markup.add(InlineKeyboardButton(text, callback_data=cb))
    return markup


def back_main_markup():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("⬅ Back to Main Menu", callback_data="menu:main"))
    return markup


def share_markup():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("✅ I'm Done", callback_data="share:done"))
    markup.add(InlineKeyboardButton("⬅ Back", callback_data="menu:main"))
    return markup


# ---------- Экраны ----------

def show_main_menu(chat_id):
    bot.send_message(chat_id, data.MAIN_MENU_TEXT, reply_markup=main_menu_markup())


def show_categories(chat_id):
    pairs = [(c["button"], f"cat:{i}") for i, c in enumerate(data.CATEGORIES)]
    bot.send_message(chat_id, data.FIND_TEXT, reply_markup=markup_from_pairs(pairs))


def show_levels(chat_id, cat_idx):
    category = data.CATEGORIES[cat_idx]
    pairs = [(lvl, f"lvl:{i}") for i, lvl in enumerate(category["levels"])]
    bot.send_message(chat_id, category["intro"], reply_markup=markup_from_pairs(pairs))


def show_countries(chat_id, cat_idx, level_idx):
    category = data.CATEGORIES[cat_idx]
    pairs = [(c, f"ctry:{i}") for i, c in enumerate(category["countries"])]
    bot.send_message(chat_id, data.COUNTRY_STEP_TEXT, reply_markup=markup_from_pairs(pairs))


def show_fields(chat_id, cat_idx):
    category = data.CATEGORIES[cat_idx]
    pairs = [(f, f"fld:{i}") for i, f in enumerate(category["fields"])]
    bot.send_message(chat_id, data.FIELD_STEP_TEXT, reply_markup=markup_from_pairs(pairs))


def show_results(chat_id, cat_idx, level_idx, ctry_idx, field_idx):
    category = data.CATEGORIES[cat_idx]
    level = category["levels"][level_idx]
    country = category["countries"][ctry_idx]
    field = category["fields"][field_idx]

    results = filter_opportunities(category, level, country, field)

    if not results:
        bot.send_message(chat_id, data.NO_RESULTS_TEXT, reply_markup=back_main_markup())
        return

    bot.send_message(chat_id, f"✨ Found {len(results)} matching opportunit"
                              f"{'y' if len(results) == 1 else 'ies'}:")

    # Telegram допускает до ~4096 символов на сообщение — режем по 8 штук
    chunk = []
    for row in results[:20]:
        chunk.append(format_result(row))
    text = "\n\n".join(chunk)
    for start in range(0, len(text), 3800):
        bot.send_message(chat_id, text[start:start + 3800])

    bot.send_message(chat_id, "⬅", reply_markup=back_main_markup())


# ---------- Хендлеры ----------

@bot.message_handler(commands=["start"])
def cmd_start(message):
    bot.send_message(message.chat.id, data.WELCOME_TEXT)
    show_main_menu(message.chat.id)


@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    data_str = call.data
    chat_id = call.message.chat.id

    if data_str == "menu:main":
        show_main_menu(chat_id)

    elif data_str == "menu:find":
        show_categories(chat_id)

    elif data_str == "menu:share":
        bot.send_message(chat_id, data.SHARE_TEXT, reply_markup=share_markup())

    elif data_str == "share:done":
        bot.send_message(chat_id, data.THANK_YOU_TEXT, reply_markup=back_main_markup())

    elif data_str == "menu:guides":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("📣 Open Channel", url=data.GUIDES_CHANNEL_URL))
        markup.add(InlineKeyboardButton("⬅ Back to Main Menu", callback_data="menu:main"))
        bot.send_message(chat_id, data.GUIDES_TEXT, reply_markup=markup)

    elif data_str == "menu:community":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("🤝 Join Community", url=data.COMMUNITY_CHAT_URL))
        markup.add(InlineKeyboardButton("⬅ Back to Main Menu", callback_data="menu:main"))
        bot.send_message(chat_id, data.COMMUNITY_TEXT, reply_markup=markup)

    elif data_str == "menu:about":
        bot.send_message(chat_id, data.ABOUT_TEXT, reply_markup=back_main_markup())

    elif data_str.startswith("cat:"):
        idx = int(data_str.split(":")[1])
        user_state[chat_id] = {"cat": idx}
        show_levels(chat_id, idx)

    elif data_str.startswith("lvl:"):
        idx = int(data_str.split(":")[1])
        state = user_state.setdefault(chat_id, {})
        state["level_idx"] = idx
        show_countries(chat_id, state["cat"], idx)

    elif data_str.startswith("ctry:"):
        idx = int(data_str.split(":")[1])
        state = user_state.setdefault(chat_id, {})
        state["ctry_idx"] = idx
        show_fields(chat_id, state["cat"])

    elif data_str.startswith("fld:"):
        idx = int(data_str.split(":")[1])
        state = user_state.get(chat_id, {})
        if "cat" in state and "level_idx" in state and "ctry_idx" in state:
            show_results(chat_id, state["cat"], state["level_idx"], state["ctry_idx"], idx)

    try:
        bot.answer_callback_query(call.id)
    except Exception:
        pass


# ---------- Flask / webhook ----------

@app.route(WEBHOOK_PATH, methods=["POST"])
def telegram_webhook():
    json_str = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200


@app.route("/")
def index():
    return "Opportunity Bridge bot is running.", 200


# Вебхук ставим сразу при импорте модуля — gunicorn импортирует bot.py,
# но не выполняет блок "if __name__ == '__main__'", так что регистрировать
# вебхук нужно здесь, а не только при прямом запуске.
if WEBHOOK_URL:
    try:
        bot.remove_webhook()
        bot.set_webhook(url=f"{WEBHOOK_URL}{WEBHOOK_PATH}")
        print("Webhook set to:", f"{WEBHOOK_URL}{WEBHOOK_PATH}")
    except Exception as e:
        print("Не удалось установить вебхук:", e)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
