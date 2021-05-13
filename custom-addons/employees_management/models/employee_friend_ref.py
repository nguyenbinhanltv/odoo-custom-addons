# -*- coding: utf-8 -*-

from odoo import models, fields, api

class employee_friend_ref(models.Model):
    _name = 'employees_management.employee_friend_ref'
    _description = 'employees_management.employee_friend_ref'

    name = fields.Char(string="Họ tên")
    ref_position = fields.Char(string="Chức vụ")
    ref_relationship = fields.Char(string="Mối quan hệ")
    ref_company = fields.Char(string="Tên công ty")
    ref_company_address = fields.Char(string="Địa chỉ")
    ref_phone_number = fields.Char(string="Số điện thoại")
    ref_time_rel = fields.Char(string="Thời gian quen")
    active = fields.Boolean(string="Active", default=True)