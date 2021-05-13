# -*- coding: utf-8 -*-

from odoo import models, fields, api

class employee_family(models.Model):
    _name = 'employees_management.employee_family'
    _description = 'employees_management.employee_family'

    name = fields.Char(string="Họ và tên")
    bdate = fields.Date(string="Năm sinh")
    relationship = fields.Selection([
        ('father', 'Cha'),
        ('mother', 'Mẹ'),
        ('brother', 'Anh (em) trai'),
        ('sister', 'Anh (em) gái'),
        ('other', 'Khác'),
    ], string="Mối quan hệ")
    job = fields.Char(string="Nghề nghiệp")
    place_work = fields.Char(string="Nơi đang công tác")
    address = fields.Text(string="Địa chỉ")
    phone_number = fields.Char(string="Số điện thoại")
    employee_id = fields.Many2one("employees_management.employees_management", string="Người thân của nhân viên")
    active = fields.Boolean(string="Active", default=True)