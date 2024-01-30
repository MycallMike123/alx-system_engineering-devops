#!/usr/bin/env ruby

# Print all occurrences of the pattern "^\d{10}$" in the command-line argument
puts ARGV[0].scan(/^\d{10}$/).join
