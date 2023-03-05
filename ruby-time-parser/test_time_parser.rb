require_relative 'time_parser'
require 'test/unit'

class TestTimeParser < Test::Unit::TestCase
  def priority_setup
    @sut = TimeParser.new()
  end

  def test_time_with_hour_only
    @sut.parse_time("4")

    assert_equal(4, @sut.hour)
    assert_equal(0, @sut.minute)
    assert_equal("am", @sut.midday)
  end

  def test_time_with_hour_and_minute_only
    @sut.parse_time("23:42")

    assert_equal(23, @sut.hour)
    assert_equal(42, @sut.minute)
    assert_equal("am", @sut.midday)
  end

  def test_time_with_hour_minute_and_midday
    @sut.parse_time("7:38pm")

    assert_equal(7, @sut.hour)
    assert_equal(38, @sut.minute)
    assert_equal("pm", @sut.midday)
  end
end
