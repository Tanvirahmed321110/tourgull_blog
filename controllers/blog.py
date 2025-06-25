from odoo import http
from odoo.http import request as req

class BlogModule(http.Controller):
    @http.route('/blogs', auth='public')
    def all_country(self,**kw):
        # all_country_data = req.env['tourgull_visa.all_country'].search([])


        return req.render('tourgull_blog.blog_page',{
            'all_country_data':'all_country_data',
        })