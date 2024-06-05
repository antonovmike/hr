from odoo import api, models, fields
from odoo.exceptions import ValidationError


class Visits(models.Model):
    _name = 'hr_hospital.visits'
    _description = 'Visits'

    name = fields.Char(string="Name")
    date = fields.Datetime(string="Date and Time")
    patient_id = fields.Many2one('hr_hospital.patient', string="Patient")
    doctor_id = fields.Many2one('hr_hospital.doctor', string="Doctor")
    diagnosis_ids = fields.Many2many(
        'hr_hospital.diagnosis', 'patient', string="Diagnosis")
    description = fields.Text(string='Description')
    appointment_is_done = fields.Boolean(string="Visit Taken", default=False)

    @api.onchange('date')
    def _check_date(self):
        for record in self:
            if record.date and record.date < fields.Datetime.now():
                raise ValidationError(
                    "The appointment date cannot be set to a past date.")

    def unlink(self):
        for visit in self:
            if visit.diagnosis_ids:
                raise ValidationError(
                    "You cannot delete a visit that contains diagnoses.")
        return super().unlink()

    def write(self, vals):
        for visit in self:
            if visit.diagnosis_ids:
                raise ValidationError(
                    "You can't change a visit that contains diagnoses.")
        return super().write(vals)
