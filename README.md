# Chapter Search

## Applying deep learning to find the right chapter for a given problem

### Flow

Input: a physics question
Output: relative chapter # of the given question

question (input) -> datasets of strings -> deep learning -> chapter # (output)

### Deep Learning Flow

Training dataset: context of the physics PDF
Test set: random physics question

physics context PDF -> dataset of strings (label word by chapter #, count # in chapter)

Figuring out special keywords of the chapter (remove words that show up in other chapters)

Give points based on how many times same word showed up in one chapter.

Increase accuracy by using deep learning to figure out best points to give based on # of occurrence.

## What should be done

1. a
2. b
3. c
4. d
5. e


## Source:
Fundamentals of Physics Extended, Jearl Walker, 10th edition
