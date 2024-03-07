# Script that configures Nginx servers with puppet

exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
} ->

exec {'install Nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
} ->

exec {'/data/web_static/releases/test/':
  provider => shell,
  command  => 'sudo mkdir -p /data/web_static/releases/test/',
} ->

exec {'/data/web_static/shared/':
  provider => shell,
  command  => 'sudo mkdir -p /data/web_static/shared/',
} ->

exec {'fake html file':
  provider => shell,
  command  => 'echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html',
} ->

exec {'add symbolic link':
  provider => shell,
  command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
} ->

exec {'add location block':
  provider => shell,
  command  => 'sudo sed -i \'41i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n\' /etc/nginx/sites-available/default',
} ->

exec {'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
