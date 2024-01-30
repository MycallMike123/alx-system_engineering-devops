#!/usr/bin/env ruby

# Extract content between 'from:' and ']'
from = ARGV[0].scan(/from:(.*?)\]/)

# Extract content between 'to:' and ']'
to = ARGV[0].scan(/to:(.*?)\]/)

# Extract content between 'flags:' and ']'
flags = ARGV[0].scan(/flags:(.*?)\]/)

# Print the extracted information, joining them with commas
puts [from, to, flags].join(',')
