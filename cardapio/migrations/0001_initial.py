import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alergenico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TabelaNutricional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calorias', models.FloatField(default=0, help_text='Valor em kcal')),
                ('carboidratos', models.FloatField(default=0, help_text='Valor em gramas (g)')),
                ('proteinas', models.FloatField(default=0, help_text='Valor em gramas (g)')),
                ('gorduras', models.FloatField(default=0, help_text='Valor em gramas (g)')),
                ('fibras', models.FloatField(default=0, help_text='Valor em gramas (g)')),
                ('sodio', models.FloatField(default=0, help_text='Valor em miligramas (mg)')),
                ('observacao', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Alimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('turno', models.CharField(choices=[('MANHA', 'Manhã'), ('ALMOCO', 'Almoço'), ('TARDE', 'Tarde')], default='ALMOCO', max_length=10)),
                ('alergenicos', models.ManyToManyField(blank=True, to='cardapio.alergenico')),
                ('ingredientes', models.ManyToManyField(blank=True, to='cardapio.ingrediente')),
                ('tabela_nutricional', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cardapio.tabelanutricional')),
            ],
        ),
        migrations.CreateModel(
            name='Cardapio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(unique=True)),
                ('alimentos', models.ManyToManyField(related_name='cardapios', to='cardapio.alimento')),
            ],
        ),
    ]
