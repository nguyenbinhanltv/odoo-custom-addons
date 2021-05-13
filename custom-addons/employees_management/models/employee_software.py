# -*- coding: utf-8 -*-

from odoo import models, fields, api

class employee_software(models.Model):
    _name = 'employees_management.employee_software'
    _description = 'employees_management.employee_software'

    name = fields.Char(string="Tên phần mềm")
    active = fields.Boolean(string="Active", default=True)