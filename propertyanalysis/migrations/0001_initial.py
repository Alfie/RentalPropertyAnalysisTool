from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_income', models.FloatField(default=0)),
                ('laundry_income', models.FloatField(default=0)),
                ('storage_income', models.FloatField(default=0)),
                ('misc_income', models.FloatField(default=0)),
            ],
        ),
    ]
