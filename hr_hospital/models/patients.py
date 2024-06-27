from odoo import models, fields


class Patient(models.Model):
    _name = 'hr_hospital.patient'
    _description = 'Patient'

    person_id = fields.Many2one(
        'hr_hospital.person', 
        required=True, 
        string="Patient")
    name = fields.Char(related='person_id.last_name')
    age = fields.Integer(related='person_id.age')
    gender = fields.Selection(related='person_id.gender')
    passport_details = fields.Char()
    contact_person = fields.Char()
    personal_doctor_id = fields.Many2one('hr_hospital.doctor')

    doctor_id = fields.Many2one('hr_hospital.doctor')
    date_time = fields.Datetime(string="Date and Time")

    _sql_constraints = [
        ('person_id_uniq', 'unique (person_id)', 'Person ID must be unique'),
    ]

    def write(self, vals):
        result = super(Patient, self).write(vals)
        if 'personal_doctor_id' in vals:
            for patient in self:
                if patient.personal_doctor_id:
                    self.env['hr_hospital.doctor_history'].create({
                        'patient_id': patient.id,
                        'doctor_id': patient.personal_doctor_id.id,
                        'appointment_date': fields.Date.today(),
                    })
        return result
