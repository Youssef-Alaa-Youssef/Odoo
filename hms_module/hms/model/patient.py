from odoo import models,fields,api,exceptions,tools
from datetime import datetime

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
    # log_ids = fields.One2many('hms.patient.log','patient_id', string='Log History')
    email = fields.Char(string='Email', required=True)
    _sql_constraints = [
        ('email_unique', 'UNIQUE(email)', 'The email address must be unique.'),
    ]
    @api.onchange('birth_date')
    def _compute_age(self):
        if self.birth_date:
            self.age = datetime.now() - self.birth_date
        else:
            self.age = 0
    @api.onchange('age')
    def age_based_birth(self):
        if self.age and self.age < 30:
            self.pcr = True
            warning_msg = 'PCR has been checked for patient under 30 years old.'
            return {'warning': {'title': 'Warning', 'message': warning_msg}}
    @api.onchange('state')
    def onchange_state(self):
        if self.state:
            log_description = f"State changed to {self.state}"
            log = self.env['hms.patient.log'].create({
                'patient_id': self.id,
                'created_by': self.env.user.name,
                'description': log_description
            })
            self.log_ids += log       
    @api.constrains('email')
    def _check_email(self):
        if self.email and not tools.email_re.match(self.email):
            raise exceptions.ValidationError("Invalid email address")
