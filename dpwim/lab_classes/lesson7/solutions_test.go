package main

import (
	"strings"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestRot13Reader(t *testing.T) {
	s := strings.NewReader("Lbh penpxrq gur pbqr!")
	r := rot13Reader{s}
	decoded := make([]byte, 100)
	r.Read(decoded)

	assert.Equal(t, "You cracked the code!", string(decoded))
}
