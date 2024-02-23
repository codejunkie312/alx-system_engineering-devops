# Remove user limits
file {'remove_user_limits':
  ensure  => present,
  path    => '/etc/security/limits.conf',
  content => ''
}
