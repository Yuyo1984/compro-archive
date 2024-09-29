N = gets.to_i

ans = 0

for i in 1..N do
  x = 10_000 * i
  ans += x
end

ans /= N

p ans
