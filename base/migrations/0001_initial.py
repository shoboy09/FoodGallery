# Generated by Django 4.2.3 on 2023-07-30 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FgMenuCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'fg_menu_category',
            },
        ),
        migrations.CreateModel(
            name='FgMenuSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category_name', models.CharField(max_length=255)),
                ('menu_category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.fgmenucategory')),
            ],
            options={
                'db_table': 'fg_menu_sub_category',
            },
        ),
        migrations.CreateModel(
            name='FgMenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_item_name', models.CharField(max_length=255)),
                ('menu_sub_category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.fgmenusubcategory')),
            ],
            options={
                'db_table': 'fg_menu_item',
            },
        ),
    ]
