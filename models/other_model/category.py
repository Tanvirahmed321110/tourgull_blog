from odoo import models, fields

class BlogsModule(models.Model):
    _name = 'tourgull_blog.blog.category'
    _description = 'Blog Category'

    name = fields.Char(string='Blog Category')


