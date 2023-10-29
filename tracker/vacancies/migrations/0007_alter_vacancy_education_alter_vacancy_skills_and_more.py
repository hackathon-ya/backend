# Generated by Django 4.1.12 on 2023-10-29 21:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_rename_work_arrangements_educationyp_and_more"),
        ("vacancies", "0006_alter_vacancy_city_alter_vacancy_education_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vacancy",
            name="education",
            field=models.ManyToManyField(
                blank=True,
                related_name="vacancies",
                to="core.education",
                verbose_name="Образование",
            ),
        ),
        migrations.AlterField(
            model_name="vacancy",
            name="skills",
            field=models.ManyToManyField(
                blank=True,
                related_name="vacancies",
                to="core.skills",
                verbose_name="Навыки",
            ),
        ),
        migrations.AlterField(
            model_name="vacancy",
            name="work_arrangement",
            field=models.ManyToManyField(
                blank=True,
                related_name="vacancies",
                to="core.workarrangements",
                verbose_name="Формат работы",
            ),
        ),
    ]
