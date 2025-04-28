# Desarrollo de Módulos de Investigación
## Documentación de Usuario (Demo)

#### Ingreso de Módulo en Búsqueda
![image](https://github.com/user-attachments/assets/2820945b-7dc7-468c-9144-1768efac6188)

### Inicialización de Módulo
![image](https://github.com/user-attachments/assets/5b4ba6bf-44b4-4bae-a7e6-472abfed24e9)

###
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

  
![image](https://github.com/user-attachments/assets/a1d2b032-57c8-4b67-95c5-2c16ee423b0c)
![image](https://github.com/user-attachments/assets/a15891ff-1c50-4065-ad4e-1d263fc929f6)
![image](https://github.com/user-attachments/assets/0f3694c6-3f23-4fad-9386-5204168294d8)
![image](https://github.com/user-attachments/assets/a4517e6c-e8f5-4375-83bd-d88ee92c38dd)
![image](https://github.com/user-attachments/assets/8df8df06-77b7-4575-9c8e-370dbff8446d)

![image](https://github.com/user-attachments/assets/58379535-bbea-421b-a618-14f538ed1182)

## Documentacion Técnica 
Previo a la integración de módulos de Odoo, es necesario instalar las dependencias. En este caso, se instalará Odoo 18 en Ubuntu.
```bash
git clone https://www.github.com/odoo/odoo --branch 18.0 --single-branch .
```

![image](https://github.com/user-attachments/assets/b33f75bc-9e0e-4bef-b549-d0e70506b26b)

![image](https://github.com/user-attachments/assets/5a69a118-37b6-4f08-a849-e4a8104e943f)


![image](https://github.com/user-attachments/assets/de558bcf-2b23-43c8-bf92-3b217af0d5e2)

![image](https://github.com/user-attachments/assets/35395abb-3258-4d93-a03f-e28db35fb1fc)


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


