from odoo import http
from odoo.http import request as req


class BlogModule(http.Controller):
    @http.route('/blogs', auth='public')
    def all_country(self, **kw):

        blog_data = req.env['tourgull_blog.blog_page'].browse(1)
        categories = req.env['tourgull_blog.blog.category'].search([])

        tag_id = kw.get('tag_id')
        if tag_id and tag_id.isdigit():
            blogs = req.env['tourgull_blog.blog'].search([('tag_ids', 'in', int(tag_id))])
        else:
            blogs = req.env['tourgull_blog.blog'].search([])

        return req.render('tourgull_blog.blog_page', {
            'blog_data': blog_data,
            'categories': categories,
            'blogs': blogs,
        })
