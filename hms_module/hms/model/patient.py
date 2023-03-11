from odoo import models,fields



class Patient(models.Model):
    _name = 'hms.patient'

    first_name =fields.Char()
    last_name = fields.Char()
    birth_date = fields.Date()
    history=fields.Html()
    cr_ratio=fields.Float()
    blood_type=fields.Selection([
        ("A+","boold A+"),
        ("A","boold A"),
        ("o","boold O"),
        ("o+","boold O+"),
    ])
    pcr = fields.Boolean()
    Image = fields.Image()
    address = fields.Text()
    age = fields.Integer()



    