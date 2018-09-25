package main

import (
	"fmt"
)

func main() {
	var slice = make([]int, 10)
	fmt.Println(slice)
	fmt.Println(myFunc(1,2))
}
// 1. arg ... int 告诉 Go 这个函数接受不定数量的参数(注意，这些参数的类型全部 是 int。在函数体中，变量arg 是一个 int 类型的 slice)
func myFunc (arg ...int) []int {
	return arg
}