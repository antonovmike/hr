from odoo import models, fields, api


class Diseases(models.Model):
    _name = 'hr_hospital.diseases'
    _description = 'Diseases'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
