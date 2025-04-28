# Desarrollo de Módulos de Investigación 
Previo a la integración de módulos de Odoo, es necesario instalar las dependencias. En este caso, se instalará Odoo 18 con hard-binding en contenedores de docker para no afectar 
el sistema operativo. 
```docker
version: '3.1'

services:
  db:
    image: postgres:15
    container_name: odoo18-db
    environment:
      POSTGRES_DB: odoo
      POSTGRES_USER: odoo
      POSTGRES_PASSWORD: odoo
    ports:
      - "5432:5432"
    restart: always
    volumes:
      - odoo18_db_data:/var/lib/postgresql/data

  odoo:
    image: odoo:18.0
    container_name: odoo18
    depends_on:
      - db
    ports:
      - "8069:8069"
    restart: always
    volumes:
      - ./custom_addons:/mnt/extra-addons
    environment:
      - HOST=db
      - USER=odoo
      - PASSWORD=odoo

volumes:
  odoo18_db_data:

```


