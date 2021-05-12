# -*- coding: utf-8 -*-

from odoo import models, fields, api


class employees_management(models.Model):
    _name = 'employees_management.employees_management'
    _description = 'employees_management.employees_management'

    employee_full_name = fields.Text(string="Họ tên", required=True)
    employee_bdate = fields.Datetime(string="Ngày sinh", required=True)
    employee_gender = fields.Selection([
        ('male', 'Nam'),
        ('female', 'Nữ'),
    ], required=True)
    employee_birthplace = fields.Text(string="Nơi sinh")

    employee_card_id = fields.Text(string="Số CMND")
    employee_card_place = fields.Text(string="Nơi cấp")
    employee_card_date = fields.Date(string="Ngày cấp")

    employee_standard = fields.Text(string="Trình độ")
    employee_ethnic_group = fields.Text(string="Dân tộc")
    employee_relegion = fields.Text(string="Tôn giáo")

    employee_weight = fields.Text(string="Cân nặng")
    employee_height = fields.Text(string="Chiều cao")
    employee_native_place = fields.Text(string="Nguyên quán")
    employee_nationality = fields.Text(string="Quốc tịch")
    employee_marital_status = fields.Text(string="Tình trạng hôn nhân")

    employee_landline_phone_number = fields.Text(string="Điện thoại nhà (không bắt buộc)")
    employee_phone_number = fields.Text(string="Di động")
    employee_email = fields.Text(string="Email (không bắt buộc)")
    employee_permanent_residence = fields.Text(string="Hộ khẩu thường trú")
    employee_address = fields.Text(string="Địa chỉ liên hệ")

    active = fields.Boolean(string="Active")

