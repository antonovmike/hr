from odoo import models, fields


class Patient(models.Model):
    _name = 'hr_hospital.patient'
    _description = 'Patient'

    person_id = fields.Many2one(
        'hr_hospital.person', 
        required=True, 
        string="Person")
    name = fields.Char(string="Name", related='person_id.last_name')
    age = fields.Integer(string='Age', related='person_id.age')
    gender = fields.Selection(string='Gender', related='person_id.gender')
    passport_details = fields.Char(string="Passport Details")
    contact_person = fields.Char(string="Contact Person")
    personal_doctor_id = fields.Many2one(
        'hr_hospital.doctor', string="Personal Doctor")

    doctor_id = fields.Many2one('hr_hospital.doctor', string="Doctor")
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
