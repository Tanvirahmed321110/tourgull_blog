from odoo import models, fields


class BlogsModule(models.Model):
    _name = 'tourgull_blog.blog'
    _description = 'tourgull_blogs'


    name = fields.Char(string='Blog Name')
    image_1920 = fields.Image(string='Blog Image', max_width=1920, max_height=1920,)
    image_1024 = fields.Image(string='Blog Image', related='image_1920', max_width=1024, max_height=1024)
    image_520 = fields.Image(string='Blog Image',  related='image_1920', max_width=520, max_height=520)
    image_256 = fields.Image(string='Blog Image',  related='image_1920', max_width=256, max_height=256)
    image_128 = fields.Image(string='Blog Image',  related='image_1920', max_width=128, max_height=128)

    description = fields.Html(string='Blog Desc')

    author_name = fields.Char(string='Author Name')
    author_image = fields.Image(string='author_image', max_width=128, max_height=128)
    publish_date = fields.Date(string='Publish Date')
    is_popular = fields.Boolean(string='Is Popular')

    category_ids  = fields.Many2many('tourgull_blog.blog.category', string='Category', required=True)
    tag_ids = fields.Many2many('tourgull_blog.blog.tag', string='Tags',required=True)
