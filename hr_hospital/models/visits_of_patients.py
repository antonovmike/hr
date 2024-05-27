from odoo import models, fields


class Visits(models.Model):
    _name = 'hr_hospital.visits'
    _description = 'Visits'

    name = fields.Char(string="Name")
    date = fields.Date(string="Date")
    patient = fields.Many2one('hr_hospital.patient', string="Patient")
    doctor = fields.Many2one('hr_hospital.doctor', string="Doctor")
    disease = fields.Many2one('hr_hospital.diseases', string="Disease")
