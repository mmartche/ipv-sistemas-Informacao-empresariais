# models/teste_modelo.py
from odoo import fields, models
class TesteModelo(models.Model):
    _name = "teste.modelo"
    _description = "Teste de modelo"
    name = fields.Char("Nome", required=True)