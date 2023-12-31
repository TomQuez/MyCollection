# Generated by Django 4.2.7 on 2023-11-20 11:04

import CollectionCatalog.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name of your category', max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CollectionObject',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular object', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Enter a name for your object,a title for your book, or the model of your watch', max_length=200)),
                ('description', models.TextField(help_text='Enter a brief description of your object', max_length=1500)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', validators=[CollectionCatalog.models.validate_image_extension])),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('collectionobject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='CollectionCatalog.collectionobject')),
                ('author', models.CharField(help_text='Enter the name of the author', max_length=200)),
                ('edition', models.CharField(blank=True, choices=[('PO', 'Poche 11 cm x 18 cm'), ('DG', 'Digest 14 cm x 21.6 cm'), ('RO', 'Roman 15 cm x 21 cm'), ('RY', 'Royal 16 cm x 24 cm'), ('A4', 'A4 21 cm x 29,7 cm'), ('AU', 'Autre')], help_text="veuillez selectionner le type d'édition dans la liste déroulante", max_length=2, null=True)),
                ('type', models.CharField(choices=[('RM', 'Roman'), ('BG', 'Biographie'), ('AB', 'Autobiographie'), ('MG', 'Manga'), ('ES', 'Essai'), ('BD', 'Bande Dessinée'), ('CS', 'Comics'), ('BL', 'Beau Livre'), ('AU', 'Autre')], help_text='choose the type of book', max_length=2)),
                ('editeur', models.CharField(blank=True, help_text="veuillez saisir le nom de l'éditeur", max_length=200, null=True)),
            ],
            bases=('CollectionCatalog.collectionobject',),
        ),
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('collectionobject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='CollectionCatalog.collectionobject')),
                ('brand', models.CharField(help_text='enter the brand of your watch', max_length=100)),
                ('Material', models.CharField(blank=True, help_text='Enter the material(s) of your watch', max_length=200, null=True)),
                ('type_of_mecanism', models.CharField(blank=True, choices=[('MM', 'Mécanique manuel'), ('MA', 'Mécanique automatique'), ('QZ', 'Quartz (pile)')], help_text='Enter the type of mecanism of your watch, e.g. automatic', max_length=2, null=True)),
            ],
            bases=('CollectionCatalog.collectionobject',),
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a name for your collection', max_length=200)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CollectionCatalog.category')),
                ('collection_objects', models.ManyToManyField(help_text='Objects in this collection', to='CollectionCatalog.collectionobject')),
            ],
        ),
    ]
