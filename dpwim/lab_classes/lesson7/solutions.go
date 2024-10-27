// From https://tour.golang.org/methods/23
package main

import (
	"errors"
	"io"
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

/*Write a function count_change that given a list of coin denominations
d and an amount of money n, returns in how many ways we can make the change.*/

func countChange(d []int, n int) int {
	if n == 0 {
		return 1
	}
	if n < 0 || len(d) == 0 {
		return 0
	}
	return countChange(d[1:], n) + countChange(d, n-d[0])
}

/* A leftist heap is a variant of a binary heap, where every node x has
an s-value which is the distance to the nearest leaf in subtree
rooted at x. In contrast to a binary heap, a leftist tree can be
unbalanced. In addition to the heap property, leftist trees are
maintained so the right descendant of each node has the lower
s-value. Implement a leftist heap by completing the following
draft implementation*/

type Heap interface {
	Insert(int) Heap
	Merge(Heap) Heap
	GetMax() (int, error)
	DeleteMax() (Heap, error)
	GetRank() int
}

type leaf struct{}

type node struct {
	data  int
	left  Heap
	right Heap
	rank  int
}

func Empty() Heap {
	return &leaf{}
}

func Singleton(n int) Heap {
	return &node{data: n, left: Empty(), right: Empty(), rank: 0} // rank of a single node is 0
}

func (l *leaf) Insert(n int) Heap {
	return Singleton(n)
}

func (n *node) Insert(value int) Heap {
	return n.Merge(Singleton(value))
}

func (l *leaf) Merge(other Heap) Heap {
	return other
}

func (n *node) Merge(other Heap) Heap {
	switch o := other.(type) {
	case *leaf:
		return n
	case *node:
		// Ensure the larger element is at the root
		if n.data < o.data {
			return o.Merge(n)
		}
		// Merge the right subtree with the other heap
		newRight := n.right.Merge(o)
		// Ensure leftist property by keeping the rank of the left child >= right child
		if rank(newRight) > rank(n.left) {
			return &node{data: n.data, left: newRight, right: n.left, rank: rank(n.left) + 1}
		}
		return &node{data: n.data, left: n.left, right: newRight, rank: rank(newRight) + 1}
	}
	return n
}

func (l *leaf) GetMax() (int, error) {
	return 0, errors.New("heap is empty")
}

func (n *node) GetMax() (int, error) {
	return n.data, nil
}

func (l *leaf) DeleteMax() (Heap, error) {
	return nil, errors.New("heap is empty")
}

func (n *node) DeleteMax() (Heap, error) {
	// Merge left and right subtrees to maintain the heap property
	return n.left.Merge(n.right), nil
}

func (l *leaf) GetRank() int {
	return -1 // rank of an empty heap (leaf) is -1
}

func (n *node) GetRank() int {
	return n.rank
}

func rank(h Heap) int {
	if h == nil {
		return -1 // nil heap should have rank -1
	}
	return h.GetRank()
}
