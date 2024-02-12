# -*- coding: utf-8 -*-
from odoo import api, fields, models

class Student(models.Model):
    _name = "school.student"
    name = fields.Char(string='name', required=True)
    birth_date = fields.Date(string='birth_date', required=True)
    age = fields.Integer(string='age', required=True)
    final_exam_grade = fields.Float(string='final_exam_grade', required=True)
    #subject_ids = fields.Char(string='name', required=True)
    