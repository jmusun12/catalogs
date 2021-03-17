from odoo import models, fields
import logging

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
    width_image = fields.Char(string='Ancho imagen (medidas en px, rem, %)', default='130px', required=True)
    height_image = fields.Char(string='Alto imagen (medidas en px, rem, %)', default='130px', required=True)

    product_ids = fields.One2many(comodel_name="product.catalog.line", inverse_name="catalog_id", string="Productos")

    def print_product_catalog(self):
        return self.env.ref('catalogs.report_product_catalog').report_action(self)

    def css_title(self):
        self.ensure_one()
        return 'color: {0} !important; font-family: {1} !important; font-size: {2}px !important;'.format(
            self.text_color_title, self.font_type_title, self.font_size_title
        )

    def css_border_rect(self):
        self.ensure_one()
        return 'border: 1px solid {0} !important; width: 200px !important; height: 300px !important;'.format(self.color_content_product)

    def css_bg_rect(self):
        self.ensure_one()
        return 'background-color:{0} !important; padding: 5px; width: 200px !important; height: 110px !important'.format(self.color_content_product)

    def css_data_rect(self):
        self.ensure_one()
        return 'color: {0} !important; font-family: {1} !important; font-size: {2}px !important; overflow-wrap: ' \
               'break-word;'.format(
            self.text_color_product, self.font_type_text_product, self.font_size_text_product
        )

    def css_data_rect(self):
        self.ensure_one()
        return 'color: {0} !important; font-family: {1} !important; font-size: {2}px !important; margin-bottom: 1px; ' \
               'margin-top: 1px;'.format(
            self.text_color_product, self.font_type_text_product, self.font_size_text_product
        )

    def css_image_product(self):
        self.ensure_one()
        return 'width: {0} !important; height: {1} !important; margin-top: 20px !important; margin-bottom: 20px ' \
               '!important;'.format("147px", "147px")

    def group_lines(self):
        self.ensure_one()

        cont = 0
        groups = []
        aux = []
        for line in self.product_ids:
            if cont > 5:
                groups.append(aux)
                aux = []
                cont = 0

            aux.append(line)
            cont += 1

        if len(aux):
            groups.append(aux)

        return groups


class ProductCatalogLine(models.Model):
    _name = 'product.catalog.line'
    _description = 'Lineas del catalogo'

    catalog_id = fields.Many2one('product.catalog', 'Catalogo', ondelete="cascade")
    product_id = fields.Many2one(comodel_name="product.template", string="Producto")
    company_id = fields.Many2one('res.company', string='Empresa', default=lambda self: self.env.user.company_id)
    product_image = fields.Binary('Imagen Producto', related='product_id.image_catalog')


