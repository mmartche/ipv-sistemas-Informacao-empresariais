# from odoo import http


# class AddonCustom(http.Controller):
#     @http.route('/addon_custom/addon_custom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addon_custom/addon_custom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('addon_custom.listing', {
#             'root': '/addon_custom/addon_custom',
#             'objects': http.request.env['addon_custom.addon_custom'].search([]),
#         })

#     @http.route('/addon_custom/addon_custom/objects/<model("addon_custom.addon_custom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addon_custom.object', {
#             'object': obj
#         })

