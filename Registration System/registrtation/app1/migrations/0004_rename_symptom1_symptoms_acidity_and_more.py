# Generated by Django 4.2 on 2023-04-11 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_symptoms_symptom1_alter_symptoms_symptom10_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='symptoms',
            old_name='symptom1',
            new_name='Acidity',
        ),
        migrations.RenameField(
            model_name='symptoms',
            old_name='symptom10',
            new_name='Anxiety',
        ),
        migrations.RenameField(
            model_name='symptoms',
            old_name='symptom11',
            new_name='Back_pain',
        ),
        migrations.RenameField(
            model_name='symptoms',
            old_name='symptom12',
            new_name='Chest_Pain',
        ),
        migrations.RenameField(
            model_name='symptoms',
            old_name='symptom13',
            new_name='Coma',
        ),
        migrations.RenameField(
            model_name='symptoms',
            old_name='symptom14',
            new_name='Constipation',
        ),
        migrations.RenameField(
            model_name='symptoms',
            old_name='symptom15',
            new_name='Continuous_Sneezing',
        ),
        migrations.RenameField(
            model_name='symptoms',
            old_name='symptom16',
            new_name='Cough',
        ),
        migrations.RenameField(
            model_name='symptoms',
            old_name='symptom17',
            new_name='Cramps',
        ),
        migrations.RenameField(
            model_name='symptoms',
            old_name='symptom18',
            new_name='Dehydration',
        ),
        migrations.RenameField(
            model_name='symptoms',
            old_name='symptom19',
            new_name='Diarrhoea',
        ),
        migrations.RenameField(
            model_name='symptoms',
            old_name='symptom2',
            new_name='Dizziness',
        ),
        migrations.RenameField(
            model_name='symptoms',
            old_name='symptom20',
            new_name='FastHeartRate',
        ),
        migrations.RenameField(
            model_name='symptoms',
            old_name='symptom21',
            new_name='Fatigue',
        ),
        migrations.RenameField(
            model_name='symptoms',
            old_name='symptom22',
            new_name='Headache',
        ),
        migrations.RenameField(
            model_name='symptoms',
            old_name='symptom23',
            new_name='High_Fever',
        ),
        migrations.RenameField(
            model_name='symptoms',
            old_name='symptom24',
            new_name='Indigestion',
        ),
        migrations.RenameField(
            model_name='symptoms',
            old_name='symptom25',
            new_name='Joint_Pain',
        ),
        migrations.RenameField(
            model_name='symptoms',
            old_name='symptom26',
            new_name='KneePain',
        ),
        migrations.RenameField(
            model_name='symptoms',
            old_name='symptom27',
            new_name='LackofConcentration',
        ),
        migrations.RenameField(
            model_name='symptoms',
            old_name='symptom3',
            new_name='MuscleWeakness',
        ),
        migrations.RenameField(
            model_name='symptoms',
            old_name='symptom4',
            new_name='Nausea',
        ),
        migrations.RenameField(
            model_name='symptoms',
            old_name='symptom5',
            new_name='Obesity',
        ),
        migrations.RenameField(
            model_name='symptoms',
            old_name='symptom6',
            new_name='Stomach_Pain',
        ),
        migrations.RenameField(
            model_name='symptoms',
            old_name='symptom7',
            new_name='Vomiting',
        ),
        migrations.RenameField(
            model_name='symptoms',
            old_name='symptom8',
            new_name='Weight_Loss',
        ),
        migrations.RenameField(
            model_name='symptoms',
            old_name='symptom9',
            new_name='itching',
        ),
        migrations.RemoveField(
            model_name='symptoms',
            name='sex',
        ),
    ]
