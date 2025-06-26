from odoo import http
from odoo.http import request as req


class BlogModule(http.Controller):
    @http.route('/blogs/blog_details/', auth='public')
    def all_country(self, **kw):
        blog_id = kw.get('id')

        blog = req.env['tourgull_blog.blog'].browse(int(blog_id))
        popular_blogs = req.env['tourgull_blog.blog'].search([('is_popular', '=', True)])


        if not blog_id:
            return req.redirect('/blogs')

        return req.render('tourgull_blog.blog_details_page', {
            'blog': blog,
            'popular_blogs': popular_blogs,
        })
