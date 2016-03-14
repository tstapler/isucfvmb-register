# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dietary_needs',
            field=models.CharField(max_length=20, choices=[(b'Standard', b'Standard'), (b'Vegitarian', b'Vegitarian'), (b'Gluten Free', b'Gluten Free (Please provide medical documentation)'), (b'Self Provided', b'Will Provide Own')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='ensemble',
            field=models.CharField(max_length=9, choices=[(b'storm', b'State Storm'), (b'varsity', b"ISUCF'V'MB")]),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(max_length=6, choices=[(b'Female', b'Female'), (b'Male', b'Male')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='instrument',
            field=models.CharField(max_length=30, choices=[(b'Alto Sax', b'Alto Sax'), (b'Baritone', b'Baritone'), (b'Bass Drum', b'Bass Drum'), (b'Bass Trombone', b'Bass Trombone'), (b'Clarinet', b'Clarinet'), (b'Color Guard', b'Color Guard'), (b'Feature Twirler', b'Feature Twirler'), (b'Melophone', b'Melophone'), (b'Piccolo', b'Piccolo'), (b'Snare Drum', b'Snare Drum'), (b'Sousaphone', b'Sousaphone'), (b'Tenor Drums', b'Tenor Drums'), (b'Tenor Sax', b'Tenor Sax'), (b'Trombone 1', b'Trombone 1'), (b'Trombone 2', b'Trombone 2'), (b'Trumpet 1', b'Trumpet 1'), (b'Trumpet 2', b'Trumpet 2'), (b'Trumpet 3', b'Trumpet 3')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='shoe_size',
            field=models.CharField(max_length=6, choices=[(b'4', b'4'), (b'4.5', b'4.5'), (b'5.0', b'5.0'), (b'5.5', b'5.5'), (b'6.0', b'6.0'), (b'6.5', b'6.5'), (b'7.0', b'7.0'), (b'7.5', b'7.5'), (b'8.0', b'8.0'), (b'8.5', b'8.5'), (b'9.0', b'9.0'), (b'9.5', b'9.5'), (b'10.0', b'10.0'), (b'10.5', b'10.5'), (b'11.0', b'11.0'), (b'11.5', b'11.5'), (b'12.0', b'12.0'), (b'12.5', b'12.5'), (b'13.0', b'13.0'), (b'13.5', b'13.5'), (b'14.0', b'14.0')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.CharField(unique=True, max_length=9),
        ),
        migrations.AlterField(
            model_name='student',
            name='tshirt_size',
            field=models.CharField(max_length=6, choices=[(b'S', b'Small'), (b'M', b'Medium'), (b'L', b'Large'), (b'XL', b'XL'), (b'XXL', b'XXL'), (b'XXXL', b'XXXL')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='years_tenure',
            field=models.CharField(max_length=3, choices=[(b'0', b'0'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5+', b'5+')]),
        ),
    ]
