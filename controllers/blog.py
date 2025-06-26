from odoo import http
from odoo.http import request as req


class BlogModule(http.Controller):
    @http.route('/blogs', auth='public')
    def all_country(self, **kw):

        blog_data = req.env['tourgull_blog.blog_page'].browse(1)
        categories = req.env['tourgull_blog.blog.category'].search([])

        tag_id = kw.get('tag_id')
        category_id = kw.get('category_id')

        blog_list = []

        if tag_id and tag_id.isdigit():
            blog_list.append(('tag_ids', 'in', int(tag_id)))

        if category_id and category_id.isdigit():
            blog_list.append(('category_ids', 'in', int(category_id)))

        blogs = req.env['tourgull_blog.blog'].search(blog_list)

        return req.render('tourgull_blog.blog_page', {
            'blog_data': blog_data,
            'categories': categories,
            'blogs': blogs,
        })

