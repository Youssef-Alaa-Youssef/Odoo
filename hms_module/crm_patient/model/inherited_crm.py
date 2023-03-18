from odoo import models,fields

class Inherited_CRM(models.Model):
    _inherit = 'res.partner'
    
    related_patient_id = fields.Many2one('hms.patient', string='Related Patient')
