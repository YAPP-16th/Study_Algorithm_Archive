import Foundation
var input = readLine()!

var arr: [Character] = []

var level = 0
var result = 0

var cutFlag = false
for c in input{
    if c == Character("("){
        level += 1
        cutFlag = true
    }else{
        level -= 1
        if cutFlag{
            cutFlag = false
            result += level
        }else{
            result += 1
        }
    }
}

print(result)
