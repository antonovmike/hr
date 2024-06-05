from odoo import api, fields, models
from odoo.exceptions import ValidationError


class DoctorSchedule(models.Model):
    _name = 'hr_hospital.doctor_schedule'
    _description = 'Doctor Schedule'

    doctor_id = fields.Many2one('hr_hospital.doctor', string="Doctor")
    date_time = fields.Datetime(string="Date of reception")

    @api.constrains('doctor_id', 'date_time')
    def get_two_date_comp(self):
        existing_appointment = self.env['hr_hospital.doctor_schedule'].search([
            ('doctor_id', '=', self.doctor_id.id),
            # Format without seconds
            ('date_time', '=', self.date_time.strftime('%Y-%m-%d %H:%M')),
            # Exclude the current record
            ('id', '!=', self.id)
        ], limit=1)

        if existing_appointment:
            raise ValidationError('The appointment hours already exist.')
