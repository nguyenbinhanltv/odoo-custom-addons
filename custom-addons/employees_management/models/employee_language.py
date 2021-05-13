# -*- coding: utf-8 -*-

from odoo import models, fields, api

class employee_language(models.Model):
    _name = 'employees_management.employee_language'
    _description = 'employees_management.employee_language'

    name = fields.Char(string="Tên ngôn ngữ")
    active = fields.Boolean(string="Active", default=True)