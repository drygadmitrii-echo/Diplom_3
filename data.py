class UserCredentials:
    email = "uitestuser@mail.ru"
    password = "UIPass123!"


class Timeout:
    DEFAULT = 10


class IngredientTypes:
    BUN = 'bun'
    SAUCE = 'sauce'
    FILLING = 'filling'


class IngredientData:
    ingredient_types = [IngredientTypes.BUN, IngredientTypes.SAUCE, IngredientTypes.FILLING]
    ingredient_hashes = {
        IngredientTypes.BUN: '61c0c5a71d1f82001bdaaa6c',
        IngredientTypes.SAUCE: '61c0c5a71d1f82001bdaaa75',
        IngredientTypes.FILLING: '61c0c5a71d1f82001bdaaa70'
    }


class CounterTypes:
    ALL_TIME = 'all_time'
    TODAY = 'today'
