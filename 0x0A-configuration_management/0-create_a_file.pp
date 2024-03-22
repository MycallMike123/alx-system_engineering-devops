# Creates a class using Puppet

class school_file {

	file { '/tmp/school':
		ensure  => file,            # Ensure it's a file
		mode    => '0744',          # Set file permissions
		owner   => 'www-data',      # Set owner
		group   => 'www-data',      # Set group
		content => "I love Puppet",  # Set file content
	}
}

include school_file
