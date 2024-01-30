#!/usr/bin/env ruby

# Print all occurrences of the pattern "^h.n$" in the command-line argument
puts ARGV[0].scan(/^h.n$/).join
