#!/bin/bash

#Space
printf "\ ";
convert -background black -fill white -font ubuntu-mono -resize 4x9\! label:"\ " ./CharacterImages/32.bmp;

#Other characters
for ((i=33;i<92;i++))
do
	printf "\\$(printf %03o "$i")";
	convert -background black -fill white -font ubuntu-mono -resize 4x9\! label:"$(printf "\\$(printf %03o "$i")")" ./CharacterImages/$i.bmp;
	
done;

#Backslash
printf "\\";
convert -background black -fill white -font ubuntu-mono -resize 4x9\! label:$(printf "\\";printf "\\") ./CharacterImages/92.bmp;


#Other characters
for ((i=93;i<127;i++))
do
	printf "\\$(printf %03o "$i")";
	convert -background black -fill white -font ubuntu-mono -resize 4x9\! label:"$(printf "\\$(printf %03o "$i")")" ./CharacterImages/$i.bmp;

done;

for ((i=161;i<254;i++))
do
	printf "\\$(printf %03o "$i")";
	convert -background black -fill white -font ubuntu-mono -resize 4x9\! label:"$(printf "\\$(printf %03o "$i")")" ./CharacterImages/$i.bmp;
 
done;
printf "\n";