from odoo import api, fields, models


class PersonalDoctorOverrideWizard(models.TransientModel):
    _name = 'personal_doctor_override_wizard'
    _description = 'Wizard to mass override personal Doctor in easy way'

    patient_ids = fields.Many2many(
        'hr_hospital.patient',
        'patient_patient_rel',
        'personal_doctor_wizard_id',
        'patient_id',
        string="Patients")
    doctor_id = fields.Many2one('hr_hospital.doctor', string="Doctor")

    @api.model
    def action_open_wizard(self):
        """ Open the wizard and return the created record"""
        return {
            'name': ('Override Personal Doctor'),
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'view_mode': 'form',
            'view_id': self.env['ir.ui.view'].search(
                [('name', '=', 'personal.doctor.override.wizard.form'), 
                ('model', '=', self._name)]).id,
            'view_type': 'form',
            'target': 'new',
        }

    def action_override(self):
        """Override the personal doctor for multiple patients"""
        for wizard in self:
            patient_ids = wizard.patient_ids.ids
            doctor_id = wizard.doctor_id.id
            self.env['hr_hospital.patient'].browse(patient_ids).write(
                {'personal_doctor_id': doctor_id})
