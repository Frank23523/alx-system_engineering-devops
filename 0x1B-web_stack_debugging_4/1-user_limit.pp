# Ensure the security limits configuration file has appropriate file limits for the holberton user

# hard file
exec { 'increase-hard-file-limit-for-holberton-user':
  command => "sed -i '/^holberton hard/s/5/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}

# soft file
exec { 'increase-soft-file-limit-for-holberton-user':
  command => "sed -i '/^holberton soft/s/4/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}
