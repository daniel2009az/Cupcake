set -o errexit

python -m pip install -r requirements.txt
python -m pip install psycopg2-binary
python manage.py makemigrations
python manage.py migrate
mkdir -p /opt/render/project/src/mediafiles
python manage.py collectstatic --no-input

# Manter criação de superusuário se necessário
if ! python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); print(User.objects.filter(is_superuser=True).exists())" | grep -q "True"; then
    python manage.py createsuperuser --no-input
fi