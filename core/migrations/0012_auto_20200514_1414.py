# Generated by Django 2.2.10 on 2020-05-14 14:14

import core.blocks
import core.mixins
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields
import wagtail_personalisation.blocks
import wagtail_personalisation.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtail_personalisation', '0025_auto_20190822_0627'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('core', '0011_auto_20200504_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='CuratedListPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('template', models.CharField(max_length=255)),
                ('heading', wagtail.core.fields.RichTextField()),
                ('topics', wagtail.core.fields.StreamField([('topic', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=255)), ('pages', wagtail.core.blocks.ListBlock(wagtail.core.blocks.PageChooserBlock(label='Detail page')))], icon='plus'))], blank=True, null=True)),
                ('record_read_progress', models.BooleanField(default=False, help_text='Should we record when a user views a page in this collection?')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='core.AltTextImage')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail_personalisation.models.PersonalisablePageMixin, core.mixins.EnableTourMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='InterstitialPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('template', models.CharField(max_length=255)),
                ('button', wagtail.core.fields.StreamField([('button', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(max_length=255)), ('link', wagtail.core.blocks.StructBlock([('internal_link', wagtail.core.blocks.PageChooserBlock(label='Internal link', required=False)), ('external_link', wagtail.core.blocks.CharBlock(label='External link', max_length=255, required=False))], required=False))], icon='cog'))], blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail_personalisation.models.PersonalisablePageMixin, core.mixins.EnableTourMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='LandingPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('template', models.CharField(max_length=255)),
                ('description', wagtail.core.fields.RichTextField()),
                ('button', wagtail.core.fields.StreamField([('button', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(max_length=255)), ('link', wagtail.core.blocks.StructBlock([('internal_link', wagtail.core.blocks.PageChooserBlock(label='Internal link', required=False)), ('external_link', wagtail.core.blocks.CharBlock(label='External link', max_length=255, required=False))], required=False))], icon='cog'))], blank=True, null=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='core.AltTextImage')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail_personalisation.models.PersonalisablePageMixin, core.mixins.EnableTourMixin, 'wagtailcore.page'),
        ),
        migrations.AlterModelOptions(
            name='detailpage',
            options={'verbose_name': 'Personalisable detail page', 'verbose_name_plural': 'Personalisable detail pages'},
        ),
        migrations.AlterModelOptions(
            name='listpage',
            options={'verbose_name': 'Automated list page', 'verbose_name_plural': 'Automated list pages'},
        ),
        migrations.RemoveField(
            model_name='listpage',
            name='body',
        ),
        migrations.RemoveField(
            model_name='listpage',
            name='record_read_progress',
        ),
        migrations.AddField(
            model_name='listpage',
            name='button_label',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listpage',
            name='description',
            field=wagtail.core.fields.RichTextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='detailpage',
            name='body',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.StructBlock([('segment', wagtail.core.blocks.ChoiceBlock(choices=wagtail_personalisation.blocks.list_segment_choices, help_text='Only show this content block for users in this segment', label='Personalisation segment', required=False)), ('paragraph', wagtail.core.blocks.RichTextBlock())], icon='pilcrow', template='core/personalised_page_struct_paragraph_block.html')), ('video', wagtail.core.blocks.StructBlock([('segment', wagtail.core.blocks.ChoiceBlock(choices=wagtail_personalisation.blocks.list_segment_choices, help_text='Only show this content block for users in this segment', label='Personalisation segment', required=False)), ('video', wagtail.core.blocks.StructBlock([('width', wagtail.core.blocks.IntegerBlock()), ('height', wagtail.core.blocks.IntegerBlock()), ('video', core.blocks.MediaChooserBlock())]))], icon='media', template='core/personalised_page_struct_video_block.html'))]),
        ),
        migrations.AlterField(
            model_name='matchproductexpertise',
            name='segment',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='core_matchproductexpertises', to='wagtail_personalisation.Segment'),
        ),
        migrations.AlterField(
            model_name='pageview',
            name='list_page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_views_list', to='core.CuratedListPage'),
        ),
        migrations.DeleteModel(
            name='HomePage',
        ),
    ]