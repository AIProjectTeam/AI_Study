package main

func main() {
	a := []byte{'1', '2', '3', '4'}
	var x int
	for i := 0; i < len(a); {
		x, i = next(a, i)
		println(x)
	}
}

func next(b []byte, i int) (num int, next int) {
	x := 0
	for ; i < len(b); i++ {
		x = x*10 + int(b[i]) - '0'
	}
	return x, i
}