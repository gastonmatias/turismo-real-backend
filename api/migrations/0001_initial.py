# Generated by Django 4.0.7 on 2022-09-23 01:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commune', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'commune',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'customer',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False)),
                ('qty_rooms', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('commune_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='department_commune_id_fk', to='api.commune')),
            ],
            options={
                'db_table': 'department',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='DepartmentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'department_type',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('mail_address', models.EmailField(max_length=100)),
                ('profile_photo', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'employee',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('guarantee_payment', models.IntegerField(default=0)),
                ('amount', models.IntegerField(default=0)),
                ('total_payment', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'payment',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'product_type',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'region',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ServicesType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'service_type',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=100)),
                ('id_vehicle', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'vehicle',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='WorkArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'work_area',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=200)),
                ('price', models.IntegerField(default=0)),
                ('location', models.CharField(default=None, max_length=250, null=True)),
                ('available', models.BooleanField(default=False)),
                ('service_type', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='service_type_fk', to='api.servicestype')),
            ],
            options={
                'db_table': 'service',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('Reservado', 'Reservado (10% pagado)'), ('Pagado', 'Pagado (100%)'), ('Cancelado', 'Cancelado')], default='Reservado', max_length=50)),
                ('total_amount', models.IntegerField()),
                ('reservation_amount', models.IntegerField()),
                ('difference_amount', models.IntegerField()),
                ('qty_customers', models.IntegerField(blank=True)),
                ('reservation_date', models.DateTimeField()),
                ('check_in', models.DateTimeField()),
                ('check_out', models.DateTimeField()),
                ('id_department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.department')),
                ('id_services', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.services')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tariff', models.IntegerField(default=0)),
                ('rental_date', models.DateField()),
                ('payment_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='payment_id_fk', to='api.payment')),
            ],
            options={
                'db_table': 'rent',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('product_type', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='product_type_fk', to='api.producttype')),
            ],
            options={
                'db_table': 'product',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income', models.IntegerField(default=0)),
                ('egress', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
                ('date_time', models.DateField()),
                ('user_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='finance_user_id_fk', to='api.employee')),
            ],
            options={
                'db_table': 'finance',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='EmployeeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100)),
                ('work_area_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='work_area_id_fk', to='api.workarea')),
            ],
            options={
                'db_table': 'employee_type',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='EmployeeSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(max_length=100)),
                ('user_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='session_user_id_fk', to='api.employee')),
            ],
            options={
                'db_table': 'employee_session',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='EmployeeAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('user_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_id_fk', to='api.employee')),
            ],
            options={
                'db_table': 'employee_account',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_type_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='employee_type_id_fk', to='api.employeetype'),
        ),
        migrations.CreateModel(
            name='DepartmentMaintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintenance_date', models.DateField()),
                ('last_maintenance', models.DateField()),
                ('description', models.CharField(max_length=100)),
                ('department_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='department_maintance_id_fk', to='api.department')),
            ],
            options={
                'db_table': 'department_maintenance',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='DepartmentInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateField()),
                ('qty', models.IntegerField(default=0)),
                ('department_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='department_id_fk', to='api.department')),
                ('product_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='product_id_fk', to='api.product')),
            ],
            options={
                'db_table': 'department_inventory',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='department',
            name='department_type_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='department_type_id_fk', to='api.departmenttype'),
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('mail_address', models.CharField(max_length=100)),
                ('legal_representative', models.CharField(max_length=100)),
                ('commune_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='commune_id_fk', to='api.commune')),
            ],
            options={
                'db_table': 'company',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='commune',
            name='id_region',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='id_region_fk', to='api.region'),
        ),
    ]
