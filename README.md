# django_test
```console
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
./manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@email.com', '123')"
chmod 777 start.sh
./start.sh
```
superuser: admin\
pass: 123

http://127.0.0.1:8000/admin/cms/cmsslider/ \
"Добавить слайд"\
"CSS class" в первом слайде "active"

pip uninstall -r requirements.txt
