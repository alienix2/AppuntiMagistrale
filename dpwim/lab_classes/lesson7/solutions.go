// From https://tour.golang.org/methods/23
package main

import (
	"fmt"
	"io"
	"strings"
)

type rot13Reader struct {
	r io.Reader
}

func (r13Reader rot13Reader) Read(b []byte) (n int, err error) {
	n, err = r13Reader.r.Read(b)
	if err == nil {
		for i := 0; i < n; i++ {
			if b[i] >= 'A' && b[i] <= 'Z' {
				b[i] = (b[i]-'A'+13)%26 + 'A'
			} else if b[i] >= 'a' && b[i] <= 'z' {
				b[i] = (b[i]-'a'+13)%26 + 'a'
			}
		}
	}
	return
}

func main() {
	s := strings.NewReader("Lbh penpxrq gur pbqr!")
	r := rot13Reader{s}
	decoded := make([]byte, 100)
	r.Read(decoded)

	fmt.Println(string(decoded))
}
