{
    'name': 'Research Project Management',
    'version': '1.0',
    'summary': 'Gestión de proyectos de investigación en Odoo 18',
    'author': 'Sebastián',
    'website': 'https://github.com/Vallit0/interview_research_project',
    'category': 'Research',
    'depends': ['base', 'mail'],
    'data': [
        # Primero siempre las reglas de seguridad y definición de modelos
        'security/security.xml',
        'security/ir.model.access.csv',
        
        # Luego datos como secuencias automáticas
        'data/project_sequence.xml',
        
        # Luego las vistas del modelo
        'views/research_project_views.xml',
        
        # Luego reportes y plantillas de impresión
        'report/research_project_templates.xml',
        'report/research_project_report.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'description': """
Este módulo permite gestionar proyectos de investigación, asignar investigadores,
controlar fechas, presupuesto y estados del proyecto. Incluye reportes en PDF.
    """,
}

