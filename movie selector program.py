
import random

serious_movies=["Split", "Spiderman 2", "Coach Carter", "Shutter Island", "The social network", "Jimmy saville", "Get rich or die tryin'", "Nerve", "Get Out"]

fun_movies=["Man from Toronto", "White Chicks", "friday", "Office invasion", "Naked", "TMNT", "Superbad"]


movie_type=input("what type of movie would you like to watch: fun or serious? ")

if movie_type=="serious" :
    print(random.choice(serious_movies))
elif movie_type=="fun" :
    print(random.choice(fun_movies))
else :
    print("please input either 'fun' or 'serious'")

    

