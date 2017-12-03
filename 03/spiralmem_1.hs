main :: IO()
main = do
        let input = 265149
            ring = calcRing input
            offset = calcOffset input ring
            steps = manhattan ring offset
        print steps

calcRing :: Int -> Int
calcRing input = length (takeWhile (\x -> squaresPerRing x < input) [1..])

calcOffset :: Int -> Int -> Int
calcOffset input ring = input - squaresPerRing ring

squaresPerRing :: Int -> Int
squaresPerRing n = 4 * n^2 - 4 * n + 1

manhattan :: Int -> Int -> Int
manhattan ringOff squareOff = abs (sideOff - ringOff) + ringOff
                                where sideOff = squareOff `rem` (2*ringOff)
