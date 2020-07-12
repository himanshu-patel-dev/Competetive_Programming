def  Min_Coin_Changes_recursive(coins, value):
	if value == 0:
		return 0

	result = float('inf')
	for coin in coins:
		if coin <= value:
			temp = Min_Coin_Changes_recursive( coins, value-coin )
			result = min( result, temp+1 )

	return result

if __name__ == "__main__":
	coins = [1, 5, 6, 9]
	value = 7
	print( Min_Coin_Changes_recursive(coins, value) )
