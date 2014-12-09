require 'rotp'

totp = ROTP::TOTP.new("R3A7PZLCUQIJFUGX", interval: 90)

puts totp.now
