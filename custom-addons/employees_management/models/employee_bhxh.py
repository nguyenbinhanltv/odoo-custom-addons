# -*- coding: utf-8 -*-

from odoo import models, fields, api

class employee_bhxh(models.Model):
    _name = 'employees_management.employee_bhxh'
    _description = 'employees_management.employee_bhxh'

    name = fields.Char(string="Họ tên")
    bhxh_card_id = fields.Char(string="Mã số BHXH")
    bhxh_family_id = fields.Char(string="Mã số hộ gia đình")
    bhxh_price = fields.Float(string="Mức tiền đóng BHXH")
    bhxh_place_res = fields.Char(string="Nơi đăng ký khám bệnh, chữa bệnh ban đầu")
    active = fields.Boolean(string="Active", default=True)
    families_list = fields.One2many("employees_management.employee_bhxh_family", "bhxh_id", string="Thông tin gia đình")

