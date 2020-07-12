def  Min_Coin_Changes_DP(coins, value):
	if value == 0:
		return 0
	
	dp = [float('inf') for i in range(value+1)]
	dp[0] = 0	# for 0 as target we dont need any coin

	# iterate for all value 1 to value and obtain answers to them all
	for sub_value in range(1,value+1):
		for Current_Coin in coins:
			if Current_Coin <= sub_value:
				if dp[sub_value - Current_Coin] + 1 < dp[sub_value]:
					dp[sub_value] = dp[sub_value - Current_Coin] + 1
	return dp[-1]

if __name__ == "__main__":
	coins = [1, 5, 6, 9]
	value = 8
	print( Min_Coin_Changes_DP(coins, value) )
