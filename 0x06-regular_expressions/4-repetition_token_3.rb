#!/usr/bin/env ruby

# Print all occurrences of the pattern "hbt*n" in the command-line argument
puts ARGV[0].scan(/hbt*n/).join
