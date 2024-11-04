package main

// Write a program that takes a URL of a web page as parameter, downloads the requested page
// and extracts all URLs it links.
// Hint: You may have a look at this page and this page to learn about regular expressions in Go.

import (
	"bufio"
	"fmt"
	"net/http"
	"os"
	"regexp"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter the URL: ")
	url, _ := reader.ReadString('\n')
	url = strings.TrimSpace(url)

	resp, err := http.Get(url)
	if err != nil {
		fmt.Println("Error: ", err)
		os.Exit(1)
	}
	defer resp.Body.Close()

	re := regexp.MustCompile(`href="(http[^"]+)`)

	buf := make([]byte, 1024)
	for {
		n, err := resp.Body.Read(buf)
		if n == 0 || err != nil {
			break
		}
		matches := re.FindAllStringSubmatch(string(buf), -1)
		for _, match := range matches {
			fmt.Println(match[1])
		}
	}
}
