#!/bin/bash
expr $(grep "(" input.txt --only-matching | wc -l) - $(grep ")" input.txt --only-matching | wc -l)
