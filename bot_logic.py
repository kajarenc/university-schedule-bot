SHEDULE = {
    '201': {
        'Monday': [
            "Discrete Mathematics",
            "Object Oriented Programming",
            "Data Structures and Algorithms",
        ],
        'Tuesday': [
            "Data Structures and Algorithms",
            "Object Oriented Programming",
            "Discrete Mathematics",
            "Writing the Essay",

        ],
        'Wednesday': [
            "Data Analysis",
            "Object Oriented Programming",
            "Discrete Mathematics",
            "Data Structures and Algorithms",
        ],
        'Thursday': [
            "Calculus II for Engineers ",
            "Object Oriented Programming",
            "Data Structures and Algorithms",

        ],
        'Friday': [
            "Data Structures and Algorithms",
            "Object Oriented Programming",
            "Calculus II for Engineers ",

        ],
    },
    '202': {
        'Monday': [
            "Object Oriented Programming",
            "Calculus II for Engineers ",
            "Data Analysis",

        ],
        'Tuesday': [
            "Discrete Mathematics",
            "Writing the Essay",
            "Intro To Topology",
            "Calculus II for Engineers ",
        ],
        'Wednesday': [
            "Data Analysis",
            "Discrete Mathematics",
            "Object Oriented Programming",
        ],
        'Thursday': [
            "Data Structures and Algorithms",
            "Object Oriented Programming",
            "Writing the Essay",
            "Data Analysis",
        ],
        'Friday': [
            "Discrete Mathematics",
            "Object Oriented Programming",
            "Data Structures and Algorithms",
        ],
    },
    '203': {
        'Monday': [
            "Writing the Essay",
            "Data Structures and Algorithms",
            "Object Oriented Programming",
            "Discrete Mathematics",
        ],
        'Tuesday': [
            "Data Analysis",
            "Data Structures and Algorithms",
            "Object Oriented Programming",

        ],
        'Wednesday': [
            "Object Oriented Programming",
            "Discrete Mathematics",
            "Data Analysis",
        ],
        'Thursday': [
            "Writing the Essay",
            "Data Analysis",
            "Intro To Topology",
            "Object Oriented Programming",

        ],
        'Friday': [
            "Data Structures and Algorithms",
            "Discrete Mathematics",
            "Data Analysis",

        ],
    }
}

SHEDULE_ARMENIAN = {
    '201': {
        'ԵՐԿՈՒՇԱԲԹԻ': [
            "Տվյալների հենքեր",
            "Հավանականությունների տեսություն",
            "Գործողությունների հետազոտում",

        ],
        'ԵՐԵՔՇԱԲԹԻ': [
            "Դիֆերենցիալ հավասարումներ",
            "Մաթեմատիկական տրամաբանություն",
            "Անգլերեն",
            "Գործողությունների հետազոտում",

        ],
        'ՉՈՐԵՔՇԱԲԹԻ': [
            "Տվյալների հենքեր",
            "Մաթեմատիկական տրամաբանություն",
            "Դիֆերենցիալ հավասարումներ",
        ],
        'ՀԻՆԳՇԱԲԹԻ': [
            "ՓԻԼԻՍՈՓԱՅՈՒԹՅՈՒՆ",
            "Դիֆերենցիալ հավասարումներ",
            "ՏՆՏԵՍԱԳԻՏՈՒԹՅՈՒՆ ",

        ],
        'ՈՒՐԲԱԹ': [
            "Տվյալների հենքեր",
            "Մաթ. ֆիզ. հավասրումներ",
            "Փիլիսոփայություն",
            "Մաթեմատիկական տրամաբանություն",

        ],
    },
    '202': {
        'ԵՐԿՈՒՇԱԲԹԻ': [
            "Տվյալների հենքեր",
            "Հավանականությունների տեսություն",
            "Գործողությունների հետազոտում",

        ],
        'ԵՐԵՔՇԱԲԹԻ': [
            "Դիֆերենցիալ հավասարումներ",
            "Մաթեմատիկական տրամաբանություն",
            "Անգլերեն",
            "Գործողությունների հետազոտում",

        ],
        'ՉՈՐԵՔՇԱԲԹԻ': [
            "Տվյալների հենքեր",
            "Մաթեմատիկական տրամաբանություն",
            "Դիֆերենցիալ հավասարումներ",
        ],
        'ՀԻՆԳՇԱԲԹԻ': [
            "ՓԻԼԻՍՈՓԱՅՈՒԹՅՈՒՆ",
            "Դիֆերենցիալ հավասարումներ",
            "Տնտեսագիտություն",

        ],
        'ՈՒՐԲԱԹ': [
            "Տվյալների հենքեր",
            "Մաթ. ֆիզ. հավասրումներ",
            "Փիլիսոփայություն",
            "Մաթեմատիկական տրամաբանություն",

        ],
    },
    '203': {
        'ԵՐԿՈՒՇԱԲԹԻ': [
            "Տվյալների հենքեր",
            "Հավանականությունների տեսություն",
            "Գործողությունների հետազոտում",

        ],
        'ԵՐԵՔՇԱԲԹԻ': [
            "Դիֆերենցիալ հավասարումներ",
            "Մաթեմատիկական տրամաբանություն",
            "Անգլերեն",
            "Գործողությունների հետազոտում",

        ],
        'ՉՈՐԵՔՇԱԲԹԻ': [
            "Տվյալների հենքեր",
            "Մաթեմատիկական տրամաբանություն",
            "Դիֆերենցիալ հավասարումներ",
        ],
        'ՀԻՆԳՇԱԲԹԻ': [
            "Փիլիսոփայություն",
            "Դիֆերենցիալ հավասարումներ",
            "Տնտեսագիտություն",

        ],
        'ՈՒՐԲԱԹ': [
            "Տվյալների հենքեր",
            "Մաթ. ֆիզ. հավասրումներ",
            "Փիլիսոփայություն",
            "Մաթեմատիկական տրամաբանություն",

        ],
    },

}
WEEKDAYS_ENGLISH = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
WEEKDAYS_ARMENIAN = ["ԵՐԿՈՒՇԱԲԹԻ", "ԵՐԵՔՇԱԲԹԻ", "ՉՈՐԵՔՇԱԲԹԻ", "ՀԻՆԳՇԱԲԹԻ", "ՈՒՐԲԱԹ"]
GROUPS = ['201', '202', '203']
LANGUAGES = ['armenian', 'english']

NEW_USER = 'new_user'
REGISTERED_USER = 'registered_user'

# States are saved in a dict that maps chat_id -> state
state = dict()
# Sometimes you need to save data temporarily
group_context = dict()
language_context = dict()

values = dict()
from telegram import ReplyKeyboardHide, Emoji, ReplyKeyboardMarkup, KeyboardButton
import xml.etree.ElementTree as ET

custom_keyboard = [["Monday", "Tuesday", "Wednesday"],
                   ["Thursday", "Friday"]]
reply_markup = ReplyKeyboardMarkup(custom_keyboard)

custom_keyboard_armenian = [["ԵՐԿՈՒՇԱԲԹԻ", "ԵՐԵՔՇԱԲԹԻ", "ՉՈՐԵՔՇԱԲԹԻ"],
                            ["ՀԻՆԳՇԱԲԹԻ", "ՈՒՐԲԱԹ"]]
reply_markup_armenian = ReplyKeyboardMarkup(custom_keyboard_armenian)

def constract_pretty_shedule_response(chat_context, text):
    resp = ''
    if text in WEEKDAYS_ARMENIAN:
        for i, lesson in enumerate(SHEDULE_ARMENIAN[chat_context][text], start=1):
            resp += str(i) + '.' + lesson + '\n'
    else:
        for i, lesson in enumerate(SHEDULE[chat_context][text], start=1):
            resp += str(i) + '.' + lesson + '\n'

    return resp


def get_random_joke():
    return "random joke"


def handler(bot, update, db, cursor):
    chat_id = update.message.chat.id
    user_id = update.message.from_user.id
    text = update.message.text.encode('utf-8')
    chat_state = state.get(chat_id, NEW_USER)
    chat_context_group = group_context.get(chat_id, None)
    chat_context_language = language_context.get(chat_id, "english")
    tree = ET.parse(chat_context_language + '.xml')
    root = tree.getroot()
    if chat_state == NEW_USER and text == '/start':
        state[chat_id] = NEW_USER  # set the state
        reply_markup_language = ReplyKeyboardMarkup(
            [["armenian", "english"]],
            one_time_keyboard=True)
        text = "Hello, %s ! I'm Shedule_bot , please select language:" % update.message.from_user.name
        bot.sendMessage(chat_id, text=text, reply_markup=reply_markup_language)
    elif text == '/reset':
        state[chat_id] = NEW_USER
        group_context[chat_id] = None
        language_context[chat_id] = "english"
        bot.sendMessage(chat_id,
                        text="Reseted your data , please use /start command to restart our communication",
                        reply_markup=ReplyKeyboardHide())

    elif chat_state == NEW_USER and text in LANGUAGES:
        state[chat_id] = NEW_USER
        language_context[chat_id] = text.lower()
        tree = ET.parse(language_context[chat_id] + '.xml')
        root = tree.getroot()
        text = root.find('lang_choose').text
        bot.sendMessage(chat_id=chat_id, text=text)
    elif chat_state == NEW_USER and text in GROUPS:
        state[chat_id] = REGISTERED_USER
        group_context[chat_id] = text
        chat_context_group = group_context[chat_id]
        text = root.find('pass').text
        query = "insert into users (user_id, chat_id, lang, gruppa) values (%s, %s, '%s', '%s'); " % (
            user_id, chat_id, chat_context_language, chat_context_group)
        print query
        try:
            cursor.execute(query)
            db.commit()
        except:
            pass
        if chat_context_language == 'english':
            bot.sendMessage(chat_id=chat_id, text=text, reply_markup=reply_markup)
        elif chat_context_language == 'armenian':
            bot.sendMessage(chat_id=chat_id, text=text, reply_markup=reply_markup_armenian)
    elif chat_state == NEW_USER and text not in GROUPS:
        text = root.find('annoying').text
        bot.sendMessage(chat_id=chat_id,
                        text=text, reply_markup=ReplyKeyboardHide())

    elif chat_state == REGISTERED_USER:
        if text in WEEKDAYS_ENGLISH or text in WEEKDAYS_ARMENIAN and chat_context_group in GROUPS:
            keyboard = reply_markup if text in WEEKDAYS_ENGLISH else reply_markup_armenian
            bot.sendMessage(chat_id=chat_id, text=constract_pretty_shedule_response(chat_context_group, text),
                            reply_markup=keyboard)
        elif text == "LOL":
            bot.sendMessage(chat_id=chat_id, text=get_random_joke(), reply_markup=reply_markup)
        else:
            keyboard = reply_markup if chat_context_language == 'english' else reply_markup_armenian
            text = "Please use keyboard!" if chat_context_language == 'english' else "Օգտագործիր ստեղնաշար..."
            bot.sendMessage(chat_id,
                            text=text,
                            reply_markup=keyboard)