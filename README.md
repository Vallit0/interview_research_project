# Desarrollo de Módulos de Investigación 🚀
## Documentación de Usuario (Demo) 🖱️

#### Ingreso de Módulo en Búsqueda 
![image](https://github.com/user-attachments/assets/2820945b-7dc7-468c-9144-1768efac6188)

### Inicialización de Módulo
![image](https://github.com/user-attachments/assets/5b4ba6bf-44b4-4bae-a7e6-472abfed24e9)

### Ingreso de Proyecto de Investigacion con Campos Solicitados
![image](https://github.com/user-attachments/assets/f6b73671-36cb-41e6-98bd-e3a9f37d63c0)

Dentro de la presente vista, es notorio que se pueden agregar los siguientes campos: 
- Modelo principal: research.project con los siguientes campos:
- name: Char (obligatorio) - Nombre del proyecto
- code: Char - Código único del proyecto (formato: PR000X)
- description: Text - Descripción detallada del proyecto
- start_date: Date - Fecha de inicio
- end_date: Date - Fecha estimada de finalización
- budget: Float - Presupuesto asignado
- state: Selection - Estados del proyecto (nuevo, en progreso, en revisión, completado, cancelado)
- priority: Selection/Integer - Prioridad del proyecto
- investigator_ids: Many2many - Relación con investigadores (res.partner)
- leader_id: Many2one - Investigador principal (res.partner)
- Al menos un campo computado de su elección

##### Ingreso de Fecha Establecida
![image](https://github.com/user-attachments/assets/a1d2b032-57c8-4b67-95c5-2c16ee423b0c)

##### Campos ManyToOne
![image](https://github.com/user-attachments/assets/a15891ff-1c50-4065-ad4e-1d263fc929f6)

#### Droplist y módulos bajo data demo de Odoo
![image](https://github.com/user-attachments/assets/0f3694c6-3f23-4fad-9386-5204168294d8)

#### Dinamismo de Formularios
![image](https://github.com/user-attachments/assets/a4517e6c-e8f5-4375-83bd-d88ee92c38dd)

#### Vista de Verificación
![image](https://github.com/user-attachments/assets/8df8df06-77b7-4575-9c8e-370dbff8446d)

#### Vista de Árbol de Proyectos 
![image](https://github.com/user-attachments/assets/58379535-bbea-421b-a618-14f538ed1182)

## Documentacion Técnica 
Previo a la integración de módulos de Odoo, es necesario instalar las dependencias. En este caso, se instalará Odoo 18 en Ubuntu.
```bash
git clone https://www.github.com/odoo/odoo --branch 18.0 --single-branch .
```

![image](https://github.com/user-attachments/assets/b33f75bc-9e0e-4bef-b549-d0e70506b26b)

![image](https://github.com/user-attachments/assets/5a69a118-37b6-4f08-a849-e4a8104e943f)

Es necesario agregar a Odoo.conf los módulos que se activarán.
![image](https://github.com/user-attachments/assets/de558bcf-2b23-43c8-bf92-3b217af0d5e2)

Además de activar el modo "Developer"
![image](https://github.com/user-attachments/assets/35395abb-3258-4d93-a03f-e28db35fb1fc)

### Organización de Módulos
```bash
custom_addons
└── research_project
    ├── data
    │   └── project_sequence.xml
    ├── __init__.py
    ├── __manifest__.py
    ├── models
    │   ├── __init__.py
    │   └── research_project.py
    ├── __pycache__
    │   └── __init__.cpython-310.pyc
    ├── README.md
    ├── report
    │   ├── research_project_report.xml
    │   └── research_project_templates.xml
    ├── security
    │   ├── ir.model.access.csv
    │   └── security.xml
    └── views
        └── research_project_views.xml

7 directories, 12 files
```

#### init.py
En primera instancia, se le debe indicar al módulo que este pueda ser importado por python en '__init__.py' 
```python
from . import models
```

#### models/research_project.py

Validaciones de Error
```python
from odoo import models, fields, api
from odoo.exceptions import ValidationError
```

### Modelo Principal 
```python
class ResearchProject(models.Model):
    _name = 'research.project'
    _description = 'Research Project'
    _inherit = ['mail.thread', 'mail.activity.mixin']
```
#### Descripcion
Define el modelo research.project para gestionar proyectos de investigación.
Se heredan funcionalidades de mail.thread (seguimiento de cambios) y mail.activity.mixin (actividades).

### Definición de Campos
```python
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
```
#### Descripcion
Define todos los campos requeridos por el ejercicio, incluyendo:
1. Campos básicos (Char, Text, Date, Float).
2. Relaciones (Many2many, Many2one).
3. Campo computado duration_days.
   
### Método Computado Solicitado 
```python
@api.depends('start_date', 'end_date')
def _compute_duration(self):
    for record in self:
        if record.start_date and record.end_date:
            record.duration_days = (record.end_date - record.start_date).days
        else:
            record.duration_days = 0
```
#### Descripcion
Calcula automáticamente el número de días entre la fecha de inicio y la fecha de finalización.
### Sobreescritura del Método 
```python
@api.model
def create(self, vals):
    if vals.get('code', 'New') == 'New':
        vals['code'] = self.env['ir.sequence'].next_by_code('research.project') or 'New'
    return super().create(vals)
```
#### Descripcion
Genera automáticamente un código único para el proyecto al momento de su creación, utilizando una secuencia.

### Constrains de Fechas 
```python
@api.constrains('start_date', 'end_date')
def _check_dates(self):
    for record in self:
        if record.start_date and record.end_date and record.start_date > record.end_date:
            raise ValidationError('The start date cannot be after the end date.')
```
#### Descripcion
Evita que la fecha de inicio sea posterior a la fecha de finalización mediante una restricción.
![image](https://github.com/user-attachments/assets/ac48661f-8c4d-43c1-af22-7d460dfac37e)

### Validacion del Presupuesto 
```python
@api.onchange('budget')
def _onchange_budget(self):
    if self.budget and self.budget < 0:
        raise ValidationError('Budget must be positive.')
```
#### Descripcion
Valida que no sea 0



### Métodos para cambio de estado 
```python
def action_in_progress(self):
    self.state = 'in_progress'

def action_review(self):
    self.state = 'review'

def action_completed(self):
    self.state = 'completed'

def action_cancelled(self):
    self.state = 'cancelled'
```






