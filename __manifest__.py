{
    'name': 'Product Catalog',
    'author': 'José Musun',
    'description': 'Creación de catálogos ',
    'version': '13.0',
    'depends': [
        'base',
        'product',
        'web_widget_colorpicker',
        'web_widget_font'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/product_catalog.xml',
        'views/report_catalog.xml',
        'views/reports.xml'
    ]
}