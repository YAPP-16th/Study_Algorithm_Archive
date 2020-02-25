import Foundation
var input = readLine()!.split(separator: " ").map { Int($0)! }
var n = input[0]
var k = input[1]

var temp:[Int] = []
for i in 0..<n{
    temp.append(i + 1)
}

var result:[Int] = []
var currentIndex = 0
while !temp.isEmpty{
    currentIndex = (currentIndex + (k - 1)) % temp.count
    result.append(temp.remove(at: currentIndex))
}

var resultStr = "<\(result.removeFirst())"

for i in result{
    resultStr += ", \(i)"
}
resultStr += ">"
print(resultStr)
