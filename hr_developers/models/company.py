from odoo import models, fields


class Company(models.Model):
    _name = "hr_developers.company"
    _description = "Company"
    _inherits = {'res.company': 'name'}

    name = fields.Many2one(
        'res.company', 
        ondelete='cascade', 
        required=True)

    # Fields name, street, city, state_id, zip and country_id
    # are available because they are present in the parent model

    employee_ids = fields.One2many(
        'hr_developers.developers', 
        'company_id', 
        string='Employees')
