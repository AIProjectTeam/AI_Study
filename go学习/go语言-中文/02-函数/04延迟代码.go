package main

func main() {
	defer func (a, b int) {
		println(a + b)
	}(3, 5)
	for i := 0; i < 5; i ++ {
		// 1. 延迟的函数是按照后进先出(LIFO)的顺序执行，所以下面的代码打印:4 3 2 1 0。
		defer println(i)
	}
	println("hello")
	println(func1())
}

func func1() (ret int) {
	// 2. 利用 defer 甚至可以修改返回值
	defer func () {
		ret ++
	}()
	return 5
}