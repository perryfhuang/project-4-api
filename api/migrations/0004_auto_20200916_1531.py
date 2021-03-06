# Generated by Django 3.0 on 2020-09-16 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200916_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='exercise_1',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_10',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_10_sets',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_10_weight',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_10reps',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_1_reps',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_1_sets',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_1_weight',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_2',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_2_reps',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_2_sets',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_2_weight',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_3',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_3_reps',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_3_sets',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_3_weight',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_4',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_4_reps',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_4_sets',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_4_weight',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_5',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_5_reps',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_5_sets',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_5_weight',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_6',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_6_reps',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_6_sets',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_6_weight',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_7',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_7_reps',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_7_sets',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_7_weight',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_8',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_8_reps',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_8_sets',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_8_weight',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_9',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_9_reps',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_9_sets',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_9_weight',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
