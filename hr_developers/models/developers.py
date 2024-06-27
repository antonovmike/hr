from odoo import api, models, fields


class Developers(models.Model):
    _name = 'hr_developers.developers'
    _inherit = ['mail.thread']  # Tracks fields changes
    _description = 'Developers'

    name = fields.Char(
        string="Name", 
        required=True,
        tracking=True)
    type = fields.Selection(
        string="Type",
        required=True,
        selection=[('front-end', 'Front-End'),
                   ('backend', 'Backend'),
                   ('fullstack', 'Fullstack'),
                   ('out-stuff', 'Out-Stuff')],
        tracking=True
    )
    global_identification = fields.Char(
        compute="_compute_global_identification")
    phone = fields.Char(
        string="Phone", 
        tracking=True
    )
    mail = fields.Char(
        string="Mail", 
        required=True, 
        tracking=True
    )
    address = fields.Char(
        string="Address", 
        required=True, 
    )
    birth_date = fields.Date(
        string="Birth Date", 
        required=True,
    )
    company_id = fields.Many2one(
        'hr_developers.company', 
        string='Company')
    position = fields.Char()

    @api.depends('name', 'type')
    def _compute_global_identification(self):
        """Compute global identification field based on developer name and type."""
        for record in self:
            record.global_identification = f"{record.name}-{record.type}"
