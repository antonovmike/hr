from odoo import models, fields


class Doctor(models.Model):
    _name = 'hr_hospital.doctor'
    _description = 'Doctor'

    name = fields.Char(string="Name")
    specialization = fields.Selection(
        default='internist',
        selection=[('internist', ('Internist')),
                   ('oculist', ('Oculist')),
                   ('surgeon', ('Surgeon'))],
    )
    is_intern = fields.Boolean(string="Intern")
    mentor_doctor_id = fields.Many2one(
        'hr_hospital.doctor',
        string="Doctor-Mentor",
        domain=[('is_intern', '=', False)]
        )
