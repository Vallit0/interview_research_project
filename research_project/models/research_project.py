from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ResearchProject(models.Model):
    _name = 'research.project'
    _description = 'Research Project'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Project Name', required=True, tracking=True)
    code = fields.Char(string='Project Code', readonly=True, default='New')
    description = fields.Text(string='Description')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    budget = fields.Float(string='Budget')
    state = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('review', 'In Review'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], default='new', tracking=True)
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Medium'),
        ('2', 'High')
    ], default='1')
    investigator_ids = fields.Many2many('res.partner', string='Investigators')
    leader_id = fields.Many2one('res.partner', string='Project Leader')

    duration_days = fields.Integer(string='Duration (days)', compute='_compute_duration')

    @api.depends('start_date', 'end_date')
    def _compute_duration(self):
        for record in self:
            if record.start_date and record.end_date:
                record.duration_days = (record.end_date - record.start_date).days
            else:
                record.duration_days = 0

    @api.model
    def create(self, vals):
        if vals.get('code', 'New') == 'New':
            vals['code'] = self.env['ir.sequence'].next_by_code('research.project') or 'New'
        return super().create(vals)

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for record in self:
            if record.start_date and record.end_date and record.start_date > record.end_date:
                raise ValidationError('The start date cannot be after the end date.')

    @api.onchange('budget')
    def _onchange_budget(self):
        if self.budget and self.budget < 0:
            raise ValidationError('Budget must be positive.')

    def action_in_progress(self):
        self.state = 'in_progress'

    def action_review(self):
        self.state = 'review'

    def action_completed(self):
        self.state = 'completed'

    def action_cancelled(self):
        self.state = 'cancelled'
