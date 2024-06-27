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
        'hr_hospital.doctor',
        required=True, 
        tracking=True)
    patient_id = fields.Many2one(
        'hr_hospital.patient', 
        required=True)
    disease_id = fields.Many2one(
        'hr_hospital.diseases', 
        required=True)
    treatment = fields.Char(required=True)
    mentor_doctor_id = fields.Many2one('hr_hospital.doctor')
    comment = fields.Text(string="Comment from mentor doctor")

    def name_get(self):
        """
        Returns a list of tuples containing the ID and name of each record in the current object.
        So that the View Visits table displays Disease name and Treatment instead of IDs.

        :return: A list of tuples where each tuple contains the ID and name of a record.
        :rtype: list[tuple[int, str]]
        """
        result = []
        for record in self:
            name = "%s (%s)" % (record.disease_id.name, record.treatment)
            result.append((record.id, name))
        return result

    @api.constrains('doctor_id', 'mentor_doctor_id', 'comment')
    def _check_fields(self):
        for record in self:
            if record.doctor_id.is_intern and not record.comment:
                raise ValidationError("Comment is required")
            if record.doctor_id.is_intern and not record.mentor_doctor_id:
                raise ValidationError("Mentor doctor is required")
