from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = "8660493419:AAG5e2mx4PPfcWDGO6Aax6Uf89WjozwBk8c"


# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        ["🔍 Find opportunities"],
        ["📢 Share an Opportunity"],
        ["📝 Application guides"],
        ["👥 Community"],
        ["ℹ️ About Opportunity Bridge"]
    ]

    await update.message.reply_text(
        "🌍 Welcome to Opportunity Bridge!\n\n"
        "We help you discover scholarships 🎓, exchange programs ✈️, "
        "internships 💼, competitions 🏆, summer schools ☀️, "
        "and other international opportunities — all matched to your interests.\n\n"
        "✨ Tell us a bit about yourself, and we'll find the perfect fit for you!",
        reply_markup=ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True
        )
    )


# MAIN MENU BUTTONS
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text


    if text == "🔍 Find opportunities":

        keyboard = [
            ["🎓 Scholarships", "✈️ Exchange Programs"],
            ["☀️ Summer Schools", "💼 Internships"],
            ["🏆 Competitions", "🔬 Research Opportunities"],
            ["🤝 Volunteer Programs"],
            ["⬅️ Back to Main Menu"]
        ]

        await update.message.reply_text(
            "🌍 Find International Opportunities\n\n"
            "Select the type of opportunity you're looking for.",
            reply_markup=ReplyKeyboardMarkup(
                keyboard,
                resize_keyboard=True
            )
        )


    elif text == "🎓 Scholarships":

        keyboard = [
            ["🏛 Bachelor's", "🎓 Master's"],
            ["📚 PhD"],
            ["⬅️ Back to Main Menu"]
        ]

        await update.message.reply_text(
            "🎓 Scholarships & Financial Aid\n\n"
            "Let's help you find scholarships that match your goals. ✨\n\n"
            "First, tell us what level you are applying for.",
            reply_markup=ReplyKeyboardMarkup(
                keyboard,
                resize_keyboard=True
            )
        )


    elif text in ["🏛 Bachelor's", "🎓 Master's", "📚 PhD"]:

        keyboard = [
            ["🇺🇸 USA"],
            ["🇩🇪 Germany"],
            ["🇬🇧 United Kingdom"],
            ["🇨🇦 Canada"],
            ["🇳🇱 Netherlands"],
            ["🇯🇵 Japan"],
            ["🇮🇹 Italy"],
            ["🇭🇺 Hungary"],
            ["🇰🇷 South Korea"],
            ["🇨🇳 China"],
            ["⬅️ Back to Main Menu"]
        ]

        await update.message.reply_text(
            "🌍 Which country would you like to study in?",
            reply_markup=ReplyKeyboardMarkup(
                keyboard,
                resize_keyboard=True
            )
        )


    elif text in [
        "🇺🇸 USA",
        "🇩🇪 Germany",
        "🇬🇧 United Kingdom",
        "🇨🇦 Canada",
        "🇳🇱 Netherlands",
        "🇯🇵 Japan",
        "🇮🇹 Italy",
        "🇭🇺 Hungary",
        "🇰🇷 South Korea",
        "🇨🇳 China"
    ]:

        keyboard = [
            ["📈 Economics"],
            ["💻 Computer Science"],
            ["💼 Business & Management"],
            ["💰 Finance & Accounting"],
            ["📜 Political Science"],
            ["🌍 International Relations"],
            ["⚖️ Law"],
            ["⚙️ Engineering"],
            ["📊 Data Science & AI"],
            ["🩺 Medicine & Health"],
            ["📋 All Fields"],
            ["⬅️ Back to Main Menu"]
        ]

        await update.message.reply_text(
            "🎯 What field of study are you interested in?\n\n"
            "💡 Tip: Tap \"All Fields\" to widen your search and see every cause available!",
            reply_markup=ReplyKeyboardMarkup(
                keyboard,
                resize_keyboard=True
            )
        )


    elif text in [
        "📈 Economics",
        "💻 Computer Science",
        "💼 Business & Management",
        "💰 Finance & Accounting",
        "📜 Political Science",
        "🌍 International Relations",
        "⚖️ Law",
        "⚙️ Engineering",
        "📊 Data Science & AI",
        "🩺 Medicine & Health",
        "📋 All Fields"
    ]:

        await update.message.reply_text(
            "🔎 Searching for opportunities...\n\n"
            "Soon I will connect this with your scholarship database."
        )


    elif text == "⬅️ Back to Main Menu":

        await start(update, context)



def main():

    app = Application.builder().token(8660493419:AAG5e2mx4PPfcWDGO6Aax6Uf89WjozwBk8c).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            menu
        )
    )

    print("Bot is running...")

    app.run_polling()



if name == "main":
    main()
