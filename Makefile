coffee.png: create_coffee.py
	python create_coffee.py
noise_coffee.png: add_noise.py coffee.png
	python add_noise.py --input coffee.png --output noise_coffee.png
noise_reduced_coffee.png: noise_coffee.png reduce_noise.py
	python reduce_noise.py --input noise_coffee.png --output noise_reduced_coffee.png
result.txt: noise_coffee.png noise_reduced_coffee.png
	python compare.py --true coffee.png --noise noise_coffee.png --reduced noise_reduced_coffee.png > result.txt
