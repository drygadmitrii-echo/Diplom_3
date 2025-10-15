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

    # хэши ингредиентов: булка, соус, начинка
    ingredient_hashes = {
        IngredientTypes.BUN: '61c0c5a71d1f82001bdaaa6c',
        IngredientTypes.SAUCE: '61c0c5a71d1f82001bdaaa75',
        IngredientTypes.FILLING: '61c0c5a71d1f82001bdaaa70'
    }

    # поведение счетчиков ингредиентов при добавлении в бургер
    counter_behavior = {
        IngredientTypes.BUN: ['0', '2', '2'],
        IngredientTypes.SAUCE: ['0', '1', '2'],
        IngredientTypes.FILLING: ['0', '1', '2']
    }


class CounterTypes:
    ALL_TIME = 'all_time'
    TODAY = 'today'