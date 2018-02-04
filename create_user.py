from subprocess import call

from config import Config


if __name__ == '__main__':
    # creating user for the application
    home_dir = '/srv/{}'.format(Config.APP_NAME)
    call(['mkdir', home_dir])
    call([
        'useradd', '-s', '/bin/false',
        '-d', home_dir,
        Config.APP_NAME
    ])
    call([
        'chown', '-Rc',
        '{}:www-data'.format(Config.APP_NAME),
        home_dir
    ])
    call(['chmod', '-R', '0755', home_dir])
