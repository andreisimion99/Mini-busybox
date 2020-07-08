import os
import sys
import shutil

def foo():
	
			if len(sys.argv) > 1:
				com = sys.argv[1]
			else:
				print("Invalid command")
				return 256

			if com == 'pwd':
				print(os.getcwd())
				return 0

			try:
				if com == 'echo' and sys.argv[2] != '-n':
					s = ''
					i = 2
					while i < len(sys.argv):
						s = s + ' ' + sys.argv[i]
						i = i + 1
					s = s.strip()
					print(s)
					return 0
				elif com == 'echo' and sys.argv[2] == '-n' and len(sys.argv) > 3:
					s = ''
					i = 3
					while i < len(sys.argv):
						s = s + ' ' + sys.argv[i]
						i = i + 1
					s = s.strip()
					print(s, end="")
					return 0
			except Exception:
				print("246")
				return -10

			try:
				if com == 'cat' and len(sys.argv) > 2:
					i = 1
					while i <= len(sys.argv) - 2 :
						f = open(sys.argv[i+1], "r")
						content = f.read()
						print(content, end="")
						i = i + 1
					return 0
			except Exception:
				print("-20")
				return -20

			try:
				if com == 'mkdir':
					i = 1
					while i <= len(sys.argv) - 2:
						os.mkdir(sys.argv[i+1])
						i = i + 1
					return 0
			except Exception:
				print("226")
				return -30

			try:
				if com == 'mv':
					src = sys.argv[2]
					dst = sys.argv[3]
					shutil.move(src, dst)
					return 0
			except Exception:
				print("216")
				return -40

			try:
				if com == 'ln' and sys.argv[2] != '-s' and sys.argv[2] != '--symbolic':
					os.link(sys.argv[2], sys.argv[3])
					return 0
				elif com == 'ln' and (sys.argv[2] == '-s' or sys.argv[2] == '--symbolic'):
					os.symlink(sys.argv[3], sys.argv[4])
					return 0
			except Exception:
				print("206")
				return -50

			try:
				if com == 'rmdir':
					i = 1
					while i <= len(sys.argv) - 2:
						os.rmdir(sys.argv[i+1])
						i = i + 1
					return 0
			except Exception:
				print("196")
				return -60

			try:
				if com == 'rm' and sys.argv[2] != '-r' and sys.argv[2] != '-R' and sys.argv[2] != '--recursive' and sys.argv[2] != '-d' and sys.argv[2] != '--dir':
					i = 1
					ok = True
					while i <= len(sys.argv) - 2:
						if os.path.isfile(sys.argv[i+1]) == True:
							os.remove(sys.argv[i+1])
							i = i + 1
						else:
							ok = False
							i = i + 1
					if(ok == True):
						return 0
					else:
						print("186")
						return -70
				elif com == 'rm' and (sys.argv[2] == '-r' or sys.argv[2] == '-R' or sys.argv[2] == '--recursive'):
					i = 2
					while i <= len(sys.argv) - 2:
						shutil.rmtree(sys.argv[i+1])
						i = i + 1
					return 0
				elif com == 'rm' and (sys.argv[2] == '-d' or sys.argv[2] == '--dir'):
					i = 2
					while i <= len(sys.argv) - 2:
						os.rmdir(sys.argv[i+1])
						i = i + 1
					return 0
			except Exception:
				print("186")
				return -70

			try:
				if com == 'ls' and len(sys.argv) == 2:
					for f in os.listdir(os.getcwd()):
						if not f.startswith('.'):
							print(f)
					return 0
				elif com == 'ls' and sys.argv[2] != '-a' and sys.argv[2] != '--all' and sys.argv[2] != '-R' and sys.argv[2] != '--recursive':
					if len(sys.argv) == 3:
						for f in os.listdir(sys.argv[2]):
							if not f.startswith('.'):
								print(f)
					return 0
				elif com == 'ls' and (sys.argv[2] == '-a' or sys.argv[2] == '--all'):
					if len(sys.argv) == 3:
						os.listdir(os.getcwd())
					elif len(sys.argv) == 4:
						os.listdir(sys.argv[3])
					return 0
				elif com == 'ls' and (sys.argv[2] == '-R' or sys.argv[2] == '--recursive'):
					if len(sys.argv) == 3:
						listOfFiles = os.listdir(os.getcwd())
						for l in listOfFiles:
							print(l)
					elif len(sys.argv) == 4:
						listOfFiles = os.listdir(sys.argv[3])
						for l in listOfFiles:
							print(l)
					return 0
			except Exception:
				print("176")
				return -80

			try:
				if com == 'cp' and sys.argv[2] != '-R' and sys.argv[2] != '-r' and sys.argv[2] != '--recursive':
					if len(sys.argv) == 3:
						os.link(sys.argv[2])
					elif len(sys.argv) == 4:
						shutil.copy(sys.argv[2], sys.argv[3])
					return 0
				elif com == 'cp' and (sys.argv[2] == '-R' or sys.argv[2] == '-r' or sys.argv[2] == '--recursive'):
					if len(sys.argv) == 4:
						shutil.copytree(sys.argv[2])
					elif len(sys.argv) == 5:
						shutil.copytree(sys.argv[3], sys.argv[4])
					return 0
			except Exception:
				print("166")
				return -90

			try:
				if com == 'touch' and sys.argv[2] != '-a' and sys.argv[2] != '-c' and sys.argv[2] != '--no-create' and sys.argv[2] != '-m':
					f = open(sys.argv[2],"w+")
					f.close()
					return 0
				elif com == 'touch' and sys.argv[2] == '-a':
					if com == 'touch' and (sys.argv[3] == '-c' or sys.argv[3] == '--no-create'):
						print("")
					return 0
				elif com == 'touch' and sys.argv[2] == '-m':
					if com == 'touch' and (sys.argv[3] == '-c' or sys.argv[3] == '--no-create'):
						print("")
					return 0
			except Exception:
				print("156")
				return -100

			try:
				if com == 'chmod' and sys.argv[2] == '':
					os.chmod(sys.argv[3], stat.S_IWOTH)
					return 0
			except Exception:
				print("231")
				return -25

	
			print("Invalid command")
			return -1

foo()
