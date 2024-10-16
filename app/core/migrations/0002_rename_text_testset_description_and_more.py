# Generated by Django 4.2.16 on 2024-10-14 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testset',
            old_name='text',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='usertestresult',
            old_name='correct_answer',
            new_name='correct_answers',
        ),
        migrations.RenameField(
            model_name='usertestresult',
            old_name='total_question',
            new_name='total_questions',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='core.question'),
        ),
        migrations.AddField(
            model_name='question',
            name='test_set',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='question', to='core.testset'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(max_length=255),
        ),
    ]
