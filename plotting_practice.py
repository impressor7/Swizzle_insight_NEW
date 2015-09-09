import matplotlib.pyplot as plt

x = [0,1,2,3,4,5,6,7,8,9,10,11]
y = [1,2,3,4,5,6,7,8,9,10,11,12]
plt.plot (x,y)
plt.title('About Playlist Graph')
plt.xlabel('The number of song in a playlist')
plt.ylabel('The number of playlists')

plt.savefig('1.png')