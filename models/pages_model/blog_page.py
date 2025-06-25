from odoo import models, fields

class BlogsModule(models.Model):
    _name = 'tourgull_blog.blog_page'

    image_1920 = fields.Image(string='Banner Image')
    banner_desc = fields.Text(string='Banner Desc')

    section_title = fields.Char(string='Section Title')
    section_desc = fields.Char(string='Section Desc')

    ads_image = fields.Image(string='Ads Image')  # ✅ Fixed field name
    ads_url = fields.Char(string='Ads URL')       # ✅ Better string name
