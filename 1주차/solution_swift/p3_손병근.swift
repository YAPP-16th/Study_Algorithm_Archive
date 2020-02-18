var input = Int(readLine()!)!
var temp = 100000000
var temp2 = 9
var result = 0
while temp > 0 {
    if input / temp > 0{
        result += (input - temp + 1) * temp2
        temp /= 10
        temp2 -= 1
        break
    }else{
        temp /= 10
        temp2 -= 1
    }
}

while temp > 0 {
    result += (temp * 9) * temp2
    temp /= 10
    temp2 -= 1
}
print(result)
