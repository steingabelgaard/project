# -*- coding: utf-8 -*-
# Copyright 2017 Tecnativa - Vicent Cubells
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Project Task Digitized Signature",
    "version": "9.0.1.0.0",
    "author": "Tecnativa, "
               "Odoo Community Association (OCA)",
    "website": "https://www.tecnativa.com",
    "category": "Project Management",
    "license": "AGPL-3",
    "depends": [
        "project",
        "web_widget_digitized_signature",
    ],
    "data": [
        "report/report_taskorder.xml",
        "report/project_task_views.xml",
        "views/project_task_views.xml",
        "data/task_template.xml",
    ],
    "installable": True,
}
