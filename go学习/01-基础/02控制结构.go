package main
import (
	"fmt"
)
func main() {
	var a int = 13
	if a == 12 { // 条件语句
		fmt.Println("ss")
	} else {
		fmt.Println("ee")
	}
	for i := 0; i < 10; i++ { // 循环语句
		if i == 5 {
			break
		}
		fmt.Println(i)
	}
	// goto的使用
	useGoto()
	// for循环的三种用法
	useFor()
	// range的使用
	useRange()
	// switch的使用
	useSwitch()
}

func useGoto () {
	i := 0
	Here:
	fmt.Println(i)
	i++
	if (i < 50) {
		goto Here
	}
}
// for循环的三种用法
func useFor () {
	// 用法一：常规用法
	for i := 0; i < 10; i ++ { //  和 C 的 for 一样
		fmt.Println("index: ", i)
	}
	// 用法二：死循环
	index := 1
	for { // 和C 的for(;;) 一样
		index ++
		if index > 100 {
			break
		}
		fmt.Println("index: ", index)
	}
	// 用法三：条件循环
	loc := 0
	for loc < 11 { // 和 while 一样 
		fmt.Println("loc: ", loc)
		loc ++
	}
}
// range的使用
func useRange () {
	list := []string{"a", "b", "c", "d", "e", "f", "g"}
	for key, value := range list {
		fmt.Println(key, ":", value)
	}
	for pos, char := range "hello world!" {
		fmt.Printf("%d: %c\n", pos, char)
	}
}
// switch的使用
func useSwitch () {
	// 用法一：常规
	for i := 0; i< 20; i ++ {
		switch i {
		case 1:
			fmt.Println("first")
		case 2:
			fmt.Println("second")
		case 3:
			fmt.Println("third")
		default:
			fmt.Println("unknow")
		}
	}
	// 用法二：if-else-if-else
	str := "f843de"
	for pos, char := range str {
		fmt.Println(pos, ": ", unhex(byte(char)))
	}
	// 用法三：case多项
	str1 := "hello, 世界"
	for pos, char := range str1 {
		switch char {
		case 'h', 'e', 'l', 'o', ',', ' ':
			fmt.Println(pos, "ASCII: true")
		default:
			fmt.Println(pos, "ASCII: false")
		}
	}
}

func unhex (c byte) byte{
	switch {
	case c >= '0' && c <= '9':
		return c - '0'
	case c >= 'a' && c <= 'f':
		return c - 'a' + 10
	case c >= 'A' && c <= 'F':
		return c - 'A' + 10
	}
	return 0
}