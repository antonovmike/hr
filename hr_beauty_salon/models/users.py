from odoo import models, fields


class User(models.Model):
    _name = 'hr_beauty_salon.user'
    _description = 'User'

    name = fields.Char(string="Name", required=True, default="Jane Doe")
    # pass
