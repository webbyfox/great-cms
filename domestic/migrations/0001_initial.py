# Generated by Django 2.2.9 on 2020-01-23 13:46

import core.mixins
from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
    ]

    operations = [
        migrations.CreateModel(
            name='DomesticHomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('hero', wagtail.core.fields.StreamField([('hero', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(blank=True, null=True)), ('url', wagtail.core.blocks.CharBlock(max_length=255)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('alt_text', wagtail.core.blocks.CharBlock(required=False))]))], blank=True, null=True)),
                ('market_access_db', wagtail.core.fields.StreamField([('market_access_db', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('text', wagtail.core.blocks.CharBlock(max_length=255)), ('url', wagtail.core.blocks.CharBlock(max_length=255)), ('source', wagtail.core.blocks.CharBlock(help_text='The source or the type of the link, e.g. GOV.UK/Advice')), ('content', wagtail.core.blocks.RichTextBlock()), ('title', wagtail.core.blocks.CharBlock())]))], blank=True, null=True)),
                ('campaign', wagtail.core.fields.StreamField([('campaign', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(max_length=255)), ('url', wagtail.core.blocks.CharBlock(max_length=255)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('heading', wagtail.core.blocks.CharBlock()), ('subheading', wagtail.core.blocks.CharBlock())]))], blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(core.mixins.WagtailAdminExclusivePageMixin, 'wagtailcore.page'),
        ),
    ]