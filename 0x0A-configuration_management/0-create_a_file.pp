# Creates a file

file { '/tmp/school':
  ensure  => file,	# Ensure it's a file
  path    => '/tmp/school',
  mode    => '0744',	# Set file permissions
  owner   => 'www-data',	# Set owner
  group   => 'www-data',	# Set group
  content => 'I love Puppet'	# Set file content
}
