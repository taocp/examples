#!/bin/bash
input_filename=base.data
output_filename=datafile.jpg
gnuplot -e "input_filename='${input_filename}';output_filename='${output_filename}'" datafile.gpi
