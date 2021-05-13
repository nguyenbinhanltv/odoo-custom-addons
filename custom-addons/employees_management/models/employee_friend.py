# -*- coding: utf-8 -*-

from odoo import models, fields, api

class employee_friend(models.Model):
    _name = 'employees_management.employee_friend'
    _description = 'employees_management.employee_friend'

    name = fields.Char(string="Họ tên")
    friend_place_work = fields.Char(string="Phòng/Ban/Bộ phận/Nhà máy'")
    friend_relationship = fields.Char(string="Mối quan hệ")
    friend_company = fields.Char(string="Tên công ty")
    friend_company_address = fields.Char(string="Địa chỉ")
    friend_company_position = fields.Char(string="Chức vụ")
    friend_company_from_date = fields.Date(string="Từ ngày")
    friend_company_to_date = fields.Date(string="Đến ngày")
    currency_id = fields.Many2one("res.currency", string="Đơn vị tiền tệ")
    friend_salary = fields.Float(string="Mức lương")
    friend_reason_leave = fields.Text(string="Lý do nghỉ việc")
    active = fields.Boolean(string="Active", default=True)