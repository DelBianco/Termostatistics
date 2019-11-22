set terminal pngcairo enhanced

set output "hist.png"
set style line 12 lc rgb '#808080' lt 0 lw 1
set grid back ls 12

set style line 1 lc rgb '#778b1a0e' pt 6 ps 2 lt 2 lw 2 # --- red
set style line 2 lc rgb '#775e9c36' pt 6 ps 2 lt 2 lw 2 # --- green
set style line 3 lc rgb '#77A9BDE6' pt 6 ps 2 lt 2 lw 2 # --- blue
set style line 4 lc rgb '#77F9C96D' pt 6 ps 2 lt 2 lw 2 # --- brown
set style line 5 lc rgb '#77c3c3c3' pt 6 ps 2 lt 2 lw 2 # --- gray
set style line 6 lc rgb '#77E47833' pt 6 ps 4 lt 1 lw 2 # --- orange

set style fill transparent solid 0.65

set xlabel 'Steps'
set ylabel 'Position'

plot 'histogram.dat' with points ls 2 title 'RandomWalk Distribution'
