from odoo import models, fields


class Patient(models.Model):
    _name = 'hr_hospital.patient'
    _description = 'Patient'

    name = fields.Char(string="Name")
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender')
    passport_details = fields.Char(string="Passport Details")
    contact_person = fields.Char(string="Contact Person")
    personal_doctor = fields.Many2one('hr_hospital.doctor', string="Doctor")
