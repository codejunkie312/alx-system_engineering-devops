# Configure the ssh client to use the private key for authentication
file { '/etc/ssh/ssh_config':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0600',
  content => "Host *\n\tIdentityFile ~/.ssh/school\n\tPasswordAuthentication no\n",
  }
