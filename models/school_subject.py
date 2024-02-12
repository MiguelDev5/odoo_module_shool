# -*- coding: utf-8 -*-
from odoo import api, fields, models

class Subject(models.Model):
    _name = 'school.subject'
    name = fields.Char(string='name', required=True)
    credits = fields.Integer(string='credits', required=True)
    max_students = fields.Integer(string='max_students', required=True)
    active = fields.Boolean(string='active', required=True)
    #student_ids = fields.Char(string=name, required=True)
    #teacher_id = fields.Char(string=name, required=True)