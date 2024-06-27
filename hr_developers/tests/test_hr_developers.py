from odoo import fields
from odoo.tests.common import TransactionCase


# odoo/odoo-bin -c conf/odoo.test.conf -d odoo16-odoo-test --test-enable --log-level=test --test-tags hr_developers


class TestDevelopers(TransactionCase):
    
    def setUp(self):
        super(TestDevelopers, self).setUp()
        self.company = self.env['res.company'].create({
            'name': 'Test Company'
        })

    def test_create_company(self):
        company = self.env['hr_developers.company'].create({
            'name': self.company.id,
        })
        self.assertEqual(company.name.id, self.company.id)
        self.assertEqual(company.street, self.company.street)
        self.assertEqual(company.city, self.company.city)
        self.assertEqual(company.state_id.id, self.company.state_id.id)
        self.assertEqual(company.zip, self.company.zip)
        self.assertEqual(company.country_id.id, self.company.country_id.id)

    def test_create_developer(self):
        company = self.env['hr_developers.company'].create({
            'name': self.company.id,
        })
        developer = self.env['hr_developers.developers'].create({
            'name': 'Test Developer',
            'type': 'front-end',
            'mail': 'test@example.com',
            'address': 'Test Address',
            'birth_date': '1990-01-01',
            'company_id': company.id,
        })

        self.assertEqual(developer.name, 'Test Developer')
        self.assertEqual(developer.type, 'front-end')
        self.assertEqual(developer.global_identification, 'Test Developer-front-end')
        self.assertEqual(developer.mail, 'test@example.com')
        self.assertEqual(developer.address, 'Test Address')
        self.assertEqual(developer.birth_date, fields.Date.from_string('1990-01-01'))
        self.assertEqual(developer.company_id.id, company.id)
