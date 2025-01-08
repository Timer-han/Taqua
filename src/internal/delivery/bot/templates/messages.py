# TODO: make levels more objective and refactor messages
KNOWLEDGE_LEVEL_DETERMINE_MSG = (
    "Привет! Я позволяю изучить новые и закрепить старые знания в исламе"
    "(на данный момент только Фикх, но я не планирую останавливаться).\n\n"
    "Позволь узнать твой примерный уровень, чтобы подбирать релевантные вопросы. Выбери цифру от 1 до 5, где:\n\n"
    "1️⃣ - Слышал про намаз и пост, но не знаю как их соблюдать. Вообще, я новенький и хочу все изучить)\n"
    "2️⃣ - Совершаю намаз, держу пост, а их что может что-то нарушить?\n"
    "3️⃣ - Знаю основные сунны и фарзы, но у меня очень расплывчатые знания\n"
    "4️⃣ - Знаю адабы/сунны/фарзы намаза/омовения/поста/брака/торговых отношений, но некоторые вещи забылись и "
    "мне хочется просто повторить\n"
    "5️⃣ - Закончил высшее образование или медресе, хочу повторить все"
)

START_HANDLER_RESPONSE_MSG = (
    "Привет! Я позволяю изучить новые и закрепить старые знания в исламе.\n"
    "Мои основные команды:\n"
    "/help - помощь в использовании\n"
    "/lesson - начать урок\n"
    "/profile - статистика\n"
    "/faq - частые вопросы\n"
    "/suggest - предложить вопрос"
    "/feedback - оставить отзыв\n"
)

LEVEL_ORIENTED_RESPONSE_MSG = {
    "1": "Круто, что ты хочешь изучать религию. Главное не останавливайся",
    "2": "Хорошо, что ты выполняешь столпы ислама. Данный бот тебе поможет изучить и узнать про ислам больше",
    "3": "something",
    "4": "something",
    "5": "Я смотрю ты знаток своего дела. Поэтому, для тебя дополнительно хотим предложить возможность добавлять и "
         "проверять вопросы перед тем, как они попадут к пользователям. \n\n"
         "Если тебе это интересно, то напиши кому-то из нас: @IskanderShakiroff или @Timer_han",
}

FIRST_LESSON_TAKE_OFFER_MSG = (
    "Если ты готов изучение, то можно начать учиться /lesson))\n\n"
    "Каждый урок состоит из 10 вопросов. В вопросе есть 4 варианта ответа, один из которых правильный.\n"
    "✅При правильном ответе, перейдешь на следующий\n"
    "❌Если ответишь неправильно, бот добавит описание правильного ответа\n"
    "‼️Советуем его прочитать и запомнить, потому что бот еще раз задаст этот вопрос через некоторое время"
)

QUESTION_SUGGEST_MSG = (
    "Спасибо, что вносишь вклад в базу вопросов. Удобнее всего добавлять вопрос не через бота, а на сайте. Ссылку можно получить в профиле\n\n"
    "Чтобы добавить вопрос, следуй инструкции ниже:\n"
    "Первым делом сформулируй вопрос и отправь его сюда без вариантов ответа. То есть в таком виде, каким его увидит ученик.\n\n"
    "Пример:\n<code>В какой временной период надо соблюдать пост?</code>"
)

QUESTION_RECEIVE_MSG = (
    "А теперь добавь варианты ответа через перевод строки, количество ответов должно быть от 2 до 5\n\n"
    "Пример:\n<code>когда проснулся - до вечера\nот восхода - до захода\nот захода - до восхода\nс зенита - до полуночи</code>"
)

CORRECT_ANSWERS_RECEIVE_MSG = (
    "Спасибо, скажи, какой из вариантов ответа верный?\n\n"
)

QUESTION_SUGGEST_GRATITUDE_MSG = (
    "Спасибо за предоставленный вопрос. Чтобы удостовериться в правильности, каждый вопрос обрабатывается знающими людьми "
    "и этот вопрос не исключение, поэтому придется подождать пока его проверят)\n\n"
)

QUESTION_CANCEL_MSG = (
    "Понял, ну ты если передумаешь, можешь создать вопрос еще раз)"
)

PROFILE_MSG = (
    "Профиль, твоя ссылка для добавления вопросов: "
)

QUESITON_REVIEW_MSG = (
    "Если ты не знаешь, как проверять вопросы, это можно узнать введя /help\n\n"
)

NO_QUESTIONS_FOR_REVIEW_MSG = (
    "Пока нет вопросов для проверки, но мы обязательно тебе сообщим, когда они появятся"
)

FINISH_QUESTION_REVIEW_MSG = (
    "Спасибо за выделенное время)"
)

BAD_QUESTION_REVIEW_MSG = (
    "Можешь описать, почему данный вопрос плохой?"
)

IMPROVE_QUESTION_REVIEW_MSG = (
    "Можешь описать, как бы ты улучшил данный вопрос?"
)

GET_ADMIN_RIGHTS = (
    "Хитрец, вначале получи права администратора)\n"
)