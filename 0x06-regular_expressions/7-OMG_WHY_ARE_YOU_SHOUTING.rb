#!/usr/bin/env ruby

# Print all occurrences of the pattern "[A-Z]*" in the command-line argument
puts ARGV[0].scan(/[A-Z]*/).join
