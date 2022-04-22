menu = [{'name': 'Пиццы', 'url_name': 'pizza_page'},
        {'name': 'Роллы', 'url_name': 'sushi_page'},
        {'name': 'Закуски', 'url_name': 'snacks_page'},
        {'name': 'Салаты', 'url_name': 'salads_page'},
        ]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        user_menu = menu.copy()
        context['menu'] = user_menu
        return context
