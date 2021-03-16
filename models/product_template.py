from odoo import fields, models, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    image_catalog = fields.Binary(string="Imagen para catálogo")