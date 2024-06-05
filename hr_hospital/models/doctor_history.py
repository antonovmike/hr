from odoo import models, fields


class DoctorHistory(models.Model):
    """
    This class is used to keep track of the history of each patient's personal
    doctor. When a patient's personal doctor is set or changed, a new record
    is created automatically in this class.

    :param appointment_date: A datetime field to store the date of appointment.
    :type appointment_date: datetime
    :param patient_id: A many2one field to store the reference to the patient.
    :type patient_id: models.Model
    :param doctor_id: A many2one field to store the reference to the doctor.
    :type doctor_id: models.Model
    """
    _name = 'hr_hospital.doctor_history'
    _description = 'Doctor History'

    appointment_date = fields.Datetime(string='Appointment Date')
    patient_id = fields.Many2one('hr_hospital.patient', string="Patient")
    doctor_id = fields.Many2one('hr_hospital.doctor', string="Doctor")
