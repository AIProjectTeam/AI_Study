package main
import (
	"fmt"
)
func main() {
	controlStructure()
}
// 变量类型
func varDefine () {
	const (
		a = iota
		b
	)
	s := "hello world!"
	c := []byte(s)
	c[0] = 'c'
	s2 := string(c)
	s3 := `Starting part
Ending part`
	var c1 complex128 = 5 + 5i
	var e error;
	fmt.Println(e)
	fmt.Println(c1)
	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(s)
	fmt.Println(c)
	fmt.Println(s2)
	fmt.Println(s3)
}
// 控制接口
func controlStructure () {
	if 3>4 {
		fmt.Println("3>4")
	} else {
		fmt.Println("3<=4")
	}
	if err := file.Chmod(0664); err != nil {
		log.Stderr(err)
		return err
		fmt.Println(err)
	}
}