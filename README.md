# Hybrid Quick Sort Implementation

This project implements a hybrid sorting algorithm based on Quick Sort (qsort).  
To improve performance, the algorithm switches to Insertion Sort for small subarrays (size < 10).

## Description

Quick Sort is an efficient divide-and-conquer sorting algorithm. However, for very small subarrays, the overhead of recursion can reduce performance.  

To optimize this, this implementation:
- Uses Quick Sort for large partitions
- Switches to Insertion Sort when the subarray size is less than 10

This approach improves overall efficiency by reducing recursion overhead at lower levels.

## Features

- Custom implementation of Quick Sort (no standard library sorting functions used)
- Hybrid approach combining Quick Sort and Insertion Sort
- Optimized for better performance on small subarrays

## Algorithm Overview

1. Select a pivot element
2. Partition the array into elements less than and greater than the pivot
3. Recursively apply Quick Sort to subarrays
4. When subarray size < 10, apply Insertion Sort instead



## Purpose

This project was created to:
- Understand and implement sorting algorithms from scratch
- Explore performance optimizations in recursive algorithms
- Strengthen knowledge of algorithm design and complexity

## Notes

- No standard library sorting functions were used
- Focus is on algorithmic efficiency and clean implementation 
