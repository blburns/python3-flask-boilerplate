# Directory Structure


```commandline
[Project Directory]
+-- app/
|   +-- bin/
|   +-- docs/
|   |   +-- INSTALL.md
|   |   +-- README.md
|   | 
|   +-- api/
|   |   +-- module_1/
|   |   |   +-- __init__.py
|   |   |   +-- routes.py
|   |   |
|   |   +-- module_2/
|   |   |   +-- __init__.py
|   |   |   +-- routes.py
|   |   |
|   |   +-- __init__.py
|   |
|   +-- console/
|   +-- data/
|   |   +-- backups/
|   |   +-- cache/
|   |   +-- db/
|   |   |   +-- admins.db
|   |   |   +-- users.db
|   |   |   +-- sessions.db
|   |   |   +-- app.db
|   |   |
|   |   +-- logs/
|   |   |   +-- archive/
|   |   |   +-- access.log
|   |   |   +-- error.log
|   |   |   +-- console.log
|   |   |
|   |   +-- seeds/
|   |   |   +-- seed_admins.csv
|   |   |   +-- seed_users.csv
|   |   |   +-- seed_module_1_data.csv
|   |   |   +-- seed_module_2_data.csv
|   |   |   
|   |   +-- sessions/
|   |
|   +-- models/
|   |   +-- admins.py
|   |   +-- users.py
|   |   +-- module_1_table.py
|   |   +-- moudle_2_table.py
|   |
|   +-- modules/
|   |       +-- main/
|   |       |   +-- __init__.py
|   |       |   +-- api.py
|   |       |   +-- routes.py
|   |       |
|   |       +-- module_1/
|   |       |   +-- __init__.py
|   |       |   +-- api.py
|   |       |   +-- routes.py
|   |       |
|   |       +-- module_2/
|   |           +-- __init__.py
|   |           +-- api.py
|   |           +-- routes.py
|   |
|   +-- static/
|   |   +-- assets/
|   |   +-- libs/
|   |   +-- js/
|   |   +-- css/
|   |   +-- pages/
|   |  
|   +-- views/
|   |   +-- module_1/
|   |   |   +-- static/
|   |   |   +-- templates/
|   |   |       +-- layout/
|   |   |           +-- elements
|   |   |               +-- cards
|   |   |               +-- forms
|   |   |               +-- mod
|   |   |   
|   |   |
|   |   +-- module_2/
|   |   |   +-- static/
|   |   |   +-- templates/
|   |   |
|   +-- templates/
|   |   +-- auth/
|   |   +-- apps/
|   |   +-- settings/
|   |   +-- layout/
|   |   |   +-- elements/
|   |   |   |   +-- cards/
|   |   |   |   +-- forms/
|   |   |   |   +-- tables/
|   |   |   |   +-- tabs/
|   |   |   |
|   |   |   +-- sections/
|   |   |   |   +-- main-header.html
|   |   |   |   +-- main-meta.html
|   |   |   |   +-- mian-navbar.html
|   |   |   |   +-- main-scripts.html
|   |   |   |   +-- main-sidebar.html
|   |   |   |   +-- main-sidebar-nofill.html
|   |   |   |   +-- main-footer.html
|   |   |   |
|   |   |   +-- partials/
|   |   |   +-- pages/
|   |   |       +-- somepage.html
|   |   |
|   |   +-- base.html
|   |   +-- custom_theme.html
|   |
|   +-- tests/
|   |   +-- module_1/
|   |   |   +-- helper_tests.py
|   |   |   +-- module_1_tests.py
|   |   |
|   |   +-- module_2/
|   |       +-- helper_tests.py
|   |       +-- module_2_tests.py
|   |
|   +-- __init__.py
|   +-- api.py
|   +-- blueprints.py
|   +-- extentions.py
|
.env
.env.example
.env.development
.env.production
.gitignore
app.db
bootstrap.sh
config.py
manage.py
README.md
requirements.txt
```

