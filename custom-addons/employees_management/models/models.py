# -*- coding: utf-8 -*-

from odoo import models, fields, api


class employees_management(models.Model):
    _name = 'employees_management.employees_management'
    _description = 'employees_management.employees_management'

    # Thông tin cá nhân
    employee_full_name = fields.Char(string="Họ tên")
    employee_bdate = fields.Datetime(string="Ngày sinh")
    employee_gender = fields.Selection([
        ('male', 'Nam'),
        ('female', 'Nữ'),
        ('other', 'Khác'),
    ], string="Giới tính")
    employee_birthplace = fields.Char(string="Nơi sinh")
    employee_card_id = fields.Char(string="Số CMND", size=12)
    employee_card_place = fields.Text(string="Nơi cấp")
    employee_card_date = fields.Date(string="Ngày cấp")
    employee_standard = fields.Char(string="Trình độ")
    employee_ethnic_group = fields.Char(string="Dân tộc")
    employee_relegion = fields.Char(string="Tôn giáo")
    employee_weight = fields.Float(string="Cân nặng (kg)")
    employee_height = fields.Float(string="Chiều cao (m)")
    employee_native_place = fields.Char(string="Nguyên quán")
    employee_nationality = fields.Char(string="Quốc tịch")
    employee_marital_status = fields.Selection([
        ('single', 'Độc thân'),
        ('married', 'Đã kết hôn'),
        ('legal_cohabitant', 'Sống chung hợp pháp'),
        ('widower', 'Góa phụ'),
        ('divorced', 'Ly hôn')
    ], string="Tình trạng hôn nhân")

    employee_landline_phone_number = fields.Char(string="Điện thoại nhà (không bắt buộc)")
    employee_phone_number = fields.Char(string="Di động")
    employee_email = fields.Char(string="Email (không bắt buộc)")
    employee_permanent_residence = fields.Text(string="Hộ khẩu thường trú")
    employee_address = fields.Text(string="Địa chỉ liên hệ")

    active = fields.Boolean(string="Active")
    emmployee_image = fields.Image(max_width=100, max_height=100)

