# -*- coding: utf-8 -*-
from odoo import api, fields, models

class Teacher(models.Model):
    _name = 'school.teacher'
    name = fields.Char(string='name', required=True)
    profile = fields.Text(string='profile', required=True)
    #subject_ids = fields.Char(string='name', required=True) 