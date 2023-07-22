for i in range(5):
	st = speedtest.Speedtest()
	dowload_speed = round(st.download()/1000000,2)
	list_download_speed.append(download_speed)
	plt.plot(x, list_download_speed, label = "Download speed")
	plt.legend()