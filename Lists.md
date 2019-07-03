# Lists

## What are lists?

An list is an ordered sequence of elements stored in a single variable.

- "ordered" means that each time we examine the list, the elements will always be in the same order.
- "ordered" does not mean that there is a special meaning to that order (such as "alphabetical").

Code.

    mycolors = ["red", "purple", "green", "blue"]

Each time we run through this list, the order will always be "red", "purple", "green", then "blue". There are four elements in this list.

## How do we index into an element of an list?

We index into an element of the list using square braces and a number. The first element index is always 0. Here's how we get the first element in the list.

    mycolors[0] # This is "red"
    mycolors[1] # This is "purple"
    mycolors[2] # This is "green"
    mycolors[3] # This is "blue"
    mycolors[4] # This is an error

The last element in a list is always the number of elements in the list minus one.

## How do we loop over all of the elements in an list?

We loop over all of the elements in a list using a **for** loop. The syntax is always **for** variable **in** list (followed by a colon).

    for color in mycolors:
        print(color)

This will print, in order: "red", "purple", "green", "blue".

## How do we find the largest element in the list?

First, we make the assumption that the first element is the largest. This assumption is often wrong, but it is sometimes right. We can correct the wrong assumptions. What is the index of the first element?

Second, we loop over all of the elements in a list to find a larger element. Each time we do, we change our assumption.

Finally and only after we have evaluated all elements, we can conclude that our last assumption is correct.

Example. Here is a list of numbers. What is the largest?

    mynumbers = [70, 90, 67, 38, 88, 66, 78, 95, 19, 81]

First, we assume the first element is the largest. Remember: this is often wrong. 70 is not the largest element in the list, but we say it is temporarily.

    largest = mynumbers[0]

Second, we loop over all of the elements in an attempt to find the largest element, correcting our assumptions along the way.

    for number in mynumbers:
        if number > largest:
            largest = number

Finally, we conclude that the latest assumption is correct.

    print("The largest number is", largest) # This should print that 95 is the largest.
