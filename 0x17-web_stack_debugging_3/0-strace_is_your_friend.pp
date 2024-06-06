# Ensure WordPress settings file is configured properly
file { '/var/www/html/wp-settings.php':
  ensure  => file,
  source  => 'puppet:///path/to/wp-settings.php', # Replace with the actual source path
  owner   => 'www-data',  # Replace with the appropriate owner
  group   => 'www-data',  # Replace with the appropriate group
  mode    => '0644',      # Adjust permissions as needed
  notify  => Exec['fix-wordpress'],  # Trigger fix command after file update
}

# Automate fix using Puppet exec
exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/usr/local/bin', '/usr/bin', '/bin'], # Specify full path to binaries
  refreshonly => true,  # Only run when triggered by file change
}
