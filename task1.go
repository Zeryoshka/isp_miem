package main

import (
	"fmt"
)

func is_all_zeros_with_odd_index(arr []int) bool {
	for i, value := range arr {
		if value == 0 && i%2 == 0 {
			return false
		}
	}
	return true
}

func main() {
	arr := []int{1, 2, 3, 4}
	if is_all_zeros_with_odd_index(arr) {
		fmt.Printf("Max of array: %d", intslice.max(arr))
	}

}
