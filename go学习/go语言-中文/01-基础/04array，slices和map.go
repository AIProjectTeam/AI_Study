package main

import (
	"fmt"
)

func main() {
	// array（数组）使用
	useArray()
	// slice 使用
	useSlice()
	// map 使用
	useMap()
}
// array（数组）使用: array是值类型
func useArray () {
	var arr [10]int
	arr[0] = 42
	arr[1] = 13
	arr1 := arr
	arr1[2] = 33
	fmt.Println(arr)
	fmt.Println(arr1)
	arr2 := [...]int{1,2,3,4,5,6,7,8,9}
	fmt.Println(arr2)
	arr3 := [...][2]int{ [...]int{1,2}, [...]int{3,4} }
	fmt.Println(arr3)
}
// slice 使用：slice是指向数组的指针，是引用类型
func useSlice () {
	// 1. make
	slice := make([]int, 10)
	fmt.Println(slice)
	// 2. array[m:n]
	a := []int{1, 2, 3, 4, 5}
	s1 := a[2:4]
	s2 := a[1:5]
	s3 := a[:]
	s4 := a[:4]
	s5 := s2[:]
	fmt.Println(s1,s2,s3,s4,s5)
	// 3. append(slice, item1, item2, ....)
	sl := []int{0, 0}
	sl1 := append(sl, 2)
	sl2 := append(sl, 3, 5, 7)
	sl3	:= append(sl2, sl...)
	fmt.Println(sl1, len(sl1), cap(sl1))
	fmt.Println(sl2)
	fmt.Println(sl3)
	// 4. copy(distSlice, srcSlice)
	b := []int{0, 1, 2, 3, 4, 5, 6, 7}
	var ss = make([]int, 6)
	n1 := copy(ss, b[:])
	fmt.Println(ss, n1)
	n2 := copy(ss, ss[2:])
	fmt.Println(ss, n2)
}
// map 使用
func useMap () {
	// 1. map赋值
	monthDays := map[string]int{
		"Jan": 31,
		"Feb": 28,
		"Mar": 31,
		"Apr": 30,
		"May": 31,
		"Jun": 30,
		"Jul": 31,
		"Aug": 31,
		"Sep": 30,
		"Oct": 31,
		"Nov": 30,
		"Dec": 31,
	}
	fmt.Println(monthDays)
	// 2. map增加元素
	monthDays["undecim"] = 30
	fmt.Println(monthDays)
	// 3. map修改元素
	monthDays["Feb"] = 29
	fmt.Println(monthDays)
	// 4. map删除元素
	delete(monthDays, "May")
	fmt.Println(monthDays)
	// 5. map查找元素
	v, ok := monthDays["May"]
	fmt.Println(v, ok)
	v1, ok1 := monthDays["Feb"]
	fmt.Println(v1, ok1)
	// 6. map遍历元素
	for key, value := range monthDays {
		fmt.Println(key, value)
	}
}