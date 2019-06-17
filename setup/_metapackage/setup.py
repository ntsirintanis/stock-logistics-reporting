import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo11-addons-oca-stock-logistics-reporting",
    description="Meta package for oca-stock-logistics-reporting Odoo addons",
    version=version,
    install_requires=[
        'odoo11-addon-stock_picking_comment_template',
        'odoo11-addon-stock_picking_report_custom_description',
        'odoo11-addon-stock_picking_report_valued',
        'odoo11-addon-stock_report_quantity_by_location',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
