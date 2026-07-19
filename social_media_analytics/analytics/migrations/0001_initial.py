from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='SocialPost',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('platform', models.CharField(max_length=50)),
                ('post_id', models.CharField(max_length=100, unique=True)),
                ('content', models.TextField()),
                ('likes', models.IntegerField(default=0)),
                ('comments', models.IntegerField(default=0)),
                ('shares', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
