package main

func main() {
	foreach([]int{1,2,3,4,5}, func (item, index int) {
		println(item)
	})
}
func foreach (arr []int, callback func(item, index int)) {
	for index, item := range arr {
		callback(item, index)
	} 
	
}