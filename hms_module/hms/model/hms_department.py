from odoo import models, fields

class Department(models.Model):
    _name = 'hms.department'
    
    name = fields.Char(string="Name", required=True)
    capacity = fields.Integer(string="Capacity", required=True)
    is_opened = fields.Boolean(string="Is Opened", default=True)
    patients = fields.Many2many('hms.patient', string='Patients')