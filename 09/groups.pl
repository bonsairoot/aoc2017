#!/usr/bin/perl
use strict;
use warnings;

open(my $fh, '<', "aoc9_input.txt") or die "Couldn't open file!";
my $stream = <$fh>;

$stream =~ s/!!//g; # Removes selfignores
$stream =~ s/![^>]//g; # Remove irrelevant ignores
my @garbage = $stream =~ /<.*?(?<!!)>/g;
$stream =~ s/<.*?(?<!!)>//g; # Remove garbage

my $groups = 0;
my $depth = 0;
for my $c (split //, $stream) {
    if ($c eq '{') {
        $depth++;
    }
    elsif ($c eq '}') {
        $groups += $depth;
        $depth --;
    }
}

my $garbage_size = 0;
for my $g (@garbage) {
    $g =~ s/!>//g;
    $garbage_size += length($g) - 2;
}

print "Part I:  $groups\n";
print "Part II: $garbage_size\n";
