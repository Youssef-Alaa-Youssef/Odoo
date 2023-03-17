from odoo import models,fields



class Patient(models.Model):
    _name = 'hms.patient'
    _rec_name ='first_name'

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
    department_ids = fields.Many2one('hms.department', string='Departments')
    doctor_ids = fields.Many2many('hms.doctor', string='Doctors')
    state = fields.Selection([
        ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious')
    ], string='State')



    