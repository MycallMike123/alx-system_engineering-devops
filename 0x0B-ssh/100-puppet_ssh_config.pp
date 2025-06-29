file_line { 'Set IdentityFile':
  path  => '/home/mycall/.ssh/config',
  line  => '    IdentityFile ~/.ssh/school',
  match => '^\\s*IdentityFile\\s+',
}

file_line { 'Disable PasswordAuthentication':
  path  => '/home/mycall/.ssh/config',
  line  => '    PasswordAuthentication no',
  match => '^\\s*PasswordAuthentication\\s+',
}
