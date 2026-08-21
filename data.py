# -*- coding: utf-8 -*-
"""
Все тексты и списки кнопок бота Opportunity Bridge.
Меняешь текст здесь — не трогая логику в bot.py.
"""

# ---------- Стандартные списки стран ----------

STANDARD_COUNTRIES = [
    "🇺🇸 USA", "🇩🇪 Germany", "🇬🇧 United Kingdom", "🇨🇦 Canada",
    "🇳🇱 Netherlands", "🇯🇵 Japan", "🇮🇹 Italy", "🇭🇺 Hungary",
    "🇰🇷 South Korea", "🇨🇳 China",
]

EXCHANGE_COUNTRIES = STANDARD_COUNTRIES + ["🌍 Worldwide"]

INTERNSHIP_COUNTRIES = [
    "🇺🇸 USA", "🇩🇪 Germany", "🇬🇧 United Kingdom", "🇨🇦 Canada",
    "🇳🇱 Netherlands", "🇯🇵 Japan", "🇮🇹 Italy", "🇭🇺 Hungary",
    "🇰🇷 South Korea", "🇨🇳 China",
]

VOLUNTEER_COUNTRIES = STANDARD_COUNTRIES + [
    "🇺🇿 Uzbekistan", "🇰🇿 Kazakhstan", "🇰🇬 Kyrgyzstan", "🇷🇺 Russian",
]

# ---------- Уровни образования ----------

LEVELS_FULL = ["🎒 Middle School", "🏫 High School", "🏛️ Bachelor's", "🎓 Master's", "📚 PhD"]
LEVELS_NO_SCHOOL = ["🏛️ Bachelor's", "🎓 Master's", "📚 PhD"]
LEVELS_NO_MIDDLE = ["🏫 High School", "🏛️ Bachelor's", "🎓 Master's", "📚 PhD"]

# ---------- Главное меню ----------

WELCOME_TEXT = (
    "🌍 Welcome to Opportunity Bridge!\n\n"
    "We help you discover scholarships 🎓, exchange programs ✈️, internships 💼, "
    "competitions 🏆, summer schools ☀️, and other international opportunities — "
    "all matched to your interests.\n\n"
    "✨ Tell us a bit about yourself, and we'll find the perfect fit for you!"
)

MAIN_MENU_TEXT = "⭐ What would you like to do?"

MAIN_MENU_BUTTONS = [
    ("🔍 Find opportunities", "menu:find"),
    ("📣 Share an Opportunity", "menu:share"),
    ("📝 Application guides", "menu:guides"),
    ("👥 Community", "menu:community"),
    ("ℹ️ About Opportunity Bridge", "menu:about"),
]

GUIDES_TEXT = (
    "📝 Application Guides\n"
    "We've put together a collection of practical guides to help you prepare "
    "stronger applications for scholarships, internships, exchange programs, "
    "and universities. 📚\n\n"
    "📢 In our Telegram channel, you'll find:\n"
    "📄 CV Guide\n"
    "✉️ Motivation Letter\n"
    "💡 Personal Statement\n"
    "💌 Recommendation Letters\n"
    "📋 Required Documents\n"
    "🎤 Interview Preparation\n"
    "⏱ Application Timeline\n"
    "💻 Useful Resources\n"
    "🏆 Accepted Students' Tips\n\n"
    "💚 Join our Telegram channel to access all guides and future updates:"
)
# ссылка на канал — впиши сюда свою
GUIDES_CHANNEL_URL = "https://t.me/oppbridge"

COMMUNITY_TEXT = (
    "👥 Opportunity Bridge Community\n\n"
    "You don't have to navigate your journey alone! 🌟 Join thousands of students "
    "worldwide who are exploring scholarships, universities, internships, and "
    "international opportunities together.\n\n"
    "In our community, you can:\n"
    "🌍 Share and discover useful opportunities\n"
    "💬 Ask questions and get real answers from students who've been there\n"
    "🤝 Connect with peers from different countries and cultures\n"
    "🎓 Discuss applications, exams, and university admissions\n\n"
    "🚀 Whether you're just starting out or already deep into applications — "
    "you'll find support, motivation, and friends here.\n\n"
    "Join us and grow together!"
)
# ссылка на группу/чат — впиши сюда свою
COMMUNITY_CHAT_URL = "https://t.me/oppbridge_01"

ABOUT_TEXT = (
    "About Opportunity Bridge team 🌟\n\n"
    "Umarova Sabina Jonibekovna 🇺🇿\n"
    "Hobbies: Dancing, reading.\n"
    "Motivation: To become the best version of myself.\n"
    "Projects & Experience:\n"
    "• Founder of Opportunity Bridge\n"
    "• Founder of Economics for Youth\n"
    "• Finance member at Hack Tashkent\n"
    "• Ambassador Research Hub\n"
    "• Research Lead\n\n"
    "Kuznetsova Anna 🇷🇺\n"
    "Hobbies: art, learning languages, skateboarding\n"
    "Motivation: Get a top-tier education in USA, receive a scholarship and become the best version of myself\n"
    "Projects & Experience:\n"
    "• Founder of catseng online school\n"
    "• Winner in 2 national English language olympiads\n"
    "• 10 years of learning English & 1.5 years of learning Chinese\n\n"
    "Bashkova Daria 🇷🇺\n"
    "Hobbies: Painting, dancing, language learning.\n"
    "Motivation: To achieve complete financial independence, receive a top-tier European education, and build a successful international career in business and art.\n"
    "Projects & Experience:\n"
    "• Artist (international artwork sales)\n"
    "• Professional dancer (10 years of competitive experience)\n\n"
    "Vasiuk Snizhana Yuriivna 🇺🇦\n"
    "Hobbies: Pilates, reading, painting.\n"
    "Motivation: The desire to live abroad as a financially independent person.\n"
    "Projects & Experience:\n"
    "• Content Manager for the School Safety Team (SST)\n"
    "• Participant in the Save the Children International programme\n\n"
    "Kazarian Arina Gareginovna 🇦🇲\n"
    "Hobbies: filming, dancing\n"
    "Motivation: to study in China\n"
    "Projects & Experience:\n"
    "• Completed internships at Slice Consulting, Digoo IT Distribution, and ReEducate Armenia, doing market research\n"
    "• Co-founder of an English speaking club in Armenia \"SPEAKS\""
)

SHARE_TEXT = (
    "📩 Share an Opportunity\n"
    "Found a scholarship, internship, summer school, competition, or research "
    "opportunity? Help other students discover it too! 🌍\n\n"
    "📦 Please send us the following details:\n"
    "🎯 Type of Opportunity: (Scholarship / Internship / Summer School / "
    "Competition / Volunteer Program / Research Opportunity)\n"
    "🎓 Opportunity Name\n"
    "🌍 Country\n"
    "📚 Field of Study\n"
    "💰 Funding\n"
    "⏳ Deadline\n"
    "🔗 Official Link\n"
    "📑 Requirements\n\n"
    "📤 Send your submission here: @hanaw_095\n"
    "✅ Once you're done, press I'm Done."
)

THANK_YOU_TEXT = (
    "✅ Thank You for Sharing!\n"
    "We've received your submission!\n"
    "🔍 Our team will carefully review the information. If it meets our quality "
    "standards, it will be added to Opportunity Bridge to help students around "
    "the world. 🌍\n"
    "💚 Thank you for making educational opportunities more accessible!"
)

FIND_TEXT = "🌍 Find International Opportunities\n\nSelect the type of opportunity you're looking for."

# ---------- Категории (порядок = порядок кнопок) ----------
# sheet_type -> должно совпадать со значением в колонке "Type" твоей Google Sheet

FIELDS_ACADEMIC = [
    "📈 Economics", "💻 Computer Science", "💼 Business & Management", "💰 Finance & Accounting",
    "🏛️ Political Science", "🌍 International Relations", "🗣️ Languages & Linguistics", "⚖️ Law",
    "⚙️ Engineering", "📊 Data Science & AI", "🌱 Natural Sciences", "🩺 Medicine & Health",
    "🎨 Graphic & Product Design", "🎬 Media & Film", "🏛️ Architecture", "📰 Journalism",
    "📑 Exact Science", "🌐 All Fields",
]

FIELDS_SUMMER = [
    "🔬 STEM & Technology", "💻 Computer Science", "💰 Business & Entrepreneurship",
    "🩺 Medicine & Health Sciences", "⚖️ Law", "🏛️ Political Science", "🎨 Art & Design",
    "🎭 Performing Arts & Music", "🗣️ Languages", "🌍 International Relations",
    "🌱 Environmental Science", "👑 Leadership", "📚 Humanities & Literature",
    "📑 Exact Science", "🌱 Natural Science", "📸 Media & Journalism", "🧩 Critical Thinking",
    "🌐 All Fields",
]

FIELDS_INTERNSHIP = [
    "📊 Data Science & AI", "💰 Finance & Banking", "📈 Business & Consulting", "📣 Marketing & Sales",
    "🩺 Medicine & Health Sciences", "⚖️ Law", "Political Science", "👥 Human Resources",
    "💻 Computer Science", "⚙️ Engineering", "📸 Media & Communications", "🌱 Environmental Science",
    "🌍 International Relations", "🍳 Hospitality & Tourism", "🎨 Art & Design",
    "📑 Exact Science", "🌱 Natural Science", "🌐 All Fields",
]

FIELDS_COMPETITION = [
    "🔬 Science & Engineering", "🔢 Mathematics", "💻 Coding", "🤖 Robotics & Technology",
    "💰 Business & Entrepreneurship", "⚖️ Law", "📈 Economics", "🏛️ Political Science", "🗣️ Debate",
    "🎨 Art & Design", "✍️ Writing & Essay", "🌍 MUN", "🌱 Environmental Science", "👑 Leadership",
    "🩺 Medicine & Health Sciences", "🌐 All Fields", 
]

FIELDS_RESEARCH = [
    "🔬 STEM & Natural Sciences", "🧬 Biology & Life Sciences", "💻 Computer Science",
    "⚙️ Engineering", "🧪 Chemistry", "🔭 Physics", "📊 Data Science & AI",
    "🩺 Medicine & Health Sciences", "🌱 Environmental Science", "🧠 Psychology & Neuroscience",
    "📈 Economics", "🏛️ Political Science", "📚 Humanities & Social Sciences",
    "🌍 International Relations", "🧑‍🤝‍🧑 Sociology", "🏙️ Society", "⚙️ Technology", "🦉 Philosophy", "🎵 Music/Music Theory",
    "🎬 Media/Film Studies", "🔢 Mathematics", "📚 Literature", "📜 History", "🚻 Gender Studies",
    "🎓 Education", "🌿 Ecology", "🎭 Culture Studies", "🗿 Anthropology", "🏗️ Architecture",
    "🖼️ Art History", "🔭 Astronomy", "💼 Business", "🌐 All Fields",
]

FIELDS_VOLUNTEER = [
    "🌱Environmental", "🩺 Health & Medical Aid", "📚 Education & Tutoring",
    "🏠 Community Development", "🍲 Poverty & Hunger Relief", "🐾 Animal Welfare",
    "⚖️ Human Rights / Social Justice", "🧒 Youth & Children Programs", "🎨 Arts & Culture",
    "🌐 All Fields",
]

CATEGORIES = [
    {
        "key": "scholarships",
        "button": "🎓 Scholarships",
        "sheet_type": ["Scholarship", "Scholarships"],
        "intro": (
            "🎓 Scholarships & Financial Aid\n"
            "Let's help you find scholarships that match your goals. ✨\n"
            "First, tell us what level you are applying for."
        ),
        "levels": LEVELS_NO_SCHOOL,
        "countries": STANDARD_COUNTRIES,
        "fields": FIELDS_ACADEMIC,
    },
    {
        "key": "exchange",
        "button": "✈️ Exchange Programs",
        "sheet_type": ["Exchange Program", "Exchange Programs"],
        "intro": (
            "✈️ Ready to study abroad and experience a new culture?\n"
            "Let's find the best exchange programs for you! ✈️\n"
            "🎓 First, select your current education level:"
        ),
        "levels": LEVELS_FULL,
        "countries": EXCHANGE_COUNTRIES,
        "fields": FIELDS_ACADEMIC,
    },
    {
        "key": "summer",
        "button": "☀️ Summer Schools",
        "sheet_type": ["Summer School", "Summer Schools"],
        "intro": (
            "☀️ Discover Summer Schools Around the World\n"
            "Explore international summer schools tailored to your profile! ✨\n"
            "🎓 First, choose your academic level:"
        ),
        "levels": LEVELS_FULL,
        "countries": STANDARD_COUNTRIES,
        "fields": FIELDS_SUMMER,
    },
    {
        "key": "internships",
        "button": "💼 Internships",
        "sheet_type": ["Internship", "Internships"],
        "intro": (
            "💼 Find International Internships\n"
            "Take the next step in your career — explore internship opportunities "
            "around the world! 🌍\n"
            "🎓 Choose your academic level to begin:"
        ),
        "levels": LEVELS_NO_MIDDLE,
        "countries": INTERNSHIP_COUNTRIES,
        "fields": FIELDS_INTERNSHIP,
    },
    {
        "key": "competitions",
        "button": "🏆 Competitions",
        "sheet_type": ["Competition", "Competitions"],
        "intro": (
            "🏆 Explore International Competitions\n"
            "Discover academic, business, science, technology, and leadership "
            "competitions from around the world! 🌍\n"
            "🎓 Choose your academic level to begin:"
        ),
        "levels": LEVELS_FULL,
        "countries": STANDARD_COUNTRIES,
        "fields": FIELDS_COMPETITION,
    },
    {
        "key": "research",
        "button": "🔬 Research Opportunities",
        "sheet_type": ["Research Opportunity", "Research Opportunities"],
        "intro": (
            "🔬 Discover Research Opportunities\n"
            "Find research programs, laboratories, academic projects, and research "
            "internships worldwide!\n"
            "🎓 Choose your academic level:"
        ),
        "levels": LEVELS_FULL,
        "countries": STANDARD_COUNTRIES,
        "fields": FIELDS_RESEARCH,
    },
    {
        "key": "volunteer",
        "button": "💚 Volunteer Programs",
        "sheet_type": ["Volunteer Program", "Volunteer Programs"],
        "intro": (
            "💚 Volunteer Around the World\n"
            "Explore volunteer and community service opportunities that let you "
            "gain experience while making a positive impact.\n"
            "🎓 Choose your academic level:"
        ),
        "levels": LEVELS_FULL,
        "countries": VOLUNTEER_COUNTRIES,
        "fields": FIELDS_VOLUNTEER,
    },
]

COUNTRY_STEP_TEXT = "🌍 Choose Your Destination\nWhich country's opportunities would you like to explore?"
FIELD_STEP_TEXT = (
    "📌 Choose Your Field of Study\n"
    "Select the category that matches your interests.\n"
)
NO_RESULTS_TEXT = (
    "😕 No matching opportunities found yet.\n"
    "Try choosing \"All Fields\" or a different country — new opportunities are "
    "added regularly!"
)
