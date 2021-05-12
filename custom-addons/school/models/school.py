from odoo import fields, models, api

class SchoolProfile(models.Model):
    _name = "school.profile"

    name = fields.Char(string="School Name")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    is_virtual_class = fields.Boolean(string="Virtual Class Support ?")
    school_rank = fields.Integer(string="Rank")
    result = fields.Float(string="Result")
    address = fields.Text(string="Address")
    estalist_date = fields.Date(string="Estalist Date")
    open_date = fields.Datetime("Open Date")
    school_type = fields.Selection([
        ('private', 'Private School'),
        ('public', 'Public School')
    ], string="Type of School")
    documents = fields.Binary(string="Documents")
    documents_name = fields.Char(string="File name")
    school_image = fields.Image(string="Upload School Image", max_width=100, max_height=100)
    school_description = fields.Html(string="Description")
    auto_rank = fields.Integer(compute="_auto_rank_populate", string="Auto rank", store=True)

    @api.depends("school_type")
    def _auto_rank_populate(self):
        for rec in self:
            if rec.school_type == "private":
                rec.auto_rank = 50
            elif rec.school_type == "public":
                rec.auto_rank = 100
            else:
                rec.auto_rank = 0