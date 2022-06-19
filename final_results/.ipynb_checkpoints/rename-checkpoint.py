import os 


folder = 'business_cards/images/test/'
for count, filename in enumerate(os.listdir(folder)):
	name = f"000{str(count)}.jpg"
	src = f'{folder}/{filename}'
	dst = f'{folder}/{name}'

	os.rename(src,dst)

