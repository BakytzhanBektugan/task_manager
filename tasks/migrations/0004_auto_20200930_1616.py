# Generated by Django 2.2.16 on 2020-09-30 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_delete_taskhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='TaskHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('file', models.FileField(blank=True, null=True, upload_to='files/%Y/%m/%d/')),
                ('status', models.CharField(choices=[('N', 'New'), ('P', 'Planned'), ('I', 'In progress'), ('C', 'Completed')], default='N', max_length=1)),
                ('completion_date', models.DateField(blank=True, null=True)),
                ('changed_at', models.DateTimeField(auto_now_add=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_history', to='tasks.Task')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
