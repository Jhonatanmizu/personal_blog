from .models import MenuLink, SiteSetup


def app_setup(_):
    setup = SiteSetup.objects.order_by('-id').first()
    menu = MenuLink.objects.filter(site_setup=setup)

    if not setup:
        return {
            "title": "",
            "description": "",
            "show_header": False,
            "show_search": False,
            "show_menu": False,
            "show_footer": False,
            "show_description": False,
            "favicon": "",
            "menu": []
        }

    return {
        "title": setup.title,
        "description": setup.description,
        "show_header": setup.show_header,
        "show_search": setup.show_search,
        "show_menu": setup.show_menu,
        "show_footer": setup.show_footer,
        "show_description": setup,
        "favicon": setup.favicon,
        "menu": menu
    }
