"""
I/O tests:

Test case 1:
Points: 5

Input:
chess-top-100.csv

Output:
Enter filename: Players by country:
-------------------
ARG (1) (2653.0):
                           Sandro Mareco      2653
ARM (3) (2710.3):
                           Levon Aronian      2780
                      Gabriel Sargissian      2691
                         Hrant Melkumyan      2660
AUT (1) (2690.0):
                           Markus Ragger      2690
AZE (6) (2722.3):
                   Shakhriyar Mamedyarov      2820
                        Teimour Radjabov      2751
                       Arkadij Naiditsch      2721
                            Rauf Mamedov      2699
                           Eltaj Safarli      2676
                          Gadir Guseinov      2667
BLR (1) (2664.0):
                       Vladislav Kovalev      2664
CHN (9) (2718.7):
                              Liren Ding      2804
                               Yangyi Yu      2765
                                  Yi Wei      2742
                                Hao Wang      2722
                             Xiangzhi Bu      2712
                               Chao b Li      2708
                                Yue Wang      2681
                                  Hua Ni      2676
                               Yifan Hou      2658
CRO (1) (2687.0):
                              Ivan Saric      2687
CUB (1) (2653.0):
                   Lazaro Bruzon Batista      2653
CZE (2) (2702.0):
                            David Navara      2740
                         Viktor Laznicka      2664
EGY (1) (2686.0):
                             Bassem Amin      2686
ENG (5) (2688.6):
                           Michael Adams      2712
                        Matthew D Sadler      2693
                        David W L Howell      2689
                        Gawain C B Jones      2677
                          Luke J McShane      2672
ESP (1) (2713.0):
                  Francisco Vallejo Pons      2713
FID (1) (2740.0):
                         Veselin Topalov      2740
FRA (2) (2729.0):
                  Maxime Vachier-Lagrave      2780
                          Etienne Bacrot      2678
GEO (1) (2715.0):
                         Ivan Cheparinov      2715
GER (1) (2667.0):
                  Liviu-Dieter Nisipeanu      2667
HUN (4) (2695.8):
                         Richard Rapport      2725
                           Zoltan Almasi      2702
                              Peter Leko      2690
                           Ferenc Berkes      2666
IND (6) (2704.7):
                       Viswanathan Anand      2771
                     Pentala Harikrishna      2733
                  Santosh Gujrathi Vidit      2711
                         S.P. Sethuraman      2673
                      Krishnan Sasikiran      2672
                              B. Adhiban      2668
IRI (1) (2685.0):
                      Parham Maghsoodloo      2685
ISR (3) (2689.0):
                           Boris Gelfand      2701
                            Tamir Nabaty      2692
                         Maxim Rodshtein      2674
NED (2) (2719.0):
                              Anish Giri      2780
                        Robin Van Kampen      2658
NOR (2) (2750.5):
                          Magnus Carlsen      2839
                       Jon Ludvig Hammer      2662
PER (1) (2664.0):
                              Jorge Cori      2664
POL (3) (2707.3):
                      Jan-Krzysztof Duda      2739
                      Radoslaw Wojtaszek      2727
                         Dariusz Swiercz      2656
RUS (21) (2706.4):
                        Vladimir Kramnik      2779
                      Alexander Grischuk      2769
                         Sergey Karjakin      2760
                      Ian Nepomniachtchi      2759
                           Peter Svidler      2756
                        Dmitry Jakovenko      2752
                        Dmitry Andreikin      2723
                       Vladimir Fedoseev      2713
                         Nikita Vitiugov      2709
                      Vladislav Artemiev      2706
                      Evgeny Tomashevsky      2705
                            Daniil Dubov      2703
                        Ernesto Inarkiev      2691
                          Maxim Matlakov      2683
                         Anton Demchenko      2679
                           Evgeniy Najer      2663
                       Vladimir Malakhov      2661
                       Alexander Motylev      2661
                    Alexander Morozevich      2656
                          Sanan Sjugirov      2654
                        Sergei Rublevsky      2652
SLO (1) (2656.0):
                              Luka Lenic      2656
SWE (1) (2655.0):
                         Nils Grandelius      2655
UAE (1) (2660.0):
                        A.R. Saleh Salem      2660
UKR (8) (2680.8):
                        Vassily Ivanchuk      2710
                           Pavel Eljanov      2703
                       Yuriy Kryvoruchko      2697
                           Anton Korobov      2694
                       Ruslan Ponomariov      2681
                           Yuriy Kuzubov      2655
                         Martyn Kravtsiv      2654
                   Alexander Areshchenko      2652
USA (7) (2727.4):
                         Fabiano Caruana      2827
                               Wesley So      2776
                         Hikaru Nakamura      2763
                        Samuel Shankland      2722
                              Ray Robson      2682
                             Gata Kamsky      2666
                           Jeffery Xiong      2656
UZB (1) (2662.0):
                     Rustam Kasimdzhanov      2662
VIE (1) (2715.0):
                           Quang Liem Le      2715

Players by birth year:
----------------------
1968 (1) (2701.0):
                           Boris Gelfand      2701
1969 (2) (2740.5):
                       Viswanathan Anand      2771
                        Vassily Ivanchuk      2710
1971 (1) (2712.0):
                           Michael Adams      2712
1974 (3) (2670.3):
                        Matthew D Sadler      2693
                             Gata Kamsky      2666
                        Sergei Rublevsky      2652
1975 (2) (2759.5):
                        Vladimir Kramnik      2779
                         Veselin Topalov      2740
1976 (3) (2708.3):
                           Peter Svidler      2756
                           Zoltan Almasi      2702
                  Liviu-Dieter Nisipeanu      2667
1977 (2) (2659.5):
                           Evgeniy Najer      2663
                    Alexander Morozevich      2656
1979 (3) (2671.0):
                              Peter Leko      2690
                     Rustam Kasimdzhanov      2662
                       Alexander Motylev      2661
1980 (1) (2661.0):
                       Vladimir Malakhov      2661
1981 (1) (2672.0):
                      Krishnan Sasikiran      2672
1982 (3) (2715.3):
                           Levon Aronian      2780
                  Francisco Vallejo Pons      2713
                   Lazaro Bruzon Batista      2653
1983 (7) (2707.1):
                      Alexander Grischuk      2769
                        Dmitry Jakovenko      2752
                           Pavel Eljanov      2703
                      Gabriel Sargissian      2691
                       Ruslan Ponomariov      2681
                          Etienne Bacrot      2678
                                  Hua Ni      2676
1984 (1) (2672.0):
                          Luke J McShane      2672
1985 (7) (2720.6):
                   Shakhriyar Mamedyarov      2820
                            David Navara      2740
                       Arkadij Naiditsch      2721
                             Xiangzhi Bu      2712
                           Anton Korobov      2694
                        Ernesto Inarkiev      2691
                           Ferenc Berkes      2666
1986 (5) (2692.8):
                     Pentala Harikrishna      2733
                         Ivan Cheparinov      2715
                       Yuriy Kryvoruchko      2697
                          Gadir Guseinov      2667
                   Alexander Areshchenko      2652
1987 (9) (2705.0):
                         Hikaru Nakamura      2763
                        Teimour Radjabov      2751
                      Radoslaw Wojtaszek      2727
                         Nikita Vitiugov      2709
                      Evgeny Tomashevsky      2705
                                Yue Wang      2681
                         Anton Demchenko      2679
                        Gawain C B Jones      2677
                           Sandro Mareco      2653
1988 (5) (2679.0):
                            Rauf Mamedov      2699
                           Markus Ragger      2690
                             Bassem Amin      2686
                         Viktor Laznicka      2664
                              Luka Lenic      2656
1989 (4) (2691.0):
                                Hao Wang      2722
                               Chao b Li      2708
                         Maxim Rodshtein      2674
                         Hrant Melkumyan      2660
1990 (10) (2720.8):
                          Magnus Carlsen      2839
                  Maxime Vachier-Lagrave      2780
                         Sergey Karjakin      2760
                      Ian Nepomniachtchi      2759
                        Dmitry Andreikin      2723
                        David W L Howell      2689
                              Ivan Saric      2687
                       Jon Ludvig Hammer      2662
                           Yuriy Kuzubov      2655
                         Martyn Kravtsiv      2654
1991 (4) (2703.0):
                        Samuel Shankland      2722
                           Quang Liem Le      2715
                            Tamir Nabaty      2692
                          Maxim Matlakov      2683
1992 (4) (2743.8):
                         Fabiano Caruana      2827
                              Liren Ding      2804
                           Eltaj Safarli      2676
                              B. Adhiban      2668
1993 (5) (2683.6):
                               Wesley So      2776
                         S.P. Sethuraman      2673
                        A.R. Saleh Salem      2660
                         Nils Grandelius      2655
                          Sanan Sjugirov      2654
1994 (8) (2696.8):
                              Anish Giri      2780
                               Yangyi Yu      2765
                  Santosh Gujrathi Vidit      2711
                              Ray Robson      2682
                       Vladislav Kovalev      2664
                               Yifan Hou      2658
                        Robin Van Kampen      2658
                         Dariusz Swiercz      2656
1995 (2) (2688.5):
                       Vladimir Fedoseev      2713
                              Jorge Cori      2664
1996 (2) (2714.0):
                         Richard Rapport      2725
                            Daniil Dubov      2703
1998 (2) (2722.5):
                      Jan-Krzysztof Duda      2739
                      Vladislav Artemiev      2706
1999 (1) (2742.0):
                                  Yi Wei      2742
2000 (2) (2670.5):
                      Parham Maghsoodloo      2685
                           Jeffery Xiong      2656
"""
