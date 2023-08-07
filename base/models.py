from django.db import models


class FgMenuCategory(models.Model):
    menu_name = models.CharField(max_length=255)

    class Meta:
        # managed = False
        db_table = 'fg_menu_category'


class FgMenuItem(models.Model):
    menu_item_name = models.CharField(max_length=255)
    menu_sub_category = models.ForeignKey(
        'FgMenuSubCategory', models.DO_NOTHING)

    class Meta:
        # managed = False
        db_table = 'fg_menu_item'


class FgMenuSubCategory(models.Model):
    sub_category_name = models.CharField(max_length=255)
    menu_category = models.ForeignKey('FgMenuCategory', models.DO_NOTHING)

    class Meta:
        # managed = False
        db_table = 'fg_menu_sub_category'
