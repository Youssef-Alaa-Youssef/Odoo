from odoo import models,fields,api,exceptions

class Inherited_CRM(models.Model):
    _inherit = 'res.partner'
    
    related_patient_id = fields.Many2one('hms.patient', string='Related Patient')

    @api.constrains('email')
    def _check_email(self):
        for lead in self:
            if lead.email:
                existing_patient = self.env['hms.patient'].search([('email', '=', lead.email)], limit=1)
                if existing_patient:
                    raise exceptions.ValidationError('Email address already exists in the patient model')
    def unlink(self):
        for partner in self:
            if partner.related_patient_id:
                raise exceptions.ValidationError('Cannot delete customer linked to a patient')
        return super().unlink()
    @api.constrains('vat')
    def _check_vat(self):
        for partner in self:
            if partner.customer and not partner.vat:
                raise exceptions.ValidationError("Tax ID is mandatory for customers.")