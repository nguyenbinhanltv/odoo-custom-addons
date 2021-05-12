{
    "name": "School Student",
    "version": "1.1",
    "author": "Nguyen Binh An",
    "summary": "School Student Management System",
    "sequence": 1,
    "description": "This is  school student management system software support in Odoo 14",
    "category": "School",
    "website": "http://localhost:8069/",
    "depends": ['base', 'school'],
    "data": [
        "security/ir.model.access.csv",
        "views/school_student_view.xml"
    ]
}