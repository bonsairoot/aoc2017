main :: IO()
main = do
        contents <- readFile "aoc2_input.txt"
        let numberlines = map (map (read::String->Int) . words) $ lines contents
        print $ sum $ map sumMinMax numberlines
        print $ sum $ map realDivisors numberlines

sumMinMax :: [Int] -> Int
sumMinMax numbers = maximum numbers - minimum numbers

realDivisors :: [Int] -> Int
realDivisors (current:line) = if res > 0 then res else realDivisors line
                              where res = sum $ map (divNoRemainder current) line
realDivisors _        = 0 -- Not really necessary since each line has real divisors

divNoRemainder :: Int -> Int -> Int
divNoRemainder x y
    | x `rem` y == 0 = quot x y
    | y `rem` x == 0 = quot y x
    | otherwise      = 0
