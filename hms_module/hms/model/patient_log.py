from odoo import models, fields

class PatientLog(models.Model):
    _name = 'hms.patient.log'
    _description = 'Patient Log History'

    patient_id = fields.Many2one('hms.patient')
    description_log = fields.Text(string='Log Description', required=True)
