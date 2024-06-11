from datetime import datetime
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models


class DiseasesReportWizard(models.TransientModel):
    _name = 'diseases_report_wizard'
    _description = 'Diseases Report'

    month = fields.Integer(string="Month", default=5)
    year = fields.Integer(string="Year", default=2024)
    disease_id = fields.Many2one(
        'hr_hospital.diseases', string="Disease", default=1)
    diseases_num = fields.Integer(string="Diseases Num")

    @api.model
    def action_open_wizard(self, active_id=None):
        """Open the wizard and return the created record"""
        result = {
            'name': ('Diseases Report'),
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'view_mode': 'form',
            'view_id': self.env['ir.ui.view'].search(
                [('name', '=', 'diseases.report.form'), 
                ('model', '=', self._name)]).id,
            'view_type': 'form',
            'target': 'new',
        }

        return result

    def action_generate(self):
        """Generate a report of diseases for a month"""
        # calculate first and last day of the month
        first_day_of_month = datetime(self.year, self.month, 1)
        month = relativedelta(months=1)
        days = relativedelta(days=1)
        last_day_of_month = first_day_of_month + month - days

        # Get the records of diagnosis with the disease_id and date of
        # diagnosis between first_day_of_month and last_day_of_month
        diagnoses = self.env['hr_hospital.diagnosis'].search([
            ('disease_id', '=', self.disease_id.id),
            ('date_of_diagnosis', '>=', first_day_of_month),
            ('date_of_diagnosis', '<=', last_day_of_month),
        ])

        self.diseases_num = len(diagnoses)

        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'res_model': 'diseases_report_wizard',
            'views': [(False, 'form')],
            'target': 'new',
            'res_id': self.id,
        }
