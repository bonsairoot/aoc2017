#!/usr/bin/perl

use strict;
use warnings;

my $filename = 'aoc4_input.txt';
my ($valid_pws_p1, $valid_pws_p2) = (0, 0);

open(my $fh, '<', $filename) or die "Couldn't open file $filename!";

while (my $row = <$fh>){
    chomp $row;
    my %encountered = ();
    my $is_valid = 1;
    my $has_clone = 0;
    my %anagrams = ();
    for my $word (split / /, $row){
        my $key = join '', sort(split(//, lc($word)));
        push @{$anagrams{$key}}, $word;
        if($encountered{$word}){
            $has_clone = 0;
        }
        $encountered{$word} = 1;
    }
    my $b = 0;
    foreach my $lst (values %anagrams){
        if (1 < @$lst) {
            $is_valid = 0;
        }
    }
    $valid_pws_p2++ if $is_valid;
    $valid_pws_p1++ if !$has_clone;
}

print "Part I: $valid_pws_p1\nPart II: $valid_pws_p2\n";
