package main

import (
	"testing"
	"time"

	"github.com/stretchr/testify/assert"
)

func TestHumanDate(t *testing.T) {
	tests := []struct {
		name string
		tm   time.Time
		want string
	}{
		{
			name: "UTC",
			tm:   time.Date(2024, 12, 14, 21, 45, 0, 0, time.UTC),
			want: "14 Dec 2024 at 21:45",
		},
		{
			name: "Empty",
			tm:   time.Time{},
			want: "",
		},
		{
			name: "CET",
			tm:   time.Date(2024, 12, 14, 21, 45, 0, 0, time.FixedZone("CET", 60*60)),
			want: "14 Dec 2024 at 20:45",
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			hd := humanDate(tt.tm)
			assert.Equal(t, tt.want, hd)
		})
	}
}
