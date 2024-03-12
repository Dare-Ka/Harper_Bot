from meal.meal_text import dinner_dict
from events.events_text import donate_reminder, ad_bot
from random import choice, randint


async def get_random_meal() -> str:
    """Get random dinner idea"""
    if randint(0, 100) < 5:
        donate = donate_reminder
    elif randint(0, 100) < 10:
        donate = ad_bot
    else:
        donate = ''
    return (f'Придумал!\n'
            f'Попробуй <u>{choice(dinner_dict["Блюдо"])}</u>,'
            f' а на гарнир пусть будет <u>{choice(dinner_dict["Гарнир"])}</u>. '
            f'К этому блюду очень хорошо подойдет <u>{choice(dinner_dict["Салат"])}</u>!\n'
            f'А на закуску попробуй <u>{choice(dinner_dict["Закуски"])}</u>🥪🍔\n'
            f'Приятного аппетита!😋') + donate
