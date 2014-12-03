require 'rotp'

totp = ROTP::TOTP.new("R3A7PZLCUQIJFUGX")
puts totp.now
