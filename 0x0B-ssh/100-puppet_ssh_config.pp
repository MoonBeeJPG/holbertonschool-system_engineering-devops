#puppet file
exec { 'puppet_ssh_config:
  path    => '/usr/bin/',
  command => 'echo "IdentityFile ~/.ssh/school\n PasswordAuthentication no" >> /etc/ssh/ssh_config',
}
