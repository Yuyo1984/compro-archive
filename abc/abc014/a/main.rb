a = gets.to_i
b = gets.to_i

x = a % b
ans = 0
ans = b - x if x != 0

puts ans
