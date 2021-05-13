# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class employees_management(models.Model):
    _name = 'employees_management.employees_management'
    _description = 'employees_management.employees_management'

    # Thông tin cá nhân
    name = fields.Char(string="Họ tên")
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

    # Thông tin địa chỉ liên lạc
    employee_landline_phone_number = fields.Char(string="Điện thoại nhà", help="Không bắt buộc")
    employee_phone_number = fields.Char(string="Di động")
    employee_email = fields.Char(string="Email", help="Không bắt buộc")
    employee_permanent_residence = fields.Text(string="Hộ khẩu thường trú")
    employee_address = fields.Text(string="Địa chỉ liên hệ")

    active = fields.Boolean(string="Active", default=True)
    emmployee_image = fields.Image(string="")
    employee_work_email = fields.Char(string="Email công ty")
    employee_work_phone = fields.Char(string="Điện thoại công ty")

    # Thông tin nhân viên
    employee_id = fields.Char(string="Mã nhân viên", help="Định dạng XXxxx, XX: Năm vào làm việc, xxx: số thứ tự tăng dần bắt đầu bằng 001 và sẽ reset theo năm tài chính")
    employee_workplace = fields.Char(string="Vị trí công tác")
    employee_office = fields.Char(string="Phòng ban công tác")
    employee_work_date = fields.Date(string="Ngày vào làm")
    employee_contract_type = fields.Char(string="Loại hợp đồng")
    employee_from_date = fields.Date(string="Từ ngày")
    employee_to_date = fields.Date(string="Đến ngày")

    employee_families = fields.One2many("employees_management.employee_family", "employee_id", string="Thông tin gia đình")

    # Thông tin quá trình học tập
    employee_standard_level = fields.Selection([
        ('intermediate', 'Trung cấp'),
        ('college', 'Cao đẳng'),
        ('university', 'Đại học'),
        ('other', 'Khác')
    ], string="Trình độ")
    employee_university_name = fields.Char(string="Tên trường đại học")
    employee_industry_change = fields.Char(string="Chuyển ngành")
    employee_edu_from_date = fields.Date(string="Từ ngày")
    employee_edu_to_date = fields.Date(string="Tới ngày")

    # Ngoại ngữ
    employee_language_list = fields.Many2many("employees_management.employee_language",
                                              "employee_language_rel", "employee_id",
                                              "language_id", string="Tên ngôn ngữ")
    employee_language_speak = fields.Selection([
        ('low', 'Yếu'),
        ('mid', 'Khá'),
        ('good', 'Tốt')
    ], string="Nói")
    employee_language_write = fields.Selection([
        ('low', 'Yếu'),
        ('mid', 'Khá'),
        ('good', 'Tốt')
    ], string="Viết")
    employee_language_listen = fields.Selection([
        ('low', 'Yếu'),
        ('mid', 'Khá'),
        ('good', 'Tốt')
    ], string="Nghe")

    employee_software_skills = fields.Many2many("employees_management.employee_software",
                                                "employee_software_rel", "employee_id",
                                                "software_id", string="Phần mềm")
    employee_special_skills = fields.Text(string="Kỹ năng đặc biệt")

    # Họ hàng or bạn bè
    employee_friend_id = fields.Reference([
        ('employees_management.employee_friend', 'Bạn bè (họ hàng)')
    ], string="Bạn bè (họ hàng)")

    # Người tham khảo
    employee_friend_ref_id = fields.Reference([
        ('employees_management.employee_friend_ref', 'Người tham khảo')
    ], string="Người tham khảo")

    # Làm sao biết công việc này
    employee_list_reason = fields.Selection([
        ('fb', 'Facebook'),
        ('friends', 'Bạn bè người thân'),
        ('emp', 'Nhân viên giới thiệu'),
        ('web', 'Trang việc làm'),
        ('other', 'Khác')
    ], string="Từ")
    employee_salary_min = fields.Char(string="Mức lương tối thiểu")
    employee_salary_want = fields.Char(string="Mức lương mong muốn")
    employee_can_work = fields.Date(string="Ngày có thể đi làm")

    # Bổ sung
    employee_health = fields.Text(string="Tình trạng sức khỏe")
    employee_blood = fields.Char(string="Nhóm máu")

    @api.constrains('employee_landline_phone_number',
                    'employee_card_id',
                    'employee_phone_number',
                    'employee_work_phone',
                    'employee_weight',
                    'employee_height')
    def _check_is_number(self):
        for record in self:
            if float(record.employee_landline_phone_number) and float(record.employee_card_id) and float(record.employee_phone_number) and float(record.employee_work_phone) and float(record.employee_weight) and float(record.employee_height):
                return True
            else:
                raise ValidationError("Các trường nhập số sai định dạng")





