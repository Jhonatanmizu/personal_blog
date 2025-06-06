from .models import SiteSetup


def app_setup(_):
    setup = SiteSetup.objects.order_by('-id').first()

    if not setup:
        return {
            'app_setup': 'app_setup'
        }

    return {
        'app_setup': 'app_setup',
        "title": setup.title,
        "description": setup.description,
        "show_header": setup.show_header,
        "show_search": setup.show_search,
        "show_menu": setup.show_menu,
        "show_description": setup,
        "favicon": setup.favicon,
    }
