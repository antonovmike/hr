from odoo import models, fields


class Doctor(models.Model):
    _name = 'hr_hospital.doctor'
    _description = 'Doctor'

    name = fields.Char(string="Name")
    specialization = fields.Char(string="Specialization")
