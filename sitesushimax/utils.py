menu = [{'name': 'Добавить статью', 'url_name': 'home'},
        ]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        user_menu = menu.copy()
        context['menu'] = user_menu
        return context
