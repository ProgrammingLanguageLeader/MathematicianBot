from subprocess import call
from nginxparser_eb import load, loads, dump

from config import Config


if __name__ == '__main__':
    home_dir = Config.HOME_DIR

    # configuring nginx
    upstream = \
        'upstream {} {{\n' \
        '   server unix:/tmp/{}.sock;\n' \
        '}}\n'.format(
            Config.APP_NAME, Config.APP_NAME
        )
    location = \
        'location /{} {{\n' \
        '   include uwsgi_params;\n' \
        '   uwsgi_pass {};\n' \
        '}}\n'.format(
            Config.TELEGRAM_TOKEN,
            Config.APP_NAME
        )
    nginx_config = load(open(Config.NGINX_CONFIG_PATH))
    nginx_config.insert(0, loads(upstream)[0])
    for section in nginx_config:
        if section[0][0] == 'server':
            section[1].append(loads(location)[0])
            break
    dump(nginx_config, open(Config.NGINX_CONFIG_PATH, 'w'))
    call([
        'ln', '-s',
        '{} /etc/nginx/sites-enabled/'.format(Config.NGINX_CONFIG_PATH)
    ])
    call(['systemctl', 'reload', 'nginx'])

    # configuring uWSGI
    uwsgi_config = \
        '[uwsgi]\n' \
        'module = wsgi:app\n' \
        'uid = {}\n' \
        'gid = www-data\n' \
        'master = true\n' \
        'processes = 5\n' \
        'socket = /tmp/{}.sock\n' \
        'chmod-socket = 660\n' \
        'chwon-socket = {}:www-data\n' \
        'vacuum = true\n' \
        'die-on-term = true\n' \
        'logto = {}\n'.format(
            Config.APP_NAME, Config.APP_NAME,
            Config.APP_NAME, Config.UWSGI_LOG_PATH
        )
    with open('{}/uwsgi.ini'.format(home_dir), 'w') as uwsgi_file:
        uwsgi_file.write(uwsgi_config)

    # creating logging directory
    call(['mkdir', Config.LOG_DIR])
    call([
        'chown', '-Rc',
        '{}:www-data'.format(Config.APP_NAME),
        Config.LOG_DIR
    ])
    call(['chmod', '-R', '0755', Config.LOG_DIR])

    # creating and starting application service
    service_string = \
        '[Unit]\n' \
        'Description=uWSGI instance to serve {} project\n' \
        'After=network.target\n' \
        '[Service]\n' \
        'User={}\n' \
        'Group=www-data\n' \
        'WorkingDirectory=/srv/{}\n' \
        'Environment="PATH=/srv/{}/venv/bin"\n' \
        'ExecStart=/srv/{}/venv/bin/uwsgi --ini uwsgi.ini\n' \
        '[Install]\n' \
        'WantedBy=multi-user.target\n'.format(
            Config.APP_NAME, Config.APP_NAME,
            Config.APP_NAME, Config.APP_NAME,
            Config.APP_NAME
        )
    service_path = '/etc/systemd/system/{}.service'.format(
        Config.APP_NAME
    )
    with open(service_path, 'w') as service_file:
        service_file.write(service_string)
    call(['systemctl', 'start', '{}'.format(Config.APP_NAME)])
    call(['systemctl', 'enable', '{}'.format(Config.APP_NAME)])
