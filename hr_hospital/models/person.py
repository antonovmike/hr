from datetime import timedelta

from odoo import api, models, fields


class Person(models.Model):
    _name = 'hr_hospital.person'
    _description = 'Person'

    last_name = fields.Char(
        string="Last Name", 
        required=True)
    first_name = fields.Char(
        string="First Name", 
        required=True)
    date_of_birth = fields.Date(
        string="Date of Birth", 
        required=True)
    age = fields.Integer(
        compute='_compute_age', 
        store=True)
    gender = fields.Selection(
        default='other',
        selection=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], 
        required=True)
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    photo = fields.Image()

    @api.depends('date_of_birth')
    def _compute_age(self):
        today = fields.Date.today()
        for record in self:
            if record.date_of_birth:
                delta = (today - record.date_of_birth) // timedelta(days=365)
                record.age = int(delta)
            else:
                record.age = 0

    def name_get(self):
        result = []
        for record in self:
            name = "%s %s" % (record.last_name, record.first_name)
            result.append((record.id, name))
        return result
