
class TimeParser
  attr_reader :hour
  attr_reader :minute
  attr_reader :midday

  def initialize()
    @hour = 0
    @minute = 0
    @midday = "am"
  end

  def parse_time(time_input)
    case time_input
    when /^(\d|\d\d)$/
      @hour = $1.to_i
    when /^(\d|\d\d)[:](\d\d)$/
      @hour = $1.to_i
      @minute = $2.to_i
    when /^(\d|\d\d)[:](\d\d)(am|pm)$/
      @hour = $1.to_i
      @minute = $2.to_i
      @midday = $3
    end
  end
end

def main
  input = ARGV.first unless ARGV.first.nil?

  parser = TimeParser.new
  parser.parse_time input
end

if __FILE__ == $0
  main
end