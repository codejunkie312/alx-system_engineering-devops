# Install the Flask Python package using pip3
package { 'python3-pip':
  ensure => installed,  # Ensure pip3 is installed
}

package { 'flask':
  ensure   => '2.1.0',  # Specify the version to install
  provider => pip3,     # Use pip3 as the provider
  require  => Package['python3-pip'],  # Ensure pip3 is installed first
}
