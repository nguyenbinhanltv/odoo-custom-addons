# -*- coding: utf-8 -*-
# from odoo import http


# class EmployeesManagement(http.Controller):
#     @http.route('/employees_management/employees_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/employees_management/employees_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('employees_management.listing', {
#             'root': '/employees_management/employees_management',
#             'objects': http.request.env['employees_management.employees_management'].search([]),
#         })

#     @http.route('/employees_management/employees_management/objects/<model("employees_management.employees_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('employees_management.object', {
#             'object': obj
#         })
