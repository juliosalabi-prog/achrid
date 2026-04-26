#!/usr/bin/env bash

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser --noinput || true
#!/usr/bin/env bash

pip install -r requirements.txt
python manage.py migrate

# Créer automatiquement un admin
python manage.py shell << END
from django.contrib.auth.models import User
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@gmail.com", "12345678")
END

python manage.py collectstatic --noinput
