# Generated by Django 3.1.10 on 2021-05-25 17:13

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('wagtailcore', '0060_fix_workflow_unique_constraint'),
        ('home', '0006_auto_20210525_1701'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'Home Page', 'verbose_name_plural': 'Home Pages'},
        ),
        migrations.AlterModelOptions(
            name='homepagecarouselimages',
            options={'ordering': ['sort_order']},
        ),
        migrations.RemoveField(
            model_name='homepagecarouselimages',
            name='banner_cta',
        ),
        migrations.RemoveField(
            model_name='homepagecarouselimages',
            name='banner_image',
        ),
        migrations.RemoveField(
            model_name='homepagecarouselimages',
            name='banner_subtitle',
        ),
        migrations.RemoveField(
            model_name='homepagecarouselimages',
            name='banner_title',
        ),
        migrations.AddField(
            model_name='homepage',
            name='banner_cta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='banner_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='banner_subtitle',
            field=wagtail.core.fields.RichTextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homepage',
            name='banner_title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]