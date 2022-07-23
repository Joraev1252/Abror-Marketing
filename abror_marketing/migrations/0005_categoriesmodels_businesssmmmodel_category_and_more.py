# Generated by Django 4.0.6 on 2022-07-23 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('abror_marketing', '0004_businesssmmmodel_body1_en_businesssmmmodel_body1_ru_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriesModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
            ],
        ),
        migrations.AddField(
            model_name='businesssmmmodel',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='abror_marketing.categoriesmodels'),
        ),
        migrations.AddField(
            model_name='contactmodel',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='abror_marketing.categoriesmodels'),
        ),
        migrations.AddField(
            model_name='ourprojectsmodel',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='abror_marketing.categoriesmodels'),
        ),
    ]
