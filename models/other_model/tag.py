from odoo import models, fields

class BlogsModule(models.Model):
    _name = 'tourgull_blog.blog.tag'
    _description = 'Blog Tags'

    name = fields.Char(string='Tag')