{
   'name': 'Theme Pragmatic',
   'description': 'Tema Pragmatic Ingeniería',
   'category': 'Theme/Website',
   'version': '16.0',
   'author': 'Pragmatic Ingeniería',
   'depends': ['web','website'],
   'data': [
        'views/pages/home.xml',
        'views/pages/contactus.xml',
        'views/pages/blog.xml',
        'views/pages/404.xml',
        'views/pages/about_us.xml',
        'views/pages/software_erp.xml',
        'views/menu.xml',
        'views/website_templates.xml',
        'views/presets.xml'
    ],


    'assets': {
        'web.assets_frontend': [
        'theme_pragmatic/static/src/scss/website_templates.scss',
        'theme_pragmatic/static/src/scss/style_home.scss',
        'theme_pragmatic/static/src/scss/style_contact.scss',
        'theme_pragmatic/static/src/scss/style_blog.scss'
        ],
    },


    'installable': True,
    'auto_install': False,
    'application': True,


}