from odoo import api, models, fields


class AppointmentTransferWizard(models.TransientModel):
    _name = 'appointment_transfer_wizard'
    _description = 'Appointment Transfer'

    patient_id = fields.Many2one(
        'hr_hospital.patient', string="Patient", required=True)
    doctor_id = fields.Many2one(
        'hr_hospital.doctor', string="New Doctor", required=True)
    new_datetime = fields.Datetime(string="New date", required=True)

    @api.model
    def action_open_wizard(self, active_id=None):
        """Open the wizard and return the created record"""
        result = {
            'name': ('Appointment Transfer'),
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'view_mode': 'form',
            'view_id': self.env['ir.ui.view'].search(
                [('name', '=', 'appointment.transfer.wizard.form'), 
                ('model', '=', self._name)]).id,
            'view_type': 'form',
            'target': 'new',
        }

        return result

    def action_transfer(self):
        for wizard in self:
            patient_id = wizard.patient_id.id

            new_date = wizard.new_datetime
            new_doctor_id = wizard.doctor_id.id

            visits_obj = self.env['hr_hospital.visits'].search(
                [('patient_id', '=', patient_id)], limit=1)
            visits_obj.write({
                'date': new_date,
                'doctor_id': new_doctor_id,
            })
