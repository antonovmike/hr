from odoo import api, models, fields
from odoo.exceptions import ValidationError


class Diagnosis(models.Model):
    _name = 'hr_hospital.diagnosis'
    _inherit = ['mail.thread']  # Tracks of doctor_id field changes
    _description = 'Diagnosis'

    date_of_diagnosis = fields.Datetime(
        string="Date of diagnosis", 
        required=True, 
        tracking=True)
    doctor_id = fields.Many2one(
        'hr_hospital.doctor', string="Doctor",
        required=True, tracking=True)
    patient_id = fields.Many2one(
        'hr_hospital.patient', string="Patient", required=True)
    disease_id = fields.Many2one(
        'hr_hospital.diseases', string="Disease", required=True)
    treatment = fields.Char(string="Treatment", required=True)
    mentor_doctor_id = fields.Many2one(
        'hr_hospital.doctor', string="Mentor Doctor")
    comment = fields.Text(string="Comment from mentor doctor")

    @api.constrains('doctor_id', 'mentor_doctor_id', 'comment')
    def _check_fields(self):
        for record in self:
            if record.doctor_id.is_intern and not record.comment:
                raise ValidationError("Comment is required")
            if record.doctor_id.is_intern and not record.mentor_doctor_id:
                raise ValidationError("Mentor doctor is required")
