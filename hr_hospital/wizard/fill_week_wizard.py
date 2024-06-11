import pytz
from datetime import datetime, timedelta

from odoo import api, models, fields


MONTH_SELECTION = [
        ('01', 'January'),
        ('02', 'February'),
        ('03', 'March'),
        ('04', 'April'),
        ('05', 'May'),
        ('06', 'June'),
        ('07', 'July'),
        ('08', 'August'),
        ('09', 'September'),
        ('10', 'October'),
        ('11', 'November'),
        ('12', 'December')
    ]

class FillWeekWizard(models.TransientModel):
    _name = 'fill_week_wizard'
    _description = 'Fill Week'

    doctor_id = fields.Many2one(
        'hr_hospital.doctor', string="Doctor", required=True)
    year = fields.Integer(string="Year", default=datetime.now().year)
    month = fields.Selection(MONTH_SELECTION, string='Month', default='06', required=True)
    weeks_odd_start_hour = fields.Integer(
        string="Weeks Odd Start Hour", default=8)
    weeks_odd_end_hour = fields.Integer(
        string="Weeks Odd End Hour", default=11)
    weeks_even_start_hour = fields.Integer(
        string="Weeks Even Start Hour", default=14)
    weeks_even_end_hour = fields.Integer(
        string="Weeks Even End Hour", default=18)

    @api.model
    def action_open_wizard(self, active_id=None):
        """Open the wizard and return the created record"""
        result = {
            'name': ('Fill Week'),
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'view_mode': 'form',
            'view_id': self.env['ir.ui.view'].search(
                [('name', '=', 'fill.week.wizard.form'), 
                ('model', '=', self._name)]).id,
            'view_type': 'form',
            'target': 'new',
        }

        return result

    def action_fill(self):
        """Fill in doctor schedule per week in one-hour increments"""
        self.ensure_one()

        doctor_id = self.doctor_id.id
        year = int(self.year)
        month = int(self.month)
        weeks_odd_start_hour = self.weeks_odd_start_hour
        weeks_odd_end_hour = self.weeks_odd_end_hour
        weeks_even_start_hour = self.weeks_even_start_hour
        weeks_even_end_hour = self.weeks_even_end_hour
        date = datetime(year, month, 1)

        while date.month == month:
            weekday = date.weekday()

            if weekday < 5:  # Monday to Friday
                week = date.isocalendar()[1]

                if week % 2 == 0:
                    start_hour = weeks_even_start_hour
                    end_hour = weeks_even_end_hour
                else:
                    start_hour = weeks_odd_start_hour
                    end_hour = weeks_odd_end_hour

                for hour in range(start_hour, end_hour):
                    date_str = f"{date.strftime('%Y-%m-%d')} {hour}:00:00"

                    def tz_datetime(date_str):
                        """Convert a date string in the format
                        "YYYY-MM-DD HH:MM:SS" to a datetime
                        object in UTC timezone."""
                        current_user = self.env.user
                        tz = pytz.timezone(current_user.tz or 'UTC')
                        return tz.localize(datetime.strptime(
                            date_str, "%Y-%m-%d %H:%M:%S")).astimezone(
                                pytz.utc).replace(tzinfo=None)

                    doctor_schedule_obj = self.env[
                        'hr_hospital.doctor_schedule']
                    doctor_schedule_obj.create({
                        'doctor_id': doctor_id,
                        'date_time': tz_datetime(date_str),
                    })

            date += timedelta(days=1)
