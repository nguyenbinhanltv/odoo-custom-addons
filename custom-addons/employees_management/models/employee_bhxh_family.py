# -*- coding: utf-8 -*-

from odoo import models, fields, api

class employee_bhxh_family(models.Model):
    _name = "employees_management.employee_bhxh_family"
    _description = 'employees_management.employee_bhxh_family'

    name = fields.Char(string="Họ và tên")
    bdate = fields.Date(string="Ngày tháng năm sinh")
    relationship = fields.Selection([
        ('father', 'Cha'),
        ('mother', 'Mẹ'),
        ('brother', 'Anh (em) trai'),
        ('sister', 'Anh (em) gái'),
        ('other', 'Khác'),
    ], string="Mối quan hệ")
    gender = fields.Selection([
        ('male', 'Nam'),
        ('female', 'Nữ'),
        ('other', 'Khác'),
    ], string="Giới tính")

    phone_number = fields.Char(string="Số điện thoại")
    address = fields.Char(string="Địa chỉ")
    current_address = fields.Text(string="Nơi ở hiện tại")

    name_head = fields.Char(string="Họ và tên chủ hộ")
    reg_book_id = fields.Char(string="Số sổ hộ khẩu")
    bhxh_book_id = fields.Char(string="Mã số sổ BHXH")
    place_bdate_cert = fields.Char(string="Nơi cấp giấy khai sinh")
    card_id = fields.Char(string="Số CMND", size=12)
    note = fields.Text(string="Ghi chú")
    bhxh_id = fields.Many2one("employees_management.employee_bhxh", string="Thành viên hộ gia đình")
