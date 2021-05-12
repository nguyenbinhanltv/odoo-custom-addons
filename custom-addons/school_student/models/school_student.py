import datetime

from odoo import fields, models, api, _
from odoo.exceptions import UserError

class school_student(models.Model):
    _name = "school.student"
    _description = "school_student.school_student"

    name = fields.Char(string="Student name")
    school_id = fields.Many2one("school.profile", string="School", options="{'no_create_edit': True, 'no_create': True}")
    hobby_list = fields.Many2many("hobby", "school_hobby_rel", "student_id", "hobby_id", string="Hobbies")
    is_virtual_school = fields.Boolean(related="school_id.is_virtual_class", string="Is virtual class")
    school_address = fields.Text(related="school_id.address", string="School address")

    currency_id = fields.Many2one("res.currency", string="Currency")
    student_fees = fields.Monetary(string="Student fees", copy=False)
    total_fees = fields.Float(string="Total fees", copy=False)
    active = fields.Boolean(string="Active", default=True)
    bdate = fields.Date(string="Date Of Birth")
    student_age = fields.Char(string="Total Age", compute="_get_age_from_student")

    ref_id = fields.Reference([
        ("school.profile", "School"),
        ("account.move", "Invoice")
    ], string="Ref", default="school.profile,1")

    @api.depends("bdate")
    def _get_age_from_student(self):
        today_date = datetime.date.today()
        for stud in self:
            if stud.bdate:
                currentDate = datetime.date.today()

                deadlineDate = fields.Datetime.to_datetime(stud.bdate).date()
                print(deadlineDate)
                daysLeft = currentDate - deadlineDate
                print(daysLeft)

                years = ((daysLeft.total_seconds()) / (365.242 * 24 * 3600))
                yearsInt = int(years)

                months = (years - yearsInt) * 12
                monthsInt = int(months)

                days = (months - monthsInt) * (365.242 / 12)
                daysInt = int(days)

                hours = (days - daysInt) * 24
                hoursInt = int(hours)

                minutes = (hours - hoursInt) * 60
                minutesInt = int(minutes)

                seconds = (minutes - minutesInt) * 60
                secondsInt = int(seconds)

                stud.student_age = 'You are {0:d} years, {1:d}  months, {2:d}  days, {3:d}  hours, {4:d} \
                                 minutes, {5:d} seconds old.'.format(yearsInt, monthsInt, daysInt, hoursInt, minutesInt,
                                                                     secondsInt)
            else:
                stud.student_age = "Not providated..."

    def write(self, vals):
        rtn = super(school_student, self).write(vals)
        if not self.hobby_list:
            raise UserError(_("Plese chose least one hobby!"))
        return rtn

    def copy(self, default={}):
        default["name"] = "copy ("+self.name+")"
        rtn = super(school_student, self).copy(default)
        return rtn

    def unlink(self):
        rtn = super(school_student, self).unlink()
        if self.active:
            UserError(_("Can't unlink student was active"))
        else:
            return rtn

    @api.model_create_multi
    def create(self, vals_list):
        rtn = super(school_student, self).create(vals_list)
        for st in rtn:
            if st.active == False:
                raise UserError(_("Active was False"))
        return rtn

class SchoolProfile(models.Model):
    _inherit = "school.profile"

    school_list = fields.One2many("school.student", "school_id", string="Students")

    @api.model
    def create(self, vals):
        rtn = super(SchoolProfile, self).create(vals)
        if not rtn.school_list:
            raise UserError(_("Student list is empty!"))
        return rtn

class Hobbies(models.Model):
    _name = "hobby"

    name = fields.Char(string="Hobby")