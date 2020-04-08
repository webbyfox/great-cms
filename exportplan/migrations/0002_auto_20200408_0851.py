# Generated by Django 2.2.10 on 2020-04-08 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('core', '0008_auto_20200408_0851'),
        ('wagtail_personalisation', '0025_auto_20190822_0627'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('exportplan', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exportplanpage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='ExportPlanDashboardPage',
        ),
        migrations.DeleteModel(
            name='ExportPlanPage',
        ),
    ]
