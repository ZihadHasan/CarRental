
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(default='', max_length=100)),
                ('b_contact', models.CharField(default='', max_length=128)),
                ('b_id', models.IntegerField(default=0)),
                ('b_address', models.CharField(default='', max_length=120)),
                ('b_email', models.EmailField(default='', max_length=110)),
                ('b_pass', models.CharField(max_length=110)),
            ],
        ),
        migrations.CreateModel(
            name='car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(default='', max_length=100)),
                ('car_id', models.IntegerField(default=0)),
                ('price_per_day', models.IntegerField(default=0)),
                ('car_type', models.CharField(default='', max_length=100)),
                ('car_img', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.IntegerField(default=0)),
                ('payment_ammount', models.IntegerField(default=0)),
                ('payment_date', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(default='', max_length=100)),
                ('s_contact', models.IntegerField(default=0)),
                ('s_id', models.IntegerField(default=0)),
                ('s_address', models.CharField(default='', max_length=120)),
                ('s_email', models.CharField(default='', max_length=110)),
                ('s_pass', models.CharField(max_length=110)),
            ],
        ),
        migrations.CreateModel(
            name='sold',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='H1.buyer')),
                ('f_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='H1.car')),
                ('payment_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='H1.payment')),
                ('s_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='H1.seller')),
            ],
        ),
    ]
