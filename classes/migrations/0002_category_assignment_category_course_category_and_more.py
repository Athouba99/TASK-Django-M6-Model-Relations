# Generated by Django 4.0.4 on 2022-10-18 18:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('image', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='classes.category'),
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='classes.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lecture',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='classes.category'),
        ),
        migrations.AddField(
            model_name='slide',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='classes.category'),
        ),
        migrations.AddField(
            model_name='tag',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='classes.category'),
        ),
    ]
