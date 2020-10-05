import applemusicpy

#for privacy not including keys
secret_key = 'x'
key_id = 'y'
team_id = 'z'

am = applemusicpy.AppleMusic(secret_key=secret_key, key_id=key_id, team_id=team_id)

def pl_fetch():
	pl_list = [] #user must specify playlists they want to migrate
	return_list = am.playlists(pl_list)
	return return_list

def song_fetch():
	playlists = pl_fetch()
	song_list = []
	
		song_list.append(x)

	return song_list





results = am.search('travis scott', types=['albums'], limit=5)
for item in results['results']['albums']['data']:
    print(item['attributes']['name'])