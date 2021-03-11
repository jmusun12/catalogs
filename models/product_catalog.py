from odoo import models, fields


class ProductCatalog(models.Model):
    _name = 'product.catalog'
    _description = 'Modelo para creación de catálogos de productos'

    name = fields.Char(string='Nombre', required=True)
    company_id = fields.Many2one('res.company', string='Empresa', default=lambda self: self.env.user.company_id,
                                 readonly=True)
    header_image = fields.Binary('Imagen de encabezado', required=True)
    footer_image = fields.Binary('Imagen del pie de pagina', required=True)
    text_color_title = fields.Char('Color del titulo del encabezado', required=True)
    font_size_title = fields.Integer(string='Tamaño de fuente', required=True, default=12)
    font_type_title = fields.Char('Tipografía del titulo del encabezado', required=True)
    color_content_product = fields.Char('Color del cuadrado del producto', required=True)
    text_color_product = fields.Char('Color de texto del producto', required=True)
    font_size_text_product = fields.Integer(string='Tamaño de fuente', required=True, default=12)
    font_type_text_product = fields.Char('Tipografía del texto del producto', required=True)

    product_ids = fields.One2many(comodel_name="product.catalog.line", inverse_name="catalog_id", string="Productos")

    def print_product_catalog(self):
        return self.env.ref('catalogs.report_product_catalog').report_action(self)

    def css_title(self):
        return 'color: {0} !important; font-family: {1} !important; font-size: {2} !important;'.format(
            self.text_color_title, self.font_type_title, self.font_size_title
        )

class ProductCatalogLine(models.Model):
    _name = 'product.catalog.line'
    _description = 'Lineas del catalogo'

    catalog_id = fields.Many2one('product.catalog', 'Catalogo', ondelete="cascade")
    product_id = fields.Many2one(comodel_name="product.template", string="Producto")
    company_id = fields.Many2one('res.company', string='Empresa', default=lambda self: self.env.user.company_id)



