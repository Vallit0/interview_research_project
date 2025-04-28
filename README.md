# Desarrollo de Módulos de Investigación
## Documentación de Usuario 
![image](https://github.com/user-attachments/assets/5b4ba6bf-44b4-4bae-a7e6-472abfed24e9)
![image](https://github.com/user-attachments/assets/f6b73671-36cb-41e6-98bd-e3a9f37d63c0)

![image](https://github.com/user-attachments/assets/2820945b-7dc7-468c-9144-1768efac6188)



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


