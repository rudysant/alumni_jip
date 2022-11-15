# Generated by Django 4.1.3 on 2022-11-11 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "database",
            "0003_remove_data_alumni_tanggal_input_data_alumni_resume_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="data_alumni",
            name="username",
        ),
        migrations.AlterField(
            model_name="data_alumni",
            name="dosen_wali",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="data_alumni",
            name="npm",
            field=models.CharField(max_length=10, verbose_name="NPM"),
        ),
    ]
