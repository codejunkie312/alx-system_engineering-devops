# fixes issue with nginx
exec {'fix_nginx':
  command => 'sed -i "s/15/2000/g" /etc/default/nginx',
  path    => '/usr/bin:/usr/sbin:/bin',
}

# restarts nginx
-> exec {'restart_nginx':
  command => 'service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin'
}
