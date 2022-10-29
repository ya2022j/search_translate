



import os



os.chdir("/usr/local/db_api/")
os.system("gunicorn -w 4 -b 0.0.0.0:5000 --access-logfile access.log --error-logfile error.log server_api:app -D")



os.chdir("/usr/local/dictionary/ja2ko/")
os.system("gunicorn -w 4 -b 0.0.0.0:8002 --access-logfile access.log --error-logfile error.log flask_search:app -D")


os.chdir("/usr/local/msg/")
os.system("gunicorn -w 4 -b 0.0.0.0:8000 --access-logfile access.log --error-logfile error.log flask_ebook:app -D")


os.system("pkill -9 nginx")
os.system("/usr/local/nginx/sbin/nginx -c /usr/local/nginx/conf/nginx.conf")